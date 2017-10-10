#!/usr/bin/env python
#  -*- coding:utf-8 -*-
import sys
import MySQLdb
import json
import chardet
from jsqbmysql import dev,test
from jsqblinux import loan,debit
from cuserid import searchuid,inver
from backstage import verify
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
uid=searchuid()
#后台机审，初审，复审

def stu(n):
	if n=="0":
		verify(inver())
	else:
		pass
		

		

#执行对应环境的脚本
if inver()[0:4]=="test":
	status=str(test("select status from tb_user_loan_order where user_id="+uid+" order  by id desc limit 1")[0][0])
	stu(status)
	loan(inver())#借款脚本
	list=test("select order_id,user_id,money from tb_financial_loan_record where user_id="+uid+" order  by id desc limit 1")
	list2=test("select name from tb_loan_person where id="+uid)
	hj=inver()+".test"
else:
	status=str(dev("select status from tb_user_loan_order where user_id="+uid+" order  by id desc limit 1")[0][0])
	stu(status)
	loan(inver())#借款脚本
	list=dev("select order_id,user_id,money from tb_financial_loan_record where user_id="+uid+" order  by id desc limit 1")
	list2=dev("select name from tb_loan_person where id="+uid)
	hj=inver()+".dev"
#改user_id
y=[]
for x in list:
	y.append(x)
orderid=y[0][0]
user_id=y[0][1]
money=y[0][2]
realname=(str(list2[0][0])).decode("utf-8")
#打款回调 
import urllib2,time
response=urllib2.urlopen("http://"+hj+".kdqugou.com/frontend/web/notify/test-callback?type=1&order_id="+orderid+"&code=0")	###code值0为成功
m=response.read().decode('utf-8') 
d=json.loads(m)
k=d['code']
if int(k)==0:
	print time.strftime("%Y-%m-%d %H:%M %p", time.localtime())+"   "+orderid+"  "+realname+u"  打款成功"
	print m
else:
	print u"  打款失败"
	print m
	
