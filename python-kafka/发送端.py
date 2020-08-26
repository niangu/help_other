from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'])
 #此处ip可以是多个['0.0.0.1:9092','0.0.0.2:9092','0.0.0.3:9092' ]
import base64
with open("/home/niangu/桌面/答题卡识别/7.jpeg", "rb") as f:#转换为二进制格式
    base64_data = base64.b64encode(f.read())#使用base64进行加密
    print(base64_data)
producer.send('test', key=b'answer_sheet1', value=base64_data)
producer.close()