import rdflib
from os.path import dirname, realpath, join
MAIN_DIR = dirname(dirname(realpath(__file__)))
METADATA_DIR = join(MAIN_DIR, '_metadata')
DATA_DIR = join(MAIN_DIR, '_data')


g = rdflib.Graph()
g.parse(join(METADATA_DIR, 'dcat.ttl'), format='turtle')
g.parse(join(METADATA_DIR, 'loci.ttl'), format='turtle')
g.parse(join(METADATA_DIR, 'void.ttl'), format='turtle')
g.parse(join(DATA_DIR, 'features.ttl'), format='turtle')

with open(join(MAIN_DIR, 'dataset.ttl'), 'w') as f:
    f.write(g.serialize(format='turtle').decode('utf-8'))
