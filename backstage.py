#!/usr/bin/env python
#  -*- coding:utf-8 -*-

import time
from selenium import webdriver
from jsqbmysql import dev,test
from cuserid import searchuid,inver
from selenium.webdriver.support.select import Select

def list(n):
	m=driver.find_elements_by_xpath('//*[@id="cpcontainer"]/table/tbody/tr/td[1]')
	list=[]
	for x in m:
		list.append(x.text)
	return list.index(n)
	
def verify(environment):
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

	driver.find_element_by_id("LoginForm_username").send_keys("admin")
	driver.find_element_by_name("LoginForm[password]").send_keys("123456")
	driver.find_element_by_name("submit_btn").click()
	driver.implicitly_wait(3)
	driver.find_element_by_id("header_loan").click()
	
	driver.find_element_by_partial_link_text(u"待机审订单列表").click()
	time.sleep(1)

	#跳过机审
	driver.switch_to.frame("main")
	#driver.switch_to.default_content()#切回主文档
	m=driver.find_elements_by_xpath('//*[@id="cpcontainer"]/table/tbody/tr/td[1]')
	list=[]
	for x in m:
		list.append(x.text)
	print list
	n=list.index(str(orderid))
	driver.find_element_by_xpath('//*[@id="cpcontainer"]/table/tbody/tr[%d]/th[10]/a[2]'%(n+2)).click()
	time.sleep(1)
	t=driver.switch_to_alert()
	t.accept()
	driver.switch_to.default_content()
	#人工初审
	driver.find_element_by_partial_link_text(u"人工初审").click()
	time.sleep(1)
	driver.switch_to.frame("main")
	m=driver.find_elements_by_xpath('//*[@id="cpcontainer"]/table/tbody/tr/td[1]')
	list=[]
	for x in m:
		list.append(x.text)
	n=list.index(str(orderid))
	driver.find_element_by_xpath('//*[@id="cpcontainer"]/table/tbody/tr[%d]/th[12]/a[2]'%(n+2)).click()#//*[@id="cpcontainer"]/table/tbody/tr[4]/th[12]/a[2]
	js="var q=document.documentElement.scrollTop=10000"	                
	driver.execute_script(js)
	time.sleep(1)
	driver.find_element_by_id("submit_btn").click()
	driver.switch_to.default_content()
	time.sleep(1)
	#人工复审
	driver.find_element_by_partial_link_text(u"人工复审").click()
	time.sleep(1)
	driver.switch_to.frame("main")
	m=driver.find_elements_by_xpath('//*[@id="cpcontainer"]/table/tbody/tr/td[1]')
	list=[]
	for x in m:
		list.append(x.text)
	n=list.index(str(orderid))
	driver.find_element_by_xpath('//*[@id="cpcontainer"]/table/tbody/tr[%d]/th[12]/a[2]'%(n+2)).click()
	time.sleep(1)
	js="var q=document.documentElement.scrollTop=10000"	                
	driver.execute_script(js)
	time.sleep(1)
	driver.find_element_by_name("submit_btn").click()
	driver.switch_to.default_content()
	time.sleep(1)
	driver.quit()
