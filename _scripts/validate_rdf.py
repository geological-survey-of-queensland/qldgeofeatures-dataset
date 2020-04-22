from rdflib import Graph


g = Graph().parse("../dataset.ttl", format="turtle")
print(len(g))
