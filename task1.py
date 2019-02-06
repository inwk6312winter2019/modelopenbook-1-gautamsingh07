def list_ifname_ip ():

 list = []
 with open("running-config.cfg","r") as file:
	for interface in file:
		list.append(interface)

 interface = []
 name = []
 ip_address = []
 vlan = []
