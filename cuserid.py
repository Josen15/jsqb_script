#!/usr/bin/env python
#  -*- coding:utf-8 -*-
import sys
import MySQLdb
import json
import chardet
from jsqbmysql import dev,test
from jsqblinux import branch
reload(sys)
sys.setdefaultencoding('utf-8')
#改用户手机号13564789331   13061986932  18221551680
#mobile="15138460851"
#mobile="13564789331"
mobile="13861068037"

#改环境名称
environment="dev-ps-900-new-we-ug0sn1"
				
def searchuid():
	if environment[0:4]=="test":
		
		try:
			return str(test("select id from tb_loan_person where phone="+mobile+" order by id desc limit 1")[0][0])
		except IndexError:
			print u"用户不存在"
	else:
		
		try:
			return str(dev("select id from tb_loan_person where phone="+mobile+" order by id desc limit 1")[0][0])
		except IndexError:
			print u"用户不存在"

	
#dev环境名称
def inver():
	if environment in branch(environment):
		return environment
	else:
		print u"分支不存在"




	

	