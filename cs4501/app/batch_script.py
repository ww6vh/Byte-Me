from elasticsearch import Elasticsearch
from kafka import KafkaConsumer
import json, time

consumer = None
es = None

while consumer is None or es is None:
    try:
        consumer = KafkaConsumer('new-listings-topic', group_id='listing-indexer', bootstrap_servers=['kafka:9092'])
        es = Elasticsearch(['es'])
    except:
        time.sleep(1)


for message in consumer:
    some_new_listing = json.loads((message.value).decode('utf-8'))
    es.index(index='listing_index', doc_type='listing', id=some_new_listing['id'], body=some_new_listing)
    es.indices.refresh(index="listing_index")