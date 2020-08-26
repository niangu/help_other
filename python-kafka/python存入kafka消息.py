# -*- coding: utf-8 -*-

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'])
 #此处ip可以是多个['0.0.0.1:9092','0.0.0.2:9092','0.0.0.3:9092' ]
for i in range(3):
     msg = "msg %d" % i
     print(msg)
     producer.send('test', key=b'ssss', value=b'sss')
producer.close()