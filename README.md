# Rudrastra


# 𝗜𝗡𝗦𝗧𝗔𝗟𝗟𝗔𝗧𝗜𝗢𝗡 𝗜𝗡𝗦𝗧𝗥𝗨𝗖𝗧𝗜𝗢𝗡𝗦
TO Install all The Required Dependencies...RUN THE FOLLOWING COMMANDS

1 chmod +x install.sh
2 ./install.sh

# 𝗠𝗢𝗥𝗘 𝗜𝗡𝗙𝗢

These Scripts Work Best With Python3

//Use Python3 to run the Scripts//


# 𝙍𝙐𝙉𝙉𝙄𝙉𝙂 𝙏𝙃𝙀 𝙁𝘼𝙆𝙀-𝘼𝙋

# 𝙎𝙏𝙀𝙋 1
This step involves configuring the IPtable rules and preparing the interfaces..!
|| python3 Internet&Interface.py <internet-interface> <FAKE-AP-INTERFACE> ||

# 𝙎𝙏𝙀𝙋 2
This step involves Configuring DHCP Server To assign IP address to Devices Connecting to our AP!
|| python3 DHCP&IP-conf.py ||

# 𝙎𝙏𝙀𝙋 3
This Step involves setting up the Fake-Ap and Finally running it..
|| python3 Start-AP.py ||

# 𝙎𝙏𝙀𝙋 4
Now WE have our Fake AP Running we can Now Use Wireshark to Sniff Packets by selecting the FAKE-AP interface..

# 𝙎𝙏𝙀𝙋 5
After Closing DHCP and FAKE-AP... you can ...run following commands to reset IP table rules and other modifications made..!
|| chmod +x reset.sh ||
|| ./reset.sh ||

# 𝑴𝑨𝑲𝑬_𝑰𝑻_𝑩𝑬𝑻𝑻𝑬𝑹
To make Rudrastra Even Better Contribute to it Or use and Report Any Bugs or fixes Required...
