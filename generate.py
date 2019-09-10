#!/usr/bin/env python3

import yaml


tpl = (
    "ssh {host} "
    "'cd ~{user} && echo ~{user}/.ssh; ( mkdir -p .ssh && chmod 700 .ssh && chown {user}:{user} .ssh &&  cat >>.ssh/authorized_keys)' <<EOF"
).format

keys = yaml.safe_load(open('keys.yaml'))
hosts = yaml.safe_load(open('hosts.yaml'))


for host, users in hosts.items():
    for user, lst in users.items():
        print(tpl(host=host, user=user))
        for i in lst:
            s = keys[i].strip()
            assert "EOF" not in s
            print(s)
        print("EOF")
