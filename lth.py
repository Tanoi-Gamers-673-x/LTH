#Script use in Application Termux Terminal
import os,sys
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############
#CodeLoad
os.system("clear")
print
os.system("figlet LTH  |lolcat")
print "\033[1m\033[32mPython Programing By Tanoi Gamers"
print "\033[0m"
print "[                    ] 0% "
time.sleep(5)
print "[=====               ] 25%"
time.sleep(5)
print "[==========          ] 50%"
time.sleep(5)
print "[===============     ] 75%"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)
os.system("pkg install ruby -y")
os.system("gem install lolcat -y")

A = raw_input("Please press [enter] to continue..")

print
print
os.system("clear")
os.system("figlet LTH | lolcat")
p = raw_input("root@L3MONTEAM~#")
print " [01] Androbugs_Framework"
print " [02] Metasploit"
print " [03] weeman"
print " [04] Ngrok"
print " [05] METASEC"
print " [06] Lazymux"
print " [07] Or my other scripts"
print " [00] Exit To Home"
print
py = raw_input("root@L3MONTEAM~#")

if py == "1" or py == "01":
 os.system("clear")
 os.system("figlet Androbugs")
 print "\033[1m\033[35m Python Progarming By Tanoi Gamers"
 os.system("git clone https://github.com/AndroBugs/AndroBugs_Framework.git")
 os.system("cat A.txt")
 os.system("cd /$HOME/LTH")
 os.system("mv AndroBugs_Framework /$HOME")
 os.system("cd AndroBugs_Framework")

elif py == "02" or py == "2":
 os.system("clear")
 os.system("figlet Metasploit")
 print "\033[1m\033[35m Python Programing By Tanoi Gamers"
 os.system("cd /$HOME/LTH")
 os.system("bash meta.sh")
elif py == "03" or py == "3":
 os.system("clear")
 os.system("figlet weeman")
 print "\033[1m\033[35m Python Progarming By Tanoi Gamers"
 os.system("git clone https://github.com/evait-security/weeman")
 os.system("mv weeman /$HOME")
 os.system("cd /$HOME/weeman")
 os.system("python2 weeman.py")
elif py == "04" or py == "4":
 os.system("clear")
 os.system("figlet Ngrok")
 print "\033[1m\033[35m Python Progarming By Tanoi Gamers"
 os.system("cp -r ngrok /$HOME")
 os.system("cat N.txt")
elif py == "05" or py == "5":
 os.system("clear")
 os.system("figlet METASEC")
 print "\033[1m\033[35m Python Progarming By Tanoi Gamers"
 os.system("git clone https://github.com/MALW4R3/METASEC")
 os.system("cd /$HOME/LTH")
 os.system("mv METASEC /$HOME")
 os.system("cd METASEC")
 os.system("bash setup.sh")
 os.system("metasec")
elif py == "06" or py == "6":
 os.system("clear")
 os.system("figlet Lazymux")
 print "\033[1m\033[35m Python Progarming By Tanoi Gamers"
 os.system("git clone git clone https://github.com/Gameye98/Lazymux")
 os.system("cp -r Lazymux")
 os.system("cd /$HOME/Lazymux")
 os.system("python2 lazymux.py")
elif py == "07" or py == "7":
 os.system("clear")
 os.system("figlet My Script")
 print "\033[1m\033[35m Python Progarming By Tanoi Gamers"
 print
 print
 print "\033[1m\033[35m [01]>[TOOL673x]"
 print "\033[1m\033[35m [02]>[Kalinux-673x]"
 print "\033[1m\033[35m [03]>[LOAD-Command]"
 print "\033[1m\033[35m [04]>[DDOSTN]"
 print "\033[1m\033[35m [99]>[BACK TO MAIN MANU]"
 print
 FT = raw_input("Pleas [Enter] to continue..")

 h2 = raw_input("root@L3MONTEAM~#")
 if h2 == "01" or h2 == "1":
  os.system("clear")
  os.system("figlet TOOL673X")
  print "\033[1m\033[35m Python Progarming By Tanoi Gamers"
  os.system("git clone https://github.com/Tanoi-Gamers-673-x/TOOL673X")
  os.system("mv TOOL673X /$HOME")
  os.system("cd /$HOME/TOOL673X")
  os.system("bash install.sh")
  os.system("clear")
  os.system("python2 Tools-Hack-673x.py")
 elif h2 == "02" or h2 == "2":
  os.system("clear")
  os.system("figlet Kalinux-673x")
  print "\033[1m\033[35m Python Programing By Tanoi Gamers"
  os.system("git clone https://github.com/Tanoi-Gamers-673-x/Kalinux-673x")
  os.system("mv Kalinux-673x /$HOME")
  os.system("cd /$HOME")
  os.system("cd Kalinux-673x")
  os.system("python2 Kalinux-673x.py")
 elif h2 == "03" or h2 == "3":
  os.system("clear")
  os.system("figlet LOAD-Command")
  print "\033[1m\033[35m Python Progarming By Tanoi Gamers"
  os.system("git clone https://github.com/Tanoi-Gamers-673-x/LOAD-Command")
  os.system("mv LOAD-Command /$HOME")
  os.system("cd /$HOME/LOAD-Command")
  os.system("python2 loadcommand.py")
 elif h2 == "04" or h2 =="4":
  os.system("clear")
  os.system("figlet DDOSTN")
  print "\033[1m\033[35m Python Progarming By Tanoi Gamers"
  os.system("git clone https://github.com/Tanoi-Gamers-673-x/DDOSTN")
  os.system("mv DDOSTN /$HOME")
  os.system("cd /$HOME/DDOSTN")
  os.system("python2 DDOSTN.py")
 elif h2 == "99":
  os.system("cd /$HOME/LTH")
  os.system("python2 date.py")
elif py == "00" or py == "0":
 os.system("clear")
 os.system("figlet BYE BYE | lolcat")
