<img src="gsq.jpg" style="width:25%" />

# Queensland Geological Features Dataset
This [RDF](https://en.wikipedia.org/wiki/RDF) dataset contains some of the geological Features of Interest of Queensland described and published by the [Geological Survey of Queensland](https://en.wikipedia.org/wiki/Geological_Survey_of_Queensland).


## _Features_

This dataset considers each _Feature_ from a number of points of view, or _profiles_:

* **named individual** - each _Feature_ is an instance of the [Web Ontology Languages](https://en.wikipedia.org/wiki/Web_Ontology_Language) 's [`NamedIndividual`](https://www.w3.org/TR/owl2-syntax/#Named_Individuals) class
  * they are specific things in the world
* **geospatial object** - each _Feature_ is an instance of the [GeoSPARQL Ontology](https://github.com/opengeospatial/ogc-geosparql/blob/master/1.1/geo.ttl) 's [`Feature`](http://www.opengis.net/ont/geosparql#Feature) class
  * they have geometries
* **feature of interest** - each _Feature_ is an instance of the [SOSA Ontology's `FeatureOfInterest`](https://www.w3.org/TR/vocab-ssn/#SOSAFeatureOfInterest) class
  * they may have obsesrvations made against them to determine their properties
  * e.g. boreholes to measure their amound of coal, gold etc.
* **'Geologic' feature** - each _Feature_ is an instance of one of the subclasses of the [SWEET Ontology](https://sweetontology.net/) 's [`GeologicFeature`](http://sweetontology.net/realmGeol/GeologicFeature) class
  * they are earth science things of type Craton, Sandbar, Volcao etc.


## Dataset

This dataset as a whole is modelled as a [LocI Dataset](https://linked.data.gov.au/def/loci#Dataset) which is a specialised form of both a [DCAT2 Dataset](https://www.w3.org/TR/vocab-dcat-2/#Class:Dataset) and a [VoID Dataset](http://rdfs.org/ns/void#Dataset). 

This means that the dataset is:

1. compatible with the [Location Index (LocI)](https://www.ga.gov.au/locationindex) Project's notion of a dataset;
2. has standard catalogue metadata - due to DCAT;
3. has some RDF/graph properties of it described - due to VoID. 

This dataset can be used with other LocI datasets for spatial interactions etc.

### Metadata

The dataset-level metadata is available in multiple RDF (Turtle) files within the [_metadata/](_metadata/) folder. These can be combined using the `[make_dataset_rdf.py](_scripts/make_dataset_rdf.py)` Python script to form [_metadata/metadata.ttl](_metadata/metadata.ttl) whihc, in turn, can be combined with the data files (see above) to form the complete dataset.

Each of the RDF files within the [_metadata/](_metadata/) folder adds another *profile* 's metadata, such as VoID, LocI etc. The main metadata file is [_metadata/dcat_dataset.ttl](_metadata/dcat_dataset.ttl).


### Persistent Identifier
The persistent identifier (PID) for this dataset is:

* **https://linked.data.gov.au/dataset/qldgeofeatures**


## Data
***Currently this dataset contains a base of publicly avaiable GSQ Structural Framework data which is certainly not all of GSQ's Features of Interest. It is being extended to contain more data over time.***

This dataset's data is all in the single file [dataset.ttl](dataset.ttl). The spatial and some of the other properties of the features were produced from the initial GSQ Structural Framework JSON data which is stored in [_data/](_data/) by the Python script [data-processor.py](_scripts/data-processor.py). The source of the JSON files is the [Queensland Globe](https://qldglobe.information.qld.gov.au/), which was originally populated with GSQ Structural Framework deliverd to the Globe by GSQ some years ago. This data is already public.

Many additions to the initial `dataset.ttl` file created from the JSON data have been made by hand and also by Python and SPARQL scripting, for instance, _older_ and _younger_ ages for features were determbined by the Python script [older_younger.py](_scripts/older_younger.py) producing the data file [older_younger.py](reference/older_younger.py), the content of which has since been merged into `dataset.ttl`.

 
## License
The content of this API is licensed for use under the [Creative Commons 4.0 License](https://creativecommons.org/licenses/by/4.0/). See the [license deed](LICENSE) for details.


## Contacts
**Geoscience Information Team**,
Geological Survey of Queensland,
Department of Resources,
Brisbane, QLD, Australia,
<geological_info@resources.qld.gov.au>
