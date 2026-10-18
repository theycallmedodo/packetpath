import{z}from'zod';import{emptyProgress,type Progress}from'./engine';
const attempt=z.object({taskId:z.string(),revision:z.number(),answers:z.record(z.string()),correct:z.boolean(),correctCount:z.number().int().nonnegative(),totalFields:z.number().int().positive(),hintCount:z.number().int().nonnegative(),at:z.string()});
const session=z.object({packId:z.string(),packRevision:z.number().int().positive(),taskCount:z.number().int().positive(),index:z.number().int().nonnegative(),answers:z.record(z.string()),checked:z.boolean(),hintCount:z.number().int().nonnegative(),attempts:z.array(attempt),finished:z.boolean(),startedAt:z.string()}).refine(s=>s.index<s.taskCount&&s.attempts.length===s.index+(s.checked?1:0)&&(!s.finished||(s.index===s.taskCount-1&&s.checked)));
export const progressSchema=z.object({sessions:z.record(session),results:z.record(z.object({bestPercent:z.number().min(0).max(100),passed:z.boolean(),completions:z.number().int().nonnegative(),lastPercent:z.number().min(0).max(100)}))});
export const KEY='packetpath:campaign:v3';
export function restore():Progress{try{const r=progressSchema.safeParse(JSON.parse(localStorage.getItem(KEY)||'null'));if(r.success)return r.data;}catch{}return emptyProgress();}
export function persist(p:Progress){try{localStorage.setItem(KEY,JSON.stringify(p));return true;}catch{return false;}}

export function parseProgress(text:string):Progress{return progressSchema.parse(JSON.parse(text));}
