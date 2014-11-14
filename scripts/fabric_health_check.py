import l2_link_check
import l3_bgp_check
import sys
import time
from datetime import datetime


while True:
  f = open('health_check.log', 'a')
  sys.stdout = f

  print str(datetime.now())
  l2_link_check.l2_check() 
 
  print str(datetime.now())
  l3_bgp_check.bgp_check()
  
  f.close()

  time.sleep(30) 
