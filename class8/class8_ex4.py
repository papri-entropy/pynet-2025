from jnpr.junos import Device
from jnpr.junos.op.routes import RouteTable
from jnpr.junos.utils.config import Config
from pprint import pprint
from jnpr_devices import srx2
from class8_ex2 import gather_routes


if __name__ == "__main__":

    srx2_device = Device(**srx2)

    srx2_device.open()  

    srx2_device.timeout = 60

    routing_before = set(gather_routes(srx2_device))
    print(routing_before)

    cfg = Config(srx2_device)

    cfg.lock()

    cfg.load(path="static_routes.conf", format="text", merge=True)

    print(cfg.diff()) 
    
    cfg.commit()

    cfg.unlock()

    routing_after = set(gather_routes(srx2_device))
    print(routing_after)

    diff = routing_after - routing_before
    print(diff)








