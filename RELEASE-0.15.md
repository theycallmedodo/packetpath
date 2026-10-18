# PacketPath 0.15 — gotowe zmiany bazy

- 4222 zadania, 48 działów, 561 sekcji.
- 2156 CCNA i 2066 ENCOR.
- BGP: 180; VLAN: 144; inne działy: 82 lub 100 zadań.
- 336 nowych przypadków, po cztery rozdzielone decyzje na przypadek.
- 460 par zgłoszeń, po cztery zadania porównawcze na parę (1840 ćwiczeń).
- 30 nowych zadań pełnych komend CLI.
- Wszystkie 168 starych paczek, ID i rewizje pozostają identyczne.

Sprawdzone: 31 testów Node, walidacja 4222 zadań, TypeScript, produkcyjny build
Vite i synchronizacja Capacitor Android. Nie wykonywano komend na rzeczywistych
routerach. Test wizualny przeglądarki był niedostępny z powodu braku działającego
pliku Chromium w środowisku. Nie zbudowano podpisanego APK.

Baza wyjściowa: commit cab0b9c7c614a4428678140af2baa556b000a66d.
Zapis do GitHub zatrzymał błąd 403 Resource not accessible by integration.
Publiczna widoczność repozytorium umożliwia odczyt, nie nadaje integracji zapisu.

Po udostępnieniu zapisu do theycallmedodo/packetpath można wysłać przygotowaną
zmianę i uruchomić workflow Build Android APK. Workflow używa istniejącego
klucza podpisu, potrzebnego do aktualizacji dotychczasowej instalacji.

Pełne źródła znajdują się w katalogu packetpath. Plik packetpath-v0.15.bundle
pozwala przenieść gotową gałąź wraz z zachowaniem historii. W istniejącym klonie:

```sh
git fetch /sciezka/packetpath-v0.15.bundle codex/expand-practice-v015
git switch -c codex/expand-practice-v015 FETCH_HEAD
npm ci
npm test
npm run build
```

Zmiany nie kasują postępów. Nie odinstalowuj poprzedniej aplikacji, aby zachować
jej dane; nowy APK powinien być podpisany tym samym kluczem.
