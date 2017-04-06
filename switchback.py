import sys

class Node(object):
    """Base class for vendor-specific network nodes.
    """
    def _connection(self):
        print ("Not implemented in base class")
    
    def hostname(self):
    """The configured hostname of the device
    """
        print ("Not implemented in base class")
      
    def mac_addresses(self):
        """A list of MAC addresses and masks allocated to this node
           :returns: MAC Addresses
           :rtype: list
           """
        print ("Not implemented in base class")
  
    def physical_interfaces(self):
        """Returns a (something of something) containing:
        interface_name,
        mac_address, 
        snmp_ifindex,
        phy_state,
        admin_state,
        media, (Copper, SFP-MM, SFP-SM)
        speed
        """
        print ("Not implemented in base class")

    def lldp_chassis_id
        """Return the local LLDP chassis ID
        """
        print ("Not implemented in base class")

    def lldp_interfaces(self):
        """Returns a (something of something) containing LLDP interface neighbourships:
        interface_name, 
        remote_chassis_id,
        remote_interface, (either ifIndex, or port name)
        remote_chassis_name
        """
        print ("Not implemented in base class")

    def stp_bridge(self):
        """Returns a list of dicts of STP information for each instance:
        instance_id,  (subtract base bridge priority from instance priority)
        instance_type, (RSTP/CIST, MSTI, VSTP/PVST+, PVST, STP)
        root_id, 
        root_cost,
        root_port,
        regional_root_id,
        regional_root_cost
        local_bridge_id,
        """
        print ("Not implemented in base class")
   
    def stp_interfaces(self):
        """Returns a (something of something) containing current xSTP interface states:
        instance_id,
        interface_name,
        local_port_id,
        desg_port_id,
        desg_bridge_id,
        port_cost,
        port_state,
        port_role
        """
    print ("Not implemented in base class")
         
    def describe(self):
        print "My IP is: {}".format(self.ip_address)
    def port_table(self):
        print ("Not implemented in base class")
    def chassis_table(self):
        print ("Not implemented in base class")
