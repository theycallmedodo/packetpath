import {test} from 'node:test';
import assert from 'node:assert/strict';
import {normalize} from '../src/engine';
test('IPv6 equivalent notation and prefix retain host bits',()=>{
 assert.equal(normalize('2001:0DB8:0000:0000:0000:0000:0000:0001','ipv6'),normalize('2001:db8::1','ipv6'));
 assert.equal(normalize('2001:0DB8:0:0:0:0:0:1/064','ipv6_prefix'),normalize('2001:db8::1/64','ipv6_prefix'));
 assert.notEqual(normalize('2001:db8::2/64','ipv6_prefix'),normalize('2001:db8::1/64','ipv6_prefix'));
 assert.notEqual(normalize('2001:db8::1/65','ipv6_prefix'),normalize('2001:db8::1/64','ipv6_prefix'));
});
test('invalid IPv6 cannot match a valid address',()=>{
 for(const s of ['2001::db8::1','fe80::1%eth0','::1]/evil','::1/129','::1/-1','::1/64/64','::1'])assert.ok(normalize(s,'ipv6_prefix').startsWith('!invalid:'),s);
 assert.ok(normalize('::1/64','ipv6').startsWith('!invalid:'));
 assert.notEqual(normalize('VTY-MGMT','identifier'),normalize('vty-mgmt','identifier'));
});
