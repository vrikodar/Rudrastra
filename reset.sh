#!/bin/bash

 
#By SxNade
#https://github.com/SxNade/Rudrastra
#CONTRIBUTE

echo [*]Resetting all the changes made......
iptables --flush --table nat
iptables --flush FORWARD
echo 0 > /proc/sys/net/ipv4/ip_forward
echo [*]Deleting Configuration Files.....
rm hostapd.conf
rm dnsmasq.conf
rm fakehosts.conf
echo [+]The Reset Was Successfully Completed...
echo [+]Consider Restarting the Networking Service with "service networking restart"..
echo [+] Also Reset the monitor mode AP interface using "airmon-ng stop <mon-interface>"
