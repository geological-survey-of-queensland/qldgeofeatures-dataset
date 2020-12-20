import rdflib

g = rdflib.Graph().parse("../dataset.ttl", format="turtle")

# remove extra classes
q = """
DELETE {
    ?f a geo:Feature .
    ?f a sdo:Landform .
}
WHERE {
    ?f a geo:Feature .
}
"""
g.update(q)

# q = """
# PREFIX geo: <http://www.opengis.net/ont/geosparql#>
# PREFIX sdo: <https://schema.org/>
#
# SELECT ?f ?c
# WHERE {
#     ?f a ?c
#
#     FILTER NOT EXISTS {?c rdf:type <https://linked.data.gov.au/def/sweetgeofeatures#Province>}
#     FILTER NOT EXISTS {?f rdf:type <https://schema.org/Organization>}
#     FILTER NOT EXISTS {?f rdf:type <http://www.w3.org/ns/org#Organization>}
# }
# ORDER BY ?f
# """
# for r in g.query(q):
#     print(r)

individuals = {}
GEO = rdflib.Namespace("http://www.opengis.net/ont/geosparql#")
GEOF = rdflib.Namespace("https://linked.data.gov.au/def/geofeatures#")
GROLE = rdflib.Namespace("https://linked.data.gov.au/def/geometry-roles/")
SDO = rdflib.Namespace("https://schema.org/")

for s, o in g.subject_objects(predicate=rdflib.namespace.RDF.type):
    if o in [
        GEOF.SubProvince,
        GEOF.Basin,
        GEOF.Depression,
        GEOF.Orogen,
        GEOF.Trough,
        GEOF.Craton,
        GEOF.Graben,
    ]:
        individuals[str(s)] = {
            "type": str(o)
        }

for s, o in g.subject_objects(predicate=rdflib.namespace.RDF.type):
    if o in [GEOF.Province] and str(s) not in individuals.keys():
        individuals[str(s)] = {
            "type": str(o)
        }

for s, o in g.subject_objects(predicate=SDO.name):
    if individuals.get(str(s)) is not None:
        individuals[str(s)]["name"] = str(o)

for i in individuals.keys():
    for o in g.objects(subject=rdflib.URIRef(i), predicate=GEO.hasGeometry):
        for p2, o2 in g.predicate_objects(subject=o):
            if o2 == rdflib.URIRef("https://linked.data.gov.au/def/geometry-roles/bounding-box"):
                for o3 in g.objects(subject=o, predicate=GEO.asWKT):
                    individuals[str(i)]["geometry"] = str(o3)


kk = sorted(individuals.keys())

csv = "id,name,alias,type,status,relationship,geometry\n"
for k in kk:
    csv += "{},{},{},{},{},{},{}\n".format(
                k.split("/")[-1],
                '"' + individuals[k]["name"] + '"',
                "",
                individuals[k]["type"].split("#")[-1],
                "",
                "",
                '"' + individuals[k]["geometry"] + '"' if individuals[k].get("geometry") else ""
            )

    with open("../dataset.csv", "w") as f:
        f.write(csv)
