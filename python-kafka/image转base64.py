import base64
with open("/home/niangu/桌面/答题卡识别/7.jpeg", "rb") as f:#转换为二进制格式
    base64_data = base64.b64encode(f.read())#使用base64进行加密
    print(base64_data)
    file = open('1.txt', 'wb')#写成文本格式
    file.write(base64_data)
    file.close()