# Usage: python3 bufferover-subdomain.py <target.com>
import sys
import requests
import json

target = sys.argv[1]
r = requests.get("https://dns.bufferover.run/dns?q="+target)
response = json.loads(r.text)
domains = response["FDNS_A"]
domainList = ",".join(domains).split(",")

filteredDomains = [i for i in domainList if target in i]

uniqueDomains = set(filteredDomains)
for i in uniqueDomains:
	print(i)