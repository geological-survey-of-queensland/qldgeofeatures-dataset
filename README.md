<img src="gsq.jpg" style="width:25%" />

# Queensland Geo Features of Interest Dataset 
This [RDF](https://en.wikipedia.org/wiki/RDF) dataset contains some of the geological Features of Interest (GeoFoIs) of Queensland described and published by the [Geological Survey of Queensland](https://en.wikipedia.org/wiki/Geological_Survey_of_Queensland).

This dataset considers each GeoFoI to be a specialised form of the [SOSA Ontology's Feature of Interest](https://www.w3.org/TR/vocab-ssn/#SOSAFeatureOfInterest), which allows them to be associated with property obsesrvations.

Each GeoFoI is also considered a specialised form of the [GeoSPARQL ontology](https://en.wikipedia.org/wiki/OGC_GeoSPARQL)'s `Feature` class meaning they can also be associated with one or more `Geometry` objects. 

The dataset as a whole is modelled as a [LocI Dataset](http://linked.data.gov.au/def/loci#Dataset) which is a specialised form of both a [DCAT2 Dataset](https://www.w3.org/TR/vocab-dcat-2/#Class:Dataset) and a [VoID Dataset](http://rdfs.org/ns/void#Dataset). This means that the dataset is 1. compatible with the [Location Index (LocI)](https://locationindex.org) Project's notion of a dataset; 2. has standard catalogue metadata (due to DCAT); and 3. has some RDF/graph properties of it described (due to VoID). This dataset can be used with other LocI datasets.


## Persistent Identifier
The proposed persistent identifier (PID) for this dataset is:

* **http://linked.data.gov.au/dataset/qldgeofoi**

This PID has been requested from the [Australian Government Linked Data Working Group](http://linked.data.gov.au), see the request catalogue entry: http://catalogue.linked.data.gov.au/resource/145.


## Data
***Currently this API only delivers already public GSQ Structural Framework data, not all of GSQ's Features of Interest but it will grow to include more data over time.***

This dataset's features data is all in the single file [features.ttl](_data/features.ttl) and that is produced using the Python script [data-processor.py](_scripts/data-processor.py) from the JSON data files in [_data/](_data).

The source for this dataset's features so far is the [Queensland Globe](https://qldglobe.information.qld.gov.au/), so all of the features information is already public.

The dataset-level metadata is available in the following files:

* [loci.ttl](_metadata/loci.ttl) - LocI 
* [dcat.ttl](_metadata/dcat.ttl) - DCAT2
* [void.ttl](_metadata/void.ttl) - VoID

The total dataset, assembled from the 4 files described above, is available in the single file [dataset.ttl](dataset.ttl).

This data is published via a Linked Data API so that the URIs for each item - each feature and the dataset as a whole - will resolve when the persistent URI is allocated (see below). See the API online in test mode:

* https://gsq.cat/foi


## Model
The model for this data is the the the GSQ's [SWEET Geological Features Profile Ontology](https://github.com/geological-survey-of-queensland/sweet-geological-features-profile-ont). So far, only the following classes are used:

* `Geological Feature`
  * `Province`
    * `Sub Province`
    * `Orogen`
    * `Craton`
    * `Depression`
    * `Basin`
    * `Trough`

 
## License
The content of this API is licensed for use under the [Creative Commons 4.0 License](https://creativecommons.org/licenses/by/4.0/). See the [license deed](LICENSE) for details.


## Contacts
*owner*:  
**Geological Survey of Queensland**  
*Within the Queensland Department of Natural Resources, Mines & Energy*  
1 William St, Brisbane, Queensland, Australia  
<https://www.business.qld.gov.au/industries/mining-energy-water/resources/geoscience-information/gsq>  
<GSQOpenData@dnrme.qld.gov.au>  

*author*:  
**Nicholas Car**  
[SURROUND Australia Pty Ltd](https://surroundaustralia.com)  
<nicholas.car@surroundaustralia.com>  
<http://orcid.org/0000-0002-8742-7730>  
