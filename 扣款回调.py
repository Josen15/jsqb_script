#!/usr/bin/env python
#  -*- coding:utf-8 -*-
import sys
import MySQLdb
import json
import chardet
from jsqbmysql import dev
from cuserid import searchuid,inver
from jsqblinux import debit

#扣款脚本
debit(inver())#扣款脚本


reload(sys)
sys.setdefaultencoding('utf-8')



uid=searchuid()



#执行对应环境的脚本
if inver()[0:4]=="test":
	debit(inver())#扣款脚本
	list=test("select order_id,user_id,plan_repayment_money from tb_financial_debit_record where user_id="+uid+" order  by id desc limit 1")
	list2=test("select name from tb_loan_person where id="+uid)
	hj=inver()+".test"
else:
	debit(inver())#扣款脚本
	list=dev("select order_id,user_id,plan_repayment_money from tb_financial_debit_record where user_id="+uid+" order  by id desc limit 1")
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
response=urllib2.urlopen("http://"+hj+".kdqugou.com/frontend/web/notify/test-callback?type=2&order_id="+orderid+"&code=2&money="+str(money))	###code值0为成功
m=response.read().decode('utf-8') 
d=json.loads(m)
k=d['code']
if int(k)==0:
	print time.strftime("%Y-%m-%d %H:%M %p", time.localtime())+"   "+orderid+"  "+realname+u"  扣款成功"
	print m
else:
	print u"  扣款失败"
	print m