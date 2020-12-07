from termcolor import colored
import os
import sys

if len(sys.argv) != 3:
	print(colored("[*]Usage python3 Internet&Interface.py <internet-interface> <FAKE-AP-INTERFACE>", "red"))
	sys.exit(0)


print(colored("[+]This Script will Configure The IP Tables Rules and interfaces.....!", "green", attrs=['bold']))

inter_ifc = sys.argv[1]
ap_ifc = sys.argv[2]

mon_ifc = ap_ifc + "mon"

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


def mac_spoof():
    ans = input("Do you want to Randemize Your MAC-address....(Y/N)!")
    if ans == "Y":
        os.system(f"ifconfig {mon_ifc} down")
        os.system(f"macchanger -r {mon_ifc}")
        os.system(f"ifconfig {mon_ifc} up")
        print(colored("Succesfully Randemized MAC-address for Fake-AP"))
        sys.exit(0)

def main():
    forward(inter_ifc, ap_ifc)
    mac_spoof()

main()
