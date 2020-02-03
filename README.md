<img src="gsq.jpg" style="width:25%" />

# Queendland Geo Features of Interest Dataset 
This  [RDF](https://en.wikipedia.org/wiki/RDF) dataset contains some of the geological Features of Interest (GeoFoIs) of Queensland described and published by the [Geological Survey of Queensland](https://en.wikipedia.org/wiki/Geological_Survey_of_Queensland).

This dataset, considering each GeoFoI to be a specialised form of a [SOS Feature of Interest](https://www.w3.org/TR/vocab-ssn/#SOSAFeatureOfInterest), allows them to be associated with property obsesrvations.

With each GeoFoI also being a specialised form of the [GeoSPARQL ontology](https://en.wikipedia.org/wiki/OGC_GeoSPARQL)'s `Feature` class and with the dataset overall being a [DCAT2 Dataset](https://www.w3.org/TR/vocab-dcat-2/#Class:Dataset), this dataset is *LocI compatable* meaning it is published in accordance with the expectations of the [Location Index (LocI)[https://locationindex.org] project and this data can be used with other LocI data.


## Data
***Currently this API only delivers already public GSQ Structural Framework data, not all of GSQ's Features of Interest.***

This dataset's final data is all in the single file [data.ttl](data.ttl).

The source data for this dataset so far is taken from data already published by GSQ via the [Queensland Globe](https://qldglobe.information.qld.gov.au/), so all of this information is already public.

This data is published via a Linked Data API so that the URIs for each item will resolve. See the API:

* https://github.com/geological-survey-of-queensland/gsq-foi-api


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



