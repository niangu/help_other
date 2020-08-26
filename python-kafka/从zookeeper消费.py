from pykafka import KafkaClient
client = KafkaClient(hosts="127.0.0.1:9092")
topic = client.topics['test']
balanced_consumer= topic.get_balanced_consumer(consumer_group='test',auto_commit_enable=True,reset_offset_on_start=True,zookeeper_connect='127.0.0.1:9092')

for message in balanced_consumer:
    if message is not None:
        print(message.offset, message.value)