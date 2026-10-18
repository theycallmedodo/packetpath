"""Independent checks of numeric and structured-data questions added in 0.7."""
from pathlib import Path
import json,ipaddress as ip
T={t['id']:t for p in Path('content/ccna').glob('*/*.yaml') for t in json.loads(p.read_text())['tasks']}
checks=0
def eq(actual,expected):
 global checks
 assert actual==expected,(actual,expected);checks+=1
def quiz(tid):
 t=T[tid];return next(o['text_md'] for o in t['options'] if o['id']==t['correct_option_id'])
def fields(tid):return [b['accepted'][0] for b in T[tid]['blanks']]
net=ip.ip_network
prefix='ccna.ipv4.ext.'
eq(quiz(prefix+'01'),str(2**(28-24)))
eq(quiz(prefix+'02'),str(ip.ip_interface('172.16.7.200/23').network.network_address))
eq(fields(prefix+'03'),[str(next(net('10.44.8.0/22').hosts())),str(net('10.44.8.0/22').netmask)])
eq(quiz(prefix+'04'),str(ip.ip_interface('192.168.5.129/25').network.broadcast_address))
eq(fields(prefix+'05'),[str(list(net('192.0.2.10/31').hosts())[1]),str(net('192.0.2.10/31').netmask)])
eq(net('0.0.0.0/24').num_addresses-2>=200>net('0.0.0.0/25').num_addresses-2,True)
eq(quiz(prefix+'07'),'/24')
eq(net('10.1.0.0/25').overlaps(net('10.1.0.64/26')),True)
eq(fields(prefix+'09'),[str(next(n.hosts())) if i%2==0 else str(n.netmask) for i,n in enumerate([net('192.168.80.0/25')]*2+[net('192.168.80.128/26')]*2)])
eq(quiz(prefix+'10'),str(ip.ip_interface('192.168.90.192/26').network))
eq(fields(prefix+'11'),['10.1.0.65',str(next(net('10.1.0.128/26').hosts())),str(net('10.1.0.128/26').netmask)])
eq(net('10.1.0.0/25').overlaps(net('10.1.0.128/26')),False)
eq(quiz(prefix+'12'),str(list(ip.collapse_addresses([net(f'10.20.{i}.0/24') for i in range(4,8)]))[0]))
eq(len(list(ip.collapse_addresses([net('10.2.0.0/24'),net('10.2.2.0/24')]))),2)
eq(ip.ip_interface('10.10.1.10/23').network==ip.ip_interface('10.10.2.10/23').network,False)
eq(fields(prefix+'15'),[str(net('0.0.0.0/'+str(p)).netmask) for p in [26,27,28]])
eq(str(net('198.51.100.8/30').broadcast_address),'198.51.100.11')
eq(fields(prefix+'17'),[str(list(net('198.51.100.8/30').hosts())[1]),str(net('198.51.100.8/30').netmask),str(net('10.255.9.9/32').netmask)])
eq(net('0.0.0.0/27').num_addresses-2,29+1)
eq(quiz('ccna.acl.ext.06'),str(net('10.8.0.0/23').hostmask))
eq(fields('ccna.acl.ext.05'),[str(net('10.20.0.0/24').hostmask),'53'])
eq(quiz('ccna.ospf.ext.10'),str(10000//1000))
eq(quiz('ccna.fhrp.13'),str(120-30))
eq(quiz('ccna.wireless.03'),str(-65-(-90))+' dB')
eq(quiz('ccna.qos.05'),str(2**3))
eq(quiz('ccna.qos.09'),str(int('101110',2)))
# Parse every candidate in the JSON syntax quiz; only one is a valid object.
t=T['ccna.automation.04'];valid=[]
for o in t['options']:
 try:
  if isinstance(json.loads(o['text_md']),dict):valid.append(o['id'])
 except json.JSONDecodeError:pass
eq(valid,[t['correct_option_id']])
eq(type(json.loads('true')).__name__,'bool')
eq(type(json.loads('"true"')).__name__,'str')
eq(type(json.loads('{"interfaces":["Gi0/0","Gi0/1"]}')['interfaces']).__name__,'list')
print(f'Release 0.7: {checks} independent checks passed (addressing, numeric answers, JSON).')
