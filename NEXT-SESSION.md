# Aktualizacja 0.14 — Android

Przygotowany projekt Android i GitHub Actions. Użytkownik pracuje wyłącznie z telefonu, ma Termux i GitHub. Następny krok: instrukcja ANDROID-Z-TELEFONU.md, logowanie GitHub, START-ANDROID-TERMUX.sh, build i test APK. Nie twierdzić, że APK został już zbudowany lub przetestowany.

# Punkt startowy następnej sesji — PacketPath 0.13

Stan końcowy: 1008 zadań, 576 CCNA + 432 ENCOR. 48 działów, 168 stopni. Motyw Matrix. Dostawa lokalna jako ZIP; START-WINDOWS.bat wymaga Node.js. Zachować ten sam profil przeglądarki i localhost:5173.

Ostatnia paczka: HSRP/VRRP, NTP/PTP, PBR — 54 zadania. Wszystkie 159 wcześniejszych plików paczek zachowano. 24 testy, TypeScript i build przeszły; 5 niezależnych kontroli kluczy nowej partii. Bez labu IOS, testu Windows ani testu wizualnego przeglądarki.

## Proponowany następny krok

1. ENCOR L2: diagnostyka trunków/DTP, EtherChannel/LACP/PAgP, MST/RSTP i ochrona STP. Trzy brakujące cele 3.1.a–c. Korzystać z wiedzy CCNA jako podstawy, ale tworzyć nowe scenariusze ENCOR, nie kopie pytań.
2. Następnie security: AAA, kontrola dostępu, ACL na poziomie ENCOR, TrustSec/MACsec i architektura ochrony.
3. Dalsze luki: NAT/PAT w kampanii ENCOR, pełniejsze IPsec/ERSPAN, API Catalyst Center i SD-WAN Manager, workflows Catalyst Center, projekt kampusu i SSO.
4. Pogłębianie wcześniejszych działów i rzeczywista walidacja labowa. Nie zwiększać licznika samą zmianą adresów.

## Ważne zasady projektu

- Dane źródłowe: content/catalog.yaml i content/encor/<dział>/stage-N.yaml (JSON zgodny z YAML).
- Jeden stopień: 6 zadań, 80% oznacza 5/6. Pierwszy stopień działu dostępny niezależnie; kolejne zależą od poprzedniego.
- Quiz: cztery różne opcje, jedna poprawna, feedback. Wielkość liter w opcjach ma znaczenie dla kodu.
- CLI: luki inline; trudność 1 = jedna, 2 = dwie, 3 = co najmniej trzy.
- Trwałe ID i rewizje; nie resetować packetpath:campaign:v3. Pobieranie paczek na żądanie, cache maksymalnie dwóch.
- Historyczne skrypty scripts/authoring uruchamiać wyłącznie jako jednorazową partię na odpowiedniej bazie; ostateczne redakcyjne poprawki są w YAML.
- 31/47 = 66% celów rozpoczętych to szerokość, nie pełne pokrycie ani gotowość egzaminacyjna. Mapa: ENCOR-COVERAGE-AUDIT.md.
- 648 zadań ENCOR to roboczy budżet, nie dowód wyczerpania blueprintu.
