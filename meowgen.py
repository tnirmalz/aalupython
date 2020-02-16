'''
This script takes a list of subdomains and prints unique keywords
Those keywords can be used again for subdomain/dirs/files bruteforcing
ex:
$ cat subdomains.txt
dev.example.com
staging-secret-69.example.com
jenkins.example.com
gitlab.example.com

$ python3 meowgen.py subdomains.txt
dev
example
com
staging-secret-69
jenkins
gitlab
'''

import sys

wordlist = open(sys.argv[1], 'r')
# wordlist to python list
subdomains = [x for x in wordlist.read().splitlines()]
# python list splitting
splitted = [subdomains[i].split('.') for i in range(len(subdomains))]
# append unique keywords to uniq words list
uniqwords = []
for x in splitted:
    for y in x:
        if y not in uniqwords:
            uniqwords.append(y)
# print the expected result
for x in uniqwords:
    print(x)