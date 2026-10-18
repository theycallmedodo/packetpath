"""Compile authored cases into spaced diagnostic exercises. No random/IP variants."""
import json, hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
SRC=ROOT/'scripts/authoring/scenarios'
cat=json.loads((ROOT/'content/catalog.yaml').read_text())
modules={m['id']:m for c in cat['courses'] for m in c['modules']}
cases={};cli={}
for path in sorted(SRC.glob('*.txt')):
    target=cli if path.name=='cli.txt' else cases
    for line in path.read_text().splitlines():
        if line.startswith('# '): key=line[2:];target[key]=[]
        elif line.strip():
            row=line.split('|');assert len(row)==(4 if target is cli else 6),(path,row)
            target[key].append(row)
assert set(cases)==set(modules),set(modules)-set(cases)
fixture=ROOT/'tests/fixtures/v014-content.json'
if not fixture.exists():
    hashes={s['pack_url'][1:].replace('.json','.yaml'):hashlib.sha256((ROOT/s['pack_url'][1:].replace('.json','.yaml')).read_bytes()).hexdigest() for m in modules.values() for s in m['stages']}
    fixture.write_text(json.dumps({'catalog':cat,'files':hashes},ensure_ascii=False,indent=2)+'\n')
base=json.loads(fixture.read_text())['catalog']
base_modules={m['id']:m for c in base['courses'] for m in c['modules']}
cat['revision']=base['revision']+1
PHASES=[('Rozpoznanie','Które rozpoznanie najlepiej wyjaśnia podane obserwacje?',2),('Działanie','Które działanie najlepiej odpowiada wymaganiom tego przypadku?',3),('Weryfikacja','Który wynik najbezpośredniej potwierdza oczekiwany stan w tym przypadku?',4),('Zależności','Która zasada najbezpośredniej wyjaśnia opisany mechanizm?',5)]
EXTRA={
'encor.ebgp':[('Cisco — BGP case studies','https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/26634-bgp-toc.html'),('Cisco — BGP command reference','https://www.cisco.com/c/en/us/td/docs/ios/iproute_bgp/command/reference/irg_book/irg_bgp3.html')],
'ccna.vlan':[('Cisco — VLAN trunking','https://www.cisco.com/c/en/us/td/docs/switches/lan/c9000/lyr2-fwd/vlan/vlan-configuration-guide/configure-vlan-trunks.html')],
'encor.python':[('Python — tutorial','https://docs.python.org/3/tutorial/')],
'encor.json':[('JSON — RFC 8259','https://www.rfc-editor.org/rfc/rfc8259')],
'encor.yang':[('YANG 1.1 — RFC 7950','https://www.rfc-editor.org/rfc/rfc7950')],
'encor.netconf':[('NETCONF — RFC 6241','https://www.rfc-editor.org/rfc/rfc6241')],
'encor.restconf':[('RESTCONF — RFC 8040','https://www.rfc-editor.org/rfc/rfc8040')],
}
summary=[]
for key,rows in cases.items():
    module=modules[key];old=base_modules[key]['stages'];module['stages']=json.loads(json.dumps(old))
    oldpacks=[json.loads((ROOT/s['pack_url'][1:].replace('.json','.yaml')).read_text()) for s in old]
    sources=[]
    for p in oldpacks:
        for t in p['tasks']:
            for s in t['sources']:
                if s['url'] not in [x['url'] for x in sources]:sources.append(s)
    sources += [dict(title=t,url=u) for t,u in EXTRA.get(key,[]) if u not in [s['url'] for s in sources]]
    refs=[]
    for p in oldpacks:
        for t in p['tasks']:
            for r in t['blueprint_refs']:
                if r not in refs:refs.append(r)
    groups=[]
    for phase,(label,question,field) in enumerate(PHASES):
        tasks=[];cards=[]
        for i,row in enumerate(rows):
            title,context,cause,action,evidence,principle=row
            tid=f'{key}.practice.case-{i+1:02}.{phase+1}'
            explain=f'{principle}\n\n**Rozpoznanie:** {cause}\n\n**Działanie:** {action}\n\n**Sprawdzenie:** {evidence}'
            # Each wrong choice is a real alternative from this module, with a specific explanatory context.
            others=[j for j in range(len(rows)) if j!=i]
            # Stable, phase-dependent alternatives; never solely rotating the correct answer.
            order=sorted(others,key=lambda j:hashlib.sha256(f'{key}/{i}/{phase}/{j}'.encode()).hexdigest())[:3]
            options=[dict(text_md=rows[j][field],feedback_md=f'Ta odpowiedź odnosi się do przypadku „{rows[j][0]}”: {rows[j][1]} W bieżącym przypadku: {row[field]}') for j in order]
            pos=(i+phase*3)%4
            options.insert(pos,dict(text_md=row[field],feedback_md=explain))
            for letter,opt in zip('ABCD',options):opt['id']=letter
            t=dict(id=tid,revision=1,title=f'{title} — {label.lower()}',skills=[f'{key}.case-{i+1:02}',f'practice.{phase+1}'],sources=sources,blueprint_refs=refs,difficulty=2 if phase==0 else 3,prompt_md=f'{context}\n\n{question}',hints=[['Oddziel stan administracyjny, transport i logikę usługi. Wykorzystaj konkretne dane z opisu.','Wybierz działanie usuwające wskazaną przyczynę i respektujące zakres zmiany.','Dowód powinien dotyczyć tego samego przepływu, segmentu lub obiektu co problem.','Rozróżnij warunek konieczny od wystarczającego; uwzględnij zakres mechanizmu.'][phase]],explanation_md=explain,card_id=tid+'.card',type='single_choice',options=options,correct_option_id='ABCD'[pos])
            tasks.append(t);cards.append({k:t[k] for k in ['revision','title','skills','sources']}|dict(id=t['card_id'],front_md=f'{context}\n\n{question}',back_md=explain,example=row[field]))
        size=12 if len(rows)>=12 else 6
        for offset in range(0,len(tasks),size):groups.append((f'{label} — przypadki {offset+1}–{min(offset+size,len(rows))}',tasks[offset:offset+size],cards[offset:offset+size]))
    # Contrast practice: distinguish two independently described incidents rather than
    # merely repeat a question with different IP addresses. Each pair appears in
    # four separated stages, testing diagnosis, action, evidence and mechanism.
    if key not in {'encor.ebgp','ccna.vlan'}:
        pairs=[(0,1),(2,3),(4,5),(0,2),(1,4),(3,5),(0,5),(1,3),(2,4),(0,3)]
        for phase,(label,question,field) in enumerate(PHASES):
            tasks=[];cards=[]
            for n,(a,b) in enumerate(pairs,1):
                left,right=rows[a],rows[b];other=rows[next(j for j in range(len(rows)) if j not in (a,b))]
                tid=f'{key}.practice.compare-{n:02}.{phase+1}'
                pair=lambda x,y:f'I — {x}\n\nII — {y}'
                good=pair(left[field],right[field])
                wrong=[pair(right[field],left[field]),pair(left[field],other[field]),pair(other[field],right[field])]
                explanations=[f'Zamieniono przypisania. Zgłoszenie I: {left[2]} Zgłoszenie II: {right[2]}',f'Pierwsze przypisanie pasuje, ale drugie dotyczy innego przypadku: {other[1]} Dla II: {right[field]}',f'Drugie przypisanie pasuje, ale pierwsze dotyczy innego przypadku: {other[1]} Dla I: {left[field]}']
                explain=f'**Zgłoszenie I:** {left[2]} {left[3]}\n\n**Sprawdzenie I:** {left[4]}\n\n**Zgłoszenie II:** {right[2]} {right[3]}\n\n**Sprawdzenie II:** {right[4]}\n\n**Zależności:** {left[5]} {right[5]}'
                opts=[dict(text_md=w,feedback_md=e) for w,e in zip(wrong,explanations)];pos=(n+phase)%4
                opts.insert(pos,dict(text_md=good,feedback_md=explain))
                for letter,opt in zip('ABCD',opts):opt['id']=letter
                prompt=f'**Zgłoszenie I**\n\n{left[1]}\n\n**Zgłoszenie II**\n\n{right[1]}\n\nOceń każde zgłoszenie oddzielnie. {question} Wybierz parę, w której **oba przypisania** są poprawne.'
                t=dict(id=tid,revision=1,title=f'Dwa zgłoszenia {n} — {label.lower()}',skills=[f'{key}.contrast',f'practice.{phase+1}'],sources=sources,blueprint_refs=refs,difficulty=3,prompt_md=prompt,hints=['Nie przenoś rozpoznania z pierwszego zgłoszenia na drugie. Sprawdź osobno wszystkie warunki obu opisów.'],explanation_md=explain,card_id=tid+'.card',type='single_choice',options=opts,correct_option_id='ABCD'[pos])
                tasks.append(t);cards.append({k:t[k] for k in ['revision','title','skills','sources']}|dict(id=t['card_id'],front_md=prompt,back_md=explain,example=good))
            groups.append((f'Dwa zgłoszenia — {label.lower()}',tasks,cards))
    tasks=[];cards=[]
    for i,(title,prompt,commands,explain) in enumerate(cli.get(key,[])):
        tid=f'{key}.practice.cli-{i+1:02}';lines=commands.split(';')
        t=dict(id=tid,revision=1,title=title,skills=[f'{key}.cli-practice'],sources=sources,blueprint_refs=refs,difficulty=3,prompt_md=prompt+' Wpisz pełne komendy w podanej kolejności, bez promptu urządzenia.',hints=['Zwróć uwagę na podany tryb CLI, kierunek działania i wymaganie zachowania istniejącej konfiguracji.'],explanation_md=explain,card_id=tid+'.card',type='cli_fill_blank',platform='Cisco IOS / IOS XE; składnia wskazana w zadaniu',template='\n'.join('{{cmd'+str(j)+'}}' for j in range(len(lines))),blanks=[dict(id=f'cmd{j}',label=f'Pełna komenda {j+1}',answer_type='command',accepted=[line],width=min(60,max(16,len(line)+2)),common_errors={}) for j,line in enumerate(lines)])
        tasks.append(t);cards.append({k:t[k] for k in ['revision','title','skills','sources']}|dict(id=t['card_id'],front_md=prompt,back_md=explain,example='\n'.join(lines)))
    for offset in range(0,len(tasks),6):groups.append((f'Praktyka CLI — zestaw {offset//6+1}',tasks[offset:offset+6],cards[offset:offset+6]))
    for n,(title,tasks,cards) in enumerate(groups,1):
        sid=f'{key}.practice-{n}';course,slug=key.split('.',1);rel=f'content/{course}/{slug}/practice-{n}.yaml'
        pack=dict(schema_version=3,id=sid,revision=1,cards=cards,tasks=tasks)
        (ROOT/rel).write_text(json.dumps(pack,ensure_ascii=False,indent=2)+'\n')
        module['stages'].append(dict(id=sid,title=title,description='Przypadki praktyczne: konkretne obserwacje, uzasadniona decyzja i informacja zwrotna.',difficulty=tasks[0]['difficulty'],order=len(module['stages'])+1,pack_url='/'+rel.replace('.yaml','.json'),pack_revision=1,task_count=len(tasks),pass_percent=80,requires=[module['stages'][-1]['id']]))
    before=sum(s['task_count'] for s in old);after=sum(s['task_count'] for s in module['stages'])
    summary.append(dict(id=key,title=module['title'],before=before,after=after,added=after-before,cases=len(rows)))
(ROOT/'content/catalog.yaml').write_text(json.dumps(cat,ensure_ascii=False,indent=2)+'\n')
(ROOT/'CONTENT-EXPANSION.json').write_text(json.dumps({'base_version':'0.14.0','version':'0.15.0','modules':summary,'total':sum(m['after'] for m in summary),'added':sum(m['added'] for m in summary)},ensure_ascii=False,indent=2)+'\n')
print('Total:',sum(m['after'] for m in summary),'Added:',sum(m['added'] for m in summary),'Modules:',len(summary))
