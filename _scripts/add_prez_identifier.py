from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import DCTERMS, GEO, RDF

filename = "qldgeofeatures.ttl"

g = Graph()
g.bind("qgf", Namespace("https://linked.data.gov.au/dataset/qldgeofeatures/"))
g.parse(filename, format="turtle")

for feature in g.subjects(RDF.type, GEO.Feature):
    g.add(
        (
            feature,
            DCTERMS.identifier,
            Literal(
                feature.n3(g.namespace_manager),
                datatype=URIRef("https://prez.dev/slug"),
            ),
        )
    )
    feature: URIRef

g.serialize(filename, format="longturtle")
