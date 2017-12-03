from kafka import KafkaConsumer
import json

consumer = None
while consumer is None:
    try:
        consumer = KafkaConsumer('clickedListings-topic', group_id='clikedListing-indexer', bootstrap_servers=['kafka:9092'])
    except:
        pass

for click in consumer:
    js = json.loads((click.value).decode('utf-8'))
    file = open("accessLog.txt", 'a')
    file.write(str(js["user_id"]) + "\t" + str(js["item_id"]) + "\n")