def first_refusal(environment,status):
	
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

	driver.find_element_by_id("LoginForm_username").send_keys("admin")
	driver.find_element_by_name("LoginForm[password]").send_keys("123456")
	driver.find_element_by_name("submit_btn").click()
	time.sleep(1)
	driver.find_element_by_id("header_loan").click()
	


	#跳过机审
	driver.find_element_by_partial_link_text(u"待机审订单列表").click()
	time.sleep(1)
	driver.switch_to.frame("main")
	#driver.switch_to.default_content()#切回主文档
	m=driver.find_elements_by_xpath('//*[@id="cpcontainer"]/table/tbody/tr/td[1]')
	list=[]
	for x in m:
		list.append(x.text)
	n=list.index(orderid)
	driver.find_element_by_xpath('//*[@id="cpcontainer"]/table/tbody/tr[%d]/th[10]/a[2]'%(n+2)).click()
	time.sleep(1)
	t=driver.switch_to_alert()
	t.accept()
	driver.switch_to.default_content()
	#人工初审
	driver.find_element_by_partial_link_text(u"人工初审").click()
	time.sleep(1)
	driver.switch_to.frame("main")
	m=driver.find_elements_by_xpath('//*[@id="cpcontainer"]/table/tbody/tr/td[1]')
	list=[]
	for x in m:
		list.append(x.text)
	n=list.index(orderid)
	driver.find_element_by_xpath('//*[@id="cpcontainer"]/table/tbody/tr[%d]/th[11]/a[2]'%(n+2)).click()
	js="var q=document.documentElement.scrollTop=20000"	                
	driver.execute_script(js)
	time.sleep(1)
	driver.find_elements_by_name("operation")[1].click()
	time.sleep(2)
	sel = driver.find_element_by_name("loan_action")
	if status==-1:
		Select(sel).select_by_value('-1')	
	elif status==1:
		pass
	elif status==2:
		Select(sel).select_by_value('2')
	driver.find_element_by_id("review-remark").send_keys(status)
	driver.find_element_by_id("submit_btn").click()
	driver.qiut()
def second_refusal(environment):
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

	driver.find_element_by_id("LoginForm_username").send_keys("admin")
	driver.find_element_by_name("LoginForm[password]").send_keys("123456")
	driver.find_element_by_name("submit_btn").click()
	time.sleep(1)
	driver.find_element_by_id("header_loan").click()
	
	driver.find_element_by_partial_link_text(u"待机审订单列表").click()
	time.sleep(1)

	#跳过机审
	"""driver.switch_to.frame("main")
	#driver.switch_to.default_content()#切回主文档
	m=driver.find_elements_by_xpath('//*[@id="cpcontainer"]/table/tbody/tr/td[1]')
	list=[]
	for x in m:
		list.append(x.text)
	n=list.index(str(orderid))
	driver.find_element_by_xpath('//*[@id="cpcontainer"]/table/tbody/tr[%d]/th[10]/a[2]'%(n+2)).click()
	time.sleep(1)
	t=driver.switch_to_alert()
	t.accept()
	driver.switch_to.default_content()
	#人工初审
	driver.find_element_by_partial_link_text(u"人工初审").click()
	time.sleep(1)
	driver.switch_to.frame("main")
	m=driver.find_elements_by_xpath('//*[@id="cpcontainer"]/table/tbody/tr/td[1]')
	list=[]
	for x in m:
		list.append(x.text)
	n=list.index(str(orderid))
	driver.find_element_by_xpath('//*[@id="cpcontainer"]/table/tbody/tr[%d]/th[11]/a[2]'%(n+2)).click()
	js="var q=document.documentElement.scrollTop=10000"	                
	driver.execute_script(js)
	time.sleep(1)
	driver.find_element_by_id("submit_btn").click()
	driver.switch_to.default_content()
	time.sleep(1)"""
	#人工复审
	driver.find_element_by_partial_link_text(u"人工复审").click()
	time.sleep(1)
	driver.switch_to.frame("main")
	m=driver.find_elements_by_xpath('//*[@id="cpcontainer"]/table/tbody/tr/td[1]')
	list=[]
	for x in m:
		list.append(x.text)
	n=list.index(str(orderid))
	driver.find_element_by_xpath('//*[@id="cpcontainer"]/table/tbody/tr[%d]/th[12]/a[2]'%(n+2)).click()
	time.sleep(1)
	js="var q=document.documentElement.scrollTop=10000"	                
	driver.execute_script(js)
	time.sleep(1)
	driver.find_elements_by_name("operation")[1].click()
	driver.find_element_by_name("remark").send_keys(u"无")
	driver.find_element_by_name("submit_btn").click()
	driver.quit()

	
	
