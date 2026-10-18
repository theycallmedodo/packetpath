# PacketPath 0.15 — rozbudowane scenariusze

Baza ma **4222 zadania**: 2156 CCNA i 2066 ENCOR, w 48 działach i 561 sekcjach.
Dodano 3214 ćwiczeń: 336 odrębnych przypadków analizowanych z czterech stron
(rozpoznanie, działanie, weryfikacja, zależności) oraz 30 ćwiczeń pełnych komend CLI. Kolejne 1840 zadań porównuje dwa zgłoszenia
i wymaga poprawnego rozpoznania, działania, weryfikacji lub wyjaśnienia obu.
BGP ma 180 zadań, VLAN 144; każdy pozostały dział otrzymał 64 nowe zadania
i ma obecnie 82 lub 100. Pełne zestawienie: `CONTENT-EXPANSION.json`.

Wszystkie 168 poprzednich paczek pozostaje identycznych bajtowo. Nowe sekcje
odblokowują się po ostatniej starej sekcji, a dotychczasowe zaliczenia i sesje
zachowują identyfikatory i wersje. Treść jest pakowana do aplikacji i działa offline.
Linki źródłowe wymagają internetu tylko przy otwieraniu dokumentacji zewnętrznej.

Weryfikacja: `npm test`, `npm run build`, `npm run android:sync`.
Instrukcja budowy APK: `ANDROID-Z-TELEFONU.md`.

## Historia poprzednich wydań

# PacketPath 0.14 — Android + Web

Nowe wydanie dodaje projekt Android, trwały zapis natywny, eksport/import postępów, obsługę Wstecz i workflow APK. Instrukcja z telefonu: **ANDROID-Z-TELEFONU.md**. 1008 zadań bez zmian.

Stan: 27 testów i build web przeszły; APK wymaga kompilacji w GitHub Actions i testu na telefonie. Poniżej dokumentacja poprzedniego wydania treści.

# PacketPath 0.13 — 1008 zadań

## Uruchomienie na Windows

Zainstaluj Node.js LTS. Zatrzymaj poprzedni serwer, rozpakuj CAŁY ZIP do nowego folderu i uruchom `START-WINDOWS.bat`. Aplikacja otworzy się pod http://localhost:5173. Pozostaw konsolę otwartą. Gotowy build jest w paczce; nie trzeba instalować zależności npm. Serwer nasłuchuje wyłącznie na 127.0.0.1.

## Nowości w 0.13

Ostatnia partia tej sesji: 54 nowe zadania ENCOR — HSRP/VRRP, NTP/PTP i PBR. Łącznie 48 quizów i 6 ćwiczeń inline CLI. Każdy nowy dział ma trzy stopnie po 6 zadań. HSRP/VRRP zawiera praktykę konfiguracji; NTP/PTP i PBR skupiają się na interpretacji i scenariuszach zgodnie z poziomem celów blueprintu.

Łącznie 1008 zadań: 576 CCNA i 432 ENCOR. 665 quizów, 343 CLI, 48 działów i 168 stopni. ENCOR ma 24 działy i 72 stopnie. Motyw Matrix i mechanika pozostają bez zmian.

`ENCOR-COVERAGE-AUDIT.md` zawiera mapę 47 końcowych podpunktów: rozpoczęto 31 (66,0%). To nieważony wskaźnik szerokości, nie procent wyczerpania zakresu ani gotowości do egzaminu. `NEXT-SESSION.md` zapisuje stan projektu i proponowane priorytety dalszej pracy.

## Postęp i aktualizacja

Wszystkie 159 wcześniejszych paczek CCNA/ENCOR oraz metadane istniejących modułów zachowano bez zmian. Klucz localStorage `packetpath:campaign:v3` pozostaje ten sam. Zachowaj tę samą przeglądarkę, profil i adres localhost:5173; nie czyść danych witryny. Postęp nie przenosi się automatycznie między przeglądarkami lub urządzeniami. Stare zapisy v1/v2 nie są migrowane.

CCNA i ENCOR mają osobne identyfikatory stopni, statystyki oraz zależności. Pierwszy stopień każdego działu jest dostępny od razu. Kolejny wymaga zaliczenia poprzedniego: 80%, czyli 5/6 zadań. Słabsza powtórka nie odbiera wcześniejszego zaliczenia. Przełączenie kursu nie usuwa zapisanej próby.

## Dane i zakres

Źródłem są `content/catalog.yaml` i `content/<kurs>/<dział>/stage-N.yaml`. Pliki używają zgodnej z YAML składni JSON. Build generuje osobne JSON-y; frontend pobiera tylko katalog i wybrany stopień, z cache dwóch paczek. Klucze odpowiedzi są jawne w tym lokalnym narzędziu do nauki.

`CONTENT-COVERAGE.md` zawiera pełny indeks i granice zakresu, `DATA-MODEL.md` kontrakt, `CONTENT-ROADMAP.md` dalszy plan. 2000+ zadań pozostaje celem. Pierwsza partia ENCOR nie stanowi pełnego pokrycia blueprintu. ENARSI nie ma jeszcze zadań. Materiały są autorskimi ćwiczeniami, nie pytaniami egzaminacyjnymi Cisco.

## Dla programisty

```sh
npm ci
npm run dev
npm test
python scripts/verify-release09.py
npm run build
```

React, TypeScript, Vite, Zod i Markdown. Edytuj źródłowe YAML. `scripts/authoring/` zawiera historyczny materiał jednorazowych partii; nie uruchamiaj go ponownie na istniejącej bazie. Ostateczne poprawki redakcyjne i przykładowe outputy są w YAML.

## Weryfikacja i ograniczenia

24 testy sprawdzają ocenianie wszystkich kluczy i wariantów, odblokowania, zapis, ładowanie na żądanie, izolację kursów i niezmienność CCNA. Dla nowej partii wykonano 5 niezależnych kontroli arytmetyki/kluczy (priorytety, reach NTP, dopasowanie podsieci PBR). W partii 0.12 wykonano 30 kontroli: uruchomienie 18 przykładów Pythona i parsowanie 12 poprawnych dokumentów JSON. Wcześniejszy skrypt verify-release09.py sprawdza 16 obliczeń i kluczy z partii 0.9. TypeScript i build przeszły poprawnie. W tej partii sprawdzono niezmienność wszystkich 159 wcześniejszych paczek. Motyw zachowuje osiem podstawowych par tekst/tło sprawdzonych w wersji 0.10 (co najmniej 4,5:1).

Nie przeprowadzono testów na IOS/emulatorze, Windows ani wizualnych w przeglądarce. Zgodność z kluczem nie zastępuje przeglądu merytorycznego ani labu. Skrócone wyniki show są przykładami dydaktycznymi. Składnia i funkcje zależą od platformy; ćwiczenia podają wymagane założenia. Fiszki i podpowiedzi służą nauce, nie symulacji egzaminu.

Brak kont, synchronizacji, XP, serc, SRS i pełnej PWA. Publikacja online pozostaje niedostępna; ta wersja jest dostarczana jako aplikacja lokalna.
