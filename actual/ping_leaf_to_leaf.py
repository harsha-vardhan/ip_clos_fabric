import connect
import parameters

leaf_gw = parameters.leaf_gw
leaf_devices = parameters.leaf_devices
device = parameters.device_details

def ping_connectivity_check():
  for x in leaf_devices:
    src = x
    for dst in leaf_devices:
      if dst != x:
        cmd = 'ping source ' + leaf_gw[src] + ' ' + leaf_gw[dst] + ' count 5'
        ping_output = connect.connect(device[src]['mgmt_ip'],
                                      device[src]['port'],
                                      cmd,
                                      device[src]['username'],
                                      device[src]['password'])
        for y in ping_output[-2:-1]:
          if ' 0% packet loss' in y:
            print 'Ping between %s and %s works fine' %(src, dst)
          else:
            print 'Cannot ping from %s to %s' %(src, dst)
