# 
# Your Monitor Number = #$34T#
#
# How to configure devices via python
# Using various SSH Libraries (Paramiko, Netmiko, Nornir, etc)
#
# Install/Update libraries
# 
# @cmd
# py -m pip install --upgrade pip
# py -m pip install netmiko
#
#
# ---------------------------------------------------------- #

# import netmiko
from netmiko import Connecthandler

# Provide information about the host/s
cbaba = {
    'device_type': 'cisco_ios_telnet',
    'host': '10.#$34T#.1.4',
    'username': 'admin',
    'password': 'pass',
    'secret': 'pass'
}

py_dictionary = {
    'key_string': 'value_string',
    'key_int': 1,
    'key_float': 1.0,
    'key_boolean': True,
    'key_list': [True, 2, 3.0, '5'],
    'key_dictionary': {
        'nested' : [
            'I\'m',
            'nested',
            'data'
        ]
    }
}

# Write the configurations
cb_config = [
    
]