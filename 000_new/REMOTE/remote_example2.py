# pip install wmi
import wmi

ip = "192.168.1.1"
username = "username"
password = "“password"
from socket import *
try:
    print("Establishing connection to %s" %ip)
    connection = wmi.WMI(ip, user=username, password=password)
    print("Connection established")
except wmi.x_wmi:
    print("Your Username and Password of "+getfqdn(ip)+" are wrong.")