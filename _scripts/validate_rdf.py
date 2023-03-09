from rdflib import Graph


g = Graph().parse("../_data/features.ttl", format="longturtle")
print(len(g))
