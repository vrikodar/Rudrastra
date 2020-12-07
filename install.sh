#!/bin/bash

echo "[*]Installing All The Required Dependencies....!"
echo "[*]You must be on a Linux Host...preferably Debian/Linux"
sudo apt install aircrack-ng
sudo apt install macchanger
sudo apt install hostapd
sudo apt install dnsmasq
sudo apt install python3-pip
sudo apt install iptables
sudo pip3 install termcolor
echo "[*]All the Required Dependencies Have Been Installed....!"

