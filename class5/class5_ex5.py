#!/usr/bin/env python

from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader([".", "./templates/"])


ntp_vars = {
    "ntp_server1": "130.126.24.24",
    "ntp_server2": "152.2.21.1"
}

sh_run_template_file = "class5_ex5.j2"
template = env.get_template(sh_run_template_file)
output = template.render(**ntp_vars)

print(output)
