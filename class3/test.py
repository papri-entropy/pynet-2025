from netmiko.accedian import AccedianSSH
from netmiko.ssh_dispatcher import CLASS_MAPPER_BASE


class SlowAccedianSSH(AccedianSSH):
    """Custom driver for Accedian NIDs that take >20s to show prompt."""

    def session_preparation(self):
        # Wait up to 90s for prompt (instead of hardcoded 20s)
        self._test_channel_read(pattern=r".*:\s?$", read_timeout=90)

        # Explicitly detect colon-style prompt (e.g., "PROMPT:")
        self.base_prompt = self.find_prompt(expect_string=r".*:\s?$")

        # Strip trailing characters for consistency
        self.base_prompt = self.base_prompt.strip()


# Register so you can call ConnectHandler with device_type="slow_accedian"
CLASS_MAPPER_BASE.update({"slow_accedian": SlowAccedianSSH})


if __name__ == "__main__":
    from netmiko import ConnectHandler
    import os

    device = {
        "device_type": "slow_accedian",  # use our new driver
        "host": "YOUR_IP",
        "username": os.environ["USERNAME"],
        "password": os.environ["PASSWORD"],
        "auth_timeout": 90,
        "banner_timeout": 90,
        "conn_timeout": 90,
        "session_log": "log.log",
    }

    net_connect = ConnectHandler(**device)

    print(net_connect.find_prompt(expect_string=r".*:\s?$"))

    output = net_connect.send_command(
        "show version", expect_string=r".*:\s?$", delay_factor=5
    )
    print(output)

    net_connect.disconnect()

