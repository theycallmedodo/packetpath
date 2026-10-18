import {test} from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {createHash} from 'node:crypto';
import {catalogSchema,packSchema} from '../src/schema';
import {unlocked} from '../src/engine';
const catalog=catalogSchema.parse(JSON.parse(fs.readFileSync('content/catalog.yaml','utf8')));
const baseline=JSON.parse(fs.readFileSync('tests/fixtures/v014-content.json','utf8'));
const modules=catalog.courses.flatMap(c=>c.modules);
test('all 168 original packs and their stage contracts are preserved byte for byte',()=>{
 assert.equal(Object.keys(baseline.files).length,168);
 for(const [path,hash] of Object.entries(baseline.files))assert.equal(createHash('sha256').update(fs.readFileSync(path)).digest('hex'),hash,path);
 for(const c of baseline.catalog.courses)for(const old of c.modules){const m=modules.find(m=>m.id===old.id)!;assert.deepEqual(m.stages.slice(0,old.stages.length),old.stages);}
});
test('each existing module gains 24 or more tasks and continues from its previous final pass',()=>{
 for(const c of baseline.catalog.courses)for(const old of c.modules){
  const m=modules.find(m=>m.id===old.id)!;const added=m.stages.slice(old.stages.length);const last=old.stages.at(-1);
  assert.ok(added.reduce((sum,s)=>sum+s.task_count,0)>=24,m.id); assert.ok(m.stages.reduce((sum,s)=>sum+s.task_count,0)>=80,m.id);
  assert.deepEqual(added[0].requires,[last.id]);assert.equal(unlocked(added[0],{}),false);
  assert.equal(unlocked(added[0],{[last.id]:{passed:true,bestPercent:100,lastPercent:80,completions:1}}),true);
  assert.equal(unlocked(added[1],{[last.id]:{passed:true,bestPercent:100,lastPercent:80,completions:1}}),false);
  for(let i=1;i<m.stages.length;i++)assert.deepEqual(m.stages[i].requires,[m.stages[i-1].id]);
 }
 for(const [id,total] of [['encor.ebgp',180],['ccna.vlan',144]] as const)assert.equal(modules.find(m=>m.id===id)!.stages.reduce((n,s)=>n+s.task_count,0),total);
});
test('336 distinct cases recur across four separated decisions, each with contextual feedback',()=>{
 const cases=new Map<string,{phases:Set<string>,stages:Set<string>}>();let cli=0;
 for(const m of modules)for(const s of m.stages.filter(s=>s.id.includes('.practice-'))){
  const p=packSchema.parse(JSON.parse(fs.readFileSync(s.pack_url.slice(1).replace('.json','.yaml'),'utf8')));
  for(const t of p.tasks){
   if(t.type==='cli_fill_blank'){cli++;assert.ok(t.blanks.every(b=>b.answer_type==='command'));continue;}
   if(t.id.includes('.compare-'))continue;
   const stem=t.id.replace(/\.[1-4]$/,'');const record=cases.get(stem)??{phases:new Set<string>(),stages:new Set<string>()};record.phases.add(t.id.slice(-1));record.stages.add(s.id);cases.set(stem,record);
   assert.equal(new Set(t.options.map(o=>o.feedback_md)).size,4,t.id);
   assert.ok(t.explanation_md.includes('**Sprawdzenie:**'),t.id);
  }
 }
 assert.equal(cases.size,336);assert.equal(cli,30);
 for(const [id,value] of cases){assert.equal(value.phases.size,4,id);assert.equal(value.stages.size,4,id);}
});
test('contrast pairs cover all 46 other modules, with four separated decisions per pair',()=>{
 let total=0;
 for(const m of modules.filter(m=>!['encor.ebgp','ccna.vlan'].includes(m.id))){
  const pairs=new Map<string,Set<string>>();
  for(const s of m.stages.filter(s=>s.id.includes('.practice-'))){
   const p=packSchema.parse(JSON.parse(fs.readFileSync(s.pack_url.slice(1).replace('.json','.yaml'),'utf8')));
   for(const t of p.tasks.filter(t=>t.id.includes('.compare-'))){
    assert.equal(t.type,'single_choice');if(t.type!=='single_choice')continue;
    assert.ok(t.prompt_md.includes('**Zgłoszenie I**')&&t.prompt_md.includes('**Zgłoszenie II**'));
    assert.equal(new Set(t.options.map(o=>o.feedback_md)).size,4,t.id);
    const key=t.id.replace(/\.[1-4]$/,'');const phases=pairs.get(key)??new Set<string>();phases.add(s.id);pairs.set(key,phases);total++;
   }
  }
  assert.equal(pairs.size,10,m.id);for(const [key,phases] of pairs)assert.equal(phases.size,4,key);
 }
 assert.equal(total,1840);
});
