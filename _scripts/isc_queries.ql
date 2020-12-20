# order all ranks if ages by time
PREFIX gts: <http://resource.geosciml.org/ontology/timescale/gts#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX time: <http://www.w3.org/2006/time#>
SELECT ?a ?rank ?beginning_time ?end_time
WHERE {
    GRAPH <http://resource.geosciml.org/vocabulary/timescale/gts2020> {
        ?a 
            gts:rank ?rank ;
            time:hasBeginning/time:inTemporalPosition [       
	        	time:numericPosition ?beginning_time ;
	    	    time:hasTRS <http://resource.geosciml.org/classifier/cgi/geologicage/ma>
    	    ] ;
		  	time:hasEnd/time:inTemporalPosition [       
	        	time:numericPosition ?end_time ;
	    	    time:hasTRS <http://resource.geosciml.org/classifier/cgi/geologicage/ma>
    	    ] .         
    }
}
ORDER BY ?end_time ?beginning_time


