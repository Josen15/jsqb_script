#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import MySQLdb
import json
import chardet
from jsqbmysql import dev
import time
from selenium import webdriver
from jsqbmysql import dev,test
from cuserid import searchuid,inver
from selenium.webdriver.support.select import Select

reload(sys)
sys.setdefaultencoding('utf-8')
environment=inver()
driver=webdriver.Firefox()
if environment[0:4]=='test':
	env=environment+".test"
	orderid=test("select id from tb_user_loan_order where user_id="+searchuid()+" order by id desc limit 1")[0][0]
elif environment=="stage":
	env=environment
else:
	env=environment+".dev"
		
	orderid=str(dev("select id from tb_user_loan_order where user_id="+searchuid()+" order by id desc limit 1")[0][0])
url="http://"+env+".kdqugou.com/backend/web/index.php"
	
driver.get(url)
try:
	print driver.find_element_by_id("LoginForm_username")
except:
	print 2
driver.find_element_by_id("LoginForm_username").send_keys("admin")
driver.find_element_by_name("LoginForm[password]").send_keys("123456")
driver.find_element_by_name("submit_btn").click()