[![SxNade](https://img.shields.io/badge/MadeBy-SxNade-red)


   ![Capture](https://github.com/SxNade/Rudrastra/blob/main/rd.png)


**`The All in One Weapon For Making Fake Access point!`**

**NOTE** : My repositories are only hosted on my offcial github page https://github.com/SxNade and May be refered on other page at https://SxNade.github.io , If you find some-body else claiming or posting them on some-kind of website social media etc.. Don't Trust it. I never publish anything about my repos on any other platform than my official github page  https://github.com/SxNade or at https://SxNade.github.io

# No Longer Maintained
- This Project is no longer updated 
- A Better Version of same Project can be found at [https://github.com/SxNade/SP-108](https://github.com/SxNade/SP-108)

# 𝗜𝗡𝗦𝗧𝗔𝗟𝗟𝗔𝗧𝗜𝗢𝗡 𝗜𝗡𝗦𝗧𝗥𝗨𝗖𝗧𝗜𝗢𝗡𝗦
TO Install all The Required Dependencies...RUN THE FOLLOWING COMMANDS

      $ git clone https://github.com/SxNade/Rudrastra
      $ cd Rudrastra
      $ chmod +x install.sh

      $ ./install.sh

# 𝗠𝗢𝗥𝗘 𝗜𝗡𝗙𝗢

These Scripts Work Best With Python3

**`Use Python3 to run the Scripts`**


# 𝙍𝙐𝙉𝙉𝙄𝙉𝙂 𝙏𝙃𝙀 𝙁𝘼𝙆𝙀-𝘼𝙋

# 𝙎𝙏𝙀𝙋 1
This step involves configuring the IPtable rules and preparing the interfaces..!

`python3 internet.py <internet-interface> <FAKE-AP-INTERFACE>`

# 𝙎𝙏𝙀𝙋 2
This step involves Configuring DHCP Server To assign IP address to Devices Connecting to our AP!

`python3 dhcp.py`

# 𝙎𝙏𝙀𝙋 3
This Step involves setting up the Fake-Ap and Finally running it..

`python3 fake_ap.py`

# 𝙎𝙏𝙀𝙋 4
`Now WE have our Fake AP Running we can Now Use Wireshark to Sniff Packets by selecting the FAKE-AP interface..`

# 𝙎𝙏𝙀𝙋 5
After Closing DHCP and FAKE-AP... you can ...run following commands to reset IP table rules and other modifications made..!

`chmod +x reset.sh`

`./reset.sh`

# 𝑴𝑨𝑲𝑬_𝑰𝑻_𝑩𝑬𝑻𝑻𝑬𝑹
To make Rudrastra Even Better Contribute to it Or use and Report Any Bugs or fixes Required...

`git clone https://github.com/SxNade/Rudrastra`


![Capture](https://raw.githubusercontent.com/SxNade/Rudrastra/main/ritm.png)
