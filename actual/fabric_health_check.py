import l2_link_check
import l3_bgp_check
import sys
import time
from datetime import datetime

f = open('health_check.log', 'a')
sys.stdout = f

while True:
  print str(datetime.now())
  l2_link_check.l2_check() 
 
  print str(datetime.now())
  l3_bgp_check.bgp_check()

  time.sleep(10) 
