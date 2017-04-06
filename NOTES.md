# switchback 
Yet another multi-vendor automation tool.  

A pythonic method of retrieving the operational state of network nodes.

Uses SNMP to try to detect node type before connecting (do this in a specific base class function, then hand vendor and model across to device-specific connection method).

Gracefully exit with unknown device type error and as much information as possible about the type.

SNMP OIDs:

sysDescr.0
sysObjectID.0 (requires vendor-specific MIBs)
sysName.0
SNMPv2-SMI::enterprises.2636.3.1.2.0 (Juniper Device)


Inspired by (and utilising) pyez-junos.

### Entering Environment
cd ~/Development/Eighth\ Layer/switchback
source activate switchback

### Exiting Environment
source deactivate switchback

