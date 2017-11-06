#!/usr/bin/env python
#  -*- coding:utf-8 -*-
import sys
import MySQLdb
import json,time,datetime
import chardet
from jsqbmysql import connection,dev,connection1,test
import paramiko
from sshtunnel import SSHTunnelForwarder
from jsqblinux import overdue
from cuserid import searchuid,inver
#芝麻15<=zmop<=39
#转化时间戳

overday=1  #需要改逾期天数
n=overday+2
m=overday+1
yesterday= str(int(time.mktime((datetime.datetime.now() - datetime.timedelta(days = overday)).timetuple())))
overd=str(int(time.mktime((datetime.datetime.now() - datetime.timedelta(days = m)).timetuple())))
if inver()[0:4]=="test":
	conn=connection1()
else:
	conn=connection()
cur=conn.cursor()
cur.execute("update tb_user_loan_order_repayment set late_fee=0 where user_id="+searchuid()+" order by id desc limit 1")
cur.execute("update tb_user_loan_order_repayment set plan_fee_time="+yesterday+" where user_id="+searchuid()+" order by id desc limit 1")
cur.close()
conn.commit()
conn.close()
for x in range(n):
	overday2=x
	twoday=str(int(time.mktime((datetime.datetime.now() - datetime.timedelta(days = overday2)).timetuple())))
	key_file ='F:\\key\\jsqb_key'
	key = paramiko.RSAKey.from_private_key_file(key_file,password='123456')
	if inver()[0:4]=="test":
		server=SSHTunnelForwarder(
				('test.kdqugou.com', 2022),
				ssh_username="test",
				ssh_pkey =key,
				remote_bind_address=('mysql-test', 3306)
		)

		server.start()

		conn = MySQLdb.connect(host='127.0.0.1',              #此处必须是是127.0.0.1
							   port=server.local_bind_port,
                               user='jsqb_user',
                               passwd='jsqb_user',
                               db='jsqb')
	else:
		server=SSHTunnelForwarder(
				('dev.kdqugou.com', 1022),
				ssh_username="test",
				ssh_pkey =key,
				remote_bind_address=('mysql_dev', 3306)
		)

		server.start()

		conn = MySQLdb.connect(host='127.0.0.1',              #此处必须是是127.0.0.1
							   port=server.local_bind_port,
                               user='jsqb_user',
                               passwd='jsqb@ArEe4LJq',
                               db='jsqb')
	cur = conn.cursor()




	if inver()[0:4]=="test":
		list=test("select id from tb_user_loan_order_repayment where user_id="+searchuid()+" order by id desc limit 1")
		#print "select id from tb_user_loan_order_repayment where user_id="+searchuid()+" order by id desc limit 1"
	else:
		list=dev("select id from tb_user_loan_order_repayment where user_id="+searchuid()+" order by id desc limit 1")

	b=list[0][0]

	exc="update tb_user_loan_order_repayment set plan_repayment_time=%s, interest_time=%s  where id=%s"%(twoday,0,b)
	#print exc

	cur.execute(exc)
	cur.close()
	conn.commit()

	conn.close()

	overdue(inver())

print "success"