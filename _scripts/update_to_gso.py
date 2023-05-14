from rdflib import Graph, Namespace, BNode
from rdflib.namespace import GEO, RDF, RDFS, SDO, TIME
QGF = Namespace("https://linked.data.gov.au/dataset/qldgeofeatures/")
SU = Namespace("http://pid.geoscience.gov.au/def/stratunits#")
GSOC = Namespace("https://w3id.org/gso/common/")
SWEETG = Namespace("http://sweetontology.net/realmGeol/")
GEOF = Namespace("https://linked.data.gov.au/def/geofeatures#")

g = Graph().parse("../qldgeofeatures.ttl")
g.bind("qgf", QGF)
g.bind("su", SU)
g.bind("gsoc", GSOC)

# qgf:BiloelaBasin
for gf in g.subjects(RDF.type, GEO.Feature):
    c = g.compute_qname(gf)
    qname = f"{c[0]}:{c[2]}"

    # title/name
    g.remove((gf, RDFS.label, None))

    # GSO stuff
    younger = g.value(gf, SU.younger)
    # if younger is None:
    #     print(f"{c[0]}:{c[2]} missing younger")
    older = g.value(gf, SU.older)
    # if older is None:
    #     print(f"{c[0]}:{c[2]} missing older")

    if younger == older:
        g.add((gf, GSOC.occupiesTimeIndirectly, younger))
    elif younger != older:
        period = BNode()
        g.add((gf, GSOC.occupiesTimeIndirectly, period))
        g.add((period, RDF.type, TIME.ProperInterval))
        g.add((period, TIME.intervalFinishedBy, younger))
        g.add((period, TIME.intervalStartedBy, older))

    g.remove((gf, SU.older, None))
    g.remove((gf, SU.younger, None))
    g.remove((gf, TIME.hasTime, None))
    g.remove((gf, RDF.type, GSOC.Spatial_Region_2D))
    g.remove((gf, RDF.type, SDO.Landform))
    g.remove((gf, RDF.type, SWEETG.GeologicFeature))

    for t in g.objects(gf, RDF.type):
        if str(t).startswith(str(GEOF)):
            g.remove((gf, RDF.type, t))
            g.add((gf, SDO.additionalType, t))

g.serialize(destination="../qldgeofeatures.gso.ttl", format="longturtle")
