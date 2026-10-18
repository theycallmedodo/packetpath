# PacketPath v3 — hierarchia i kontrakty treści

## Hierarchia

Katalog → kurs (egzamin + wersja blueprintu) → dział → stopień → paczka zadań.

Katalog zawiera wyłącznie metadane i ścieżki do paczek, bez pytań i odpowiedzi. Start aplikacji pobiera `/content/catalog.json`. Otwarcie dostępnego stopnia pobiera tylko jego `pack_url`. Moduły mogą mieć dowolną liczbę stopni; stopień jest małą paczką, docelowo około 6–12 zadań. Nie tworzymy jednej paczki z 2000 zadaniami.

Przykładowa organizacja:

```text
content/
  catalog.yaml
  ccna/ospf/stage-1.yaml
  ccna/ospf/stage-2.yaml
  ccna/ospf/stage-3.yaml
  # kolejne działy: vlan/, acl/, nat/...
  # kolejne kursy: encor/, enarsi/...
```

Budowanie aplikacji waliduje wszystkie pliki źródłowe w środowisku deweloperskim i generuje osobne pliki JSON w `public/content/`. Przeglądarka otrzymuje tylko katalog oraz paczki otwieranych stopni. Walidacja wszystkich źródeł podczas builda nie oznacza ładowania ich w aplikacji.

## Katalog

```yaml
schema_version: 3
revision: 1
courses:
  - id: ccna
    title: CCNA 200-301
    exam: 200-301
    blueprint_version: '1.1'
    modules:
      - id: ccna.ospf
        title: Fundamenty OSPF
        description: Od pierwszych komend do konfiguracji.
        stages:
          - id: ccna.ospf.stage-1
            title: Pierwsze komendy
            description: Pojedyncze luki i pytania teoretyczne.
            difficulty: 1
            order: 1
            pack_url: /content/ccna/ospf/stage-1.json
            pack_revision: 1
            task_count: 6
            pass_percent: 80
            requires: []
          - id: ccna.ospf.stage-2
            title: Łączenie elementów
            description: Dwie luki i krótkie bloki CLI.
            difficulty: 2
            order: 2
            pack_url: /content/ccna/ospf/stage-2.json
            pack_revision: 1
            task_count: 6
            pass_percent: 80
            requires: [ccna.ospf.stage-1]
```

`requires` oznacza spełnienie wszystkich wskazanych zależności. Walidator odrzuca brakujące referencje, zależność od siebie i cykle. Pierwszy stopień nie ma zależności. Schemat dopuszcza wiele kursów i działów, ale aktualnie dostarczamy 24 działy CCNA (576 zadań).

## Wspólne pola zadania

Każde zadanie ma stabilne `id`, `revision`, `title`, `skills`, `sources`, `blueprint_refs`, `difficulty`, `prompt_md`, `hints`, `explanation_md` oraz `card_id`. `card_id` odsyła do fiszki zawartej w tej samej paczce — bez dodatkowego żądania sieciowego. Fiszki mogą być powtarzane pomiędzy małymi paczkami; ID zadań są globalnie unikatowe.

`type` rozróżnia dwa kontrakty:

| Typ | Pola specyficzne | Zasada oceny |
|---|---|---|
| `single_choice` | `options`, `correct_option_id` | Dokładnie 4 opcje A–D i jedna poprawna |
| `cli_fill_blank` | `platform`, `template`, `blanks` | Wszystkie nazwane luki muszą być poprawne |

Przykład części specyficznej quizu (uzupełnia pola wspólne):

```yaml
type: single_choice
options:
  - id: A
    text_md: 255.255.255.0
    feedback_md: To maska podsieci, a nie wildcard dla /24.
  - id: B
    text_md: 0.0.0.0
    feedback_md: Ta wartość dopasowuje pojedynczy adres.
  - id: C
    text_md: 0.0.0.3
    feedback_md: To wildcard dla dopasowania /30.
  - id: D
    text_md: 0.0.0.255
    feedback_md: Pierwsze 24 bity są porównywane, ostatnie 8 ignorowane.
correct_option_id: D
```

