#!/usr/bin/python3
# Simple script to check what domains are loaded into HIBP monitoring

import requests
import json
import argparse
import os
from dotenv import load_dotenv, dotenv_values
import urllib3


def do_check():
    """Query HIBP subscription status"""
    load_dotenv()
    urllib3.disable_warnings()
    customheaders = {"User-Agent": "haveibeenpwned-dot-py", "hibp-api-key": os.getenv("hibp-api-key")}
    checkurl = "https://haveibeenpwned.com/api/v3/subscribeddomains"
    r = requests.get(checkurl, headers=customheaders, verify=False)
    if r.status_code == 200:
        parsed = json.loads(r.text)
        print(json.dumps(parsed, indent=4))
    else:
        print("Something weird happened - " + str(r.status_code))



def __main__():
    """Lets get this party started"""
    parser = argparse.ArgumentParser(description='Query our monitored domains in HIBP', usage='%(prog)s')
    parser.add_argument('--version', '-v', action='version', version='%(prog)s 0.2')
    args = parser.parse_args()

    do_check()

if __name__ == '__main__':
    __main__()

