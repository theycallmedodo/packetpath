import { Capacitor } from '@capacitor/core';
import { Preferences } from '@capacitor/preferences';
import { KEY, restore, persist, parseProgress } from './storage';
import type { Progress } from './engine';

export async function initialProgress(): Promise<Progress> {
  if (!Capacitor.isNativePlatform()) return restore();
  const { value } = await Preferences.get({ key: KEY });
  // An unreadable native store must not be silently replaced by empty progress.
  return value === null ? restore() : parseProgress(value);
}

let pending: Promise<unknown> = Promise.resolve();
export function saveProgress(progress: Progress): Promise<boolean> {
  if (!Capacitor.isNativePlatform()) return Promise.resolve(persist(progress));
  const value = JSON.stringify(progress);
  const write = pending.then(async () => {
    await Preferences.set({ key: KEY, value });
    persist(progress); // Best-effort WebView mirror; native storage is authoritative.
    return true;
  }).catch(() => false);
  pending = write;
  return write;
}

export async function flushProgress() { await pending; }
