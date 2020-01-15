# This script processes JSON files of the Structural Framework content downloaded from the Queensland Globe
# into RDF.

import os
import pickle
import json
from rdflib import Graph, URIRef, Literal, Namespace, BNode
from rdflib.namespace import RDF
from os.path import dirname, realpath, join
DATA_DIR = join(dirname(dirname(realpath(__file__))), '_data')
CONFIG_DIR = join(dirname(dirname(realpath(__file__))), 'structf', 'config')

g = Graph()
SF = Namespace('http://linked.data.gov.au/dataset/qld-structural-framework/')
g.bind('sf', SF)
SGF = Namespace('http://linked.data.gov.au/def/sweetgeofeatures#')
g.bind('sgf', SGF)
GEO = Namespace("http://www.opengis.net/ont/geosparql#")
g.bind('geo', GEO)
SDO = Namespace("https://schema.org/")
g.bind('sdo', SDO)
TIME = Namespace("http://www.w3.org/2006/time#")
g.bind('time', TIME)
GEOX = Namespace("http://linked.data.gov.au/def/geox#")
g.bind('geox', GEOX)

AGES = {
    'CAMBRIAN':         ['http://resource.geosciml.org/classifier/ics/ischart/Cambrian'],
    'CARBONIFEROUS':    ['http://resource.geosciml.org/classifier/ics/ischart/Carboniferous'],
    'CRETACEOUS':       ['http://resource.geosciml.org/classifier/ics/ischart/Cretaceous'],
    'DEVONIAN':         ['http://resource.geosciml.org/classifier/ics/ischart/Devonian'],
    'JURASSIC':         ['http://resource.geosciml.org/classifier/ics/ischart/LowerDevonian'],
    'MESOPROTEROZOIC':  ['http://resource.geosciml.org/classifier/ics/ischart/Mesoproterozoic'],
    'ORDOVICIAN':       ['http://resource.geosciml.org/classifier/ics/ischart/Ordovician'],
    'PALAEOPROTEROZOIC': ['http://resource.geosciml.org/classifier/ics/ischart/Paleoproterozoic'],
    'PERMIAN':          ['http://resource.geosciml.org/classifier/ics/ischart/Permian'],
    'TRIASSIC':         ['http://resource.geosciml.org/classifier/ics/ischart/Triassic'],
    'LATE DEVONIAN':    ['http://resource.geosciml.org/classifier/ics/ischart/UpperDevonian'],
    'SILURIAN':         ['http://resource.geosciml.org/classifier/ics/ischart/Silurian'],
    'EARLY DEVONIAN':   ['http://resource.geosciml.org/classifier/ics/ischart/LowerDevonian'],
    'NEOPROTEROZOIC':   ['http://resource.geosciml.org/classifier/ics/ischart/Neoproterozoic'],
    'EARLY CARBONIFEROUS':  ['http://resource.geosciml.org/classifier/ics/ischart/Mississipian'],
    'EARLY PALAEOZOIC': [
        'http://resource.geosciml.org/classifier/ics/ischart/Ordovician',
        'http://resource.geosciml.org/classifier/ics/ischart/Cambrian'
    ],
    'MIDDLE DEVONIAN':  ['http://resource.geosciml.org/classifier/ics/ischart/MiddleDevonian'],
    'LATE SILURIAN': [
        'http://resource.geosciml.org/classifier/ics/ischart/Pridoli',
        'http://resource.geosciml.org/classifier/ics/ischart/Ludlow',
        'http://resource.geosciml.org/classifier/ics/ischart/Wenlock'
    ],
    'EARLY PALAEOZOIC?': [
        'http://resource.geosciml.org/classifier/ics/ischart/Ordovician',
        'http://resource.geosciml.org/classifier/ics/ischart/Cambrian'
    ],
    'PALAEOZOIC': ['http://resource.geosciml.org/classifier/ics/ischart/Paleozoic']
}

FEATURE_TYPES = {
    'PROVIN': SGF.Province,
    'SUBPRO': SGF.SubProvince,
    'CRATON': SGF.Craton,
    'OROGEN': SGF.Orogen
    # if the item ends with Basin or Depression, it's one of those
}

