"""Hand-authored release 0.7 content; run once against 0.6. No random variants."""
import json,re,copy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
cat=json.loads((ROOT/'content/catalog.yaml').read_text())
existing={m['id']:m for m in cat['courses'][0]['modules']}
all_new=[]
def start(key,title,obj,urls,extend=False):
 global meta,tasks,cards
 meta=(key,title,obj,urls,extend);tasks=[];cards=[]
def base(title,prompt,explain,hint):
 key,title_m,obj,urls,ext=meta;n=len(tasks)+1
 tid=f'ccna.{key}.'+('ext.' if ext else '')+f'{n:02}'
 d=([2,3,3] if ext else [1,2,3])[(n-1)//6]
 common=dict(id=tid,revision=1,title=title,skills=[f'{key}.'+re.sub(r'[^a-z0-9]+','-',title.lower()).strip('-')],sources=[dict(title='Dokumentacja Cisco — '+title_m,url=u) for u in urls])
 return dict(common,blueprint_refs=[dict(exam='200-301',version='1.1',objective=obj)],difficulty=d,prompt_md=prompt,hints=[hint or explain],explanation_md=explain,card_id=tid+'.theory')
def card(t,example):
 cards.append({k:t[k] for k in ['revision','title','skills','sources']}|dict(id=t['card_id'],front_md=t['title'],back_md=t['explanation_md'],example=example));tasks.append(t)
def q(title,prompt,answer,wrong,explain,hint=''):
 t=base(title,prompt,explain,hint);n=len(tasks);pos=(n*3+n//6)%4
 opts=[]
 for w in wrong:
  text,reason=w.split('|',1);opts.append(dict(text_md=text,feedback_md=reason))
 opts.insert(pos,dict(text_md=answer,feedback_md=explain));assert len(opts)==4
 for i,o in enumerate(opts):o['id']='ABCD'[i]
 t.update(type='single_choice',options=opts,correct_option_id='ABCD'[pos]);card(t,answer)
def c(title,prompt,template,values,explain,hint=''):
 t=base(title,prompt,explain,hint);blanks=[];example=template
 for i,v in enumerate(values):
  if isinstance(v,str):a=[v];typ='command'
  else:a,typ=v
  blanks.append(dict(id=f'b{i}',label=f'Luka {i+1}',answer_type=typ,accepted=a,width=min(56,max(6,len(a[0])+2)),common_errors={}))
  example=example.replace('{{b'+str(i)+'}}',a[0])
 t.update(type='cli_fill_blank',platform='Cisco IOS / IOS XE; zgodnie z założeniami zadania',template=template,blanks=blanks);card(t,example)
def end():
 key,title,obj,urls,ext=meta;assert len(tasks)==18,(key,len(tasks))
 module=existing.get('ccna.'+key) if ext else dict(id='ccna.'+key,title=title,description='Od pojęć do analizy i praktycznych scenariuszy.',stages=[])
 if not ext:
  assert module['id'] not in existing
  cat['courses'][0]['modules'].append(module)
 start_order=len(module['stages'])
 for i in range(3):
  order=start_order+i+1;sid=f'ccna.{key}.stage-{order}';path=f'content/ccna/{key}/stage-{order}.yaml'
  p=ROOT/path;assert not p.exists(),path;p.parent.mkdir(exist_ok=True)
  p.write_text(json.dumps(dict(schema_version=3,id=sid,revision=1,cards=cards[i*6:i*6+6],tasks=tasks[i*6:i*6+6]),ensure_ascii=False,indent=2)+'\n')
  module['stages'].append(dict(id=sid,title=(['Rozszerzenie — zależności','Rozszerzenie — konfiguracja','Rozszerzenie — diagnostyka'] if ext else ['Podstawy','Zastosowanie','Scenariusze'])[i],description='Sześć zadań z teorią i wyjaśnieniem odpowiedzi.',difficulty=tasks[i*6]['difficulty'],order=order,pack_url='/'+path.replace('.yaml','.json'),pack_revision=1,task_count=6,pass_percent=80,requires=[] if order==1 else [f'ccna.{key}.stage-{order-1}']))
 all_new.extend(tasks)

def save():
 assert len(all_new)==180,len(all_new)
 cat['revision']+=1;(ROOT/'content/catalog.yaml').write_text(json.dumps(cat,ensure_ascii=False,indent=2)+'\n')
 print('Added',len(all_new),'tasks')
