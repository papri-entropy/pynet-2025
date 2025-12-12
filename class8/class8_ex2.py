from jnpr.junos import Device
from jnpr.junos.op.routes import RouteTable
from jnpr.junos.op.arp import ArpTable
from pprint import pprint
from jnpr_devices import srx2


def check_connected(device_obj):
    return device_obj.connected

def gather_routes(device_obj):
    routes = RouteTable(device_obj)
    routes.get()
    for k, v in routes.items():
        print(k)

    return routes.keys()


def gather_arp_table(device_obj):
    arp_entries = ArpTable(device_obj)
    arp_entries.get()
    for k, v in arp_entries.items():
        print(k)
        pprint(v)


def print_output(device_obj, gather_routes, gather_arp_table):
    
    print(device_obj.hostname)
    print(device_obj.user)
    print(device_obj.port)
    
    routing_table = gather_routes(device_obj)

    arp_table = gather_arp_table(device_obj)
    
    
   
    
    


if __name__ == "__main__":

    srx2_device = Device(**srx2)

    srx2_device.open()

    print(check_connected(srx2_device))

    gather_routes(srx2_device)

    gather_arp_table(srx2_device)

    print_output(srx2_device, gather_routes, gather_arp_table)



