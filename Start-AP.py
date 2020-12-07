 
#By SxNade
#https://github.com/SxNade
#CONTRIBUTE

from termcolor import colored
import sys 
import os
import time

print(colored("[+]Configuring Fake AP now....!", "green", attrs=['bold']))

ssid = input(colored("[*]Enter The Broadcast Name For your Fake-AP: ", "red", attrs=['bold']))
ifc = input(colored("[*]Enter The Monitor mode Interface For your Fake-AP: ", "red", attrs=['bold']))
cl = input(colored("[*]Enter The Channel For your Fake-AP OR Type anything Between 1-14: ", "red", attrs=['bold']))
ask = input("[?]Do you want a Password for your Fake-AP..(Y/N)")

if int(cl) > 14 or int(cl) < 1:
    print(colored("[!]YOU ENTERED WRONG CHANNEL!!", "red", attrs=['bold']))
    print(colored("[!]Exiting Now....", "red", attrs=['bold']))
    sys.exit(0)


def ap_file():
    if ask == "Y":
        global Password
        Password = input(colored("[*]Enter The Password For your Fake-AP: ", "red", attrs=['bold']))
        print(colored("[+]Making Fake-Ap config File...", "green"))
        time.sleep(3)
        make_pass_wifi_file()
        print(colored("[+]FAKE AP READY TO DEPLOY!!", "green", attrs=['bold']))
        check = input(colored("[?]Do you want to Run the Fake AP Now..(Y/N)", "red", attrs=['bold']))
        if check == "Y":
            start_fake_AP()
        elif check == "N":
            print(colored("[!]YOU SAID NO EXITING NOW...", "red", attrs=['bold']))
            sys.exit(0)
    elif ask == "N":
        print(colored("[+]Making OPEN Fake-AP config file", "green", attrs=['bold']))
        make_open_wifi_file()
        print(colored("[+]FAKE AP READY TO DEPLOY!!", "green", attrs=['bold']))
        check = input(colored("[?]Do you want to Run the Fake AP Now..(Y/N)", "red", attrs=['bold']))
        if check == "Y":
            start_fake_AP()
        elif check == "N":
            print(colored("[!]YOU SAID NO EXITING NOW...", "red", attrs=['bold']))
            sys.exit(0)


def make_open_wifi_file():
        file = open("hostapd.conf", 'w')
        file.write(f"interface={ifc}")
        file.write("\n")
        file.write(f"ssid={ssid}")
        file.write("\n")
        file.write(f"channel={cl}")
        file.write("\n")
        file.write("hw_mode=g")
        file.close()

def make_pass_wifi_file():
        file = open("hostapd.conf", 'w')
        file.write(f"interface={ifc}")
        file.write("\n")
        file.write("driver=nl80211")
        file.write("\n")
        file.write(f"ssid={ssid}")
        file.write("\n")
        file.write("hw_mode=g")
        file.write("\n")
        file.write(f"channel={cl}")
        file.write("\n")
        file.write("macaddr_acl=0")
        file.write("\n")
        file.write("ignore_broadcast_ssid=0")
        file.write("\n")
        file.write("auth_algs=1")
        file.write("\n")
        file.write("wpa=2")
        file.write("\n")
        file.write(f"wpa_passphrase={Password}")
        file.write("\n")
        file.write("wpa_key_mgmt=WPA-PSK")
        file.write("\n")
        file.write("wpa_pairwise=CCMP")
        file.write("\n")
        file.write("wpa_group_rekey=86400")
        file.write("\n")
        file.write("ieee80211n=1")
        file.write("\n")
        file.write("wme_enabled=1")
        file.close()

def start_fake_AP():
    print(colored("<0>ONLINE", "green", attrs=['bold']))
    os.system("hostapd hostapd.conf")

def main():
    ap_file()
main()



def reset():
    os.system("iptables --flush --table nat")
    os.system("iptables --flush FORWARD")
    os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")
    
