import os
import time
import requests
from requests.auth import HTTPBasicAuth

#Set each value
ENDPOINT = ""
INTERFACE = ""
BASIC_USER = ""
BASIC_PASSWORD = ""
FQDN = ""
USERNAME = ""
PASSWORD = ""
CHECK_INTERVAL = 1

#Get ipv6
def get_ipv6(INTERFACE):
    ipv6 = os.popen(f"ip addr show {INTERFACE}").read().split("inet6 ")[1].split("/")[0]
    return ipv6

#Notify xpass endpoints of changes
def change_xpass(ipv6):
    requests.get(f"{ENDPOINT}?d={FQDN}&p={PASSWORD}&a={ipv6}&u={USERNAME}", 
                 verify=False, auth=HTTPBasicAuth(BASIC_USER,BASIC_PASSWORD))
    
#Set initial value of old ipv6 address
ipv6_old = get_ipv6(INTERFACE)

#Start loop
while True:
    ipv6 = get_ipv6(INTERFACE)

    if ipv6 == ipv6_old:
        pass 
    else:
        print(f"{ipv6_old} to {ipv6} changed")
        change_xpass(ipv6)

    ipv6_old = ipv6
    time.sleep(CHECK_INTERVAL)
