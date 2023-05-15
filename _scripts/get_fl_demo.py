from rdflib import Graph
import shapely
import json

g = Graph().parse("../qldgeofeatures.gso.case.ttl")

q = """
    PREFIX dcterms: <http://purl.org/dc/terms/>
    PREFIX geo: <http://www.opengis.net/ont/geosparql#>
    PREFIX qgf: <https://linked.data.gov.au/dataset/qldgeofeatures/>
    PREFIX sdo: <https://schema.org/>
    
    SELECT DISTINCT * 
    WHERE {
        VALUES ?v {
            qgf:BarrolkaDepression
            qgf:CentralianSuperbasin
            qgf:CooperBasin
            qgf:EromangaBasin
            qgf:GalileeBasin
            qgf:GeorginaBasin
            qgf:NorthAustralianCraton
            qgf:WarburtonBasin
            qgf:ThomsonOrogen        
        }
        ?v 
            a geo:Feature ;
            sdo:name ?label ;
            sdo:additionalType ?type ;  
            geo:hasGeometry/geo:asWKT ?geom ;    
        .
        
        OPTIONAL {
            ?v dcterms:isPartOf ?parent ;
        }
    
        OPTIONAL {
            {
                ?v gsoc:occupiesTimeIndirectly/time:intervalFinishedBy ?t1 .
                ?v gsoc:occupiesTimeIndirectly/time:intervalStartedBy ?t2 .
            }
            UNION
            {
                ?v gsoc:occupiesTimeIndirectly ?t1 .
                ?v gsoc:occupiesTimeIndirectly ?t2 .
    
                FILTER isIRI(?t1)
            }
        }
    }  
    """
j = []
for r in g.query(q):
    iri = r["v"].lstrip("https://linked.data.gov.au/dataset/qldgeofeatures/")
    name = str(r["label"])
    younger = r["t1"].lstrip("http://resource.geosciml.org/classifier/ics/ischart/")
    older = r["t2"].lstrip("http://resource.geosciml.org/classifier/ics/ischart/")
    type = r["type"].lstrip("https://linked.data.gov.au/def/geofeatures/")
    geom = r["geom"]
    bounds = shapely.from_wkt(geom).bounds
    bboxwkt = f"POLYGON(({bounds[0]} {bounds[1]},{bounds[0]} {bounds[3]},{bounds[2]} {bounds[3]},{bounds[2]} {bounds[1]},{bounds[0]} {bounds[1]}))"
    bbox = shapely.from_wkt(bboxwkt)
    j.append({
        "type": "Feature",
        "properties": {
            "iri": iri,
            "name": name,
            "younger": younger,
            "older": older,
            "type": type,
        },
        "geometry": json.loads(shapely.to_geojson(bbox))
    })
fc = {
  "type": "FeatureCollection",
  "name": "Statistical Areas 3s of the ACT",
  "features": j
}
print(json.dumps(fc))

