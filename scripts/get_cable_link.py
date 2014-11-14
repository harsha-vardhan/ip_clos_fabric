import urllib
import json
import re

devices_dict = {}
device_ifc_dict = {}

def get_ip_cable_plan(host_name, ip_fabric_id):
  ip_url = 'http://%s/openclos/ip-fabrics/%s/cabling-plan' %(host_name,ip_fabric_id)
  u = urllib.urlopen(ip_url)
  data = u.read()
  lists = data.split('\n')
  device_ls = []
  link_ls = []
  for devices in lists:
    if 'leaf' in devices or 'spine' in devices:
      device_ls.append(devices)
    if 'color' in devices:
      link_ls.append(devices)
  for x in device_ls:
    if 'leaf' in x:
      l_strip = x.split()
      if 'et-' in l_strip[2]:
        raw_leaf_str = l_strip[2].split('|')
        devices_dict[raw_leaf_str[-1][1:-5]] = l_strip[0][1:-1]
        for y in raw_leaf_str[0:-1]:
          match1 = re.search(r'\w+-\w+-\w+-\w+-\w+', y)
          match2 = re.search(r'et-\d+/\d+/\d+', y)
          if match1 and match2:
            device_ifc_dict[match1.group()] = {'ifc_id':match2.group(),'device_id':l_strip[0][1:-1]}
    if 'spine' in x:
      s_strip = x.split()
      if 'et-' in s_strip[2]:
        raw_spine_str = s_strip[2].split('|')
        devices_dict[raw_spine_str[0][9:-1]] = s_strip[0][1:-1]
        for y in raw_spine_str[1:]:
          match1 = re.search(r'\w+-\w+-\w+-\w+-\w+', y)
          match2 = re.search(r'et-\d+/\d+/\d+', y)
          if match1 and match2:
            device_ifc_dict[match1.group()] = {'ifc_id':match2.group(),'device_id':s_strip[0][1:-1]}
  cable_links = []
  for x in link_ls:
    if 'color' in x:
      y = x.split()
      spine_link = y[0]
      leaf_link = y[2]
      match1 = re.findall(r'\w+-\w+-\w+-\w+-\w+', spine_link)
      match2 = re.findall(r'\w+-\w+-\w+-\w+-\w+', leaf_link)
      for spine_keys in devices_dict.keys():
        if devices_dict[spine_keys] == match1[0]:
          spine_device = spine_keys
      for spine_link_keys in device_ifc_dict.keys():
        if spine_link_keys == match1[1]:
          spine_interface = device_ifc_dict[spine_link_keys]['ifc_id']
      for leaf_keys in devices_dict.keys():
        if devices_dict[leaf_keys] == match2[0]:
          leaf_device = leaf_keys
      for leaf_link_keys in device_ifc_dict.keys():
        if leaf_link_keys == match2[1]:
          leaf_interface = device_ifc_dict[leaf_link_keys]['ifc_id']
      link_tup = (spine_device, spine_interface, leaf_device, leaf_interface)
      cable_links.append(link_tup)
  return cable_links
