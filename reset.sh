#!/bin/bash

 
#By SxNade
#https://github.com/SxNade
#CONTRIBUTE

iptables --flush --table nat
iptables --flush FORWARD
echo 0 > /proc/sys/net/ipv4/ip_forward
rm hostapd.conf
rm dnsmasq.conf
rm fakehosts.conf
