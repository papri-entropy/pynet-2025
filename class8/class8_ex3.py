from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import LockError
from pprint import pprint
from jnpr_devices import srx2




if __name__ == "__main__":

    srx2_device = Device(**srx2)
    srx2_device.open()
    srx2_device.timeout = 60
    
    cfg = Config(srx2_device)

    try:
        print(cfg.lock())
    except LockError:
        print("Device config already locked")

    cfg.load("set system host-name python4life", format="set", merge=True)

    print(cfg.diff())
    
    cfg.rollback(0)

    print(cfg.diff())

    cfg.unlock() 




