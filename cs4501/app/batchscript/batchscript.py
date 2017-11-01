import json
from kafka import KafkaProducer
from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
from kafka.common import NodeNotReadyError




while True:
    try: 
        es = Elasticsearch(['es'])
        consumer = KafkaConsumer('new-listings-topic', group_id='listing-indexer', bootstrap_servers=['kafka:9092'])
        break

        
        
    except NodeNotReadyError:
        continue
    
while True:
    try:
        for message in consumer:
            listing = (json.loads((message.value).decode('utf-8')))
            es.index(index='listing_index', doc_type='listing', id=listing['id'], body=listing)
            es.indices.refresh(index="listing_index")
            
            
    except:
        continue

