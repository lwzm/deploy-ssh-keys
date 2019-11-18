#!/usr/bin/env python3

import yaml


root_key = """
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDHWrD5V10X9SWTYnfIGQcglQmjiCK6KyMDKyTgwb3Vx+Dfpa5EiRFerAKzxM+IiL8lQmUVKzoRk5rl36iQMRCcN5QNQJCtuhJSos94OMWotfvspIqhIuRig8S7CI7SNgvPRkzup8a/J78EQAr40ukjKRlQzJkuWtD22RhqdpPZRrF/JNE+8m/+sHt0UyVJ3GD0dcBDO7vrfGukjSZ3XqM+CDi/5xBgOOG0PR3K0VWQjtuqQoJbkFBGAFwZqTFk32nF7RzE+JyyUE0TPnfrNaNBCFJQcr9jr5icaGgEY7J5R2B55FwwDAPK6qfJ1P4srEm9zcL1g3LtZjMwIm2hx9a1 i-am-root
""".strip()

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
        if user == "root":
            print(root_key)
        for i in lst:
            s = keys[i].strip()
            assert "EOF" not in s
            print(s)
        print("EOF")
