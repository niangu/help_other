from minio import Minio
from minio.error import ResponseError
import urllib3




minioClient = Minio('0.0.0.0:9000', access_key='niangu', secret_key='11223344', secure=False)
##创建桶
#try:
#minioClient.make_bucket("bucket-niangu", location="us-east-1")
#except ResponseError as err:
 #   print(err)

#列出所有存储桶
buckets = minioClient.list_buckets()
for bucket in buckets:
    print(bucket.name, bucket.creation_date)

#检查存储桶是否存在
try:
    print(minioClient.bucket_exists("bucket-niangu"))
except ResponseError as err:
    print(err)

#删除存储桶
#try:
#    minioClient.remove_bucket("bucket-niangu")
#except ResponseError as err:
#    print(err)
#列出桶中所有对象
objects = minioClient.list_objects('bucket-niangu', prefix='my-prefixname', recursive=True)
for obj in objects:
    print(obj.bucket_name, obj.object_name.encode('utf-8'), obj.last_modified, obj.etag, obj.size, obj.content_type)

#列出桶中未完整上传的对象
uploads = minioClient.list_incomplete_uploads('bucket-niangu', prefix='my-prefixname', recursive=True)
for obj in uploads:
    print(obj.bucket_name, obj.object_name, obj.upload_id, obj.size)

#获取存储桶的当前策略
#policy = minioClient.get_bucket_policy('bucket-niangu')
#print(policy)

#设置桶的存储策略
#minioClient.set_bucket_policy('bucket-niangu', 'pre', Policy.READ_ONLY)

#获取桶上的通知配置
notification = minioClient.get_bucket_notification('bucket-niangu')
print(notification)

#设置桶的存储配置

#移除桶上配置的所有通知
#minioClient.remove_all_bucket_notification('bucket-niangu')
"""
#监听桶上的通知
events = minioClient.listen_bucket_notification('bucket-niangu', '', '',['s3:ObjectCreated:*',
                                                                                   's3:ObjectRemoved:*',
                                                                                   's3:ObjectAccessed:*'])
for event in events:
    print(event)

#下载一个对象
try:
    data = minioClient.get_object('bucket-niangu', 'query_text.jpeg')#get_partial_object('mybucket', 'myobject', 2, 4)
    with open('my-testfile', 'wb') as file_data:
        for d in data.stream(32*1024):
            file_data.write(d)
except ResponseError as err:
    print(err)
    

#下载并且将文件保存在本地
try:
    print(minioClient.fget_object('bucket-niangu', 'query_text.jpeg', '/home/niangu/桌面/python kafka/myobject'))
except ResponseError as err:
    print(err)
"""


