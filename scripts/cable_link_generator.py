import sys
import argparse
import get_cable_link


def cable_generate(fabric_id, hostname):
  cable_link = get_cable_link.get_ip_cable_plan(hostname, fabric_id)
#  print cable_link 
  f = open('cable-links.csv', 'w')
  sys.stdout = f
  
  print 'Spine Device Name:Spine Interface Name, Leaf Device Name:Leaf Interface Name'
  for x in cable_link:
    print x[0] + ':' + x[1] + ', ' + x[2] + ':' +x[3]

  f.close()  

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='This is a fabric cable generator script.')
  parser.add_argument('-f', '--fabric_id', help='Network fabric id', required=True)
  parser.add_argument('-s', '--server_host', help='IP/Hostname of the REST server', required=True)
  args = parser.parse_args()
 
  fabric = args.fabric_id
  host_name = args.server_host
 
  cable_generate(fabric, host_name)
