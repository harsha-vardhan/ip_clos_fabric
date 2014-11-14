ip_clos_fabric
==============
The scripts are used for troubleshooting an IP CLOS Fabric

All the different scripts are available in the "ip_clos_fabric/scripts" 
directory


Different available scripts:

1. list_ipfabrics.py - This will list all the ip fabrics in a REST server

2. cable_link_generator.py - creates a csv file with links between Spine and Leaf in a human readable form for a Fabric
usage: cable_link_generator.py [-h] -f FABRIC_ID -s SERVER_HOST


ip_troubleshooting.py - This will manually troubleshoot the IP Fabric for Layer 2 and Layer 3
Usage:
python ip_troubleshoot.py lldp_check, 
python ip_troubleshoot.py bgp_check,
python ip_troubleshoot.py ping_connectivity

fabric_health_check.py - This will periodically check the fabric every 30 secs and log the status into file named health_check.log
