#!/usr/bin/python 
# -*- coding:utf-8 -*-
#连接linux
import paramiko,os,chardet
#from jsqbmysql import command

#command("select order_id,user_id from tb_financial_loan_record order by id desc limit 15")


def loan(environment):#先申请成功复审通过

#生成打款记录

	
	key_file ='F:\\key\\jsqb_key'
	key = paramiko.RSAKey.from_private_key_file(key_file,password='123456')
	ssh = paramiko.SSHClient()

	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	if environment[0:4]=="test":
		ssh.connect('139.224.22.30',2022,'test',pkey=key)
		stdin, stdout, stderr = ssh.exec_command('cd /code/test;cd '+environment+';php yii ygd-check/ygd-zc-cw-check')
	else:
		ssh.connect('dev.kdqugou.com',1022,'test',pkey=key)
		stdin, stdout, stderr = ssh.exec_command('cd /code/dev;cd '+environment+';php yii ygd-check/ygd-zc-cw-check')
	info=stdout.read()
	if ((info[26:64])=="ygd-check/ygd-zc-cw-check begin action")&(info[-37:-1]=="ygd-check/ygd-zc-cw-check end action"):
		pass
	else:
		print info

#打款脚本
	if environment[0:4]=="test":
		ssh.connect('139.224.22.30',2022,'test',pkey=key)
		stdin, stdout, stderr = ssh.exec_command('cd /code/test;cd '+environment+';php yii financial-loan-pay/lite-withdraw-fsyf')
	else:
		ssh.connect('dev.kdqugou.com',1022,'test',pkey=key)
		stdin, stdout, stderr = ssh.exec_command('cd /code/dev;cd '+environment+';php yii financial-loan-pay/lite-withdraw-fsyf')
	
	info2=(stdout.read()).decode('UTF-8').encode('GBK')#
	if (info2[26:76]=='financial-loan-pay/lite-withdraw-fsyf begin action')&((info2[90:91])!=("0".decode('UTF-8').encode('GBK'))):#改单数
		pass
	else:
		print info2#.decode('UTF-8')#.encode('GBK')

	
def debit(ambient):#扣款回调流程
#计算零钱包利息或者违约金,并自动提交订单，每天计算逾期订单滞纳金，到期发起自动扣款申请，更新逾期天数等

	key_file ='F:\\key\\jsqb_key'
	key = paramiko.RSAKey.from_private_key_file(key_file,password='123456')
	ssh = paramiko.SSHClient()

	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	if ambient[0:4]=="test":
		ssh.connect('139.224.22.30',2022,'test',pkey=key)
		stdin, stdout, stderr = ssh.exec_command('cd /code/test;cd '+ambient+';php yii overdue-calculate/calculate-late-money')
	else:
		ssh.connect('dev.kdqugou.com',1022,'test',pkey=key)
		stdin, stdout, stderr = ssh.exec_command('cd /code/dev;cd '+ambient+';php yii overdue-calculate/calculate-late-money')
	
	#stdin, stdout, stderr = ssh.exec_command('cd /code/dev;cd '+ambient+';php yii overdue-calculate/calculate-late-money')
	info3=stdout.read()
	if ((info3[26:75])=="overdue-calculate/calculate-late-money begin action")&(info3[-48:-1]=="overdue-calculate/calculate-late-money end action"):
		pass
	else:
		pass#print info3
#生成扣款记录脚本
	if ambient[0:4]=="test":
		ssh.connect('139.224.22.30',2022,'test',pkey=key)
		stdin, stdout, stderr = ssh.exec_command('cd /code/test;cd '+ambient+';php yii overdue-calculate/generate-debit-record')
	else:
		ssh.connect('dev.kdqugou.com',1022,'test',pkey=key)
		stdin, stdout, stderr = ssh.exec_command('cd /code/dev;cd '+ambient+';php yii overdue-calculate/generate-debit-record')
	#stdin, stdout, stderr = ssh.exec_command('cd /code/dev;cd '+ambient+';php yii overdue-calculate/generate-debit-record')
	info4=stdout.read()
	if ((info4[26:74])=="overdue-calculate/generate-debit-record begin action")&(info4[-47:-1]=="overdue-calculate/generate-debit-record end action"):
		pass
	else:
		pass#print info4
	
#主动扣款脚本
	if ambient[0:4]=="test":
		ssh.connect('139.224.22.30',2022,'test',pkey=key)
		stdin, stdout, stderr = ssh.exec_command('cd /code/test;cd '+ambient+';php yii ygd-reject/auto-debit')
	else:
		ssh.connect('dev.kdqugou.com',1022,'test',pkey=key)
		stdin, stdout, stderr = ssh.exec_command('cd /code/dev;cd '+ambient+';php yii ygd-reject/auto-debit')
	#stdin, stdout, stderr = ssh.exec_command('cd /code/dev;cd '+ambient+';php yii ygd-reject/auto-debit-five')#暂时加five
	info5=stdout.read().decode('UTF-8').encode('GBK')
	if ((info5[26:60])=="ygd-reject/auto-debit begin action")&(info5[73:74]!=("0".decode('UTF-8').encode('GBK')))&(info5[-33:-1]=='ygd-reject/auto-debit end action'):#改单数
		pass
	else:
		print info5
def overdue(env):
	key_file ='F:\\key\\jsqb_key'
	key = paramiko.RSAKey.from_private_key_file(key_file,password='123456')
	ssh = paramiko.SSHClient()
	
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	
	if env[0:4]=="test":
		ssh.connect('139.224.22.30',2022,'test',pkey=key)
		stdin, stdout, stderr = ssh.exec_command('cd /code/test;cd '+env+';php yii overdue-calculate/test-calculate')
	else:
		ssh.connect('dev.kdqugou.com',1022,'test',pkey=key)
		stdin, stdout, stderr = ssh.exec_command('cd /code/dev;cd '+env+';php yii overdue-calculate/test-calculate')

	info3=stdout.read()

	if ((info3[26:75])=="overdue-calculate/calculate-late-money begin action")&(info3[-48:-1]=="overdue-calculate/calculate-late-money end action"):
		pass
	else:
		pass#print info3
def branch(env):
	key_file ='F:\\key\\jsqb_key'
	key = paramiko.RSAKey.from_private_key_file(key_file,password='123456')
	ssh = paramiko.SSHClient()
	
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	if env[0:4]=="test":
		ssh.connect('139.224.22.30',2022,'test',pkey=key)
		stdin, stdout, stderr = ssh.exec_command('cd /code/test;ls -l')
		return stdout.read()
	else:
		ssh.connect('dev.kdqugou.com',1022,'test',pkey=key)
		stdin, stdout, stderr = ssh.exec_command('cd /code/dev;ls -l')
		return stdout.read()


	

