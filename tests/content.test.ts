import{test}from'node:test';import assert from'node:assert/strict';import fs from'node:fs';import YAML from'yaml';import{catalogSchema,packSchema}from'../src/schema';import{grade,freshSession,submit,advance,record,unlocked,emptyProgress}from'../src/engine';
const catalog=catalogSchema.parse(YAML.parse(fs.readFileSync('content/catalog.yaml','utf8')));const modules=catalog.courses.flatMap(c=>c.modules);const stages=modules.flatMap(m=>m.stages);const packs=stages.map(s=>packSchema.parse(YAML.parse(fs.readFileSync(s.pack_url.slice(1).replace('.json','.yaml'),'utf8'))));
test('1008 authored tasks: 665 quizzes, 343 CLI, forty-eight independent module starts',()=>{const tasks=packs.flatMap(p=>p.tasks);assert.equal(tasks.length,1008);assert.equal(tasks.filter(t=>t.type==='single_choice').length,665);assert.equal(tasks.filter(t=>t.type==='cli_fill_blank').length,343);assert.equal(new Set(tasks.map(t=>t.id)).size,1008);assert.equal(new Set(tasks.map(t=>t.prompt_md.trim())).size,1008);assert.equal(modules.length,48);assert.equal(stages.filter(s=>unlocked(s,{})).length,48);});
test('every accepted value and every quiz alternative grades as intended',()=>{for(const p of packs)for(const t of p.tasks){if(t.type==='single_choice'){for(const o of t.options){assert.equal(grade(t,{choice:o.id}).correct,o.id===t.correct_option_id,t.id);assert.ok(o.feedback_md.length>15);}}else{const answers=Object.fromEntries(t.blanks.map(b=>[b.id,b.accepted[0]]));for(const b of t.blanks){for(const a of b.accepted)assert.equal(grade(t,{...answers,[b.id]:a}).correct,true,t.id);assert.equal(grade(t,{...answers,[b.id]:'invalid-answer'}).correct,false,t.id);}}}});
test('all forty-eight module campaigns can be completed, with progression enforced independently',()=>{let progress=emptyProgress();for(const m of modules){for(const stage of m.stages){assert.equal(unlocked(stage,progress.results),true);const p=packs.find(p=>p.id===stage.id)!;let s=freshSession(p);for(const t of p.tasks){const answers=t.type==='single_choice'?{choice:t.correct_option_id}:Object.fromEntries(t.blanks.map(b=>[b.id,b.accepted[0]]));s=advance(submit({...s,answers},t));}progress=record(progress,stage,s);assert.equal(progress.results[stage.id].passed,true);}}assert.equal(Object.values(progress.results).filter(x=>x.passed).length,168);});
test('new modules contain progressive field counts and stage-specific theory',()=>{for(const p of packs.filter(p=>!p.id.includes('.ospf.'))){for(const t of p.tasks){if(t.type==='cli_fill_blank'){assert.ok(t.difficulty===1?t.blanks.length===1:t.difficulty===2?t.blanks.length===2:t.blanks.length>=3,t.id);}assert.ok(p.cards.some(c=>c.id===t.card_id));assert.ok(t.sources.every(s=>new URL(s.url).hostname.endsWith('cisco.com')));}}});
test('extensions unlock from existing stage 3, and preserve the old earned pass',()=>{
 for(const id of ['ipv4','vlan','acl','ospf','ipv6','stp','etherchannel','nat']){
  const m=modules.find(m=>m.id==='ccna.'+id)!;
  assert.equal(m.stages.length,6);
  const [third,fourth,fifth,sixth]=m.stages.slice(2);
  assert.deepEqual(fourth.requires,[third.id]);
  assert.equal(unlocked(fourth,{}),false);
  const results={[third.id]:{passed:true,bestPercent:100,lastPercent:50,completions:2}};
  assert.equal(unlocked(fourth,results),true);
  assert.equal(unlocked(fifth,results),false);
  assert.equal(unlocked(sixth,results),false);
  assert.deepEqual(fifth.requires,[fourth.id]);
  assert.deepEqual(sixth.requires,[fifth.id]);
 }
});
