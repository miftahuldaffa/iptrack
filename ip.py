#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
IP Tracking - Tools Termux
This project was created by Dfv47 with Black Codet Crush. 
Copyright 2k19 @m_d4fv
'''

#color
A='\033[1;30m'
W='\033[1;37m'
N='\033[0m'
R='\033[31m'
G='\033[1;32m'
B='\033[34m'
Y='\033[1;33m'

try:
        import requests,json,os,urllib,sys,time,readline,rlcompleter
except Exception as F:
        exit("[ModuleErr] %s"%(F))

if sys.version[0] in '2':
        exit(R+" [Sorry] use python version 3")

def main():
	print (G+"\t   ___         _____                 _    _           ") 
	print (G+"\t  |   | ___   |_   _| ___  ___  ___ | |_ |_| ___  ___ ") 
	print (G+"\t  |- -|| . |    | |  |  _|| .'||  _|| '_|| ||   || . |") 
	print (G+"\t  |___||  _|    |_|  |_|  |__,||___||_,_||_||_|_||_  |") 
	print (G+"\t       |_| "+R+"@"+W+"Dfv47               "+R+"@"+W+"BlackCoderCrush"+G+" |___|	") 
	print (W+"\n\t  1"+G+"]"+W+" Check my IP adress.")
	print (W+"\t  2"+G+"]"+W+" Tracking location IP adress.\n") 
	pilih = input(R+'     ┌─'+B+'['+R+'Ip-Tracking'+A+'@'+G+'Dfv47'+B+']'+R+'-'+B+'['+G+'BlackCoderCrush'+B+']\n     '+R+'└─────'+Y+'▶'+W+' # ')
	if "1" in pilih:
	    print (W+"\n  ["+G+"*"+W+"] Checking your public IP") 
	    print (W+"  ["+G+"+"+W+"] Your public IP : "+G+requests.get('http://ip-api.com/json/').json()["query"]) 
	    print (W+"  ["+G+"#"+W+"] Finished.") 
	    input(W+"  ["+G+"?"+W+"] Press enter to menu")
	    os.system('clear')
	    main()
	elif "2"  in pilih:
		print (W+"\n  ["+G+"*"+W+"] Dump Location From Public IP") 
		print (W+"   1"+G+"]"+W+" Manual") 
		print (W+"   2"+G+"]"+W+" Massal\n") 
		t=input(W+'  ['+G+'?'+W+'] Choose : ')
		if "1" in t:
			ip=input(W+'  ['+G+'#'+W+'] IP : ')
			print (W+"  ["+G+"*"+W+"] Tracking IP : "+G+ip+"") 
			rk=requests.get('http://ipapi.co/'+ip+'/json/')
			r=json.loads(rk.text)
			try:								
				print (W+"\n  ["+G+"+"+W+"] IP\t\t:"+G+"",r["ip"]) 
				print (W+"  ["+G+"+"+W+"] City\t\t:"+G+"",r["city"]) 
				print (W+"  ["+G+"+"+W+"] Region Code\t:"+G+"",r["region_code"]) 
				print (W+"  ["+G+"+"+W+"] Country\t\t:"+G+"",r["country"]) 
				print (W+"  ["+G+"+"+W+"] Country Name\t:"+G+"",r["country_name"]) 
				print (W+"  ["+G+"+"+W+"] Region\t\t:"+G+"",r["region"]) 
				print (W+"  ["+G+"+"+W+"] Lang\t\t:"+G+"",r["languages"]) 
				print (W+"  ["+G+"+"+W+"] Calling Code\t:"+G+"",r["country_calling_code"]) 
				print (W+"  ["+G+"+"+W+"] Utc Offset\t:"+G+"",r["utc_offset"]) 
				print (W+"  ["+G+"+"+W+"] Continent Code\t:"+G+"",r["continent_code"]) 
				print (W+"  ["+G+"+"+W+"] Currency\t\t:"+G+"",r["currency"]) 
				print (W+"  ["+G+"+"+W+"] Latitude\t\t:"+G+"",r["latitude"]) 
				print (W+"  ["+G+"+"+W+"] Longitude\t\t:"+G+"",r["longitude"]) 
				print (W+"  ["+G+"+"+W+"] Timezone\t\t:"+G+"",r["timezone"]) 
				print (W+"  ["+G+"+"+W+"] Postal\t\t:"+G+"",r["postal"]) 
				print (W+"  ["+G+"+"+W+"] In Eu\t\t:"+G+"",r["in_eu"]) 
				print (W+"\n  ["+G+"#"+W+"] Finished") 
				input(W+"  ["+G+"?"+W+"] Press enter to menu")
				os.system('clear')
				main()
			except:
				print (W+"  ["+R+"-"+W+"] IP\t\t: "+R+"Unkwon") 
				print (W+"\n  ["+G+"#"+W+"] Finished") 
				input(W+"  ["+G+"?"+W+"] Press enter to menu")
				os.system('clear')
				main()
		elif "2" in t:
			ip=input(W+'  ['+G+'#'+W+'] IP List : ')
			try:
				vk=open(ip).readlines()
				vko=len(vk)
				vki=open(ip)
				for k in range(vko):
					word=vki.readline().replace('\n','')
					rk=requests.get('http://ipapi.co/'+word+'/json/')
					r=json.loads(rk.text)
					try:
						print (W+"\n  ["+G+"*"+W+"] Tracking IP "+W+R+word+"") 
						print (W+"\n  ["+G+"+"+W+"] IP\t\t:"+G+"",r["ip"])
						print (W+"  ["+G+"+"+W+"] City\t\t:"+G+"",r["city"]) 
						print (W+"  ["+G+"+"+W+"] Region Code\t:"+G+"",r["region_code"]) 
						print (W+"  ["+G+"+"+W+"] Country\t\t:"+G+"",r["country"]) 
						print (W+"  ["+G+"+"+W+"] Country Name\t:"+G+"",r["country_name"]) 
						print (W+"  ["+G+"+"+W+"] Region\t\t:"+G+"",r["region"]) 
						print (W+"  ["+G+"+"+W+"] Lang\t\t:"+G+"",r["languages"]) 
						print (W+"  ["+G+"+"+W+"] Calling Code\t:"+G+"",r["country_calling_code"]) 
						print (W+"  ["+G+"+"+W+"] Utc Offset\t:"+G+"",r["utc_offset"]) 
						print (W+"  ["+G+"+"+W+"] Continent Code\t:"+G+"",r["continent_code"]) 
						print (W+"  ["+G+"+"+W+"] Currency\t\t:"+G+"",r["currency"]) 
						print (W+"  ["+G+"+"+W+"] Latitude\t\t:"+G+"",r["latitude"]) 
						print (W+"  ["+G+"+"+W+"] Longitude\t\t:"+G+"",r["longitude"]) 
						print (W+"  ["+G+"+"+W+"] Timezone\t\t:"+G+"",r["timezone"]) 
						print (W+"  ["+G+"+"+W+"] Postal\t\t:"+G+"",r["postal"]) 
						print (W+"  ["+G+"+"+W+"] In Eu\t\t:"+G+"",r["in_eu"]) 
					except:
					    print (W+"  ["+R+"-"+W+"] IP\t\t: "+R+"Unknown") 
				print (W+"\n  ["+G+"#"+W+"] Finished") 
				input(W+"  ["+G+"?"+W+"] Press enter to menu")
				os.system('clear')
				main()
			except:
				print (W+"\n  ["+R+"-"+W+"] List "+R+"'"+ip+"'"+W+" Not Found") 
				print (W+"  ["+R+"-"+W+"] Please edit list (nano list.txt) and input your IP") 				
				input(W+"  ["+G+"?"+W+"] Press enter to menu")
				os.system('clear')
				main()
		else: 
		    print (W+"\n  ["+R+"-"+W+"] Wrong Input !!!")
		    time.sleep(2) 
		    os.system('clear')
		    main() 
		      				
if __name__ == "__main__":
	os.system('clear') 
	main()
