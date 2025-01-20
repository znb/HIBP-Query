#!/usr/bin/python3
# Simple script to check an email against any stealer logs

import requests
import json
import argparse
import os
from dotenv import load_dotenv, dotenv_values
import urllib.parse
import urllib3


def checkemail(aemail):
    """Query if email is on any stealer log lists"""
    load_dotenv()
    urllib3.disable_warnings()
    customheaders = {"User-Agent": "haveibeenpwned-dot-py", "hibp-api-key": os.getenv("hibp-api-key")}
    checkurl = "https://haveibeenpwned.com/api/v3/stealerlogsbyemail/" + urllib.parse.quote(aemail)
    r = requests.get(checkurl, headers=customheaders, verify=False)
    if r.status_code == 200:
        parsed = json.loads(r.text)
        print(json.dumps(parsed, indent=4))
    else:
        print("Something weird happened - " + str(r.status_code) + " - " + str(r.text))


def __main__():
    """Lets get this party started"""
    parser = argparse.ArgumentParser(description='Query if an email address appears on any stealer logs', usage='%(prog)s')
    parser.add_argument('--email', '-e', dest='email', help='Email to check')
    parser.add_argument('--version', '-v', action='version', version='%(prog)s 0.2')
    args = parser.parse_args()
    aemail = args.email

    checkemail(aemail)

if __name__ == '__main__':
    __main__()

