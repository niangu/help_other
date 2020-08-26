import pymysql

conn= pymysql.connect(host='localhost', user='root', passwd='a112233.', db ='baidumap', charset="utf8")
cur = conn.cursor()
sql = """CREATE TABLE city (
         id INT NOT NULL AUTO_INCREMENT,
         city VARCHAR(200) NOT NULL,
         park VARCHAR(200) NOT NULL,
         location_lat FLOAT,
         location_lng FLOAT,
         address VARCHAR(200),
         street_id VARCHAR(200),
         uid VARCHAR(200),
         created_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
         PRIMARY KEY (id)
         );"""
cur.execute(sql)
cur.close()
conn.commit()
conn.close()