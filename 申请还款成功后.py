#!/usr/bin/env python
#  -*- coding:utf-8 -*-
import sys
import MySQLdb
import json
import chardet
from jsqbmysql import dev,test
from cuserid import searchuid,inver
#dev-239-zmop-feed-0teehx.dev.kdqugou.com/frontend/web/notify/test-callback?type=1&order_id=2017072116203_55971c933a2d16&code=1003
uid=searchuid()
reload(sys)
sys.setdefaultencoding('utf-8')
if inver()[0:4]=="test":
	list=test("select order_uuid,user_id,operator_money from tb_user_credit_money_log  where user_id="+uid+" order by id desc limit 1")
	hj=inver()+".test"
	list2=test("select name from tb_loan_person where id="+uid)
else:
	list=dev("select order_uuid,user_id,operator_money from tb_user_credit_money_log  where user_id="+uid+" order by id desc limit 1")
	hj=inver()+".dev"
	list2=dev("select name from tb_loan_person where id="+uid)
y=[]
for x in list:
	y.append(x)	
orderuuid=y[0][0]
user_id=y[0][1]
money=y[0][2]
realname=(str(list2[0][0])).decode("utf-8")

#打款回调 
import urllib2,time
#response=urllib2.urlopen("http://"+hj+".kdqugou.com/frontend/web/notify/test-callback?type=2&code=2&order_id="+orderuuid+"&money=30000")#部分还款改money后的
print "http://"+hj+".kdqugou.com/frontend/web/notify/test-callback?type=2&code=0&order_id="+orderuuid+"&money="+str(money)
response=urllib2.urlopen("http://"+hj+".kdqugou.com/frontend/web/notify/test-callback?type=2&code=0&order_id="+orderuuid+"&money="+str(money))
#response=urllib2.urlopen("http://"+hj+".kdqugou.com/frontend/web/notify/test-callback?type=2&code=0&money=100000&order_id="+orderuuid)#部分还款
m=response.read().decode('utf-8') 
d=json.loads(m)
k=d['code']
if int(k)==0:
	print time.strftime("%Y-%m-%d %H:%M %p", time.localtime())+"   "+realname+u"  还款成功"
elif int(k)==-2: 
		print u"还款没有输入密码"
else:
	print u"  还款失败"
	print m
