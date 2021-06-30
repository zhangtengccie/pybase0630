#!/usr/bin/python3.9
# -*- coding=utf8 -*- 
# Creater:zhangteng

import re
import os

str ='''eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.13.29  netmask 255.255.255.0  broadcast 192.168.13.255
        inet6 fe80::250:56ff:fe8b:8e82  prefixlen 64  scopeid 0x20<link>
        ether 00:50:56:8b:8e:82  txqueuelen 1000  (Ethernet)
        RX packets 213964305  bytes 870058624044 (810.3 GiB)
        RX errors 0  dropped 3456  overruns 0  frame 0
        TX packets 175417068  bytes 26985966902 (25.1 GiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0'''




ipv4_add = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',str)[0]
netmask = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',str)[1]
broadcast = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',str)[2]
mac_add = re.findall('((([a-f0-9]{2}:){5})|(([a-f0-9]{2}-){5}))[a-f0-9]{2}',str)


format_string = '{:<10}:{}'
print(format_string.format('ipv4_add', ipv4_add))
print(format_string.format('netmask', netmask))
print(format_string.format('broadcast', broadcast))
print(format_string.format('mac_add', mac_add[0][0][:-1]))

ipv4_gw = '192.168.13.254'
ping_result = os.popen('ping '+ ipv4_gw +'  -c 1').read()
re_ping_result =  re.findall('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',
                  ping_result)
print('\n我们假设网关IP地址为最后一位为254，因此网关IP地址为：'+ ipv4_gw +'\n')
if re_ping_result:
    print('网关可达！')
else:
    print('网关不可达！')