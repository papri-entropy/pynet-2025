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

    cfg = Config(srx2_device)

    cfg.lock()

    cfg.load("delete routing-options static route 203.0.113.5/32", format="set")
    cfg.load("delete routing-options static route 203.0.113.200/32", format="set")
    
    print(cfg.diff()) 

    cfg.commit()

    cfg.unlock()

    gather_routes(srx2_device)









