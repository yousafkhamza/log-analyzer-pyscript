import ipstack
import logparser
import apikey
import os

def get_hit(t):
    return t[1]

path = input('Enter your log file name (include path): ')

if path.lower().split('/')[-1].endswith('log') and os.path.isfile('{}'.format(path)):
    file = open("{}".format(path),'r')
    ipcount = {}
    for line in file:
        part = logparser.parser(line)
        ip = part['host']
        if ip not in ipcount:
            ipcount[ip] = 1
        else:
            ipcount[ip] += 1
            
    result = sorted(ipcount.items(),key=get_hit,reverse=True)[:10]
    for item in result:
        ip,hit = item
        country = ipstack.get_country(ip=ip,key=api.api)
        print("{:20}:{:10}  [{}]".format(ip,hit,country))
else:
    print('This is not a access_log')
