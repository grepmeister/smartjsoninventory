#!/usr/bin/env bash

# demo agent plugin for smartjsoninventory
# requires jq and jc 

# Pretty print the json output
# ./sysctl2smartjsoninventory.sh | sed 1d | jq | less


echo '<<<smartjsoninventory:sep(0)>>>'
sysctl -a | grep ipv6 | jc --sysctl | jq -c 'to_entries | map({key: .key, value: .value})'
