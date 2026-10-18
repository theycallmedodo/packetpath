import batch08_network
import batch08_services
import batch08_ipv6
import batch08_stp
import batch08_etherchannel
import batch08_nat
from batch07 import ROOT,cat,all_new,json
assert len(all_new)==144
cat['revision']+=1
(ROOT/'content/catalog.yaml').write_text(json.dumps(cat,ensure_ascii=False,indent=2)+'\n')
print('Added',len(all_new),'tasks')