Pytanie do przykładu: „Który wildcard dopasowuje całą podsieć 192.168.10.0/24?”. Kliknięcie jest zatwierdzeniem. Błędna wybrana opcja staje się czerwona, właściwa zielona; ikony i tekst przekazują wynik także bez rozpoznawania kolorów. Dalsze zmiany odpowiedzi są blokowane. Wyjaśnienie i fiszka pokazują się po odpowiedzi. Nie liczymy kliknięcia w każdą opcję jako kolejnych prób.

Przykład części specyficznej CLI:

```yaml
type: cli_fill_blank
platform: IOS / IOS XE
template: |
  R1(config)# router ospf {{process}}
  R1(config-router)# network 10.0.12.0 {{wildcard}} area 0
blanks:
  - id: process
    label: ID procesu
    answer_type: integer
    accepted: ['10']
    width: 5
    common_errors: {}
  - id: wildcard
    label: Wildcard dla /30
    answer_type: ipv4
    accepted: ['0.0.0.3']
    width: 12
    common_errors:
      '255.255.255.252': To maska podsieci, a nie wildcard.
```

Do całej komendy służy `answer_type: command`. Każde pole może reprezentować parametr, frazę lub jedną pełną linię. Wieloliniowy scenariusz ma kilka nazwanych pól. Normalizujemy białe znaki; wielkość liter ignorujemy dla `keyword` i `command`. Akceptowane warianty są jawne — nie jest to emulator parsera IOS. Zatwierdzenie CLI wymaga uzupełnienia wszystkich pól.

## Odblokowanie i postęp

Wynik próby = liczba w pełni poprawnych zadań / liczba wszystkich zadań. Quiz oraz wielopolowe CLI mają po jednym punkcie; częściowo poprawne CLI daje informację diagnostyczną, ale nie pełny punkt. Podpowiedzi są zapisywane, nie obniżają wyniku w tym trybie nauki.

80% z sześciu zadań oznacza minimum pięć poprawnych. Obliczenie używa dokładnego stosunku, nie zaokrąglonego procentu z UI. Dopiero ukończenie całego stopnia i przejście do wyniku zapisuje zaliczenie. Nieukończona próba nie odblokowuje następnego stopnia.

Zapis (`packetpath:campaign:v3`):

- `sessions[stageId]`: bieżąca próba, wersja paczki, indeks zadania, odpowiedzi, podpowiedzi i próby per zadanie.
- `results[stageId]`: najlepszy procent, ostatni procent, flaga zaliczenia i liczba ukończonych prób.

Wznowienie zachowuje odpowiedzi i stan oceny. Nowa próba zastępuje bieżącą sesję, ale zachowuje najlepszy wynik i wcześniejsze odblokowania. Stare klucze v1/v2 pozostają nietknięte; przejście z v1/v2 do v3 zaczyna od stopnia 1, ponieważ kampania ma nowe pytania i reguły zaliczenia. Aktualizacja aplikacji 0.3 → 0.6 pozostawia ten sam format v3 i zachowuje postęp OSPF. Zmiana `pack_revision` resetuje bieżącą sesję paczki, zachowując zdobyte zaliczenie. Przy zasadniczej zmianie celu dydaktycznego należy nadać nowe `stage.id`, aby wymagać nowego zaliczenia.

Mechanika lokalna nie stanowi zabezpieczenia antycheat. Klucze odpowiedzi są w pobranej paczce, a postęp w localStorage. To świadomy wybór dla narzędzia do samodzielnej nauki. Synchronizacja i weryfikacja serwerowa są przyszłym etapem.

## Rozszerzenie do 2000+

1. Dodaj mały plik YAML stopnia, ze źródłami i odniesieniami do zatwierdzonego blueprintu.
2. Dodaj rekord w katalogu i jawne wymagania odblokowania.
3. Uruchom testy i build; walidacja sprawdza zależności, liczbę zadań, ID, wersje paczek, placeholdery, cztery opcje i fiszki.
4. Przejrzyj merytorykę. Walidator struktury nie zastępuje przeglądu technicznego.

