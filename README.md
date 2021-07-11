# Access Log Analyzer + Location Finder
[![Build](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

---
## Description

It's a python script for find which IPs are hitting on our servers mostly and that location where we find from the log with the help of [ipstack]('https://ipstack.com/').

----
## Feature

- Log sorting with the highest hit (_first 10 positions_)
- Log location printing with the script

-----

## Pre-Requests

- Need an IPstack Login and API for location finding
- Need to add apikey file before running the script. So, please find the IPstack URL and grab the key and change the same on "_apikey.py_" 
- Need to install python3.
-----

## How to get IPstack API

- Please go through the [ipstack](https://ipstack.com/) and click "_GET FREE API KEY_" on the top right corner. 

![alt text](https://i.ibb.co/FJwjZWP/ipstack.png)

---
# How to get the script
_Steps: (Amazon-Linux)_
```sh
sudo yum install git -y
sudo yum install python3
git clone https://github.com/yousafkhamza/log-analyzer-pyscript.git
cd log-analyzer-pyscript
```
----

## Script running Demonstration 
```sh
$ python3 log.py
Enter your log file name (absalute path): ../Downloads/Python/access.log
193.106.31.130      :    313055  [Ukraine]
197.52.128.37       :     40777  [Egypt]
45.133.1.60         :      7514  [Netherlands]
173.255.176.5       :      5220  [United States]
172.93.129.211      :      4195  [United States]
178.44.47.170       :      2824  [Russia]
51.210.183.78       :      2684  [France]
84.17.45.105        :      2360  [United States]
193.9.114.182       :      2205  [Belgium]
45.15.143.155       :      1927  [United States]
```
> Most Hitting Ip Address : hit count [location]

----

## Modules used

- ipstack (Custome made module)
- logparser (Custome made module)
- apikey (Custome made module for API key passing)
- [requests](https://pypi.org/project/requests/) (API key passing module)
- [re](https://docs.python.org/3/library/re.html) (Regular expression module)

----

## Behind the code

_# cat apikey.py_ (_Using for api key passing to the script_)
```sh
api = '<enter your apikey from ipstack site>'            #<------------------- Replace with your API key where you got from ipstack
# eg:
# api = 'a37f9a05417225606d6650e16167'
```
_# cat ipstack.py_  (_API connection establishing and country name grabbing_)
```sh
import requests

def get_country(ip=None,key=None):
 if ip != None and key != None:
    url_ipstack = "http://api.ipstack.com/{}?access_key={}".format(ip,key)
    response = requests.get(url=url_ipstack)
    geodata = response.json()
    return geodata['country_name']
```
_# cat logparser.py_ (_it's using for log parsing and it's a outsource script and who had made this and really thank you for him._)
```sh
#!/usr/bin/env  python3

import re

regex_host = r'(?P<host>.*?)'
regex_identity = r'(?P<identity>\S+)'
regex_user = r'(?P<user>\S+)'
regex_time = r'\[(?P<time>.*?)\]'
regex_request = r'\"(?P<request>.*?)\"'
regex_status = r'(?P<status>\d{3})'
regex_size = r'(?P<size>\S+)'
regex_referer = r'\"(?P<referer>.*?)\"'
regex_agent = r'\"(?P<agent>.*?)\"'
regex_space = r'\s'

pattern = regex_host + regex_space + regex_identity + regex_space + \
          regex_user + regex_space + regex_time + regex_space + \
                  regex_request + regex_space + regex_status + regex_space + \
                  regex_size + regex_space + regex_referer + regex_space + \
                  regex_agent


def parser(s):
        """
        return type : dict()
        return format: {
                       host:str , identity:str , user:str ,
                                           time:str ,request:str , status:str ,
                                           size:str , referer:str, agent:str
                                        }
        returns None if failed.
        """
        try:
                parts = re.match(pattern,s)
                return parts.groupdict()
        except Exception as err:
                print(err)
```
_# cat log.py_ (_The script for sort IP hit and finding which of the location where it's from_)
```sh
import ipstack
import logparser
import apikey

def get_hit(t):
    return t[1]

path = input('Enter your log file name (absalute path): ')

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
        country = ipstack.get_country(ip=ip,key=apikey.api)
        print("{:20}:{:10}  [{}]".format(ip,hit,country))
else:
    print('This is not a access_log')
```
----

## Sticky Note
![alt text](https://i.ibb.co/K5Vsd8t/sticky.png)

----
## Conclusion

It's just a python script for analyzing our access log which log were we entered into the script then we can find most hitting IP address and corresponding location. 

<p align="center">
<a href="mailto:yousaf.k.hamza@gmail.com"><img src="https://img.shields.io/badge/-yousaf.k.hamza@gmail.com-D14836?style=flat&logo=Gmail&logoColor=white"/></a>
<a href="https://www.linkedin.com/in/yousafkhamza"><img src="https://img.shields.io/badge/-Linkedin-blue"/></a>
<a href="https://techbit-new.blogspot.com/"><img src="https://img.shields.io/badge/-Blogger-orange"/></a>


