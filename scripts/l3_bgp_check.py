import connect
import parameters

spine_11_bgp = parameters.spine_11_bgp
spine_12_bgp = parameters.spine_12_bgp
cmd = 'show bgp summary'
device = parameters.device_details

def bgp_check():
  spine_11_new = []
  spine_12_new=[]
  spine_11_l3_output = connect.connect(device['spine-11']['mgmt_ip'],
                                       device['spine-11']['port'],
                                       cmd,
                                       device['spine-11']['username'],
                                       device['spine-11']['password']) 
  for x in spine_11_l3_output:
    y = x.split()
    if y[7] == 'Established':
      z = ('spine-11', y[1], y[0])
      spine_11_new.append(z)
  spine_12_l3_output = connect.connect(device['spine-12']['mgmt_ip'],
                                       device['spine-12']['port'],
                                       cmd,
                                       device['spine-12']['username'],
                                       device['spine-12']['password'])
  for x in spine_12_l3_output:
    y = x.split()
    if y[7] == 'Established':
      z = ('spine-12', y[1], y[0])
      spine_12_new.append(z)  
  a = set(spine_11_bgp) - set(spine_11_new)
  b = set(spine_12_bgp) - set(spine_12_new)
  if not list(a):
    print 'INFO: All BGP peers are connected from Spine-11'
  if list(a):
    for m in list(a):
      print 'ERROR: BGP failure between %s and %s whose AS is %s' % (m[0],m[2],m[1])
  if not list(b):
    print 'INFO: All BGP peers are connected from Spine-12'
  if list(b):
    for m in list(b):
      print 'ERROR: BGP failure between %s and %s whose AS is %s' % (m[0],m[2],m[1])
