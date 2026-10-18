import type {Task,Blank,Stage,Pack} from './schema';
export type Answers=Record<string,string>;
export function normalize(value:string,type:Blank['answer_type']){
 const s=value.trim().replace(/\s+/g,' ');
 if(type==='ipv6'||type==='ipv6_prefix'){
  const parts=s.split('/');
  if(parts.length!==(type==='ipv6'?1:2)||!/^[:0-9a-fA-F.]+$/.test(parts[0]))return '!invalid:'+s;
  if(type==='ipv6_prefix'&&(!/^\d{1,3}$/.test(parts[1])||Number(parts[1])>128))return '!invalid:'+s;
  try {const host=new URL('http://['+parts[0]+']/').hostname;return host+(type==='ipv6_prefix'?'/'+Number(parts[1]):'');}
  catch{return '!invalid:'+s;}
 }
 return type==='keyword'||type==='command'?s.toLowerCase():s;
}
export function gradeBlank(b:Blank,value:string){const v=normalize(value,b.answer_type);return {correct:b.accepted.some(a=>normalize(a,b.answer_type)===v),feedback:b.common_errors[v]??'Sprawdź wymagania i kontekst tej luki.'};}
export function grade(task:Task,answers:Answers){const fields=task.type==='cli_fill_blank'?Object.fromEntries(task.blanks.map(b=>[b.id,gradeBlank(b,answers[b.id]??'')])):{choice:{correct:answers.choice===task.correct_option_id,feedback:task.options.find(o=>o.id===answers.choice)?.feedback_md??'Wybierz jedną odpowiedź.'}};const correctCount=Object.values(fields).filter(f=>f.correct).length;return {fields,correctCount,totalFields:Object.keys(fields).length,correct:correctCount===Object.keys(fields).length};}
export const complete=(t:Task,a:Answers)=>t.type==='single_choice'?t.options.some(o=>o.id===a.choice):t.blanks.every(b=>!!a[b.id]?.trim());
export type Attempt={taskId:string;revision:number;answers:Answers;correct:boolean;correctCount:number;totalFields:number;hintCount:number;at:string};
export type Session={packId:string;packRevision:number;taskCount:number;index:number;answers:Answers;checked:boolean;hintCount:number;attempts:Attempt[];finished:boolean;startedAt:string};
export const freshSession=(pack:Pack):Session=>({packId:pack.id,packRevision:pack.revision,taskCount:pack.tasks.length,index:0,answers:{},checked:false,hintCount:0,attempts:[],finished:false,startedAt:new Date().toISOString()});
export function submit(s:Session,t:Task):Session{if(s.checked||s.finished||!complete(t,s.answers))return s;const r=grade(t,s.answers);return {...s,checked:true,attempts:[...s.attempts,{taskId:t.id,revision:t.revision,answers:{...s.answers},correct:r.correct,correctCount:r.correctCount,totalFields:r.totalFields,hintCount:s.hintCount,at:new Date().toISOString()}]};}
export function advance(s:Session):Session{if(!s.checked||s.finished)return s;return s.index===s.taskCount-1?{...s,finished:true}:{...s,index:s.index+1,answers:{},checked:false,hintCount:0};}
export type Result={bestPercent:number;passed:boolean;completions:number;lastPercent:number};
export type Progress={sessions:Record<string,Session>;results:Record<string,Result>};
export const emptyProgress=():Progress=>({sessions:{},results:{}});
export const unlocked=(s:Stage,results:Progress['results'])=>s.requires.every(id=>results[id]?.passed===true);
export function record(progress:Progress,stage:Stage,s:Session):Progress{const previous=progress.sessions[stage.id];const next={sessions:{...progress.sessions,[stage.id]:s},results:{...progress.results}};if(s.finished&&s.attempts.length===s.taskCount&&!(previous?.finished&&previous.startedAt===s.startedAt)){const percent=s.attempts.filter(a=>a.correct).length/s.taskCount*100;const old=progress.results[stage.id];next.results[stage.id]={bestPercent:Math.max(old?.bestPercent??0,percent),passed:(old?.passed??false)||percent>=stage.pass_percent,completions:(old?.completions??0)+1,lastPercent:percent};}return next;}
