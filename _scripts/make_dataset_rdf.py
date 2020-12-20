from pathlib import Path
from rdflib import Graph, Namespace
from rdflib.util import guess_format

METADATA_DIR = Path("/Users/nick/Work/gsq/qldgeofeatures-dataset/_metadata/")

g = Graph()
prefixes = {
    "dcat":     Namespace("http://www.w3.org/ns/dcat#"),
    "dcterms":  Namespace("http://purl.org/dc/terms/"),
    "geo":      Namespace("http://www.opengis.net/ont/geosparql#"),
    "loci":     Namespace("https://linked.data.gov.au/def/loci#"),
    "locn":     Namespace("http://www.w3.org/ns/locn#"),
    "sdo":      Namespace("https://schema.org/"),
    "owl":      Namespace("http://www.w3.org/2002/07/owl#"),
    "void":     Namespace("http://rdfs.org/ns/void#"),
    "xsd":      Namespace("http://www.w3.org/2001/XMLSchema#"),
}
for k, v in prefixes.items():
    g.bind(k, v)

for rdf_file in METADATA_DIR.glob("*.ttl"):
    print("loading {}".format(rdf_file))
    g.parse(str(rdf_file), format=guess_format(rdf_file))

print("writing metadata.ttl")
g.serialize(destination=str(METADATA_DIR / "metadata.ttl"), format="turtle")

