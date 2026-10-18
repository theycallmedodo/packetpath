"""Independent arithmetic checks against authored ENCOR answer keys; not an IOS lab."""
import json,ipaddress
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
tasks={t['id']:t for p in (ROOT/'content/encor').rglob('*.yaml') for t in json.loads(p.read_text())['tasks']}
checks=0
def quiz(key,expected):
 global checks
 t=tasks['encor.'+key];a=next(o['text_md'] for o in t['options'] if o['id']==t['correct_option_id']);assert a==expected,(key,a,expected);checks+=1
def blank(key,index,expected):
 global checks
 assert str(expected) in tasks['encor.'+key]['blanks'][index]['accepted'],key;checks+=1
summary=list(ipaddress.collapse_addresses(ipaddress.ip_network('10.10.'+str(i)+'.0/24') for i in range(4)))
assert len(summary)==1
quiz('ospf-multi.08',str(summary[0]));blank('ospf-multi.09',1,str(summary[0].netmask))
blank('ebgp.05',0,str(ipaddress.ip_network('10.20.0.0/16').netmask))
blank('ebgp.11',0,str(ipaddress.ip_network('172.20.4.0/24').netmask))
blank('ebgp.11',1,str(ipaddress.ip_network('172.20.8.0/23').netmask))
blank('vrf.11',1,str(ipaddress.ip_network('192.0.2.0/30').netmask))
quiz('gre.08',str(20+4));quiz('gre.13',f'{1500-20-4} B');quiz('gre.16',f'{1500-20-4-20-20} B')
quiz('qos-interpret.15',f'{20*25//100} Mb/s')
quiz('qos-interpret.02',str(int('101110',2)))
quiz('routing-compare.09','Tak, RD jest mniejsze od FD' if 1500<2000 else 'Nie')
quiz('routing-compare.10','Nie' if not 2000<2000 else 'Tak')
quiz('routing-compare.16',f'A, koszt {10+20}' if 10+20<5+40 else 'B')
quiz('routing-compare.17','OSPF' if 110<170 else 'External EIGRP')
assert ipaddress.ip_address('10.1.2.9') in ipaddress.ip_network('10.1.2.0/24')
quiz('routing-compare.18','Najdłuższy prefiks: /24')
print(f'{checks} independent ENCOR arithmetic/key checks passed')
