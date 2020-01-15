<img src="gsq.jpg" style="width:25%" />

# GSQ's Features of Interest Dataset 
This  [RDF](https://en.wikipedia.org/wiki/RDF) dataset contains the [Geological Survey of Queensland](https://en.wikipedia.org/wiki/Geological_Survey_of_Queensland)'s Structural Framework [Features of Interest](https://www.w3.org/TR/vocab-ssn/#SOSAFeatureOfInterest).

This dataset, being in the RDF format and with semantic relations in it, can be added to the total pool of GSQ's semantic data.


## Data
***Currently this API only delivers Structural Framework data, not all of GSQ's Features of Interest.***

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



