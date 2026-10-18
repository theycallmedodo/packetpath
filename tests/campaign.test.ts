import{test}from'node:test';import assert from'node:assert/strict';import fs from'node:fs';import{catalogSchema,packSchema,taskSchema}from'../src/schema';import{courseView}from'../src/campaign';import{unlocked}from'../src/engine';
const catalog=catalogSchema.parse(JSON.parse(fs.readFileSync('content/catalog.yaml','utf8')));
test('course selection scopes totals, attempts and passes without modifying saved results',()=>{
 const results={'ccna.ospf.stage-1':{passed:true,bestPercent:100,lastPercent:100,completions:2},'encor.ebgp.stage-1':{passed:true,bestPercent:100,lastPercent:100,completions:1}};
 const before=JSON.stringify(results);
 const ccna=courseView(catalog,'ccna',results),encor=courseView(catalog,'encor',results);
 assert.equal(ccna.stages.length,290);assert.equal(encor.stages.length,271);
 assert.equal(ccna.passed,1);assert.equal(encor.passed,1);
 assert.equal(ccna.completions,2);assert.equal(encor.completions,1);
 assert.equal(courseView(catalog,'missing',results).course?.id,'ccna');
 assert.equal(courseView(null,'encor',results).stages.length,0);
 assert.equal(JSON.stringify(results),before);
});
test('CCNA completion cannot unlock ENCOR stage two; ENCOR progression remains local',()=>{
 const encor=courseView(catalog,'encor',{});
 const results={'ccna.ospf.stage-1':{passed:true,bestPercent:100,lastPercent:100,completions:1}};
 for(const m of encor.modules){assert.equal(unlocked(m.stages[0],results),true);assert.equal(unlocked(m.stages[1],results),false);assert.deepEqual(m.stages[1].requires,[m.stages[0].id]);assert.deepEqual(m.stages[2].requires,[m.stages[1].id]);}
});
test('ENCOR packs declare 350-401 v1.2 and contain 2066 unique tasks in twenty-four modules',()=>{
 const c=catalog.courses.find(c=>c.id==='encor')!;assert.equal(c.exam,'350-401');assert.equal(c.blueprint_version,'1.2');assert.equal(c.modules.length,24);
 let n=0;
 for(const m of c.modules)for(const s of m.stages){const p=packSchema.parse(JSON.parse(fs.readFileSync(s.pack_url.slice(1).replace('.json','.yaml'),'utf8')));n+=p.tasks.length;for(const t of p.tasks){assert.ok(t.id.startsWith('encor.'));assert.ok(t.blueprint_refs.every(r=>r.exam==='350-401'&&r.version==='1.2'));}}
 assert.equal(n,2066);
});
test('all 96 CCNA v0.8 packs and course metadata remain unchanged',async()=>{
 const{createHash}=await import('node:crypto');
 const before=JSON.parse(fs.readFileSync('tests/fixtures/ccna-v08-hashes.json','utf8'));
 const current=structuredClone(catalog.courses.find(c=>c.id==='ccna')!); for(const m of current.modules)m.stages=m.stages.filter(s=>!s.id.includes('.practice-')) as typeof m.stages; assert.deepEqual(current,before.course);
 assert.equal(Object.keys(before.files).length,96);
 for(const[file,hash]of Object.entries(before.files))assert.equal(createHash('sha256').update(fs.readFileSync(file)).digest('hex'),hash,file);
});

test('code options preserve case distinctions but reject exact duplicate options',()=>{
 const pack=JSON.parse(fs.readFileSync('content/encor/python/stage-2.yaml','utf8'));
 const task=pack.tasks.find((t:any)=>t.id==='encor.python.11');
 assert.equal(taskSchema.safeParse(task).success,true);
 const bad=structuredClone(task);bad.options[1].text_md=bad.options[0].text_md;
 assert.equal(taskSchema.safeParse(bad).success,false);
});