Pamięć podręczna LRU mieści najwyżej dwie paczki; ponowne otwarcie starszej pobiera ją ponownie. Przerwane i nieudane żądania mają obsługę błędów i ponowienie. Struktura umożliwia rozbudowę; 2000 zadań jeszcze nie zostało napisanych ani przetestowanych obciążeniowo.

## Typy odpowiedzi dodane w 0.6

`ipv6` porównuje adresy niezależnie od wielkości liter i kompresji zer. `ipv6_prefix` dodatkowo wymaga identycznej długości prefiksu, zachowując bity hosta (adres interfejsu). Identyfikatory stref nie są obsługiwane. `identifier` zachowuje wielkość liter nazw obiektów. Typ `command` nadal porównuje jawne warianty; nie emuluje parsera IOS.

## Rozszerzenia w 0.7

Stopień oznacza pozycję w ścieżce (`order`), a `difficulty` osobną ocenę złożoności 1–3. Dział może mieć więcej niż trzy stopnie. IPv4, VLAN, ACL i OSPF mają teraz stopnie 4–6, z zależnością od istniejącego stopnia 3. Nowe ID zadań używają segmentu `.ext.`, żeby nie kolidować ze starymi. Wcześniejszych paczek i klucza zapisu nie zmieniono.

Nie narzucamy stałych proporcji typów zadań w stopniu. Moduł teoretyczny może mieć sześć quizów, a moduł składni mieszać quizy i CLI. Każdy quiz nadal ma dokładnie cztery opcje oraz jedną poprawną odpowiedź. Katalog i aplikacja obsługują te proporcje bez specjalnej logiki.

## Rozszerzenia 0.8

Dodano 24 paczki po 6 zadań: cztery nowe działy i stopnie 4–6 IPv6, STP, EtherChannel oraz NAT. Wcześniejsze 72 paczki pozostały bez zmian. Format zapisu i klucz localStorage nie zostały zmienione.

## Kursy w wersji 0.9

Katalog zawiera `ccna` (200-301, v1.1) i `encor` (350-401, v1.2). Każdy moduł, stopień i zadanie ma globalnie unikalny identyfikator z prefiksem kursu. `requires` łączy stopnie wewnątrz danego działu. Wybór kursu filtruje mapę i statystyki; nie zmienia formatu zapisu ani wyników innego kursu. ENCOR ma 30 niezależnie pobieranych paczek.

Wersja 0.10 rozszerza ENCOR do 42 paczek bez zmiany kontraktu danych i klucza localStorage. Motyw Matrix nie modyfikuje sesji ani wyników.

Wersja 0.11 rozszerza ENCOR do 51 paczek, bez zmiany schematu ani formatu zapisu. Nowe moduły multicast, sdwan i sdaccess zawierają quizy single_choice.

Wersja 0.12: ENCOR ma 63 paczki. Unikalność opcji quizu jest case-sensitive po trim(), ponieważ kod rozróżnia true/True i up/UP. Nadal wymagane są cztery różne opcje A–D. Format zapisu postępu nie zmienił się.

Wersja 0.13: ENCOR ma 72 paczki. Dodano fhrp, time-sync i pbr. Bez zmiany kontraktu oraz klucza zapisu postępu.

## Rozszerzenie 0.15

Nowe sekcje `.practice-N` kontynuują istniejące ścieżki. Nie zmieniono starych
ID, rewizji ani klucza zapisu. Cztery decyzje dotyczące przypadku umieszczono
w osobnych paczkach. Poziom trudności CLI określa samodzielne wpisanie pełnej
komendy, nie wymóg co najmniej trzech luk.

Działy mają 82–180 zadań. BGP: 180, VLAN: 144. Pozostałe działy mają
82 lub 100 zadań. Ćwiczenia porównawcze przedstawiają dwa odrębne przypadki
i wymagają poprawnego przypisania rozpoznania, działania, dowodu lub zasady
do obu zgłoszeń. Pełny zakres: CONTENT-EXPANSION.json.
