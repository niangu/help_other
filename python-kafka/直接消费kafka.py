from pykafka import KafkaClient
import os, base64


client = KafkaClient(hosts="127.0.0.1:9092")
topic = client.topics['test']
#获取consumer消费者
consumer = topic.get_simple_consumer(consumer_group="test", reset_offset_on_start=True)
for message in consumer:
    print(message)
    if message is not None:
        print(">>>>>>>>>>>>>>", message.offset)
        print(">>>>>>>>>>>>>>", message.value)
        with open("/home/niangu/桌面/python kafka/1.txt", "r") as f:
            imgdata = base64.b64decode(f.read())
            file = open('2.jpg', 'wb')
            file.write(imgdata)
            file.close()