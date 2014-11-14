import parameters
import connect

spine_11_ls = parameters.spine_11_ls
spine_12_ls = parameters.spine_12_ls
cmd = 'show lldp neighbors'
device = parameters.device_details

def l2_check():
  spine_11_new = []
  spine_12_new=[]
  spine_11_l2_output = connect.connect(device['spine-11']['mgmt_ip'],
                                       device['spine-11']['port'],
                                       cmd,
                                       device['spine-11']['username'],
                                       device['spine-11']['password'])
  for x in spine_11_l2_output:
    y = x.split()
    z = ('spine-11', y[0], y[4], y[3])
    spine_11_new.append(z)  
  spine_12_l2_output = connect.connect(device['spine-12']['mgmt_ip'],
                                       device['spine-12']['port'],
                                       cmd,
                                       device['spine-12']['username'],
                                       device['spine-12']['password'])
  for x in spine_12_l2_output:
    y = x.split()
    z = ('spine-12', y[0], y[4], y[3])
    spine_12_new.append(z)
  a = set(spine_11_ls) - set(spine_11_new)
  b = set(spine_12_ls) - set(spine_12_new)
  if not list(a):
    print 'INFO: L2 from Spine-11 is working fine'
  if list(a):
    for m in list(a):
      print 'ERROR: Link failure between %s:%s and %s:%s' % (m[0],m[1],m[2],m[3])
  if not list(b):
    print 'INFO: L2 from Spine-12 is working fine'
  if list(b):
    for m in list(b):
      print 'ERROR: Link failure between %s:%s and %s:%s' % (m[0],m[1],m[2],m[3])
