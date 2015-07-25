import ConfigParser
import jangopath
import getpass
import os

def add_name():
   print "\nJANGO - CONFIGURATION\n"
   Config = ConfigParser.ConfigParser()
   cfgfile = open(jangopath.CONFIG_PATH, 'w')
   Config.add_section('Person')
   name = raw_input("Enter your name : ")
   uname = raw_input("Enter your email : ")
   pswd = getpass.getpass("Enter your password : ")
   Config.set('Person','name',name)
   Config.set('Person','uname',uname)
   Config.set('Person','pswd',pswd)
   Config.add_section('Location')
   loc = raw_input("Enter your current location (city, country) : ")
   Config.set('Location','name',loc)
   Config.add_section('Directory')
   music = os.getenv("HOME") + "/Music"
   Config.set('Directory','music',music)
   Config.write(cfgfile)
   cfgfile.close()

