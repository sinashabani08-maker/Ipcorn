#coded by N2838 《■》KINGHacker《■》

#modules required
import argparse
import requests, json
import sys
from sys import argv
import os
import time
#colours used
red = '\033[31m'
yellow = '\033[93m'
green = '\033[92m'
reset = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'

#banner of script
jo = f"""{green}
                 _,__        .:
         Darwin <*  /        | \
            .-./     |.     :  :,
           /           '-._/     \_
          /                '       \
        .'                         *: Brisbane
     .-'                             ;
     |                               |
     \                              /
      |                            /
Perth  \*        __.--._          /
        \     _.'       \:.       |
        >__,-'             \_/*_.-'

                              Melbourne

     snd                     :--,

                              '/

                              
                              IPCORN
                     《■》KINGHacker《■》
"""
print(jo, end=" ", flush=True)
time.sleep(0.090)

print("""

""")
print(f"{red}[!]{green}RUBIKA{reset}\_____/{yellow}https://rubika.ir/KINGHacker051s{reset}")
time.sleep(3)

#arguments and parser

parser = argparse.ArgumentParser()

parser.add_argument ("-I", help= "target/host IP address", type=str, dest='target', required=True )

args = parser.parse_args()
api = "http://ip-api.com/json/"
ip = args.target
try:
        data = requests.get(api+ip).json()
        sys.stdout.flush()
        a = green+bold+"[$]"
        b = cyan+bold+"[$]"
        print (a, "[Victim]:", data['query'])
        print(red+"<--------------->"+red)
        print (b, "[ISP]:", data['isp'])
        print(red+"<--------------->"+red)
        print (a, "[organisation]:", data['org'])
        print(red+"<--------------->"+red)
        print (b, "[city]:", data['city'])
        print(red+"<--------------->"+red)
        print (a, "[Region]:", data['region'])
        print(red+"<--------------->"+red)
        print (b, "[Longitude]:", data['lon'])
        print(red+"<--------------->"+red)
        print (a, "[Latitude]:", data['lat'])
        print(red+"<--------------->"+red)
        print (b, "[Time zone]:", data['timezone'])
        print(red+"<--------------->"+red)
        print (a, "[zip code]:", data['zip'])
        print (" "+yellow)

except KeyboardInterrupt:
        print ('Terminating, Bye'+lgreen)
        sys.exit(0)
except requests.exceptions.ConnectionError as e:
        print (red+"[~]"+" check your internet connection!"+clear)
sys.exit(1)
