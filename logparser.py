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