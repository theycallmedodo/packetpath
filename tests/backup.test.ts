import test from 'node:test';
import assert from 'node:assert/strict';
import { encodeBackup, decodeBackup } from '../src/backup';
import { emptyProgress } from '../src/engine';
test('backup preserves progress, scores and unlocks',()=>{
  const p=emptyProgress();p.results['encor.fhrp.stage-1']={bestPercent:100,passed:true,completions:2,lastPercent:50};
  assert.deepEqual(decodeBackup(encodeBackup(p)),p);
});
test('backup rejects unrelated JSON, future versions and invalid scores',()=>{
  assert.throws(()=>decodeBackup('{"hello":1}'));
  assert.throws(()=>decodeBackup(encodeBackup(emptyProgress()).replace('"version": 1','"version": 99')));
  const p=emptyProgress();p.results.bad={bestPercent:120,passed:true,completions:1,lastPercent:100};
  assert.throws(()=>encodeBackup(p));
});
test('backup rejects oversized input before parsing',()=>{
  assert.throws(()=>decodeBackup(' '.repeat(5*1024*1024+1)),/zbyt duży/);
});
