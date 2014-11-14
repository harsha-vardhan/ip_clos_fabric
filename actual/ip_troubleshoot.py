import sys
import l2_link_check
import l3_bgp_check
import ping_leaf_to_leaf

if len(sys.argv) == 2:
  if sys.argv[1] == 'lldp_check':
    l2_link_check.l2_check() 
  if sys.argv[1] == 'bgp_check':
    l3_bgp_check.bgp_check() 
  if sys.argv[1] == 'ping_connectivity':
    ping_leaf_to_leaf.ping_connectivity_check() 
else:
  print ('Please enter any one of the below arguements\n'
         'lldp_check\n'
         'bgp_check\n'
         'ping_connectivity\n')
