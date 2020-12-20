#By SxNade
#https://github.com/SxNade
#CONTRIBUTE

from termcolor import colored
import sys 
import os
import time
#importing the required Libraries
ap = '''
 ____  _   _ ____  ____      _    ____ _____ ____      _           _    ____  
|  _ \| | | |  _ \|  _ \    / \  / ___|_   _|  _ \    / \         / \  |  _ \ 
| |_) | | | | | | | |_) |  / _ \ \___ \ | | | |_) |  / _ \ _____ / _ \ | |_) |
|  _ <| |_| | |_| |  _ <  / ___ \ ___) || | |  _ <  / ___ \_____/ ___ \|  __/ 
|_| \_\\___/|____/|_| \_\/_/   \_\____/ |_| |_| \_\/_/   \_\   /_/   \_\_|    
                                                                              '''

print(ap)

print(colored("[+]Configuring Fake AP now....!", "green", attrs=['bold']))

#Receiving the User Input For Properties of Access Point..
ssid = input(colored("[*] Enter The Broadcast Name For your Fake-AP: ", "red"))
ifc = input(colored("[*] Enter The Monitor mode Interface For your Fake-AP: ", "red"))
cl = input(colored("[*] Enter The Channel For your Fake-AP OR Type anything Between 1-14: ", "red"))
ask = input("\n\n[*]Do you want a Password for your Fake-AP..(Y/N)")

#Conditional Statement For Handelling Error In-case User INPUT is Invalid
if int(cl) > 14 or int(cl) < 1:
    print(colored("[!]YOU ENTERED WRONG CHANNEL!!", "red", attrs=['bold']))
    print(colored("[!]Exiting Now....", "red", attrs=['bold']))
    sys.exit(0)

#A Function That will Both make the Fake-ap file and also run the Fake-ap..This Function will also ask the user If they want a OPEN Wifi or WPA2-Wifi
def ap_file():
    if ask == "Y":
   #Making Password a Global Variable as it is used in Inclosed in a Function Already and is Also Used in Other Two Functions Used For Creating the Fake-AP
        global Password
        Password = input(colored("[*] Enter The Password For your Fake-AP: "))
        print(colored("\n[+]Making Fake-Ap config File...", "green"))
        time.sleep(3)
        make_pass_wifi_file()
        print(colored("\n\n[+]FAKE AP READY TO DEPLOY!!", "green", attrs=['bold']))
        check = input(colored("\n[!]Do you want to Run the Fake AP Now..(Y/N)", "red", attrs=['bold']))
        if check == "Y":
            start_fake_AP()
        elif check == "N":
            print(colored("[!]YOU SAID NO EXITING NOW...", "red", attrs=['bold']))
            sys.exit(0)
    elif ask == "N":
        print(colored("\n[+]Making OPEN Fake-AP config file", "green", attrs=['bold']))
        make_open_wifi_file()
        print(colored("\n\n[+]FAKE AP READY TO DEPLOY!!", "green", attrs=['bold']))
        check = input(colored("[*]Do you want to Run the Fake AP Now..(Y/N)", "red", attrs=['bold']))
        if check == "Y":
            start_fake_AP()
        elif check == "N":
            print(colored("[!]YOU SAID NO EXITING NOW...", "red", attrs=['bold']))
            sys.exit(0)


#This Function will make File for a OPEN Wifi that is with no Password..!
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

#This Function will make a File for a WPA2 Wifi which has the Password Specified By the User..!
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

#This Function will Finally Run the FAKE-ACCESS-POINT
def start_fake_AP():
    print(colored("<0>ONLINE", "green", attrs=['bold']))
    os.system("hostapd hostapd.conf")

#Main Function That will Run the Whole Script
def main():
    ap_file()

#Finally Calling the Main Function to Run the Program..!
main()



#This Function will be used Later in a UPDATE that will Be made SOON..!
def reset():
    os.system("iptables --flush --table nat")
    os.system("iptables --flush FORWARD")
    os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")
    
