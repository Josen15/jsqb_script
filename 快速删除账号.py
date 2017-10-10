#!/usr/bin/env python
#  -*- coding:utf-8 -*-

from cuserid import searchuid,inver
import urllib2,time
import sys
import MySQLdb
import json
import chardet
from jsqbmysql import dev,test,connection,connection1
from jsqblinux import loan,debit

#/html/body/div[3]/section

uid=searchuid()
list=['tb_user_realname_verify','tb_user_verification','tb_user_contact','tb_card_info']
if uid=="":
	print u"用户不存在"
else:
	print uid
env=inver()

if env[0:4]=="test":#test环境删除
	conn=connection1()
	cur=conn.cursor()
	cur.execute("delete from tb_loan_person where id="+uid+" order by id desc limit 1")
	cur.close()
	conn.commit()
	for x in list:
		print x
		conn=connection1()
		cur=conn.cursor()
		#conn=connection()
		cur.execute("delete from "+x+" where user_id="+uid+" order by id desc limit 1")
		cur.close()
		conn.commit()
		conn.close()
else:#dev环境删除
	conn=connection()
	cur=conn.cursor()
	cur.execute("delete from tb_loan_person where id="+uid+" order by id desc limit 1")
	cur.close()
	conn.commit()
	for x in list:
		conn=connection()
		cur=conn.cursor()
		#conn=connection()
		cur.execute("delete from "+x+" where user_id="+uid+" order by id desc limit 1")
		cur.close()
		conn.commit()
		print x
		conn.close()
	
print "success"