#!/usr/bin/env python3

import yaml


tpl = (
    r"""ssh {host} """
    r"""'"""
    r"""cd ~{user} && mkdir -p .ssh && cat >.ssh/authorized_keys && chown -R {user}:{user} .ssh && chmod -R go-rwx .ssh"""
    r"""'"""
    r""" <<EOF"""
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
