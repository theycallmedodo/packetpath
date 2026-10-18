import React, { useState } from 'react';
import { Capacitor } from '@capacitor/core';
import { Filesystem, Directory, Encoding } from '@capacitor/filesystem';
import { Share } from '@capacitor/share';
import type { Progress } from './engine';
import { encodeBackup, decodeBackup, MAX_BACKUP_BYTES } from './backup';

export function BackupPanel({progress,onImport}:{progress:Progress;onImport:(p:Progress)=>Promise<void>}) {
  const [candidate,setCandidate] = useState<Progress|null>(null);
  const [message,setMessage] = useState('');
  const [busy,setBusy] = useState(false);
  async function exportFile() {
    setBusy(true); setMessage('');
    try {
      const text = encodeBackup(progress);
      const filename = `PacketPath-postepy-${new Date().toISOString().replace(/[:.]/g,'-')}.json`;
      if (Capacitor.isNativePlatform()) {
        const file = await Filesystem.writeFile({path:filename,data:text,directory:Directory.Cache,encoding:Encoding.UTF8});
        await Share.share({title:'Kopia postępów PacketPath',url:file.uri,dialogTitle:'Zapisz kopię postępów'});
        setMessage('Wybierz miejsce zapisu w menu udostępniania.');
      } else {
        const url=URL.createObjectURL(new Blob([text],{type:'application/json'}));
        const link=document.createElement('a');link.href=url;link.download=filename;link.click();
        setTimeout(()=>URL.revokeObjectURL(url),10000);
        setMessage('Kopia została przygotowana do pobrania.');
      }
    } catch { setMessage('Nie udało się wyeksportować kopii lub anulowano udostępnianie.'); }
    finally { setBusy(false); }
  }
  return <section className="backup-panel"><h2>Kopia postępów</h2>
    <p>Przenieś wyniki między przeglądarką i telefonem. Zachowaj kopię przed odinstalowaniem aplikacji.</p>
    <button className="primary" disabled={busy} onClick={exportFile}>Eksportuj postępy</button>
    <label className="backup-import">Wczytaj kopię JSON<input disabled={busy} type="file" accept="application/json,.json" onChange={async e=>{
      const file=e.target.files?.[0];e.target.value='';if(!file)return;
      setMessage('');setCandidate(null);
      try { if(file.size>MAX_BACKUP_BYTES)throw Error('Plik jest zbyt duży.');setCandidate(decodeBackup(await file.text())); }
      catch {setMessage('Nieprawidłowa kopia PacketPath. Obecne postępy nie zostały zmienione.');}
    }}/></label>
    {candidate&&<div role="group" aria-label="Potwierdzenie importu"><p>Kopia zawiera {Object.keys(candidate.results).length} wyników stopni. Import zastąpi bieżące postępy.</p>
      <button disabled={busy} className="primary" onClick={async()=>{setBusy(true);try{await onImport(candidate);setCandidate(null);setMessage('Postępy zaimportowane.');}catch{setMessage('Nie udało się zapisać kopii. Import nie został zastosowany.');}finally{setBusy(false);}}}>Zastąp postępy kopią</button>
      <button disabled={busy} className="text-button" onClick={()=>setCandidate(null)}>Anuluj</button></div>}
    <p role="status">{message}</p>
  </section>;
}