FEATURE_TYPES_FROM_NAMES = {
    'Province':     SGF.Province,
    'Subprovince':  SGF.SubProvince,
    'Craton':       SGF.Craton,
    'Orogen':       SGF.Orogen,
    'Depression':   SGF.Depression,
    'Basin':        SGF.Basin,
    'Trough':       SGF.Trough
}

directory = os.fsencode('_data')


for file in os.listdir(DATA_DIR):
    filename = os.fsdecode(file)
    if filename.endswith(".json"):
        print('processing ' + filename)
        data = json.load(open(join(DATA_DIR, filename)))

        name = data['features'][0]['properties']['Structure Name']\
            .replace('undivided', '')\
            .replace('extent', '')\
            .strip()
        this_feature_uri = URIRef(
            SF + 'province/' + name
            .replace(' ', '')
            .replace('\'', '')
        )

        # types
        g.add((
            this_feature_uri,
            RDF.type,
            SDO.Landform
        ))
        g.add((
            this_feature_uri,
            RDF.type,
            GEO.Feature
        ))
        g.add((
            this_feature_uri,
            RDF.type,
            SGF.Province
        ))
        g.add((
            this_feature_uri,
            RDF.type,
            # URIRef(FEATURE_TYPES.get(data['features'][0]['properties']['Rank']))
            FEATURE_TYPES_FROM_NAMES[name.split(' ')[-1]]
        ))

        # label
        g.add((
            this_feature_uri,
            SDO.name,
            Literal(name, lang='en')
        ))

        for age in data['features'][0]['properties']['Age'].split(' - '):
            for each_age in AGES.get(age):
                g.add((
                    this_feature_uri,
                    TIME.hasTime,
                    URIRef(each_age)
                ))

        bbox = BNode()
        g.add((
            bbox,
            RDF.type,
            GEO.Geometry
        ))
        g.add((
            bbox,
            GEOX.hasRole,
            GEOX.BoundingBox
        ))
        bbox_points = data['features'][0]['geometry']['bbox']
        bbox_wkt = '<http://www.opengis.net/def/crs/EPSG/0/4326> POLYGON(({} {}, {} {}))'.format(
            bbox_points[0],
            bbox_points[1],
            bbox_points[2],
            bbox_points[3]
        )
        g.add((
            bbox,
            GEOX.asWKT,
            Literal(bbox_wkt, datatype=GEO.wktLiteral)
        ))

        g.add((
            this_feature_uri,
            GEO.hasGeometry,
            bbox
        ))

        boundary_points = data['features'][0]['geometry']['coordinates']
        polygon = ''
        if len(boundary_points) == 1:
            # process single polygon
            # boundary_points[0]
            for pair in boundary_points[0]:
                polygon += '{} {},'.format(pair[0], pair[1])
            polygon = polygon.rstrip(',')
        else:
            for pair in boundary_points[0][0]:  # only the first one is in degrees
                polygon += '{} {},'.format(pair[0], pair[1])
            polygon = polygon.rstrip(',')
        boundary_wkt = '<http://www.opengis.net/def/crs/EPSG/0/4326> POLYGON(({}))'.format(polygon)

        boundary = BNode()
        g.add((
            boundary,
            RDF.type,
            GEO.Geometry
        ))
        g.add((
            boundary,
            GEOX.hasRole,
            GEOX.Boundary
        ))

        g.add((
            boundary,
            GEOX.asWKT,
            Literal(boundary_wkt, datatype=GEO.wktLiteral)
        ))

        g.add((
            this_feature_uri,
            GEO.hasGeometry,
            boundary
        ))

# import pprint
# pprint.pprint(g.serialize(format='turtle').decode('utf-8'))

with open(join(CONFIG_DIR, 'data.ttl'), 'w') as f:
    f.write(g.serialize(format='turtle').decode('utf-8'))

with open(join(CONFIG_DIR, 'data.pickle'), 'wb') as f:
    pickle.dump(g, f)
    f.close()
