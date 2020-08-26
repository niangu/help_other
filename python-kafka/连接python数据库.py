import pymysql

conn= pymysql.connect(host='localhost', user='root', passwd='a112233.', db ='answer_sheet', charset="utf8")
cur = conn.cursor()
ss = "".join(['2','2'])
sttt = "".join(['2','2'])
print(sttt)
print()
sql = """insert into score2(stu_id, subject, dan_xuan, duo_xuan, wei_xuan, n_url, n2_url, y_url) values
(%s,
 "3",
  "[1,2,3]", 
  "{1:'A', 2:'B'}",
   "",
    "",
     "",
      "");
"""
#insert into score2 (stu_id, subject, dan_xuan, duo_xuan, wei_xuan, n_url, n2_url, y_url) values("112333445", "3", "", "" , "", "" "", "");
cur.execute(sql, str(['2','2']))
cur.close()
conn.commit()
conn.close()