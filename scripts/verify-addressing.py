"""Independent ipaddress checks of authored network calculations (JSON-compatible YAML)."""
import json,ipaddress
from pathlib import Path
T={t['id']:t for p in Path('content/ccna').glob('*/*.yaml') for t in json.loads(p.read_text())['tasks']}
def answer(id,key):return next(b['accepted'][0] for b in T[id]['blanks'] if b['id']==key)
def net(cidr):return ipaddress.ip_network(cidr)
checks=[('ccna.ipv4.02','mask',str(net('192.168.10.0/24').netmask)),('ccna.ipv4.05','host',str(net('10.0.0.0/30').broadcast_address-1)),('ccna.ipv4.08','host',str(net('192.168.20.64/26').network_address+1)),('ccna.ipv4.08','mask',str(net('192.168.20.64/26').netmask)),('ccna.ipv4.09','host',str(net('172.16.4.32/28').broadcast_address-1)),('ccna.ipv4.09','mask',str(net('172.16.4.32/28').netmask)),('ccna.ipv4.11','mask',str(net('10.255.0.1/32').netmask)),('ccna.ipv4.14','mask',str(net('192.168.50.0/26').netmask)),('ccna.ipv4.15','r1',str(net('10.0.8.4/30').network_address+1)),('ccna.ipv4.15','r2',str(net('10.0.8.4/30').broadcast_address-1)),('ccna.ipv4.17','a',str(net('192.168.60.0/26').network_address+1)),('ccna.ipv4.17','b',str(net('192.168.60.64/27').network_address+1)),('ccna.ipv4.17','amask',str(net('192.168.60.0/26').netmask)),('ccna.ipv4.17','bmask',str(net('192.168.60.64/27').netmask)),('ccna.ipv4.18','gateway',str(net('10.20.30.64/27').broadcast_address-1)),('ccna.ipv4.18','mask',str(net('10.20.30.64/27').netmask)),('ccna.acl.17','wildcard',str(net('172.16.8.0/29').hostmask)),('ccna.nat.18','w1',str(net('10.10.0.0/24').hostmask)),('ccna.nat.18','w2',str(net('10.20.0.0/25').hostmask))]
for id,key,expected in checks:assert answer(id,key)==expected,(id,key,expected)
# Independently derive the six subnetting quiz answers.
expected={'ccna.ipv4.01':str(net('0.0.0.0/26').num_addresses-2),'ccna.ipv4.04':str(ipaddress.ip_interface('192.168.10.77/27').network),'ccna.ipv4.07':str(net('172.16.4.32/28').broadcast_address),'ccna.ipv4.10':'192.168.1.129','ccna.ipv4.13':'/26'}
for id,val in expected.items():
 t=T[id];opt=next(o for o in t['options'] if o['id']==t['correct_option_id']);assert opt['text_md']==val,(id,val)
assert ipaddress.ip_address(expected['ccna.ipv4.10']) in ipaddress.ip_interface('192.168.1.130/26').network
assert net('0.0.0.0/26').num_addresses-2>=50>net('0.0.0.0/27').num_addresses-2
assert not net('192.168.60.0/26').overlaps(net('192.168.60.64/27'))
print(f'Independent IPv4 checks passed: {len(checks)} fields, 5 quiz keys, VLSM size and overlap.')
# Validate every declared IPv6 answer independently of JavaScript URL parsing.
ipv6_fields=0
for t in T.values():
 for b in t.get('blanks',[]):
  if b['answer_type'] in ('ipv6','ipv6_prefix'):
   parse=ipaddress.IPv6Address if b['answer_type']=='ipv6' else ipaddress.IPv6Interface
   for a in b['accepted']:parse(a)
   ipv6_fields+=1
q=T['ccna.ipv6.13'];correct=next(o['text_md'] for o in q['options'] if o['id']==q['correct_option_id'])
assert str(2**(64-48)) in correct.replace(' ','')
q=T['ccna.dhcp.16'];correct=next(o['text_md'] for o in q['options'] if o['id']==q['correct_option_id'])
assert str(net('192.168.1.0/27').num_addresses-2-10) in correct
print(f'IPv6 syntax verified independently: {ipv6_fields} fields; /48-to-/64 and DHCP /27 capacity checked.')
