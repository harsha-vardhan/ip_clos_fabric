import urllib
import json
import os
import re

host_name = 'localhost'
ip_fabrics = []
ip_fab_id = []

def get_ip_fabric_link():
  ip_url = 'http://%s/openclos/ip-fabrics' %(host_name)
  u = urllib.urlopen(ip_url)
  data = u.read()

  t = json.loads(data)
  
  for s in t['ipFabrics']['ipFabric']:
    ip_fabrics.append(s['uri'])
  for x in ip_fabrics:
    match = re.search(r'\w+-\w+-\w+-\w+-\w+', x)
    if match:
      print match.group()
#      ip_fab_id.append(match.group())
#  print ip_fab_id

get_ip_fabric_link()
