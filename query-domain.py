#!/usr/bin/python3
# Simple script to check what HIBP has on our domain

import requests
import json
import argparse
import os
from dotenv import load_dotenv, dotenv_values
import urllib3


def checkdomain(adomain):
    """Query HIBP for our domain"""
    load_dotenv()
    urllib3.disable_warnings()
    customheaders = {"User-Agent": "haveibeenpwned-dot-py", "hibp-api-key": os.getenv("hibp-api-key")}
    checkurl = "https://haveibeenpwned.com/api/v3/breacheddomain/" + str(adomain)
    r = requests.get(checkurl, headers=customheaders, verify=False)
    print(r.text)
    if r.status_code == 200:
        parsed = json.loads(r.text)
        print(json.dumps(parsed, indent=4))
    else:
        print("Something weird happened - " + str(r.status_code))



def __main__():
    """Lets get this party started"""
    parser = argparse.ArgumentParser(description='Query our domain against HIBP', usage='%(prog)s')
    parser.add_argument('--domain', '-d', dest='domain', help='Domain to check')
    parser.add_argument('--version', '-v', action='version', version='%(prog)s 0.2')
    args = parser.parse_args()
    adomain = args.domain

    checkdomain(adomain)

if __name__ == '__main__':
    __main__()

