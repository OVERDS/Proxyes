# -*- coding: utf-8 -*-
import requests, os, socket, sys, json

os.system("clear")

h = "\33[0;32m"
hm = "\33[32;1m"
b = "\33[0;36m"
bm = "\33[36;1m"
m = "\33[31;1m"
mg = "\33[0;31m"
p = "\33[37;1m"
hit = "\33[30;1m"
o = "\33[33;1m"
km = "\33[1;33m"
k = "\33[0;33m"


print mg + """
██████╗ ██████╗  ██████╗ ██╗  ██╗██╗   ██╗███████╗███████╗
██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝██╔════╝██╔════╝
██████╔╝██████╔╝██║   ██║ ╚███╔╝  ╚████╔╝ █████╗  ███████╗
""" + p + """██╔═══╝ ██╔══██╗██║   ██║ ██╔██╗   ╚██╔╝  ██╔══╝  ╚════██║
██║     ██║  ██║╚██████╔╝██╔╝ ██╗   ██║   ███████╗███████║
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚══════╝""" + p
print m + "\t      <"+ km +"☆ "+ p +"Author "+ m +": "+ p +"OverDosis"+ km +" ☆"+ m +">" + p      
print m + "      <"+ km +"☆ "+ p +"Github "+ m +": "+ p +"https://github.com/OVERDS"+ km +" ☆"+ m +">"
print "\t     <"+ km +"☆ "+ p +"Youtube "+ m +":"+ p +" Over Coding "+ km +"☆"+ m +">" + p

print m + "\n{"+ km +"!"+ m +"}"+ p +" Contoh "+ hm +"÷>"+ p +" indosatooredoo.com"
value = raw_input(m + "{"+ km +"?"+ m +"}"+ p +" Masukkan url "+ hm +"÷> "+ p)
hilang = value.replace("https://", "").replace("http://", "").replace("www.", "")
url = "https://crt.sh"
data = {
  "q" : hilang,
  "output" : "json"
}

r = requests.get(url, params=data)
j = json.loads(r.text)
save = open("/sdcard/proxy.txt", "w")


for i in j:
  try:
    domain = i["name_value"]
    ip = socket.gethostbyname(domain)
    response = r.status_code
    save.write("Domain : " + domain + "\nIP : " + ip)
    
    print hm + "\nDomain "+ bm +":"+ m +" " + domain
    print hm + "IP     "+ bm +":"+ p +" " +  ip
    print hm + "Status "+ bm +":"+ km +" " + str(response) + p
    print "+++++++++++++++++++++++++++++++"
    
  except: 
    pass

print m + "{"+ km +"+"+ m +"} "+ p +"Tersimpan di /sdcard/proxy.txt"
  
save.close()
  




  
  