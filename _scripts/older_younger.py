from rdflib import Graph, Namespace

SU = Namespace("http://pid.geoscience.gov.au/def/stratunits#")
g = Graph("SPARQLStore")
g.open("http://localhost:7200/repositories/geofeatures")
g2 = Graph()

# get younger
q = """
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX eg: <http://example.org/>
SELECT *
WHERE {
    ?a time:hasTime ?t .

    ?t eg:beginning ?b ;
       eg:end ?e .
}
ORDER BY ?a ?e ?b
"""

p = None
for r in g.query(q):
    if r["a"] != p:
        g2.add((
            r["a"],
            SU.younder,
            r["t"]
        ))
        p = r["a"]
    else:
        pass


# get older
q = """
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX eg: <http://example.org/>
SELECT *
WHERE {
    ?a time:hasTime ?t .

    ?t eg:beginning ?b ;
       eg:end ?e .
}
ORDER BY ?a DESC(?e) DESC(?b)
"""

p = None
for r in g.query(q):
    if r["a"] != p:
        g2.add((
            r["a"],
            SU.older,
            r["t"]
        ))
        p = r["a"]
    else:
        pass

g2.serialize(destination="/Users/nick/Work/gsq/qldgeofeatures-dataset/older_younger.ttl", format="turtle")
