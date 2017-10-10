#!/usr/bin/env python
#  -*- coding:utf-8 -*-
#机审，初审，复审，打款，还款，扣款的get请求
import urllib2,time
from jsqbmysql import dev
from cuserid import searchuid,inver
from jsqblinux import debit
import json,re,requests
"""跳过机审o3i22n1d6bcf9e4qbpcjevu2u5

http://review-179-h5gong-w83mjd.dev.kdqugou.com/backend/web/index.php?r=pocket%2Fcheck-status&id=610

人工初审

http://review-179-h5gong-w83mjd.dev.kdqugou.com/backend/web/index.php?r=pocket%2Fpocket-first-trail&id=610&view=other

人工复审

http://review-179-h5gong-w83mjd.dev.kdqugou.com/backend/web/index.php?r=pocket%2Fpocket-twice-trail&id=610"""

import urllib2,time



uid=searchuid()
#logindata={"UserName":"admin","Password":"123456"}
loginurl="http://test-change-backe-5tyi8p.test.kdqugou.com/backend/web/index.php?r=main%2Flogin&_csrf=eUF3MlUwcDIIHiJfOlIBe0x3GgIeXxFwTiQzWgZbKnAwOxhUGXkGYQ%3D%3D&LoginForm%5Busername%5D=admin&LoginForm%5Bpassword%5D=123456&LoginForm%5BverifyCode%5D=&submit_btn=%E7%99%BB%E5%BD%95"
loginreq = urllib2.Request(loginurl)  
response=urllib2.urlopen(loginreq)#.decode('utf-8')
logincookie=response.headers['Set-Cookie']
headers={'cookie':'0log6jrea2up5nb3j3hmhq1br1'}
pa=re.compile("([0-9a-z]{6,50};)")
ma=pa.findall(logincookie)
cookie=ma[0][:-1]

#print logincookie
print response.headers
headers={'cookie':logincookie}
session = requests.Session()
cookie1={'Hm_lpvt_2d7ead83d6647b772a8a6c0661d68240':'1498096312','Hm_lvt_2d7ead83d6647b772a8a6c0661d68240':'1498096312','SESSIONID':'3is27144desscl729tltoggem3','_csrf':'dcc3c2dcea91bd444781aa4a6fc1f0ddb22094a2e517576dbf661305568c6d78a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%223SjMdWuC7abPoMekaAWzr14aOnvVTIRF%22%3B%7D','cpmenu_M6933518e015a68d1bf56574dc5690761':'1'}
#print session.post(loginurl)
#orderuuid=str(dev("select id from tb_user_loan_order where user_id="+uid+" order  by id desc limit 1")[0][0])
#机审，人工初审，复审全部通过
#Hm_lvt_2d7ead83d6647b772a8a6c0661d68240=1497358593; Hm_lpvt_2d7ead83d6647b772a8a6c0661d68240=1497358593
#Hm_lvt_2d7ead83d6647b772a8a6c0661d68240=1497358593; Hm_lpvt_2d7ead83d6647b772a8a6c0661d68240=1497358593
def get(url):
	
	#print "http://"+url+".dev.kdqugou.com/backend/web/index.php?r=pocket%2Fcheck-status&id="+orderuuid
	if inver()[0:4]=="test":
		req1 = urllib2.Request("http://"+url+".dev.kdqugou.com/backend/web/index.php?r=pocket%2Fpocket-list",headers=cookie1)
	else:
		req1 = urllib2.Request("http://"+url+".dev.kdqugou.com/backend/web/index.php?r=pocket%2Fcheck-status&_csrf=OEVVZU5jWnFJGgAIIQErOA1zOFUFDDszDyARDR0IADNxPzoDAiosIg%3D%3D&operation=1&code=A1o06&nocode=D1o08&loan_action=1&remark=&submit_btn=%E6%8F%90%E4%BA%A4&id="+orderuuid,headers=headers)
	response1=urllib2.urlopen(req1)
	print response1.read()
	#req1 = urllib2.Request("http://"+url+".dev.kdqugou.com/backend/web/index.php?r=pocket%2Fpocket-first-trail&view=other&_csrf=OEVVZU5jWnFJGgAIIQErOA1zOFUFDDszDyARDR0IADNxPzoDAiosIg%3D%3D&operation=1&code=A1o06&nocode=D1o08&loan_action=1&remark=&submit_btn=%E6%8F%90%E4%BA%A4&id="+orderuuid,headers=headers)
	#response1=urllib2.urlopen(req1)
	#print response1.read()
	#response2=urllib2.urlopen("http://"+url+".dev.kdqugou.com/backend/web/index.php?r=pocket%2Fpocket-first-trail&view=other&id="+orderuuid)#初审
	#response3=urllib2.urlopen("http://"+url+".dev.kdqugou.com/backend/web/index.php?r=pocket%2Fpocket-twice-trail&id="+orderuuid)#复审
	
get(inver())
#机审通过，人工初审驳回






#机审，人工初审通过，复审驳回
	
	
	

