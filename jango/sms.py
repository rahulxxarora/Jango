import os
import sys
import ConfigParser
import jangopath
import requests

Config = ConfigParser.ConfigParser()
Contact = ConfigParser.ConfigParser()
f = open('/Users/coderahul/Desktop/JANGO/jango/ans.txt','w')

try:
   Config.read(jangopath.CONFIG_PATH)
   Contact.read(jangopath.CONTACTS_PATH)
except:
   print "Couldn't read config file."

uname = Config.get('Person', 'phone')
pwd = Config.get('Person', 'ppswd')

flag = 0
msg = ""
contact = ""

for arg in sys.argv:
   if flag==1:
      msg = msg + arg + " "
   if arg.lower()=="saying":
      flag = 1 

msg = msg.strip()
flag = 0

for arg in sys.argv:
   if flag==1:
      contact = arg
      break
   if arg.lower()=="to":
      flag = 1 

try:
   to = Contact.get('Person', contact.lower())
except:
   cfgfile = open(jangopath.CONTACTS_PATH, 'w')
   num = raw_input("Contact does'nt exists. Enter number : ")
   Contact.set('Person',contact.lower(),num)
   to = num
   Contact.write(cfgfile)
   cfgfile.close()

msg = msg.replace(" ", "+")
#print "curl --get --include \'https://freesms8.p.mashape.com/index.php?msg=" + msg + "&phone=" + to + "&pwd=" + pwd + "&uid=" + uname + "\' -H \'X-Mashape-Key: Sr71TH5PRmmshuOGsE2LNaU3UtQ6p1B3609jsn72dtTvwRkAhb\' >/dev/null 2>&1"
try:
   requests.get("http://www.smszone.in/sendsms.asp?page=SendSmsBulk&username=918010969391&password=43BF&number=" + to + "&message=" + msg.capitalize())
   f.write("Message Sent")
except:
   print "Something went wrong."

f.close()



      
