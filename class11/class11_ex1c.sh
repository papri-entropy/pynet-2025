#!/bin/bash

curl -H "Authorization: Token $NETBOX_TOKEN" https://netbox.lasthop.io/api/dcim/devices/2/ --insecure | jq
