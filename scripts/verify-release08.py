"""Independent arithmetic and IPv6 checks for release 0.8."""
from pathlib import Path
import json,ipaddress as ip
T={t['id']:t for p in Path('content/ccna').glob('*/*.yaml') for t in json.loads(p.read_text())['tasks']}
checks=0
def eq(a,b):
 global checks
 assert a==b,(a,b);checks+=1
def quiz(id):
 t=T[id];return next(o['text_md'] for o in t['options'] if o['id']==t['correct_option_id'])
def fields(id):return [b['accepted'][0] for b in T[id]['blanks']]
eq(quiz('ccna.transport.07'),str(1000+100))
eq(quiz('ccna.transport.08'),str(700+1))
eq(quiz('ccna.transport.17'),str(1500-20-20)+' B')
eq(quiz('ccna.ipv6.ext.16'),str(2**(64-56)))
eq(fields('ccna.ipv6.ext.05'),[str(ip.IPv6Network('::/0')),str(ip.IPv6Address('fe80::1'))])
eq(fields('ccna.ipv6.ext.09'),[str(ip.IPv6Address('fe80::9')),str(ip.IPv6Network('2001:db8:90::/64')),str(ip.IPv6Address('fe80::2'))])
a,b=ip.IPv6Interface('2001:db8:ab00:1::1/64'),ip.IPv6Interface('2001:db8:ab00:2::1/64')
eq(a.network.overlaps(b.network),False)
eq(fields('ccna.ipv6.ext.17'),['unicast-routing',str(a),str(b)])
eq(fields('ccna.nat.ext.03'),['443','8443'])
eq(fields('ccna.stp.ext.03'),[str(4096),str(2*4096)])
# All newly authored IPv6 accepted values are syntactically checked using Python,
# independent of the app's URL-based canonicalisation.
for t in T.values():
 if t['id'].startswith('ccna.ipv6.ext.'):
  for b in t.get('blanks',[]):
   if b['answer_type'] in ['ipv6','ipv6_prefix']:
    parser=ip.IPv6Address if b['answer_type']=='ipv6' else ip.IPv6Interface
    for value in b['accepted']:
     parsed=parser(value);eq(str(parsed),value)
print(f'Release 0.8: {checks} independent checks passed.')
