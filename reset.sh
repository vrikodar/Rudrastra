iptables --flush --table nat
iptables --flush FORWARD
echo 0 > /proc/sys/net/ipv4/ip_forward

