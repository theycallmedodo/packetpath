import type {Catalog} from './schema';
import type {Progress} from './engine';
export function courseView(catalog:Catalog|null,id:string,results:Progress['results']){
 const course=catalog?.courses.find(c=>c.id===id)??catalog?.courses[0];
 const modules=course?.modules??[];
 const stages=modules.flatMap(m=>m.stages);
 const passed=stages.filter(s=>results[s.id]?.passed).length;
 const completions=stages.reduce((n,s)=>n+(results[s.id]?.completions??0),0);
 return {course,modules,stages,passed,completions};
}
