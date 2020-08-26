from pykafka import KafkaClient
client = KafkaClient(hosts="127.0.0.1:9092")
for topic in client.topics:
    print(topic)