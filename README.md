ip_clos_fabric
==============
The scripts are used for troubleshooting an IP CLOS Fabric

All the different scripts are available in the "ip_clos_fabric/scripts" 
directory


list_ipfabrics.py
-----------------
This will list all the ip fabrics in a REST server

cable_link_generator.py 
------------------------
creates a csv file with links between Spine and Leaf in a human readable form for a IP Fabric      
cable_link_generator.py [-h] -f FABRIC_ID -s SERVER_HOST

ip_troubleshooting.py
----------------------
This will manually troubleshoot the IP Fabric for Layer 2 and Layer 3

fabric_health_check.py
----------------------
This will periodically check the fabric every 30 secs and log the status into file named health_check.log
