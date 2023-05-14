from pathlib import Path
from rdflib import Graph
import pickle


def parse_or_load(p: Path) -> Graph:
    pkl_path = p.with_suffix(".pkl")

    if pkl_path.is_file():
        return pickle.load(open(pkl_path, "rb"))  # type: Graph
    else:
        g = Graph().parse(p)
        pickle.dump(g, open(pkl_path, "wb"))
        return g


g = parse_or_load(Path("../qldgeofeatures.ttl"))

q = """
    PREFIX geo: <http://www.opengis.net/ont/geosparql#>
    PREFIX sdo: <https://schema.org/>
    
    SELECT ?type
    WHERE {
        ?f a geo:Feature ;
            sdo:name ?name ;
        .
        ?f a ?type .
        
        FILTER REGEX(STR(?type), "^https://linked.data.gov.au/def/geofeatures#")
    }
    GROUP BY ?type
    ORDER BY ?type
    """

for r in g.query(q):
    print(r[0].lstrip("https://linked.data.gov.au/def/geofeatures#"))
