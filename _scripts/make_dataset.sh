METADATA_DIR='/Users/nick/Work/gsq/qldgeofeatures-dataset/_metadata'
/Users/nick/Work/surround/rdfx/rdfx.sh $METADATA_DIR/agents.ttl nt
/Users/nick/Work/surround/rdfx/rdfx.sh $METADATA_DIR/dcat_dataset.ttl nt
/Users/nick/Work/surround/rdfx/rdfx.sh $METADATA_DIR/dcat_data_services.ttl nt
/Users/nick/Work/surround/rdfx/rdfx.sh $METADATA_DIR/loci.ttl nt
/Users/nick/Work/surround/rdfx/rdfx.sh $METADATA_DIR/void.ttl nt

cat $METADATA_DIR/*.nt >> $METADATA_DIR/_metadata.nt

/Users/nick/Work/surround/rdfx/rdfx.sh $METADATA_DIR/_metadata.nt ttl

rm $METADATA_DIR/*.nt
