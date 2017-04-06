# switchback 
Yet another multi-vendor automation tool.  

A pythonic method of retrieving the operational state of network nodes.

Uses SNMP to try to detect node type before connecting (do this in a specific base class function, then hand vendor and model across to device-specific connection method).

Gracefully exit with unknown device type error and as much information as possible about the type.

SNMP OIDs:



Inspired by (and utilising) pyez-junos.

### Entering Environment
cd ~/Development/Eighth\ Layer/switchback
source activate switchback

### Exiting Environment
source deactivate switchback

