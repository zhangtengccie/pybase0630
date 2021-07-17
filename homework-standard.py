import re
import os


ifconfig_result = os.popen('ifconfig ' + 'ens33').read()
print(ifconfig_result)

ipv4_address = re.findall(r'inet (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',ifconfig_result)[0]
netmask = re.findall(r'netmask (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',ifconfig_result)[0]
broadcast = re.findall(r'broadcast (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',ifconfig_result)[0]
mac_address = re.findall(r'ether ([0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2})',
                         ifconfig_result)[0]
print(ipv4_address)
print(netmask)
print(broadcast)
print(mac_address)
#
ipv4_list= ipv4_address.split('.')
ipv4_list[3] = '2'
gateway = '.'.join(ipv4_list)
ping_result = os.popen('ping ' + gateway + ' -c 1').read()
re_ping = re.findall(r'1 received',ping_result)

if re_ping:
    print('网关可达！')
else:
    print('网关不可达！')