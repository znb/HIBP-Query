#!/usr/bin/python3
# Simple script to pull info on a specific breach

import json
import requests
import argparse
import os
import urllib3


def get_info(abreach):
    """Query HIBP"""
    urllib3.disable_warnings()
    customheaders = {"User-Agent": "haveibeenpwned-dot-py"}
    checkurl = "https://haveibeenpwned.com/api/v3/breach/" + abreach
    r = requests.get(checkurl, headers=customheaders, verify=False)
    if r.status_code == 200:
        parsed = json.loads(r.text)
        print(json.dumps(parsed, indent=4))
    else:
        print("Something weird happened - " + str(r.status_code))


def __main__():
    """Lets get this party started"""
    parser = argparse.ArgumentParser(description='What breaches does HIBP know about?', usage='%(prog)s')
    parser.add_argument('--breach', '-b', dest='breach', help='Get information on this breach')
    parser.add_argument('--version', '-v', action='version', version='%(prog)s 0.2')
    args = parser.parse_args()
    abreach = args.breach

    get_info(abreach)

if __name__ == '__main__':
    __main__()

