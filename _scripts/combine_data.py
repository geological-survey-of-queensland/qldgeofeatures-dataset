import rdflib
from pathlib import Path
THIS_DIR = Path(__file__).parent


g = rdflib.Graph()
g.parse(Path(THIS_DIR.parent / "_data" / "dataset.ttl"))
g.parse(Path(THIS_DIR.parent / "_data" / "fc.ttl"))
g.parse(Path(THIS_DIR.parent / "_data" / "features.ttl"))

with open(Path(THIS_DIR.parent / "qldgeofeatures.ttl"), "w") as f:
    f.write(g.serialize(format="longturtle"))
