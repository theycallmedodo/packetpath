import { z } from 'zod';
import { progressSchema } from './storage';
import type { Progress } from './engine';
const backupSchema = z.object({
  app: z.literal('PacketPath'), version: z.literal(1),
  exportedAt: z.string(), progress: progressSchema,
});
export const MAX_BACKUP_BYTES = 5 * 1024 * 1024;
export function encodeBackup(progress: Progress): string {
  return JSON.stringify({ app: 'PacketPath', version: 1,
    exportedAt: new Date().toISOString(), progress: progressSchema.parse(progress) }, null, 2);
}
export function decodeBackup(text: string): Progress {
  if (new TextEncoder().encode(text).length > MAX_BACKUP_BYTES) throw Error('Plik jest zbyt duży (maks. 5 MB).');
  const result = backupSchema.safeParse(JSON.parse(text));
  if (!result.success) throw Error('Nieprawidłowa kopia postępów PacketPath.');
  return result.data.progress;
}
