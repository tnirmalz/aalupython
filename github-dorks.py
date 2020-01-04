#!/usr/bin/python2.7
# This code belongs to https://github.com/gwen001 and it was taken from https://github.com/gwen001/github-search/blob/master/github-dorks.py
# since the author doesnt mind modifying his code, the original code has been modified to fit my own needs
# This code only generates a list of urls which you need to manually enter in the browser
'''
Usage:
-----------------------------------------------------------------
$ python github-dorks.py -d dorks.txt -o uber
https://github.com/search?q=org%3Auber+filename%3Aconstants
https://github.com/search?q=org%3Auber+filename%3Asettings
https://github.com/search?q=org%3Auber+filename%3Adatabase
https://github.com/search?q=org%3Auber+filename%3Aconfig
https://github.com/search?q=org%3Auber+filename%3Aenvironment
------------------------------------------------------------------
'''
# I don't believe in license.
# You can do whatever you want with this program.

import os
import sys
import json
import time
import re
import argparse
import random
from termcolor import colored

parser = argparse.ArgumentParser()
parser.add_argument( "-d","--dorks",help="dorks file (required)" )
parser.add_argument( "-o","--org",help="organization (required or -u)" )
parser.add_argument( "-u","--user",help="user (required or -o)" )
parser.parse_args()
args = parser.parse_args()

t_tokens = []
t_orgs = []
t_users = []
t_dorks = []

if args.user:
    t_users = args.user.split(',')

else:
    threads = 1

if args.org:
    t_orgs = args.org.split(',')

if not args.user and not args.org:
    parser.error( 'user or organization missing' )

if not args.dorks:
    parser.error( 'dorks file is missing' )

fp = open(args.dorks,'r')
for line in fp:
    t_dorks.append( line.strip() )

def __urlencode( str ):
	str = str.replace( ':', '%3A'  );
	str = str.replace( '"', '%22' );
	str = str.replace( ' ', '+' );
	return str


t_urls = {}
t_results = {}
t_results_urls = {}
t_stats = {
    # 'l_tokens': len(t_tokens)-1,
    'l_tokens': len(t_tokens),
    'n_current': 0,
    'n_total_urls': 0
}

for org in t_orgs:
    t_results[org] = []
    for dork in t_dorks:
        dork = 'org:' + org + ' ' + dork
        url = 'https://github.com/search?q=' + __urlencode(dork)
        t_results[org].append( url )
        t_urls[url] = 0

for user in t_users:
    t_results[user] = []
    for dork in t_dorks:
        dork = 'user:' + user + ' ' + dork
        # dork = '"' + dork + '"'
        url = 'https://github.com/search?q=' + __urlencode(dork)
        t_results[user].append( url )
        t_urls[url] = 0

for keys,values in t_results.items():
    for value in values:
        print(value)
