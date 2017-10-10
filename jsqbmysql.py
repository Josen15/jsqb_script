#!/usr/bin/env python
#  -*- coding:utf-8 -*-
#通过ssh连接数据库

import sys
import MySQLdb
import json
import chardet
import paramiko

reload(sys)
sys.setdefaultencoding('utf-8')

from sshtunnel import SSHTunnelForwarder  

#dev环境数据库
def dev(exc):
	key_file ='F:\\key\\jsqb_key'
	key = paramiko.RSAKey.from_private_key_file(key_file,password='123456')
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
						   charset='utf8',						   
                           db='jsqb')
	cur = conn.cursor()
	mysqlexc=cur.execute(exc)
	list=cur.fetchmany(mysqlexc)
	return list

	
	
	
def connection():
	key_file ='F:\\key\\jsqb_key'
	key = paramiko.RSAKey.from_private_key_file(key_file,password='123456')
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
						   charset='utf8',						   
                           db='jsqb')
	
	return conn

def connection1():
	key_file ='F:\\key\\jsqb_key'
	key = paramiko.RSAKey.from_private_key_file(key_file,password='123456')
	server=SSHTunnelForwarder(  
			('139.224.22.30', 2022),    
			ssh_username="test",  
			ssh_pkey =key,
			remote_bind_address=('mysql-test', 3306)
	)
		   
	server.start()

	conn = MySQLdb.connect(host='127.0.0.1',              #此处必须是是127.0.0.1  
					       port=server.local_bind_port,  
                           user='jsqb_user',  
                           passwd='jsqb_user', 
						   charset='utf8',
                           db='jsqb')
	
	return conn
	

#线上测试test环境数据库
def test(command):
	key_file ='F:\\key\\jsqb_key'
	key = paramiko.RSAKey.from_private_key_file(key_file,password='123456')
	server=SSHTunnelForwarder(  
			('139.224.22.30', 2022),    
			ssh_username="test",  
			ssh_pkey =key,
			remote_bind_address=('mysql-test', 3306)
	)
		   
	server.start()

	conn = MySQLdb.connect(host='127.0.0.1',              #此处必须是是127.0.0.1  
					       port=server.local_bind_port,  
                           user='jsqb_user',  
                           passwd='jsqb_user', 
						   charset='utf8',
                           db='jsqb')
	cur = conn.cursor()
	mysqlcommand=cur.execute(command)
	list=cur.fetchmany(mysqlcommand)
	return list
	
#print str(test("select name from tb_loan_person where id=3967756")[0][0]).decode("utf-8")

