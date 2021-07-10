import requests

def get_country(ip=None,key=None):
 if ip != None and key != None:
    url_ipstack = "http://api.ipstack.com/{}?access_key={}".format(ip,key)
    response = requests.get(url=url_ipstack)
    geodata = response.json()
    return geodata['country_name']