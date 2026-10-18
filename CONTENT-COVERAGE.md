# Baza treści 0.13 — 1008 zadań

576 CCNA + 432 ENCOR. 48 działów, 168 stopni po 6 zadań. Łącznie 665 quizów i 343 zadań inline CLI.

ENCOR 350-401 jest przypięty do blueprintu v1.2. CCNA pozostaje przypięte do v1.1. To częściowe pokrycie obu ścieżek; licznik zadań nie jest procentem pokrycia egzaminu. ENARSI nie zawiera jeszcze treści.

## Weryfikacja

24 testy aplikacji i treści oraz 16 niezależnych kontroli obliczeń ENCOR przeszło poprawnie. Zachowano 159 wcześniejszych paczek CCNA/ENCOR i metadane istniejących modułów. Test zgodności z kluczem nie dowodzi poprawności konfiguracji na IOS. Nie wykonano testu routerowego, wizualnego ani na Windows. Przykładowe wyniki show są dydaktycznymi, skróconymi przykładami, nie zapisami z urządzeń.

## Zakres pierwszej partii ENCOR

eBGP bezpośredni i wybór tras; OSPFv2/v3 w normalnych obszarach; VRF-lite; GRE z koncepcją ochrony IPsec; porównanie EIGRP/OSPF; interpretacja QoS; VM/vSwitch, LISP i VXLAN; ICMP Echo IP SLA; local SPAN/RSPAN i koncepcja ERSPAN; applet EEM.

Nie deklarujemy pełnego pokrycia podcelów. Brakuje m.in. kompletnej konfiguracji IPsec i ERSPAN, pogłębienia architektur SD-WAN/SDA i multicast, rozbudowanej security, pogłębionych scenariuszy NETCONF/RESTCONF, pogłębienia Python/JSON/YANG i pozostałych celów. Pojęcie RD/RT w module VRF jest kontekstem uzupełniającym.

## Zestawienie

| Kurs / dział | Stopnie | Quizy | CLI | Razem |
|---|---:|---:|---:|---:|
| CCNA / IPv4 i subnetting | 6 | 18 | 18 | 36 |
| CCNA / VLAN i trunk 802.1Q | 6 | 18 | 18 | 36 |
| CCNA / STP i ochrona portów | 6 | 18 | 18 | 36 |
| CCNA / Fundamenty OSPF | 6 | 18 | 18 | 36 |
| CCNA / ACL IPv4 | 6 | 18 | 18 | 36 |
| CCNA / NAT i PAT | 6 | 18 | 18 | 36 |
| CCNA / IPv6: adresacja i sąsiedzi | 6 | 18 | 18 | 36 |
| CCNA / Routing statyczny | 3 | 6 | 12 | 18 |
| CCNA / EtherChannel i LACP | 6 | 18 | 18 | 36 |
| CCNA / DHCP: klient, relay i pula | 3 | 6 | 12 | 18 |
| CCNA / SSH i dostęp administracyjny | 3 | 6 | 12 | 18 |
| CCNA / NTP, syslog i SNMP | 3 | 6 | 12 | 18 |
| CCNA / CDP i LLDP | 3 | 6 | 12 | 18 |
| CCNA / Port Security | 3 | 6 | 12 | 18 |
| CCNA / DHCP Snooping | 3 | 6 | 12 | 18 |
| CCNA / Dynamic ARP Inspection | 3 | 6 | 12 | 18 |
| CCNA / Redundancja bramy — HSRP | 3 | 6 | 12 | 18 |
| CCNA / WLAN — radio, architektura i bezpieczeństwo | 3 | 18 | 0 | 18 |
| CCNA / QoS — klasyfikacja i kolejki | 3 | 18 | 0 | 18 |
| CCNA / Automatyzacja — JSON i API | 3 | 18 | 0 | 18 |
| CCNA / Ethernet, MAC i ARP | 3 | 12 | 6 | 18 |
| CCNA / TCP i UDP — sesje i diagnostyka | 3 | 18 | 0 | 18 |
| CCNA / DNS — nazwy i rozwiązywanie problemów | 3 | 12 | 6 | 18 |
| CCNA / AAA — tożsamość, uprawnienia i audyt | 3 | 11 | 7 | 18 |
| ENCOR / eBGP — sąsiedztwo i wybór trasy | 3 | 12 | 6 | 18 |
| ENCOR / OSPF — obszary, agregacja i OSPFv3 | 3 | 12 | 6 | 18 |
| ENCOR / VRF — oddzielne tablice routingu | 3 | 12 | 6 | 18 |
| ENCOR / GRE — tunele i zależność od underlay | 3 | 12 | 6 | 18 |
| ENCOR / EIGRP a OSPF — metryki i zbieżność | 3 | 18 | 0 | 18 |
| ENCOR / QoS — czytanie konfiguracji i liczników | 3 | 18 | 0 | 18 |
| ENCOR / Wirtualizacja — VM, LISP i VXLAN | 3 | 18 | 0 | 18 |
| ENCOR / IP SLA — pomiary i diagnoza dostępności | 3 | 12 | 6 | 18 |
| ENCOR / SPAN, RSPAN i ERSPAN — obserwacja ruchu | 3 | 12 | 6 | 18 |
| ENCOR / EEM — automatyzacja zdarzeń i zbieranie danych | 3 | 12 | 6 | 18 |

| ENCOR / Flexible NetFlow — rekord, monitor i eksport | 3 | 12 | 6 | 18 |
| ENCOR / NETCONF — sesje, możliwości i operacje | 3 | 12 | 6 | 18 |
| ENCOR / RESTCONF — HTTP, modele i diagnostyka API | 3 | 12 | 6 | 18 |
| ENCOR / CoPP — ochrona CPU i diagnostyka SNMP | 3 | 12 | 6 | 18 |

| ENCOR / Multicast — RPF, PIM, IGMP i SSM | 3 | 18 | 0 | 18 |
| ENCOR / SD-WAN — płaszczyzny, OMP i jakość łączy | 3 | 18 | 0 | 18 |
| ENCOR / SD-Access — fabric, segmentacja i dostęp zewnętrzny | 3 | 18 | 0 | 18 |

| ENCOR / Python — odczyt skryptów sieciowych | 3 | 18 | 0 | 18 |
| ENCOR / JSON — poprawny zapis i struktury danych | 3 | 18 | 0 | 18 |
| ENCOR / YANG — model danych i walidacja | 3 | 18 | 0 | 18 |
| ENCOR / Automatyzacja — agent, agentless i kontrola zmian | 3 | 18 | 0 | 18 |

| ENCOR / HSRP i VRRP — wybór bramy i awarie | 3 | 12 | 6 | 18 |
| ENCOR / NTP i PTP — interpretacja synchronizacji | 3 | 18 | 0 | 18 |
| ENCOR / PBR — interpretacja polityk routingu | 3 | 18 | 0 | 18 |

## Indeks zadań

### CCNA 200-301

#### IPv4 i subnetting

**ccna.ipv4.stage-1**

- `ccna.ipv4.01` — Ile hostów mieści /26? (quiz, trudność 1; cel 1.6)
- `ccna.ipv4.02` — Maska interfejsu /24 (CLI, trudność 1; cel 1.6)
- `ccna.ipv4.03` — Podnieś interfejs (CLI, trudność 1; cel 1.6)
- `ccna.ipv4.04` — Adres sieci /27 (quiz, trudność 1; cel 1.6)
- `ccna.ipv4.05` — Adres drugiego końca /30 (CLI, trudność 1; cel 1.6)
- `ccna.ipv4.06` — Szybki przegląd interfejsów (CLI, trudność 1; cel 1.6)

**ccna.ipv4.stage-2**

- `ccna.ipv4.07` — Broadcast w /28 (quiz, trudność 2; cel 1.6)
- `ccna.ipv4.08` — Pierwszy host i maska (CLI, trudność 2; cel 1.6)
- `ccna.ipv4.09` — Ostatni host i maska (CLI, trudność 2; cel 1.6)
- `ccna.ipv4.10` — Dwa hosty w jednej podsieci (quiz, trudność 2; cel 1.6)
- `ccna.ipv4.11` — Loopback do identyfikacji (CLI, trudność 2; cel 1.6)
- `ccna.ipv4.12` — Opis i stan (CLI, trudność 2; cel 1.6)

**ccna.ipv4.stage-3**

- `ccna.ipv4.13` — Dobór podsieci VLSM (quiz, trudność 3; cel 1.6)
- `ccna.ipv4.14` — LAN dla 50 hostów (CLI, trudność 3; cel 1.6)
- `ccna.ipv4.15` — Dwa końce łącza (CLI, trudność 3; cel 1.6)
- `ccna.ipv4.16` — Diagnoza złej maski (quiz, trudność 3; cel 1.6)
- `ccna.ipv4.17` — Dwie podsieci VLSM (CLI, trudność 3; cel 1.6)
- `ccna.ipv4.18` — Popraw adres bramy (CLI, trudność 3; cel 1.6)

**ccna.ipv4.stage-4**

- `ccna.ipv4.ext.01` — Podział /24 na /28 (quiz, trudność 2; cel 1.6)
- `ccna.ipv4.ext.02` — Granica /23 (quiz, trudność 2; cel 1.6)
- `ccna.ipv4.ext.03` — Interfejs w dużym LAN (CLI, trudność 2; cel 1.6)
- `ccna.ipv4.ext.04` — Nieprawidłowa brama (quiz, trudność 2; cel 1.6)
- `ccna.ipv4.ext.05` — Łącze /31 (CLI, trudność 2; cel 1.6)
- `ccna.ipv4.ext.06` — VLSM i kolejność (quiz, trudność 2; cel 1.6)

**ccna.ipv4.stage-5**

- `ccna.ipv4.ext.07` — Minimalny LAN dla 200 (quiz, trudność 3; cel 1.6)
- `ccna.ipv4.ext.08` — Nakładanie VLSM (quiz, trudność 3; cel 1.6)
- `ccna.ipv4.ext.09` — VLSM: 100 i 50 hostów (CLI, trudność 3; cel 1.6)
- `ccna.ipv4.ext.10` — Adres na granicy (quiz, trudność 3; cel 1.6)
- `ccna.ipv4.ext.11` — Usuń nakładający adres (CLI, trudność 3; cel 1.6)
- `ccna.ipv4.ext.12` — Podsumowanie czterech /24 (quiz, trudność 3; cel 1.6)

**ccna.ipv4.stage-6**

- `ccna.ipv4.ext.13` — Sumaryzacja z luką (quiz, trudność 3; cel 1.6)
- `ccna.ipv4.ext.14` — Wspólna podsieć? (quiz, trudność 3; cel 1.6)
- `ccna.ipv4.ext.15` — Trzy minimalne LAN-y (CLI, trudność 3; cel 1.6)
- `ccna.ipv4.ext.16` — Pomyłka /30 (quiz, trudność 3; cel 1.6)
- `ccna.ipv4.ext.17` — Adres końca i loopback (CLI, trudność 3; cel 1.6)
- `ccna.ipv4.ext.18` — Rezerwa adresów (quiz, trudność 3; cel 1.6)

#### VLAN i trunk 802.1Q

**ccna.vlan.stage-1**

- `ccna.vlan.01` — Co rozdziela VLAN? (quiz, trudność 1; cel 2.1)
- `ccna.vlan.02` — Utwórz VLAN (CLI, trudność 1; cel 2.1)
- `ccna.vlan.03` — Port dla komputera (CLI, trudność 1; cel 2.1)
- `ccna.vlan.04` — Wiele VLAN-ów jednym łączem (quiz, trudność 1; cel 2.2)
- `ccna.vlan.05` — Przypisz VLAN access (CLI, trudność 1; cel 2.1)
- `ccna.vlan.06` — Lista VLAN-ów (CLI, trudność 1; cel 2.1)

**ccna.vlan.stage-2**

- `ccna.vlan.07` — Dodawanie bez nadpisania (quiz, trudność 2; cel 2.2)
- `ccna.vlan.08` — Nazwij VLAN (CLI, trudność 2; cel 2.1)
- `ccna.vlan.09` — Access w dwóch krokach (CLI, trudność 2; cel 2.1)
- `ccna.vlan.10` — Native VLAN mismatch (quiz, trudność 2; cel 2.2)
- `ccna.vlan.11` — Trunk i native (CLI, trudność 2; cel 2.2)
- `ccna.vlan.12` — Rozszerz listę allowed (CLI, trudność 2; cel 2.2)

**ccna.vlan.stage-3**

- `ccna.vlan.13` — Dlaczego VLAN nie przechodzi? (quiz, trudność 3; cel 2.2)
- `ccna.vlan.14` — Przygotuj port użytkownika (CLI, trudność 3; cel 2.1)
- `ccna.vlan.15` — Pełny uplink (CLI, trudność 3; cel 2.2)
- `ccna.vlan.16` — Ruch między VLAN-ami (quiz, trudność 3; cel 2.1.c)
- `ccna.vlan.17` — Router-on-a-stick (CLI, trudność 3; cel 2.1.c)
- `ccna.vlan.18` — Usuń jeden VLAN, zachowaj resztę (CLI, trudność 3; cel 2.2)

**ccna.vlan.stage-4**

- `ccna.vlan.ext.01` — Telefon i komputer (quiz, trudność 2; cel 2.1)
- `ccna.vlan.ext.02` — Dynamic auto po obu stronach (quiz, trudność 2; cel 2.2)
- `ccna.vlan.ext.03` — Telefon: dwa VLAN-y (CLI, trudność 2; cel 2.1)
- `ccna.vlan.ext.04` — Wyłączenie DTP (quiz, trudność 2; cel 2.2)
- `ccna.vlan.ext.05` — Statyczny trunk bez negocjacji (CLI, trudność 2; cel 2.2)
- `ccna.vlan.ext.06` — SVI a port fizyczny (quiz, trudność 2; cel 2.1)

**ccna.vlan.stage-5**

- `ccna.vlan.ext.07` — SVI down przy no shutdown (quiz, trudność 3; cel 2.1)
- `ccna.vlan.ext.08` — Allowed nie tworzy VLAN-u (quiz, trudność 3; cel 2.2)
- `ccna.vlan.ext.09` — SVI dla użytkowników (CLI, trudność 3; cel 2.1)
- `ccna.vlan.ext.10` — Zarządzanie L2 (quiz, trudność 3; cel 2.1)
- `ccna.vlan.ext.11` — Zarządzanie bez routingu (CLI, trudność 3; cel 2.1)
- `ccna.vlan.ext.12` — VLAN a podsieć (quiz, trudność 3; cel 2.1)

**ccna.vlan.stage-6**

- `ccna.vlan.ext.13` — Native mismatch w praktyce (quiz, trudność 3; cel 2.2)
- `ccna.vlan.ext.14` — Trunk a STP (quiz, trudność 3; cel 2.2)
- `ccna.vlan.ext.15` — Utwórz, dodaj, sprawdź (CLI, trudność 3; cel 2.2)
- `ccna.vlan.ext.16` — PC bez tagów (quiz, trudność 3; cel 2.1)
- `ccna.vlan.ext.17` — Pełny port telefonu (CLI, trudność 3; cel 2.1)
- `ccna.vlan.ext.18` — Brama jest osiągalna, zdalny VLAN nie (quiz, trudność 3; cel 2.1)

#### STP i ochrona portów

**ccna.stp.stage-1**

- `ccna.stp.01` — Rola STP (quiz, trudność 1; cel 2.5)
- `ccna.stp.02` — Wybierz Rapid PVST+ (CLI, trudność 1; cel 2.5)
- `ccna.stp.03` — Priorytet mostu (CLI, trudność 1; cel 2.5)
- `ccna.stp.04` — Kto zostanie root? (quiz, trudność 1; cel 2.5)
- `ccna.stp.05` — PortFast na porcie PC (CLI, trudność 1; cel 2.5)
- `ccna.stp.06` — BPDU Guard per port (CLI, trudność 1; cel 2.5)

**ccna.stp.stage-2**

- `ccna.stp.07` — STP czy MAC? (quiz, trudność 2; cel 2.5)
- `ccna.stp.08` — Root primary dla VLAN (CLI, trudność 2; cel 2.5)
- `ccna.stp.09` — Chroniony port hosta (CLI, trudność 2; cel 2.5)
- `ccna.stp.10` — Odebrano BPDU (quiz, trudność 2; cel 2.5)
- `ccna.stp.11` — Weryfikuj instancję (CLI, trudność 2; cel 2.5)
- `ccna.stp.12` — Koszt portu (CLI, trudność 2; cel 2.5)

**ccna.stp.stage-3**

- `ccna.stp.13` — Alternatywna ścieżka RSTP (quiz, trudność 3; cel 2.5)
- `ccna.stp.14` — Rozdziel root dla VLAN-ów (CLI, trudność 3; cel 2.5)
- `ccna.stp.15` — Pełny port końcowy (CLI, trudność 3; cel 2.5)
- `ccna.stp.16` — Root port przy różnych kosztach (quiz, trudność 3; cel 2.5)
- `ccna.stp.17` — Root Guard na łączu w dół (CLI, trudność 3; cel 2.5)
- `ccna.stp.18` — Przywróć port po usunięciu przyczyny (CLI, trudność 3; cel 2.5)

**ccna.stp.stage-4**

- `ccna.stp.ext.01` — Najlepszy bridge ID (quiz, trudność 2; cel 2.5)
- `ccna.stp.ext.02` — Remis priorytetu (quiz, trudność 2; cel 2.5)
- `ccna.stp.ext.03` — Dwa rooty VLAN (CLI, trudność 2; cel 2.5)
- `ccna.stp.ext.04` — Root port (quiz, trudność 2; cel 2.5)
- `ccna.stp.ext.05` — Root Guard i kontrola (CLI, trudność 2; cel 2.5)
- `ccna.stp.ext.06` — Root-inconsistent (quiz, trudność 2; cel 2.5)

**ccna.stp.stage-5**

- `ccna.stp.ext.07` — Powrót Root Guard (quiz, trudność 3; cel 2.5)
- `ccna.stp.ext.08` — Loop Guard (quiz, trudność 3; cel 2.5)
- `ccna.stp.ext.09` — Loop Guard i diagnostyka (CLI, trudność 3; cel 2.5)
- `ccna.stp.ext.10` — PortFast to nie brak STP (quiz, trudność 3; cel 2.5)
- `ccna.stp.ext.11` — Port hosta z ochroną (CLI, trudność 3; cel 2.5)
- `ccna.stp.ext.12` — BPDU Guard a Root Guard (quiz, trudność 3; cel 2.5)

**ccna.stp.stage-6**

- `ccna.stp.ext.13` — RSTP learning (quiz, trudność 3; cel 2.5)
- `ccna.stp.ext.14` — Zmiana kosztu (quiz, trudność 3; cel 2.5)
- `ccna.stp.ext.15` — Koszt i stan VLAN (CLI, trudność 3; cel 2.5)
- `ccna.stp.ext.16` — Utrata BPDU jednostronnie (quiz, trudność 3; cel 2.5)
- `ccna.stp.ext.17` — Usunięta przyczyna BPDU Guard (CLI, trudność 3; cel 2.5)
- `ccna.stp.ext.18` — BPDU Filter ryzyko (quiz, trudność 3; cel 2.5)

#### Fundamenty OSPF

**ccna.ospf.stage-1**

- `ccna.ospf.quiz.01` — ID procesu na sąsiadach (quiz, trudność 1; cel 3.4)
- `ccna.ospf.01` — Uruchom proces (CLI, trudność 1; cel 3.4)
- `ccna.ospf.02` — Lokalny numer procesu (CLI, trudność 1; cel 3.4)
- `ccna.ospf.quiz.02` — Wildcard w praktyce (quiz, trudność 1; cel 3.4)
- `ccna.ospf.03` — Wildcard dla /24 (CLI, trudność 1; cel 3.4)
- `ccna.ospf.04` — Wildcard dla /30 (CLI, trudność 1; cel 3.4)

**ccna.ospf.stage-2**

- `ccna.ospf.quiz.03` — Co wybiera network? (quiz, trudność 2; cel 3.4)
- `ccna.ospf.05` — Dwa elementy polecenia (CLI, trudność 2; cel 3.4)
- `ccna.ospf.06` — Dopasowanie konkretnego adresu (CLI, trudność 2; cel 3.4)
- `ccna.ospf.quiz.04` — Wspólne łącze, wspólny obszar (quiz, trudność 2; cel 3.4)
- `ccna.ospf.07` — Proces i backbone (CLI, trudność 2; cel 3.4)
- `ccna.ospf.08` — Dołącz R2 do obszaru (CLI, trudność 2; cel 3.4)

**ccna.ospf.stage-3**

- `ccna.ospf.quiz.05` — Router ID a adres interfejsu (quiz, trudność 3; cel 3.4)
- `ccna.ospf.09` — Tożsamość i proces (CLI, trudność 3; cel 3.4)
- `ccna.ospf.10` — Konfiguracja R2 od podstaw (CLI, trudność 3; cel 3.4)
- `ccna.ospf.quiz.06` — Co pozostaje po passive-interface? (quiz, trudność 3; cel 3.4)
- `ccna.ospf.11` — LAN bez sąsiadów (CLI, trudność 3; cel 3.4)
- `ccna.ospf.12` — Finał: bezpieczny uplink (CLI, trudność 3; cel 3.4)

**ccna.ospf.stage-4**

- `ccna.ospf.ext.01` — Kiedy 2-WAY jest normalne? (quiz, trudność 2; cel 3.4)
- `ccna.ospf.ext.02` — Kandydat na DR (quiz, trudność 2; cel 3.4)
- `ccna.ospf.ext.03` — Hello i Dead razem (CLI, trudność 2; cel 3.4)
- `ccna.ospf.ext.04` — DR bez wywłaszczenia (quiz, trudność 2; cel 3.4)
- `ccna.ospf.ext.05` — Punkt-punkt i koszt (CLI, trudność 2; cel 3.4)
- `ccna.ospf.ext.06` — Pierwszy wybór DR (quiz, trudność 2; cel 3.4)

**ccna.ospf.stage-5**

- `ccna.ospf.ext.07` — EXSTART i MTU (quiz, trudność 3; cel 3.4)
- `ccna.ospf.ext.08` — Stan INIT (quiz, trudność 3; cel 3.4)
- `ccna.ospf.ext.09` — Referencja, koszt i kontrola (CLI, trudność 3; cel 3.4)
- `ccna.ospf.ext.10` — Koszt obliczany (quiz, trudność 3; cel 3.4)
- `ccna.ospf.ext.11` — Aktywuj OSPF na porcie (CLI, trudność 3; cel 3.4)
- `ccna.ospf.ext.12` — Różne obszary na łączu (quiz, trudność 3; cel 3.4)

**ccna.ospf.stage-6**

- `ccna.ospf.ext.13` — Remis w wyborze DR (quiz, trudność 3; cel 3.4)
- `ccna.ospf.ext.14` — FULL a trasa do LAN (quiz, trudność 3; cel 3.4)
- `ccna.ospf.ext.15` — Wyklucz z wyboru DR (CLI, trudność 3; cel 3.4)
- `ccna.ospf.ext.16` — Dwa równe koszty (quiz, trudność 3; cel 3.4)
- `ccna.ospf.ext.17` — Przywróć timery (CLI, trudność 3; cel 3.4)
- `ccna.ospf.ext.18` — Zmiana router ID (quiz, trudność 3; cel 3.4)

#### ACL IPv4

**ccna.acl.stage-1**

- `ccna.acl.01` — Standardowa czy rozszerzona? (quiz, trudność 1; cel 5.6)
- `ccna.acl.02` — Nazwana ACL standardowa (CLI, trudność 1; cel 5.6)
- `ccna.acl.03` — Zezwól jednemu hostowi (CLI, trudność 1; cel 5.6)
- `ccna.acl.04` — Niejawny koniec ACL (quiz, trudność 1; cel 5.6)
- `ccna.acl.05` — ACL dla całej podsieci (CLI, trudność 1; cel 5.6)
- `ccna.acl.06` — Zastosuj na wejściu (CLI, trudność 1; cel 5.6)

**ccna.acl.stage-2**

- `ccna.acl.07` — Pierwsze dopasowanie (quiz, trudność 2; cel 5.6)
- `ccna.acl.08` — Dopuść HTTPS (CLI, trudność 2; cel 5.6)
- `ccna.acl.09` — Zablokuj Telnet do serwera (CLI, trudność 2; cel 5.6)
- `ccna.acl.10` — Źródło kontra cel portu (quiz, trudność 2; cel 5.6)
- `ccna.acl.11` — Wstaw regułę pomiędzy (CLI, trudność 2; cel 5.6)
- `ccna.acl.12` — Usuń pojedynczy wpis (CLI, trudność 2; cel 5.6)

**ccna.acl.stage-3**

- `ccna.acl.13` — ACL w NAT nie jest firewallem (quiz, trudność 3; cel 5.6)
- `ccna.acl.14` — Polityka WWW z LAN (CLI, trudność 3; cel 5.6)
- `ccna.acl.15` — Blokada hosta z zachowaniem reszty (CLI, trudność 3; cel 5.6)
- `ccna.acl.16` — Kierunek na porcie LAN (quiz, trudność 3; cel 5.6)
- `ccna.acl.17` — Diagnostyka ICMP z jednej podsieci (CLI, trudność 3; cel 5.6)
- `ccna.acl.18` — Sprawdź i odepnij, nie kasuj (CLI, trudność 3; cel 5.6)

**ccna.acl.stage-4**

- `ccna.acl.ext.01` — Reguła zasłonięta (quiz, trudność 2; cel 5.6)
- `ccna.acl.ext.02` — TCP established (quiz, trudność 2; cel 5.6)
- `ccna.acl.ext.03` — Ponumeruj od nowa (CLI, trudność 2; cel 5.6)
- `ccna.acl.ext.04` — Źródłowy port odpowiedzi (quiz, trudność 2; cel 5.6)
- `ccna.acl.ext.05` — DNS do jednego resolvera (CLI, trudność 2; cel 5.6)
- `ccna.acl.ext.06` — Wildcard nie jest maską (quiz, trudność 2; cel 5.6)

**ccna.acl.stage-5**

- `ccna.acl.ext.07` — Dwa kierunki (quiz, trudność 3; cel 5.6)
- `ccna.acl.ext.08` — Wildcard 0.0.0.0 (quiz, trudność 3; cel 5.6)
- `ccna.acl.ext.09` — Dwa transporty DNS (CLI, trudność 3; cel 5.6)
- `ccna.acl.ext.10` — Licznik hitów (quiz, trudność 3; cel 5.6)
- `ccna.acl.ext.11` — Wyjątek przed blokadą (CLI, trudność 3; cel 5.6)
- `ccna.acl.ext.12` — Samo utworzenie ACL (quiz, trudność 3; cel 5.6)

**ccna.acl.stage-6**

- `ccna.acl.ext.13` — ICMP echo a echo-reply (quiz, trudność 3; cel 5.6)
- `ccna.acl.ext.14` — Brak transportu w fragmencie (quiz, trudność 3; cel 5.6)
- `ccna.acl.ext.15` — Kontrolowany ping (CLI, trudność 3; cel 5.6)
- `ccna.acl.ext.16` — Permit przed końcem (quiz, trudność 3; cel 5.6)
- `ccna.acl.ext.17` — Odepnij i zbadaj listę (CLI, trudność 3; cel 5.6)
- `ccna.acl.ext.18` — Szeroki wildcard (quiz, trudność 3; cel 5.6)

#### NAT i PAT

**ccna.nat.stage-1**

- `ccna.nat.01` — Inside local (quiz, trudność 1; cel 4.1)
- `ccna.nat.02` — Oznacz LAN (CLI, trudność 1; cel 4.1)
- `ccna.nat.03` — Oznacz WAN (CLI, trudność 1; cel 4.1)
- `ccna.nat.04` — Co umożliwia overload? (quiz, trudność 1; cel 4.1)
- `ccna.nat.05` — Tablica translacji (CLI, trudność 1; cel 4.1)
- `ccna.nat.06` — Rodzaj mapowania (CLI, trudność 1; cel 4.1)

**ccna.nat.stage-2**

- `ccna.nat.07` — Deny w selektorze NAT (quiz, trudność 2; cel 4.1)
- `ccna.nat.08` — Stałe mapowanie 1:1 (CLI, trudność 2; cel 4.1)
- `ccna.nat.09` — Wybierz sieć do NAT (CLI, trudność 2; cel 4.1)
- `ccna.nat.10` — Wyczerpana pula bez PAT (quiz, trudność 2; cel 4.1)
- `ccna.nat.11` — PAT na adresie interfejsu (CLI, trudność 2; cel 4.1)
- `ccna.nat.12` — Przypisz pulę (CLI, trudność 2; cel 4.1)

**ccna.nat.stage-3**

- `ccna.nat.13` — Brak wpisu po konfiguracji (quiz, trudność 3; cel 4.1)
- `ccna.nat.14` — Kompletny PAT LAN–WAN (CLI, trudność 3; cel 4.1)
- `ccna.nat.15` — Dynamiczny NAT z pulą (CLI, trudność 3; cel 4.1)
- `ccna.nat.16` — Kolejność adresów statycznego NAT (quiz, trudność 3; cel 4.1)
- `ccna.nat.17` — Publikacja i weryfikacja (CLI, trudność 3; cel 4.1)
- `ccna.nat.18` — Dwie sieci w jednej polityce PAT (CLI, trudność 3; cel 4.1)

**ccna.nat.stage-4**

- `ccna.nat.ext.01` — NAT nie jest routingiem (quiz, trudność 2; cel 4.1)
- `ccna.nat.ext.02` — NAT nie jest firewallem (quiz, trudność 2; cel 4.1)
- `ccna.nat.ext.03` — Statyczny port HTTPS (CLI, trudność 2; cel 4.1)
- `ccna.nat.ext.04` — Odpowiedź do adresu globalnego (quiz, trudność 2; cel 4.1)
- `ccna.nat.ext.05` — PAT na pulę (CLI, trudność 2; cel 4.1)
- `ccna.nat.ext.06` — Różne sesje jednego hosta (quiz, trudność 2; cel 4.1)

**ccna.nat.stage-5**

- `ccna.nat.ext.07` — Dynamic mapping in use (quiz, trudność 3; cel 4.1)
- `ccna.nat.ext.08` — Czyszczenie translacji (quiz, trudność 3; cel 4.1)
- `ccna.nat.ext.09` — Zmiana mapowania w labie (CLI, trudność 3; cel 4.1)
- `ccna.nat.ext.10` — Wpis jest, usługa nie działa (quiz, trudność 3; cel 4.1)
- `ccna.nat.ext.11` — LAN, WAN i stan (CLI, trudność 3; cel 4.1)
- `ccna.nat.ext.12` — Nadmiar selektora (quiz, trudność 3; cel 4.1)

**ccna.nat.stage-6**

- `ccna.nat.ext.13` — Pula bez overload (quiz, trudność 3; cel 4.1)
- `ccna.nat.ext.14` — Asymetria i drugi NAT (quiz, trudność 3; cel 4.1)
- `ccna.nat.ext.15` — Sprawdź cały kontekst (CLI, trudność 3; cel 4.1)
- `ccna.nat.ext.16` — Adres z konfiguracji a osiągalność (quiz, trudność 3; cel 4.1)
- `ccna.nat.ext.17` — Nowa polityka PAT (CLI, trudność 3; cel 4.1)
- `ccna.nat.ext.18` — Dane w treści aplikacji (quiz, trudność 3; cel 4.1)

#### IPv6: adresacja i sąsiedzi

**ccna.ipv6.stage-1**

- `ccna.ipv6.01` — Zapis IPv6 (quiz, trudność 1; cel 1.8)
- `ccna.ipv6.02` — Włącz routing IPv6 (CLI, trudność 1; cel 1.8)
- `ccna.ipv6.03` — Prefiks LAN (CLI, trudność 1; cel 1.8)
- `ccna.ipv6.04` — Zasięg link-local (quiz, trudność 1; cel 1.8)
- `ccna.ipv6.05` — Jawny link-local (CLI, trudność 1; cel 1.8)
- `ccna.ipv6.06` — Przegląd interfejsów IPv6 (CLI, trudność 1; cel 1.8)

**ccna.ipv6.stage-2**

- `ccna.ipv6.07` — Neighbor Discovery (quiz, trudność 2; cel 1.8)
- `ccna.ipv6.08` — Adres i aktywacja (CLI, trudność 2; cel 1.8)
- `ccna.ipv6.09` — Globalny i lokalny na jednym porcie (CLI, trudność 2; cel 1.8)
- `ccna.ipv6.10` — Multicast zamiast broadcastu (quiz, trudność 2; cel 1.8)
- `ccna.ipv6.11` — Tylko IPv6 link-local (CLI, trudność 2; cel 1.8)
- `ccna.ipv6.12` — Adres loopback IPv6 (CLI, trudność 2; cel 1.8)

**ccna.ipv6.stage-3**

- `ccna.ipv6.13` — Podział /48 na /64 (quiz, trudność 3; cel 1.8)
- `ccna.ipv6.14` — Router między dwoma LAN-ami IPv6 (CLI, trudność 3; cel 1.8)
- `ccna.ipv6.15` — Podwójny stos na interfejsie (CLI, trudność 3; cel 1.8)
- `ccna.ipv6.16` — Brama przy SLAAC (quiz, trudność 3; cel 1.8)
- `ccna.ipv6.17` — Powtarzalny link-local i globalny adres (CLI, trudność 3; cel 1.8)
- `ccna.ipv6.18` — Napraw tylko błędny adres (CLI, trudność 3; cel 1.8)

**ccna.ipv6.stage-4**

- `ccna.ipv6.ext.01` — ND zamiast ARP (quiz, trudność 2; cel 1.8)
- `ccna.ipv6.ext.02` — Duplicate Address Detection (quiz, trudność 2; cel 1.8)
- `ccna.ipv6.ext.03` — Link-local next-hop (CLI, trudność 2; cel 3.3)
- `ccna.ipv6.ext.04` — SLAAC a DHCPv6 (quiz, trudność 2; cel 1.8)
- `ccna.ipv6.ext.05` — Domyślna trasa link-local (CLI, trudność 2; cel 3.3)
- `ccna.ipv6.ext.06` — Adres ULA (quiz, trudność 2; cel 1.9)

**ccna.ipv6.stage-5**

- `ccna.ipv6.ext.07` — Adres nieokreślony (quiz, trudność 3; cel 1.9)
- `ccna.ipv6.ext.08` — Loopback IPv6 (quiz, trudność 3; cel 1.9)
- `ccna.ipv6.ext.09` — Napraw zły next-hop (CLI, trudność 3; cel 3.3)
- `ccna.ipv6.ext.10` — Wiele adresów na interfejsie (quiz, trudność 3; cel 1.9)
- `ccna.ipv6.ext.11` — Dwa adresy i stan (CLI, trudność 3; cel 1.8)
- `ccna.ipv6.ext.12` — Adres multicast (quiz, trudność 3; cel 1.9)

**ccna.ipv6.stage-6**

- `ccna.ipv6.ext.13` — Blokowanie ICMPv6 (quiz, trudność 3; cel 1.8)
- `ccna.ipv6.ext.14` — RA z prefiksem bez SLAAC (quiz, trudność 3; cel 1.8)
- `ccna.ipv6.ext.15` — Trzy widoki IPv6 (CLI, trudność 3; cel 1.8)
- `ccna.ipv6.ext.16` — Podział /56 (quiz, trudność 3; cel 1.8)
- `ccna.ipv6.ext.17` — Rozdziel nowe LAN-y (CLI, trudność 3; cel 1.8)
- `ccna.ipv6.ext.18` — IPv4 działa, IPv6 nie (quiz, trudność 3; cel 1.8)

#### Routing statyczny

**ccna.static.stage-1**

- `ccna.static.01` — Longest prefix match (quiz, trudność 1; cel 3.2)
- `ccna.static.02` — Trasa do sieci (CLI, trudność 1; cel 3.3)
- `ccna.static.03` — Default IPv4 (CLI, trudność 1; cel 3.3)
- `ccna.static.04` — Domyślna AD statycznej (quiz, trudność 1; cel 3.1.e)
- `ccna.static.05` — Trasa do jednego hosta (CLI, trudność 1; cel 3.3)
- `ccna.static.06` — Weryfikacja statycznych (CLI, trudność 1; cel 3.3)

**ccna.static.stage-2**

- `ccna.static.07` — Floating static za OSPF (quiz, trudność 2; cel 3.3)
- `ccna.static.08` — Default: maska i next-hop (CLI, trudność 2; cel 3.3)
- `ccna.static.09` — Floating do konkretnej sieci (CLI, trudność 2; cel 3.3)
- `ccna.static.10` — Dokładniejsza trasa a default (quiz, trudność 2; cel 3.2)
- `ccna.static.11` — Statyczna IPv6 (CLI, trudność 2; cel 3.3)
- `ccna.static.12` — Default IPv6 (CLI, trudność 2; cel 3.3)

**ccna.static.stage-3**

- `ccna.static.13` — Wciąż osiągalny sąsiad zapasu (quiz, trudność 3; cel 3.3)
- `ccna.static.14` — Primary i backup default (CLI, trudność 3; cel 3.3)
- `ccna.static.15` — Next-hop link-local IPv6 (CLI, trudność 3; cel 3.3)
- `ccna.static.16` — Trasa hosta IPv6 (quiz, trudność 3; cel 3.3)
- `ccna.static.17` — Wymień tylko błędną trasę (CLI, trudność 3; cel 3.3)
- `ccna.static.18` — Trasa sieci i wyjątek hosta (CLI, trudność 3; cel 3.3)

#### EtherChannel i LACP

**ccna.etherchannel.stage-1**

- `ccna.etherchannel.01` — Dlaczego Port-channel? (quiz, trudność 1; cel 2.4)
- `ccna.etherchannel.02` — LACP inicjujący (CLI, trudność 1; cel 2.4)
- `ccna.etherchannel.03` — LACP odpowiadający (CLI, trudność 1; cel 2.4)
- `ccna.etherchannel.04` — Dwie strony passive (quiz, trudność 1; cel 2.4)
- `ccna.etherchannel.05` — Wejdź na interfejs logiczny (CLI, trudność 1; cel 2.4)
- `ccna.etherchannel.06` — Zestawienie kanałów (CLI, trudność 1; cel 2.4)

**ccna.etherchannel.stage-2**

- `ccna.etherchannel.07` — on nie oznacza LACP (quiz, trudność 2; cel 2.4)
- `ccna.etherchannel.08` — Numer grupy i tryb (CLI, trudność 2; cel 2.4)
- `ccna.etherchannel.09` — Trunk na Port-channel (CLI, trudność 2; cel 2.4)
- `ccna.etherchannel.10` — Niezgodne porty członkowskie (quiz, trudność 2; cel 2.4)
- `ccna.etherchannel.11` — Dodaj VLAN na kanale (CLI, trudność 2; cel 2.4)
- `ccna.etherchannel.12` — Weryfikacja LACP sąsiadów (CLI, trudność 2; cel 2.4)

**ccna.etherchannel.stage-3**

- `ccna.etherchannel.13` — Jeden przepływ i dwa łącza (quiz, trudność 3; cel 2.4)
- `ccna.etherchannel.14` — Dwa porty LACP access (CLI, trudność 3; cel 2.4)
- `ccna.etherchannel.15` — Trunk LACP od początku (CLI, trudność 3; cel 2.4)
- `ccna.etherchannel.16` — Flaga P w summary (quiz, trudność 3; cel 2.4)
- `ccna.etherchannel.17` — Napraw passive/passive (CLI, trudność 3; cel 2.4)
- `ccna.etherchannel.18` — Zmiana wspólnej polityki trunku (CLI, trudność 3; cel 2.4)

**ccna.etherchannel.stage-4**

- `ccna.etherchannel.ext.01` — Lokalny numer grupy (quiz, trudność 2; cel 2.4)
- `ccna.etherchannel.ext.02` — Active plus passive (quiz, trudność 2; cel 2.4)
- `ccna.etherchannel.ext.03` — Od pasywnego do aktywnego (CLI, trudność 2; cel 2.4)
- `ccna.etherchannel.ext.04` — LACP a PAgP (quiz, trudność 2; cel 2.4)
- `ccna.etherchannel.ext.05` — Dwa członki access (CLI, trudność 2; cel 2.4)
- `ccna.etherchannel.ext.06` — Statyczne on (quiz, trudność 2; cel 2.4)

**ccna.etherchannel.stage-5**

- `ccna.etherchannel.ext.07` — STP i wiązka (quiz, trudność 3; cel 2.4)
- `ccna.etherchannel.ext.08` — Awaria jednego członka (quiz, trudność 3; cel 2.4)
- `ccna.etherchannel.ext.09` — Trunk logiczny (CLI, trudność 3; cel 2.4)
- `ccna.etherchannel.ext.10` — Nierówny rozkład (quiz, trudność 3; cel 2.4)
- `ccna.etherchannel.ext.11` — Sprawdź wiązkę warstwami (CLI, trudność 3; cel 2.4)
- `ccna.etherchannel.ext.12` — Nie ten partner (quiz, trudność 3; cel 2.4)

**ccna.etherchannel.stage-6**

- `ccna.etherchannel.ext.13` — Stan suspended (quiz, trudność 3; cel 2.4)
- `ccna.etherchannel.ext.14` — Różna lista VLAN (quiz, trudność 3; cel 2.4)
- `ccna.etherchannel.ext.15` — Rozszerz bez nadpisania (CLI, trudność 3; cel 2.4)
- `ccna.etherchannel.ext.16` — Konfiguracja a operacyjność (quiz, trudność 3; cel 2.4)
- `ccna.etherchannel.ext.17` — Kontrola po awarii (CLI, trudność 3; cel 2.4)
- `ccna.etherchannel.ext.18` — Haszowanie a test (quiz, trudność 3; cel 2.4)

#### DHCP: klient, relay i pula

**ccna.dhcp.stage-1**

- `ccna.dhcp.01` — Kolejność DORA (quiz, trudność 1; cel 4.3)
- `ccna.dhcp.02` — Interfejs jako klient DHCP (CLI, trudność 1; cel 4.6)
- `ccna.dhcp.03` — Utwórz pulę (CLI, trudność 1; cel 4.3)
- `ccna.dhcp.04` — DHCP w innej podsieci (quiz, trudność 1; cel 4.3)
- `ccna.dhcp.05` — Brama w puli (CLI, trudność 1; cel 4.3)
- `ccna.dhcp.06` — Wyświetl dzierżawy (CLI, trudność 1; cel 4.3)

**ccna.dhcp.stage-2**

- `ccna.dhcp.07` — Gdzie ip helper-address? (quiz, trudność 2; cel 4.6)
- `ccna.dhcp.08` — Zakres sieci puli (CLI, trudność 2; cel 4.3)
- `ccna.dhcp.09` — Wyklucz infrastrukturę (CLI, trudność 2; cel 4.3)
- `ccna.dhcp.10` — ACK a DNS (quiz, trudność 2; cel 4.3)
- `ccna.dhcp.11` — Przekaż bramę i resolver (CLI, trudność 2; cel 4.3)
- `ccna.dhcp.12` — Relay dla VLAN 40 (CLI, trudność 2; cel 4.6)

**ccna.dhcp.stage-3**

- `ccna.dhcp.13` — Dobór zakresu przez relay (quiz, trudność 3; cel 4.6)
- `ccna.dhcp.14` — Pełna pula LAN (CLI, trudność 3; cel 4.3)
- `ccna.dhcp.15` — Dzierżawa i DNS (CLI, trudność 3; cel 4.3)
- `ccna.dhcp.16` — Pula /27 z wykluczeniami (quiz, trudność 3; cel 4.3)
- `ccna.dhcp.17` — Dwa segmenty, jeden relay server (CLI, trudność 3; cel 4.6)
- `ccna.dhcp.18` — Zmień tylko błędny helper (CLI, trudność 3; cel 4.6)

#### SSH i dostęp administracyjny

**ccna.ssh.stage-1**

- `ccna.ssh.01` — SSH zamiast Telnet (quiz, trudność 1; cel 4.8)
- `ccna.ssh.02` — Tylko SSH na VTY (CLI, trudność 1; cel 4.8)
- `ccna.ssh.03` — Lokalna baza użytkowników (CLI, trudność 1; cel 4.8)
- `ccna.ssh.04` — Dlaczego samo transport input nie wystarcza? (quiz, trudność 1; cel 4.8)
- `ccna.ssh.05` — Wersja SSH (CLI, trudność 1; cel 4.8)
- `ccna.ssh.06` — Stan serwera SSH (CLI, trudność 1; cel 4.8)

**ccna.ssh.stage-2**

- `ccna.ssh.07` — VTY a console (quiz, trudność 2; cel 4.8)
- `ccna.ssh.08` — Spójna para ustawień VTY (CLI, trudność 2; cel 4.8)
- `ccna.ssh.09` — Timeout bezczynności (CLI, trudność 2; cel 4.8)
- `ccna.ssh.10` — Skąd wolno zarządzać? (quiz, trudność 2; cel 4.8)
- `ccna.ssh.11` — Przypnij istniejącą ACL do VTY (CLI, trudność 2; cel 4.8)
- `ccna.ssh.12` — Nazwa i domena w klasycznym labie SSH (CLI, trudność 2; cel 4.8)

**ccna.ssh.stage-3**

- `ccna.ssh.13` — Wszystkie linie VTY (quiz, trudność 3; cel 4.8)
- `ccna.ssh.14` — Pełne VTY w zadanym zakresie (CLI, trudność 3; cel 4.8)
- `ccna.ssh.15` — Konto i serwer SSH w labie (CLI, trudność 3; cel 4.8)
- `ccna.ssh.16` — Szyfrowanie hasła typu 7 (quiz, trudność 3; cel 4.8)
- `ccna.ssh.17` — Ogranicz zarządzanie do podsieci (CLI, trudność 3; cel 4.8)
- `ccna.ssh.18` — Klucz RSA i weryfikacja (CLI, trudność 3; cel 4.8)

#### NTP, syslog i SNMP

**ccna.monitoring.stage-1**

- `ccna.monitoring.01` — Po co wspólny czas? (quiz, trudność 1; cel 4.2)
- `ccna.monitoring.02` — Klient NTP (CLI, trudność 1; cel 4.2)
- `ccna.monitoring.03` — Stan synchronizacji (CLI, trudność 1; cel 4.2)
- `ccna.monitoring.04` — Skala syslog (quiz, trudność 1; cel 4.5)
- `ccna.monitoring.05` — Serwer syslog (CLI, trudność 1; cel 4.5)
- `ccna.monitoring.06` — SNMP tylko odczyt w labie (CLI, trudność 1; cel 4.4)

**ccna.monitoring.stage-2**

- `ccna.monitoring.07` — Próg logging trap warnings (quiz, trudność 2; cel 4.5)
- `ccna.monitoring.08` — NTP: serwer i źródło (CLI, trudność 2; cel 4.2)
- `ccna.monitoring.09` — Syslog: cel i poziom (CLI, trudność 2; cel 4.5)
- `ccna.monitoring.10` — Polling a trap (quiz, trudność 2; cel 4.4)
- `ccna.monitoring.11` — Lokalny bufor logów (CLI, trudność 2; cel 4.5)
- `ccna.monitoring.12` — Sprawdź relacje NTP (CLI, trudność 2; cel 4.2)

**ccna.monitoring.stage-3**

- `ccna.monitoring.13` — SNMPv3 authPriv (quiz, trudność 3; cel 4.4)
- `ccna.monitoring.14` — Spójne znaczniki czasu (CLI, trudność 3; cel 4.2)
- `ccna.monitoring.15` — Ograniczony polling SNMPv2c (CLI, trudność 3; cel 4.4)
- `ccna.monitoring.16` — Dlaczego brak informational? (quiz, trudność 3; cel 4.5)
- `ccna.monitoring.17` — Polityka logów na źródle loopback (CLI, trudność 3; cel 4.5)
- `ccna.monitoring.18` — Weryfikacja czasu i lokalnych logów (CLI, trudność 3; cel 4.2)

#### CDP i LLDP

**ccna.discovery.stage-1**

- `ccna.discovery.01` — Sąsiad innego producenta (quiz, trudność 1; cel 2.3)
- `ccna.discovery.02` — Globalny CDP (CLI, trudność 1; cel 2.3)
- `ccna.discovery.03` — Lokalne wyłączenie CDP (CLI, trudność 1; cel 2.3)
- `ccna.discovery.04` — Sąsiedztwo a routing (quiz, trudność 1; cel 2.3)
- `ccna.discovery.05` — Globalny LLDP (CLI, trudność 1; cel 2.3)
- `ccna.discovery.06` — Szczegóły CDP (CLI, trudność 1; cel 2.3)

**ccna.discovery.stage-2**

- `ccna.discovery.07` — Odbiór bez nadawania (quiz, trudność 2; cel 2.3)
- `ccna.discovery.08` — LLDP w obie strony (CLI, trudność 2; cel 2.3)
- `ccna.discovery.09` — CDP od urządzenia do portu (CLI, trudność 2; cel 2.3)
- `ccna.discovery.10` — Lokalny czy zdalny port (quiz, trudność 2; cel 2.3)
- `ccna.discovery.11` — Cichy odbiorca LLDP (CLI, trudność 2; cel 2.3)
- `ccna.discovery.12` — Porównanie protokołów (CLI, trudność 2; cel 2.3)

**ccna.discovery.stage-3**

- `ccna.discovery.13` — Pusty LLDP (quiz, trudność 3; cel 2.3)
- `ccna.discovery.14` — Uplink wieloproducentowy (CLI, trudność 3; cel 2.3)
- `ccna.discovery.15` — Port bez discovery (CLI, trudność 3; cel 2.3)
- `ccna.discovery.16` — Wpis po odłączeniu (quiz, trudność 3; cel 2.3)
- `ccna.discovery.17` — Odtwórz CDP i sprawdź (CLI, trudność 3; cel 2.3)
- `ccna.discovery.18` — LLDP jednokierunkowo i kontrola (CLI, trudność 3; cel 2.3)

#### Port Security

**ccna.portsecurity.stage-1**

- `ccna.portsecurity.01` — Co ogranicza Port Security? (quiz, trudność 1; cel 5.7)
- `ccna.portsecurity.02` — Włącz ochronę portu (CLI, trudność 1; cel 5.7)
- `ccna.portsecurity.03` — Limit dwóch źródeł (CLI, trudność 1; cel 5.7)
- `ccna.portsecurity.04` — Domyślne naruszenie (quiz, trudność 1; cel 5.7)
- `ccna.portsecurity.05` — Nauka sticky (CLI, trudność 1; cel 5.7)
- `ccna.portsecurity.06` — Restrict zamiast shutdown (CLI, trudność 1; cel 5.7)

**ccna.portsecurity.stage-2**

- `ccna.portsecurity.07` — Protect a restrict (quiz, trudność 2; cel 5.7)
- `ccna.portsecurity.08` — Access i ochrona (CLI, trudność 2; cel 5.7)
- `ccna.portsecurity.09` — Limit i reakcja (CLI, trudność 2; cel 5.7)
- `ccna.portsecurity.10` — Sticky po restarcie (quiz, trudność 2; cel 5.7)
- `ccna.portsecurity.11` — Naucz i utrwal (CLI, trudność 2; cel 5.7)
- `ccna.portsecurity.12` — Ożyw port po naprawie (CLI, trudność 2; cel 5.7)

**ccna.portsecurity.stage-3**

- `ccna.portsecurity.13` — Trzecie urządzenie (quiz, trudność 3; cel 5.7)
- `ccna.portsecurity.14` — Nowy port stanowiska (CLI, trudność 3; cel 5.7)
- `ccna.portsecurity.15` — Jawna polityka dla dwóch MAC (CLI, trudność 3; cel 5.7)
- `ccna.portsecurity.16` — Secure-up nie oznacza 802.1X (quiz, trudność 3; cel 5.7)
- `ccna.portsecurity.17` — Napraw i zweryfikuj interfejs (CLI, trudność 3; cel 5.7)
- `ccna.portsecurity.18` — Zmień politykę i sprawdź (CLI, trudność 3; cel 5.7)

#### DHCP Snooping

**ccna.snooping.stage-1**

- `ccna.snooping.01` — Rogue DHCP (quiz, trudność 1; cel 5.7)
- `ccna.snooping.02` — Proces snooping (CLI, trudność 1; cel 5.7)
- `ccna.snooping.03` — Chroniony VLAN (CLI, trudność 1; cel 5.7)
- `ccna.snooping.04` — Granica zaufania DHCP (quiz, trudność 1; cel 5.7)
- `ccna.snooping.05` — Zaufany serwer (CLI, trudność 1; cel 5.7)
- `ccna.snooping.06` — Baza dzierżaw snooping (CLI, trudność 1; cel 5.7)

**ccna.snooping.stage-2**

- `ccna.snooping.07` — Jednostka limitu (quiz, trudność 2; cel 5.7)
- `ccna.snooping.08` — Proces i zakres (CLI, trudność 2; cel 5.7)
- `ccna.snooping.09` — Zaufanie cofnięte (CLI, trudność 2; cel 5.7)
- `ccna.snooping.10` — Adres statyczny w tabeli (quiz, trudność 2; cel 5.7)
- `ccna.snooping.11` — Uplink i weryfikacja (CLI, trudność 2; cel 5.7)
- `ccna.snooping.12` — Wyłącz jeden VLAN (CLI, trudność 2; cel 5.7)

**ccna.snooping.stage-3**

- `ccna.snooping.13` — Brak DHCP po wdrożeniu (quiz, trudność 3; cel 5.7)
- `ccna.snooping.14` — Pełne wdrożenie snooping (CLI, trudność 3; cel 5.7)
- `ccna.snooping.15` — Port klienta po zmianie roli (CLI, trudność 3; cel 5.7)
- `ccna.snooping.16` — Opcja 82 (quiz, trudność 3; cel 5.7)
- `ccna.snooping.17` — Dwa wejścia serwera (CLI, trudność 3; cel 5.7)
- `ccna.snooping.18` — Kontrolowane wycofanie (CLI, trudność 3; cel 5.7)

#### Dynamic ARP Inspection

**ccna.dai.stage-1**

- `ccna.dai.01` — Fałszywe ARP (quiz, trudność 1; cel 5.7)
- `ccna.dai.02` — DAI dla VLAN (CLI, trudność 1; cel 5.7)
- `ccna.dai.03` — Zaufanie ARP (CLI, trudność 1; cel 5.7)
- `ccna.dai.04` — Baza odniesienia DAI (quiz, trudność 1; cel 5.7)
- `ccna.dai.05` — Cofnięcie zaufania ARP (CLI, trudność 1; cel 5.7)
- `ccna.dai.06` — Liczniki inspekcji (CLI, trudność 1; cel 5.7)

**ccna.dai.stage-2**

- `ccna.dai.07` — Dwa różne trust (quiz, trudność 2; cel 5.7)
- `ccna.dai.08` — Zakres i uplink DAI (CLI, trudność 2; cel 5.7)
- `ccna.dai.09` — Sprawdź dane wejściowe (CLI, trudność 2; cel 5.7)
- `ccna.dai.10` — Statyczna drukarka (quiz, trudność 2; cel 5.7)
- `ccna.dai.11` — Zaufanie odwołane, kontrola (CLI, trudność 2; cel 5.7)
- `ccna.dai.12` — Wyłączenie jednego zakresu (CLI, trudność 2; cel 5.7)

**ccna.dai.stage-3**

- `ccna.dai.13` — Pusta baza po restarcie (quiz, trudność 3; cel 5.7)
- `ccna.dai.14` — Snooping plus DAI (CLI, trudność 3; cel 5.7)
- `ccna.dai.15` — Dwie granice zaufania (CLI, trudność 3; cel 5.7)
- `ccna.dai.16` — Czy DAI filtruje IPv6? (quiz, trudność 3; cel 5.7)
- `ccna.dai.17` — Port klienta bez wyjątków (CLI, trudność 3; cel 5.7)
- `ccna.dai.18` — Walidacja źródłowego MAC (CLI, trudność 3; cel 5.7)

#### Redundancja bramy — HSRP

**ccna.fhrp.stage-1**

- `ccna.fhrp.01` — Wspólna brama (quiz, trudność 1; cel 3.5)
- `ccna.fhrp.02` — Wirtualny adres (CLI, trudność 1; cel 3.5)
- `ccna.fhrp.03` — Priorytet HSRP (CLI, trudność 1; cel 3.5)
- `ccna.fhrp.04` — Active i standby (quiz, trudność 1; cel 3.5)
- `ccna.fhrp.05` — Powrót preferowanej bramy (CLI, trudność 1; cel 3.5)
- `ccna.fhrp.06` — Skrócony stan HSRP (CLI, trudność 1; cel 3.5)

**ccna.fhrp.stage-2**

- `ccna.fhrp.07` — Wysoki priorytet bez preempt (quiz, trudność 2; cel 3.5)
- `ccna.fhrp.08` — Preferencja i przejęcie (CLI, trudność 2; cel 3.5)
- `ccna.fhrp.09` — Wersja i grupa (CLI, trudność 2; cel 3.5)
- `ccna.fhrp.10` — Awaria za bramą (quiz, trudność 2; cel 3.5)
- `ccna.fhrp.11` — Powiąż obiekt śledzenia (CLI, trudność 2; cel 3.5)
- `ccna.fhrp.12` — Odroczone przejęcie (CLI, trudność 2; cel 3.5)

**ccna.fhrp.stage-3**

- `ccna.fhrp.13` — Arytmetyka trackingu (quiz, trudność 3; cel 3.5)
- `ccna.fhrp.14` — Brama preferowana (CLI, trudność 3; cel 3.5)
- `ccna.fhrp.15` — Śledź fizyczny uplink (CLI, trudność 3; cel 3.5)
- `ccna.fhrp.16` — Dwie aktywne bramy (quiz, trudność 3; cel 3.5)
- `ccna.fhrp.17` — Zapas z możliwością przejęcia (CLI, trudność 3; cel 3.5)
- `ccna.fhrp.18` — Przygotowanie po restarcie (CLI, trudność 3; cel 3.5)

#### WLAN — radio, architektura i bezpieczeństwo

**ccna.wireless.stage-1**

- `ccna.wireless.01` — SSID a BSSID (quiz, trudność 1; cel 1.11)
- `ccna.wireless.02` — Dwa poziomy sygnału (quiz, trudność 1; cel 1.11)
- `ccna.wireless.03` — Sygnał a szum (quiz, trudność 1; cel 1.11)
- `ccna.wireless.04` — Wspólny kanał (quiz, trudność 1; cel 1.11)
- `ccna.wireless.05` — Kanały 2,4 GHz (quiz, trudność 1; cel 1.11)
- `ccna.wireless.06` — Ukryte SSID (quiz, trudność 1; cel 5.9)

**ccna.wireless.stage-2**

- `ccna.wireless.07` — CAPWAP (quiz, trudność 2; cel 2.6)
- `ccna.wireless.08` — Local switching (quiz, trudność 2; cel 2.6)
- `ccna.wireless.09` — AP i kontroler (quiz, trudność 2; cel 2.6)
- `ccna.wireless.10` — WPA2-Enterprise (quiz, trudność 2; cel 5.9)
- `ccna.wireless.11` — WPA3-Personal (quiz, trudność 2; cel 5.9)
- `ccna.wireless.12` — To samo SSID (quiz, trudność 2; cel 2.9)

**ccna.wireless.stage-3**

- `ccna.wireless.13` — Silny sygnał, niska jakość (quiz, trudność 3; cel 1.11)
- `ccna.wireless.14` — Za szeroki kanał (quiz, trudność 3; cel 1.11)
- `ccna.wireless.15` — Oddział bez WAN (quiz, trudność 3; cel 2.6)
- `ccna.wireless.16` — WLAN działa, IP brak (quiz, trudność 3; cel 2.9)
- `ccna.wireless.17` — Portal a szyfrowanie (quiz, trudność 3; cel 5.9)
- `ccna.wireless.18` — Decyzja o roamingu (quiz, trudność 3; cel 1.11)

#### QoS — klasyfikacja i kolejki

**ccna.qos.stage-1**

- `ccna.qos.01` — Po co QoS? (quiz, trudność 1; cel 4.7)
- `ccna.qos.02` — Klasyfikacja (quiz, trudność 1; cel 4.7)
- `ccna.qos.03` — Marking (quiz, trudność 1; cel 4.7)
- `ccna.qos.04` — Pole DSCP (quiz, trudność 1; cel 4.7)
- `ccna.qos.05` — CoS w 802.1Q (quiz, trudność 1; cel 4.7)
- `ccna.qos.06` — Jitter (quiz, trudność 1; cel 4.7)

**ccna.qos.stage-2**

- `ccna.qos.07` — Shaping (quiz, trudność 2; cel 4.7)
- `ccna.qos.08` — Policing (quiz, trudność 2; cel 4.7)
- `ccna.qos.09` — EF liczbowo (quiz, trudność 2; cel 4.7)
- `ccna.qos.10` — AF drop precedence (quiz, trudność 2; cel 4.7)
- `ccna.qos.11` — Granica zaufania QoS (quiz, trudność 2; cel 4.7)
- `ccna.qos.12` — Kolejka priorytetowa (quiz, trudność 2; cel 4.7)

**ccna.qos.stage-3**

- `ccna.qos.13` — 10 Mb/s pod ruchem 14 Mb/s (quiz, trudność 3; cel 4.7)
- `ccna.qos.14` — Samo oznaczenie EF (quiz, trudność 3; cel 4.7)
- `ccna.qos.15` — Zła klasyfikacja głosu (quiz, trudność 3; cel 4.7)
- `ccna.qos.16` — Utrata a jitter (quiz, trudność 3; cel 4.7)
- `ccna.qos.17` — CoS bez tagu (quiz, trudność 3; cel 4.7)
- `ccna.qos.18` — QoS end-to-end (quiz, trudność 3; cel 4.7)

#### Automatyzacja — JSON i API

**ccna.automation.stage-1**

- `ccna.automation.01` — API zamiast klikania (quiz, trudność 1; cel 6.1)
- `ccna.automation.02` — Odczyt zasobu (quiz, trudność 1; cel 6.5)
- `ccna.automation.03` — Nowy zasób (quiz, trudność 1; cel 6.5)
- `ccna.automation.04` — Obiekt JSON (quiz, trudność 1; cel 6.7)
- `ccna.automation.05` — Tablica JSON (quiz, trudność 1; cel 6.7)
- `ccna.automation.06` — Typ logiczny a tekst (quiz, trudność 1; cel 6.7)

**ccna.automation.stage-2**

- `ccna.automation.07` — Usunięcie obiektu (quiz, trudność 2; cel 6.5)
- `ccna.automation.08` — Częściowa aktualizacja (quiz, trudność 2; cel 6.5)
- `ccna.automation.09` — Idempotencja (quiz, trudność 2; cel 6.5)
- `ccna.automation.10` — 401 z API (quiz, trudność 2; cel 6.5)
- `ccna.automation.11` — 403 z API (quiz, trudność 2; cel 6.5)
- `ccna.automation.12` — 200 a zgodność stanu (quiz, trudność 2; cel 6.5)

**ccna.automation.stage-3**

- `ccna.automation.13` — Utracona odpowiedź POST (quiz, trudność 3; cel 6.5)
- `ccna.automation.14` — Paginacja (quiz, trudność 3; cel 6.5)
- `ccna.automation.15` — Asynchroniczne zadanie (quiz, trudność 3; cel 6.5)
- `ccna.automation.16` — Sekret w repozytorium (quiz, trudność 3; cel 6.5)
- `ccna.automation.17` — Walidacja schematu (quiz, trudność 3; cel 6.7)
- `ccna.automation.18` — Najpierw mała grupa (quiz, trudność 3; cel 6.1)

#### Ethernet, MAC i ARP

**ccna.ethernet.stage-1**

- `ccna.ethernet.01` — Nauka MAC (quiz, trudność 1; cel 1.13)
- `ccna.ethernet.02` — Decyzja L2 (quiz, trudność 1; cel 1.13)
- `ccna.ethernet.03` — Dynamiczna tabela (CLI, trudność 1; cel 1.13)
- `ccna.ethernet.04` — Unknown unicast (quiz, trudność 1; cel 1.13)
- `ccna.ethernet.05` — Cache ARP routera (CLI, trudność 1; cel 1.6)
- `ccna.ethernet.06` — ARP w lokalnym LAN (quiz, trudność 1; cel 1.6)

**ccna.ethernet.stage-2**

- `ccna.ethernet.07` — Zdalny cel i lokalny MAC (quiz, trudność 2; cel 1.6)
- `ccna.ethernet.08` — Broadcast Ethernet (quiz, trudność 2; cel 1.13)
- `ccna.ethernet.09` — MAC dla jednego VLAN-u (CLI, trudność 2; cel 1.13)
- `ccna.ethernet.10` — Cel na porcie wejściowym (quiz, trudność 2; cel 1.13)
- `ccna.ethernet.11` — Port i adresy (CLI, trudność 2; cel 1.13)
- `ccna.ethernet.12` — Wiek wpisu MAC (quiz, trudność 2; cel 1.13)

**ccna.ethernet.stage-3**

- `ccna.ethernet.13` — MAC flapping (quiz, trudność 3; cel 1.13)
- `ccna.ethernet.14` — FCS (quiz, trudność 3; cel 1.13)
- `ccna.ethernet.15` — Trzy widoki diagnostyczne (CLI, trudność 3; cel 1.6)
- `ccna.ethernet.16` — ARP nie jest MAC table (quiz, trudność 3; cel 1.6)
- `ccna.ethernet.17` — Porównaj sąsiednie porty (CLI, trudność 3; cel 1.13)
- `ccna.ethernet.18` — Ethernet przez router (quiz, trudność 3; cel 1.6)

#### TCP i UDP — sesje i diagnostyka

**ccna.transport.stage-1**

- `ccna.transport.01` — TCP a UDP (quiz, trudność 1; cel 1.5)
- `ccna.transport.02` — Handshake TCP (quiz, trudność 1; cel 1.5)
- `ccna.transport.03` — Brak handshake UDP (quiz, trudność 1; cel 1.5)
- `ccna.transport.04` — Numer portu (quiz, trudność 1; cel 1.5)
- `ccna.transport.05` — Kierunek odpowiedzi TCP (quiz, trudność 1; cel 1.5)
- `ccna.transport.06` — UDP i niezawodna aplikacja (quiz, trudność 1; cel 1.5)

**ccna.transport.stage-2**

- `ccna.transport.07` — ACK kolejnego bajtu (quiz, trudność 2; cel 1.5)
- `ccna.transport.08` — SYN zajmuje numer (quiz, trudność 2; cel 1.5)
- `ccna.transport.09` — Odbiorca i okno (quiz, trudność 2; cel 1.5)
- `ccna.transport.10` — MSS a MTU (quiz, trudność 2; cel 1.5)
- `ccna.transport.11` — FIN kontra RST (quiz, trudność 2; cel 1.5)
- `ccna.transport.12` — ACK nie potwierdza aplikacji (quiz, trudność 2; cel 1.5)

**ccna.transport.stage-3**

- `ccna.transport.13` — Ping działa, HTTPS nie (quiz, trudność 3; cel 1.5)
- `ccna.transport.14` — Powtarzający się SYN (quiz, trudność 3; cel 1.5)
- `ccna.transport.15` — Retransmisja a utrata (quiz, trudność 3; cel 1.5)
- `ccna.transport.16` — Okno zero (quiz, trudność 3; cel 1.5)
- `ccna.transport.17` — MSS przy IPv4 (quiz, trudność 3; cel 1.5)
- `ccna.transport.18` — Dwie sesje HTTPS (quiz, trudność 3; cel 1.5)

#### DNS — nazwy i rozwiązywanie problemów

**ccna.dns.stage-1**

- `ccna.dns.01` — Rola DNS (quiz, trudność 1; cel 4.3)
- `ccna.dns.02` — AAAA (quiz, trudność 1; cel 4.3)
- `ccna.dns.03` — Resolver routera (CLI, trudność 1; cel 4.3)
- `ccna.dns.04` — CNAME (quiz, trudność 1; cel 4.3)
- `ccna.dns.05` — Tabela nazw IOS (CLI, trudność 1; cel 4.3)
- `ccna.dns.06` — TTL rekordu (quiz, trudność 1; cel 4.3)

**ccna.dns.stage-2**

- `ccna.dns.07` — Resolver a authoritative (quiz, trudność 2; cel 4.3)
- `ccna.dns.08` — NXDOMAIN (quiz, trudność 2; cel 4.3)
- `ccna.dns.09` — Włącz i wskaż DNS (CLI, trudność 2; cel 4.3)
- `ccna.dns.10` — UDP i TCP DNS (quiz, trudność 2; cel 4.3)
- `ccna.dns.11` — Statyczna nazwa w labie (CLI, trudność 2; cel 4.3)
- `ccna.dns.12` — Usługa po IP a nazwa (quiz, trudność 2; cel 4.3)

**ccna.dns.stage-3**

- `ccna.dns.13` — Split DNS (quiz, trudność 3; cel 4.3)
- `ccna.dns.14` — Cache po zmianie (quiz, trudność 3; cel 4.3)
- `ccna.dns.15` — Dwa resolvery i kontrola (CLI, trudność 3; cel 4.3)
- `ccna.dns.16` — DNS działa, HTTPS nie (quiz, trudność 3; cel 4.3)
- `ccna.dns.17` — Usuń błędny lokalny wpis (CLI, trudność 3; cel 4.3)
- `ccna.dns.18` — PTR (quiz, trudność 3; cel 4.3)

#### AAA — tożsamość, uprawnienia i audyt

**ccna.aaa.stage-1**

- `ccna.aaa.01` — Authentication (quiz, trudność 1; cel 5.8)
- `ccna.aaa.02` — Authorization (quiz, trudność 1; cel 5.8)
- `ccna.aaa.03` — Włączenie AAA w labie (CLI, trudność 1; cel 5.8)
- `ccna.aaa.04` — Accounting (quiz, trudność 1; cel 5.8)
- `ccna.aaa.05` — Lokalna lista logowania (CLI, trudność 1; cel 5.8)
- `ccna.aaa.06` — Przypięcie listy do VTY (CLI, trudność 1; cel 5.8)

**ccna.aaa.stage-2**

- `ccna.aaa.07` — RADIUS i transport (quiz, trudność 2; cel 5.8)
- `ccna.aaa.08` — TACACS+ (quiz, trudność 2; cel 5.8)
- `ccna.aaa.09` — TACACS+ z fallbackiem (CLI, trudność 2; cel 5.8)
- `ccna.aaa.10` — Reject a timeout (quiz, trudność 2; cel 5.8)
- `ccna.aaa.11` — RADIUS i lokalny zapas (CLI, trudność 2; cel 5.8)
- `ccna.aaa.12` — Login nie oznacza pełnych praw (quiz, trudność 2; cel 5.8)

**ccna.aaa.stage-3**

- `ccna.aaa.13` — Dwie tożsamości (quiz, trudność 3; cel 5.8)
- `ccna.aaa.14` — Synchronizacja audytu (quiz, trudność 3; cel 5.8)
- `ccna.aaa.15` — Lokalna lista i tylko SSH (CLI, trudność 3; cel 5.8)
- `ccna.aaa.16` — Sekret współdzielony AAA (quiz, trudność 3; cel 5.8)
- `ccna.aaa.17` — Metoda zdalna i przypisanie (CLI, trudność 3; cel 5.8)
- `ccna.aaa.18` — Least privilege (quiz, trudność 3; cel 5.8)

### CCNP ENCOR 350-401

#### eBGP — sąsiedztwo i wybór trasy

**encor.ebgp.stage-1**

- `encor.ebgp.01` — Granica AS (quiz, trudność 1; cel 3.2.c)
- `encor.ebgp.02` — Transport BGP (quiz, trudność 1; cel 3.2.c)
- `encor.ebgp.03` — Zdalny system autonomiczny (CLI, trudność 1; cel 3.2.c)
- `encor.ebgp.04` — Stan Established (quiz, trudność 1; cel 3.2.c)
- `encor.ebgp.05` — Dokładna maska network (CLI, trudność 1; cel 3.2.c)
- `encor.ebgp.06` — BGP to nie odkrywanie (quiz, trudność 1; cel 3.2.c)

**encor.ebgp.stage-2**

- `encor.ebgp.07` — Active nie znaczy gotowe (quiz, trudność 2; cel 3.2.c)
- `encor.ebgp.08` — Waga lokalna (quiz, trudność 2; cel 3.2.c)
- `encor.ebgp.09` — Pełna deklaracja peera (CLI, trudność 2; cel 3.2.c)
- `encor.ebgp.10` — Długość AS_PATH (quiz, trudność 2; cel 3.2.c)
- `encor.ebgp.11` — Dwa konkretne prefiksy (CLI, trudność 2; cel 3.2.c)
- `encor.ebgp.12` — Zasięg weight (quiz, trudność 2; cel 3.2.c)

**encor.ebgp.stage-3**

- `encor.ebgp.13` — Brak dokładnej trasy (quiz, trudność 3; cel 3.2.c)
- `encor.ebgp.14` — Local preference przed AS_PATH (quiz, trudność 3; cel 3.2.c)
- `encor.ebgp.15` — Pierwszy peering z ISP (CLI, trudność 3; cel 3.2.c)
- `encor.ebgp.16` — Nieosiągalny next hop (quiz, trudność 3; cel 3.2.c)
- `encor.ebgp.17` — Dwa łącza eBGP (CLI, trudność 3; cel 3.2.c)
- `encor.ebgp.18` — MED z jednego AS (quiz, trudność 3; cel 3.2.c)

#### OSPF — obszary, agregacja i OSPFv3

**encor.ospf-multi.stage-1**

- `encor.ospf-multi.01` — Router graniczny obszaru (quiz, trudność 1; cel 3.2.b)
- `encor.ospf-multi.02` — Backbone (quiz, trudność 1; cel 3.2.b)
- `encor.ospf-multi.03` — Przypisanie obszaru (CLI, trudność 1; cel 3.2.b)
- `encor.ospf-multi.04` — Trasa między obszarami (quiz, trudność 1; cel 3.2.b)
- `encor.ospf-multi.05` — Dwa routery bez wyboru DR (CLI, trudność 1; cel 3.2.b)
- `encor.ospf-multi.06` — LSA typu 3 (quiz, trudność 1; cel 3.2.b)

**encor.ospf-multi.stage-2**

- `encor.ospf-multi.07` — Dwa procesy lokalne (quiz, trudność 2; cel 3.2.b)
- `encor.ospf-multi.08` — Agregacja na ABR (quiz, trudność 2; cel 3.2.b)
- `encor.ospf-multi.09` — Konfiguracja area range (CLI, trudność 2; cel 3.2.b)
- `encor.ospf-multi.10` — Pasywny LAN (quiz, trudność 2; cel 3.2.b)
- `encor.ospf-multi.11` — Zezwól tylko na tranzyt (CLI, trudność 2; cel 3.2.b)
- `encor.ospf-multi.12` — OSPFv3 i router ID (quiz, trudność 2; cel 3.2.b)

**encor.ospf-multi.stage-3**

- `encor.ospf-multi.13` — Diagnoza 2-WAY (quiz, trudność 3; cel 3.2.b)
- `encor.ospf-multi.14` — Filtr prefix-list na ABR (quiz, trudność 3; cel 3.2.b)
- `encor.ospf-multi.15` — Dwa normalne obszary (CLI, trudność 3; cel 3.2.b)
- `encor.ospf-multi.16` — Stan EXSTART (quiz, trudność 3; cel 3.2.b)
- `encor.ospf-multi.17` — OSPFv3 w klasycznej składni (CLI, trudność 3; cel 3.2.b)
- `encor.ospf-multi.18` — Agregat i dziura (quiz, trudność 3; cel 3.2.b)

#### VRF — oddzielne tablice routingu

**encor.vrf.stage-1**

- `encor.vrf.01` — Izolacja klientów (quiz, trudność 1; cel 2.2.a)
- `encor.vrf.02` — VRF-lite (quiz, trudność 1; cel 2.2.a)
- `encor.vrf.03` — Nowy kontekst (CLI, trudność 1; cel 2.2.a)
- `encor.vrf.04` — Brak domyślnego przecieku (quiz, trudność 1; cel 2.2.a)
- `encor.vrf.05` — Przypisanie interfejsu (CLI, trudność 1; cel 2.2.a)
- `encor.vrf.06` — Odczyt tablicy BLUE (quiz, trudność 1; cel 2.2.a)

**encor.vrf.stage-2**

- `encor.vrf.07` — Adres znika (quiz, trudność 2; cel 2.2.a)
- `encor.vrf.08` — Ping z właściwego miejsca (quiz, trudność 2; cel 2.2.a)
- `encor.vrf.09` — Trasa statyczna BLUE (CLI, trudność 2; cel 2.2.a)
- `encor.vrf.10` — Globalny default nie pomaga (quiz, trudność 2; cel 2.2.a)
- `encor.vrf.11` — Adres w RED (CLI, trudność 2; cel 2.2.a)
- `encor.vrf.12` — RD a polityka (quiz, trudność 2; cel 2.2.a)

**encor.vrf.stage-3**

- `encor.vrf.13` — Nakładające się connected (quiz, trudność 3; cel 2.2.a)
- `encor.vrf.14` — Diagnoza asymetrii (quiz, trudność 3; cel 2.2.a)
- `encor.vrf.15` — Pełna konfiguracja klienta (CLI, trudność 3; cel 2.2.a)
- `encor.vrf.16` — Trasa w złej RIB (quiz, trudność 3; cel 2.2.a)
- `encor.vrf.17` — Oddzielne trasy dwóch klientów (CLI, trudność 3; cel 2.2.a)
- `encor.vrf.18` — Trasa connected we właściwym VRF (quiz, trudność 3; cel 2.2.a)

#### GRE — tunele i zależność od underlay

**encor.gre.stage-1**

- `encor.gre.01` — Cel GRE (quiz, trudność 1; cel 2.2.b)
- `encor.gre.02` — Numer protokołu (quiz, trudność 1; cel 2.2.b)
- `encor.gre.03` — Cel tunelu (CLI, trudność 1; cel 2.2.b)
- `encor.gre.04` — Underlay (quiz, trudność 1; cel 2.2.b)
- `encor.gre.05` — Jawny tryb GRE IPv4 (CLI, trudność 1; cel 2.2.b)
- `encor.gre.06` — Adres wewnętrzny (quiz, trudność 1; cel 2.2.b)

**encor.gre.stage-2**

- `encor.gre.07` — GRE a IPsec (quiz, trudność 2; cel 2.2.b)
- `encor.gre.08` — Minimalny narzut (quiz, trudność 2; cel 2.2.b)
- `encor.gre.09` — Adresacja i destination (CLI, trudność 2; cel 2.2.b)
- `encor.gre.10` — Rekurencja (quiz, trudność 2; cel 2.2.b)
- `encor.gre.11` — Bezpieczna zależność routingu (CLI, trudność 2; cel 2.2.b)
- `encor.gre.12` — Up/up bez testu (quiz, trudność 2; cel 2.2.b)

**encor.gre.stage-3**

- `encor.gre.13` — MTU po enkapsulacji (quiz, trudność 3; cel 2.2.b)
- `encor.gre.14` — Duże pakiety zawodzą (quiz, trudność 3; cel 2.2.b)
- `encor.gre.15` — Kompletny koniec GRE (CLI, trudność 3; cel 2.2.b)
- `encor.gre.16` — TCP MSS (quiz, trudność 3; cel 2.2.b)
- `encor.gre.17` — Zdalny koniec GRE (CLI, trudność 3; cel 2.2.b)
- `encor.gre.18` — Tunel działa, LAN nie (quiz, trudność 3; cel 2.2.b)

#### EIGRP a OSPF — metryki i zbieżność

**encor.routing-compare.stage-1**

- `encor.routing-compare.01` — Rodzina protokołu (quiz, trudność 1; cel 3.2.a)
- `encor.routing-compare.02` — Algorytm OSPF (quiz, trudność 1; cel 3.2.a)
- `encor.routing-compare.03` — Algorytm EIGRP (quiz, trudność 1; cel 3.2.a)
- `encor.routing-compare.04` — Domyślna metryka klasyczna (quiz, trudność 1; cel 3.2.a)
- `encor.routing-compare.05` — Koszt OSPF (quiz, trudność 1; cel 3.2.a)
- `encor.routing-compare.06` — Hierarchia (quiz, trudność 1; cel 3.2.a)

**encor.routing-compare.stage-2**

- `encor.routing-compare.07` — Successor (quiz, trudność 2; cel 3.2.a)
- `encor.routing-compare.08` — Reported distance (quiz, trudność 2; cel 3.2.a)
- `encor.routing-compare.09` — Warunek wykonalności (quiz, trudność 2; cel 3.2.a)
- `encor.routing-compare.10` — Równość nie wystarczy (quiz, trudność 2; cel 3.2.a)
- `encor.routing-compare.11` — Nierówne koszty (quiz, trudność 2; cel 3.2.a)
- `encor.routing-compare.12` — Wybór protokołu w RIB (quiz, trudność 2; cel 3.2.a)

**encor.routing-compare.stage-3**

- `encor.routing-compare.13` — Feasible successor a awaria (quiz, trudność 3; cel 3.2.a)
- `encor.routing-compare.14` — Brak feasible successor (quiz, trudność 3; cel 3.2.a)
- `encor.routing-compare.15` — Variance z ograniczeniem (quiz, trudność 3; cel 3.2.a)
- `encor.routing-compare.16` — Koszty OSPF na dwóch drogach (quiz, trudność 3; cel 3.2.a)
- `encor.routing-compare.17` — External EIGRP kontra OSPF (quiz, trudność 3; cel 3.2.a)
- `encor.routing-compare.18` — Najdłuższy prefiks (quiz, trudność 3; cel 3.2.a)

#### QoS — czytanie konfiguracji i liczników

**encor.qos-interpret.stage-1**

- `encor.qos-interpret.01` — Klasyfikacja (quiz, trudność 1; cel 1.4)
- `encor.qos-interpret.02` — DSCP EF (quiz, trudność 1; cel 1.4)
- `encor.qos-interpret.03` — Klasa domyślna (quiz, trudność 1; cel 1.4)
- `encor.qos-interpret.04` — Kierunek polityki (quiz, trudność 1; cel 1.4)
- `encor.qos-interpret.05` — Marking (quiz, trudność 1; cel 1.4)
- `encor.qos-interpret.06` — Ograniczenie QoS (quiz, trudność 1; cel 1.4)

**encor.qos-interpret.stage-2**

- `encor.qos-interpret.07` — LLQ (quiz, trudność 2; cel 1.4)
- `encor.qos-interpret.08` — Bandwidth (quiz, trudność 2; cel 1.4)
- `encor.qos-interpret.09` — Policing (quiz, trudność 2; cel 1.4)
- `encor.qos-interpret.10` — Shaping (quiz, trudność 2; cel 1.4)
- `encor.qos-interpret.11` — Match-any (quiz, trudność 2; cel 1.4)
- `encor.qos-interpret.12` — Granica zaufania (quiz, trudność 2; cel 1.4)

**encor.qos-interpret.stage-3**

- `encor.qos-interpret.13` — Licznik klasy jest zerowy (quiz, trudność 3; cel 1.4)
- `encor.qos-interpret.14` — Polityka istnieje, ale nie działa (quiz, trudność 3; cel 1.4)
- `encor.qos-interpret.15` — Obliczenie udziału (quiz, trudność 3; cel 1.4)
- `encor.qos-interpret.16` — Dwa narzędzia razem (quiz, trudność 3; cel 1.4)
- `encor.qos-interpret.17` — Drop precedence AF (quiz, trudność 3; cel 1.4)
- `encor.qos-interpret.18` — Nie utożsamiaj oznaczenia z obsługą (quiz, trudność 3; cel 1.4)

#### Wirtualizacja — VM, LISP i VXLAN

**encor.virtualization.stage-1**

- `encor.virtualization.01` — Hypervisor typu 1 (quiz, trudność 1; cel 2.1)
- `encor.virtualization.02` — Hypervisor typu 2 (quiz, trudność 1; cel 2.1)
- `encor.virtualization.03` — Interfejs VM (quiz, trudność 1; cel 2.1)
- `encor.virtualization.04` — Wirtualny switch (quiz, trudność 1; cel 2.1)
- `encor.virtualization.05` — Uplink hosta (quiz, trudność 1; cel 2.1)
- `encor.virtualization.06` — Izolacja VM (quiz, trudność 1; cel 2.1)

**encor.virtualization.stage-2**

- `encor.virtualization.07` — Cel VXLAN (quiz, trudność 2; cel 2.3.b)
- `encor.virtualization.08` — VTEP (quiz, trudność 2; cel 2.3.b)
- `encor.virtualization.09` — Identyfikator segmentu (quiz, trudność 2; cel 2.3.b)
- `encor.virtualization.10` — Underlay VXLAN (quiz, trudność 2; cel 2.3.b)
- `encor.virtualization.11` — EID w LISP (quiz, trudność 2; cel 2.3.a)
- `encor.virtualization.12` — RLOC w LISP (quiz, trudność 2; cel 2.3.a)

**encor.virtualization.stage-3**

- `encor.virtualization.13` — BUM w VXLAN (quiz, trudność 3; cel 2.3.b)
- `encor.virtualization.14` — VNI to nie szyfrowanie (quiz, trudność 3; cel 2.3.b)
- `encor.virtualization.15` — Rola ITR (quiz, trudność 3; cel 2.3.a)
- `encor.virtualization.16` — Rola ETR (quiz, trudność 3; cel 2.3.a)
- `encor.virtualization.17` — Nie działa tylko między hostami (quiz, trudność 3; cel 2.1)
- `encor.virtualization.18` — Przeniesienie endpointu (quiz, trudność 3; cel 2.3.a)

#### IP SLA — pomiary i diagnoza dostępności

**encor.ip-sla.stage-1**

- `encor.ip-sla.01` — Pomiar aktywny (quiz, trudność 1; cel 4.4)
- `encor.ip-sla.02` — Wynik echo (quiz, trudność 1; cel 4.4)
- `encor.ip-sla.03` — Numer operacji (CLI, trudność 1; cel 4.4)
- `encor.ip-sla.04` — Cel ICMP (quiz, trudność 1; cel 4.4)
- `encor.ip-sla.05` — Częstotliwość (CLI, trudność 1; cel 4.4)
- `encor.ip-sla.06` — Konfiguracja a uruchomienie (quiz, trudność 1; cel 4.4)

**encor.ip-sla.stage-2**

- `encor.ip-sla.07` — Timeout (quiz, trudność 2; cel 4.4)
- `encor.ip-sla.08` — Threshold (quiz, trudność 2; cel 4.4)
- `encor.ip-sla.09` — Uruchom teraz (CLI, trudność 2; cel 4.4)
- `encor.ip-sla.10` — Statystyki operacji (quiz, trudność 2; cel 4.4)
- `encor.ip-sla.11` — Jawne źródło (CLI, trudność 2; cel 4.4)
- `encor.ip-sla.12` — Pomiar nie jest aplikacją (quiz, trudność 2; cel 4.4)

**encor.ip-sla.stage-3**

- `encor.ip-sla.13` — Wynik Timeout (quiz, trudność 3; cel 4.4)
- `encor.ip-sla.14` — Źródło i routing powrotny (quiz, trudność 3; cel 4.4)
- `encor.ip-sla.15` — Kompletna sonda (CLI, trudność 3; cel 4.4)
- `encor.ip-sla.16` — Jedna próbka to za mało (quiz, trudność 3; cel 4.4)
- `encor.ip-sla.17` — Sonda z kontrolą źródła (CLI, trudność 3; cel 4.4)
- `encor.ip-sla.18` — Pomiar a failover (quiz, trudność 3; cel 4.4)

#### SPAN, RSPAN i ERSPAN — obserwacja ruchu

**encor.span.stage-1**

- `encor.span.01` — Zadanie SPAN (quiz, trudność 1; cel 4.3)
- `encor.span.02` — Źródło i cel (quiz, trudność 1; cel 4.3)
- `encor.span.03` — Sesja lokalna (CLI, trudność 1; cel 4.3)
- `encor.span.04` — Kierunek rx (quiz, trudność 1; cel 4.3)
- `encor.span.05` — Oba kierunki (CLI, trudność 1; cel 4.3)
- `encor.span.06` — Lokalność SPAN (quiz, trudność 1; cel 4.3)

**encor.span.stage-2**

- `encor.span.07` — RSPAN transport (quiz, trudność 2; cel 4.3)
- `encor.span.08` — ERSPAN transport (quiz, trudność 2; cel 4.3)
- `encor.span.09` — Lokalna para portów (CLI, trudność 2; cel 4.3)
- `encor.span.10` — Wydajność analizatora (quiz, trudność 2; cel 4.3)
- `encor.span.11` — Specjalny VLAN (CLI, trudność 2; cel 4.3)
- `encor.span.12` — Port analizatora (quiz, trudność 2; cel 4.3)

**encor.span.stage-3**

- `encor.span.13` — Brakuje jednej strony rozmowy (quiz, trudność 3; cel 4.3)
- `encor.span.14` — RSPAN przez trunk (quiz, trudność 3; cel 4.3)
- `encor.span.15` — Źródło RSPAN (CLI, trudność 3; cel 4.3)
- `encor.span.16` — ERSPAN nie jest VPN (quiz, trudność 3; cel 4.3)
- `encor.span.17` — Odbiornik RSPAN (CLI, trudność 3; cel 4.3)
- `encor.span.18` — Pusty przechwyt ERSPAN (quiz, trudność 3; cel 4.3)

#### EEM — automatyzacja zdarzeń i zbieranie danych

**encor.eem.stage-1**

- `encor.eem.01` — Zdarzenie i akcja (quiz, trudność 1; cel 6.6)
- `encor.eem.02` — Lokalna automatyzacja (quiz, trudność 1; cel 6.6)
- `encor.eem.03` — Nazwa appletu (CLI, trudność 1; cel 6.6)
- `encor.eem.04` — Ręczny start (quiz, trudność 1; cel 6.6)
- `encor.eem.05` — Komunikat w logach (CLI, trudność 1; cel 6.6)
- `encor.eem.06` — Reakcja na syslog (quiz, trudność 1; cel 6.6)

**encor.eem.stage-2**

- `encor.eem.07` — Timer watchdog (quiz, trudność 2; cel 6.6)
- `encor.eem.08` — Kolejność akcji (quiz, trudność 2; cel 6.6)
- `encor.eem.09` — Ręczny logger (CLI, trudność 2; cel 6.6)
- `encor.eem.10` — Akcja CLI (quiz, trudność 2; cel 6.6)
- `encor.eem.11` — Cykliczny znacznik (CLI, trudność 2; cel 6.6)
- `encor.eem.12` — Uprawnienia EEM (quiz, trudność 2; cel 6.6)

**encor.eem.stage-3**

- `encor.eem.13` — Ryzyko pętli syslog (quiz, trudność 3; cel 6.6)
- `encor.eem.14` — Idempotencja (quiz, trudność 3; cel 6.6)
- `encor.eem.15` — Ręczny odczyt stanu (CLI, trudność 3; cel 6.6)
- `encor.eem.16` — Nie każda reakcja to naprawa (quiz, trudność 3; cel 6.6)
- `encor.eem.17` — Cykliczny odczyt interfejsów (CLI, trudność 3; cel 6.6)
- `encor.eem.18` — Testowanie appletu (quiz, trudność 3; cel 6.6)


## Partia 0.10 — 72 nowe zadania

Cztery nowe działy po 18 zadań: Flexible NetFlow, NETCONF, RESTCONF i CoPP. Łącznie 48 quizów i 24 CLI. Podstawy konfiguracji i diagnostyki nie oznaczają pełnego pokrycia tych celów.

### Flexible NetFlow — rekord, monitor i eksport

**encor.netflow.stage-1**

- `encor.netflow.01` — Trzy elementy FNF (quiz, trudność 1; cel 4.2)
- `encor.netflow.02` — Pola kluczowe (quiz, trudność 1; cel 4.2)
- `encor.netflow.03` — Adres źródłowy w rekordzie (CLI, trudność 1; cel 4.2)
- `encor.netflow.04` — NetFlow a przechwytywanie (quiz, trudność 1; cel 4.2)
- `encor.netflow.05` — Adres kolektora (CLI, trudność 1; cel 4.2)
- `encor.netflow.06` — Powiązanie elementów (quiz, trudność 1; cel 4.2)

**encor.netflow.stage-2**

- `encor.netflow.07` — Kierunek obserwacji (quiz, trudność 2; cel 4.2)
- `encor.netflow.08` — Cache bez kolektora (quiz, trudność 2; cel 4.2)
- `encor.netflow.09` — Rekord i exporter (CLI, trudność 2; cel 4.2)
- `encor.netflow.10` — Dwa przepływy czy jeden (quiz, trudność 2; cel 4.2)
- `encor.netflow.11` — Port i wersja eksportu (CLI, trudność 2; cel 4.2)
- `encor.netflow.12` — Active timeout (quiz, trudność 2; cel 4.2)

**encor.netflow.stage-3**

- `encor.netflow.13` — Brak szablonu (quiz, trudność 3; cel 4.2)
- `encor.netflow.14` — Cache rośnie, eksport nie dociera (quiz, trudność 3; cel 4.2)
- `encor.netflow.15` — Przypięcie monitora (CLI, trudność 3; cel 4.2)
- `encor.netflow.16` — Sampling a dokładność (quiz, trudność 3; cel 4.2)
- `encor.netflow.17` — Rekord z licznikami (CLI, trudność 3; cel 4.2)
- `encor.netflow.18` — Dwa punkty obserwacji (quiz, trudność 3; cel 4.2)

### NETCONF — sesje, możliwości i operacje

**encor.netconf.stage-1**

- `encor.netconf.01` — Transport NETCONF (quiz, trudność 1; cel 4.6)
- `encor.netconf.02` — Model i protokół (quiz, trudność 1; cel 4.6)
- `encor.netconf.03` — Włączenie usługi (CLI, trudność 1; cel 4.6)
- `encor.netconf.04` — Kodowanie RPC (quiz, trudność 1; cel 4.6)
- `encor.netconf.05` — Powitanie serwera (quiz, trudność 1; cel 4.6)
- `encor.netconf.06` — Odczyt sesji (CLI, trudność 1; cel 4.6)

**encor.netconf.stage-2**

- `encor.netconf.07` — Get a get-config (quiz, trudność 2; cel 4.6)
- `encor.netconf.08` — Datastore running (quiz, trudność 2; cel 4.6)
- `encor.netconf.09` — ACL usługi NETCONF (CLI, trudność 2; cel 4.6)
- `encor.netconf.10` — Candidate nie jest pewne (quiz, trudność 2; cel 4.6)
- `encor.netconf.11` — Lock (quiz, trudność 2; cel 4.6)
- `encor.netconf.12` — Zaufane źródło (CLI, trudność 2; cel 4.6)

**encor.netconf.stage-3**

- `encor.netconf.13` — Błąd RPC (quiz, trudność 3; cel 4.6)
- `encor.netconf.14` — Sesja CLI a NETCONF (quiz, trudność 3; cel 4.6)
- `encor.netconf.15` — Minimalny ograniczony dostęp (CLI, trudność 3; cel 4.6)
- `encor.netconf.16` — Niepewny wynik zapisu (quiz, trudność 3; cel 4.6)
- `encor.netconf.17` — Dwie dozwolone stacje (CLI, trudność 3; cel 4.6)
- `encor.netconf.18` — Bezpieczne zakończenie (quiz, trudność 3; cel 4.6)

### RESTCONF — HTTP, modele i diagnostyka API

**encor.restconf.stage-1**

- `encor.restconf.01` — Transport RESTCONF (quiz, trudność 1; cel 4.6)
- `encor.restconf.02` — Metoda odczytu (quiz, trudność 1; cel 4.6)
- `encor.restconf.03` — Włącz RESTCONF (CLI, trudność 1; cel 4.6)
- `encor.restconf.04` — YANG w RESTCONF (quiz, trudność 1; cel 4.6)
- `encor.restconf.05` — Serwer HTTPS (CLI, trudność 1; cel 4.6)
- `encor.restconf.06` — Kodowanie danych (quiz, trudność 1; cel 4.6)

**encor.restconf.stage-2**

- `encor.restconf.07` — Accept (quiz, trudność 2; cel 6.5)
- `encor.restconf.08` — Content-Type (quiz, trudność 2; cel 6.5)
- `encor.restconf.09` — Dwie usługi (CLI, trudność 2; cel 4.6)
- `encor.restconf.10` — PUT i PATCH (quiz, trudność 2; cel 6.5)
- `encor.restconf.11` — Odpowiedź 204 (quiz, trudność 2; cel 6.5)
- `encor.restconf.12` — ACL RESTCONF (CLI, trudność 2; cel 4.6)

**encor.restconf.stage-3**

- `encor.restconf.13` — 401 Unauthorized (quiz, trudność 3; cel 6.5)
- `encor.restconf.14` — 404 Not Found (quiz, trudność 3; cel 6.5)
- `encor.restconf.15` — Dostęp jednej stacji API (CLI, trudność 3; cel 4.6)
- `encor.restconf.16` — Nieprawidłowy JSON (quiz, trudność 3; cel 6.2)
- `encor.restconf.17` — HTTPS z lokalnym uwierzytelnianiem (CLI, trudność 3; cel 4.6)
- `encor.restconf.18` — TLS i zaufanie (quiz, trudność 3; cel 5.3)

### CoPP — ochrona CPU i diagnostyka SNMP

**encor.copp.stage-1**

- `encor.copp.01` — Cel ochrony (quiz, trudność 1; cel 5.2.b)
- `encor.copp.02` — Ruch do routera (quiz, trudność 1; cel 5.2.b)
- `encor.copp.03` — Klasa CoPP (CLI, trudność 1; cel 5.2.b)
- `encor.copp.04` — ACL klasyfikująca (quiz, trudność 1; cel 5.2.b)
- `encor.copp.05` — Przypięcie do control plane (CLI, trudność 1; cel 5.2.b)
- `encor.copp.06` — Odczyt liczników (quiz, trudność 1; cel 5.2.b)

**encor.copp.stage-2**

- `encor.copp.07` — Policer odrzucający wszystko (quiz, trudność 2; cel 5.2.b)
- `encor.copp.08` — SNMP agent odpowiada lokalnie (quiz, trudność 2; cel 5.2.b)
- `encor.copp.09` — Limit z dopuszczeniem (CLI, trudność 2; cel 5.2.b)
- `encor.copp.10` — Właściwe źródło SNMP (quiz, trudność 2; cel 5.2.b)
- `encor.copp.11` — Para class-map i policy-map (CLI, trudność 2; cel 5.2.b)
- `encor.copp.12` — Bps a pps (quiz, trudność 2; cel 5.2.b)

**encor.copp.stage-3**

- `encor.copp.13` — Dwie klasy SNMP (quiz, trudność 3; cel 5.2.b)
- `encor.copp.14` — Nie wyłączaj ochrony w ciemno (quiz, trudność 3; cel 5.2.b)
- `encor.copp.15` — Spójny łańcuch CoPP (CLI, trudność 3; cel 5.2.b)
- `encor.copp.16` — Burst i okresowe odpytywanie (quiz, trudność 3; cel 5.2.b)
- `encor.copp.17` — Reguła zaufanego SNMP (CLI, trudność 3; cel 5.2.b)
- `encor.copp.18` — Różnice platform (quiz, trudność 3; cel 5.2.b)


## Partia 0.11 — multicast i architektury

54 nowe quizy; treści koncepcyjne i diagnostyczne. Każdy nowy dział ma trzy stopnie po sześć zadań.

### Multicast — RPF, PIM, IGMP i SSM

**encor.multicast.stage-1**

- `encor.multicast.01` — Członkostwo hosta (quiz, trudność 1; cel 3.3.d)
- `encor.multicast.02` — Rola PIM (quiz, trudność 1; cel 3.3.d)
- `encor.multicast.03` — Drzewo współdzielone (quiz, trudność 1; cel 3.3.d)
- `encor.multicast.04` — Kanał źródło–grupa (quiz, trudność 1; cel 3.3.d)
- `encor.multicast.05` — Rendezvous Point (quiz, trudność 1; cel 3.3.d)
- `encor.multicast.06` — IGMPv3 (quiz, trudność 1; cel 3.3.d)

**encor.multicast.stage-2**

- `encor.multicast.07` — Kontrola RPF (quiz, trudność 2; cel 3.3.d)
- `encor.multicast.08` — RPF w przykładzie (quiz, trudność 2; cel 3.3.d)
- `encor.multicast.09` — SSM i RP (quiz, trudność 2; cel 3.3.d)
- `encor.multicast.10` — Zakres SSM IPv4 (quiz, trudność 2; cel 3.3.d)
- `encor.multicast.11` — IGMP a snooping (quiz, trudność 2; cel 3.3.d)
- `encor.multicast.12` — Przełączenie na SPT (quiz, trudność 2; cel 3.3.d)

**encor.multicast.stage-3**

- `encor.multicast.13` — Dwa źródła, jedna grupa (quiz, trudność 3; cel 3.3.d)
- `encor.multicast.14` — Brak zainteresowanych interfejsów (quiz, trudność 3; cel 3.3.d)
- `encor.multicast.15` — Rola MSDP (quiz, trudność 3; cel 3.3.d)
- `encor.multicast.16` — Bidir-PIM (quiz, trudność 3; cel 3.3.d)
- `encor.multicast.17` — IGMPv2 w sieci SSM (quiz, trudność 3; cel 3.3.d)
- `encor.multicast.18` — RPF a odbiorca (quiz, trudność 3; cel 3.3.d)

### SD-WAN — płaszczyzny, OMP i jakość łączy

**encor.sdwan.stage-1**

- `encor.sdwan.01` — Płaszczyzna zarządzania (quiz, trudność 1; cel 1.2)
- `encor.sdwan.02` — Płaszczyzna sterowania (quiz, trudność 1; cel 1.2)
- `encor.sdwan.03` — Rola Validator (quiz, trudność 1; cel 1.2)
- `encor.sdwan.04` — Gdzie płyną dane (quiz, trudność 1; cel 1.2)
- `encor.sdwan.05` — Protokół OMP (quiz, trudność 1; cel 1.2)
- `encor.sdwan.06` — Underlay SD-WAN (quiz, trudność 1; cel 1.2)

**encor.sdwan.stage-2**

- `encor.sdwan.07` — TLOC (quiz, trudność 2; cel 1.2)
- `encor.sdwan.08` — Znaczenie color (quiz, trudność 2; cel 1.2)
- `encor.sdwan.09` — Monitorowanie tuneli (quiz, trudność 2; cel 1.2)
- `encor.sdwan.10` — Application-aware routing (quiz, trudność 2; cel 1.2)
- `encor.sdwan.11` — Łącze up, SLA niespełnione (quiz, trudność 2; cel 1.2)
- `encor.sdwan.12` — Segmentacja VPN (quiz, trudność 2; cel 1.2)

**encor.sdwan.stage-3**

- `encor.sdwan.13` — Wybór ścieżki według progów (quiz, trudność 3; cel 1.2)
- `encor.sdwan.14` — Brak ścieżki zgodnej z SLA (quiz, trudność 3; cel 1.2)
- `encor.sdwan.15` — Control up, data down (quiz, trudność 3; cel 1.2)
- `encor.sdwan.16` — Manager chwilowo niedostępny (quiz, trudność 3; cel 1.2)
- `encor.sdwan.17` — Certyfikaty i czas (quiz, trudność 3; cel 1.2)
- `encor.sdwan.18` — Dwa łącza, wspólna awaria (quiz, trudność 3; cel 1.2)

### SD-Access — fabric, segmentacja i dostęp zewnętrzny

**encor.sdaccess.stage-1**

- `encor.sdaccess.01` — Płaszczyzna sterowania fabric (quiz, trudność 1; cel 1.3)
- `encor.sdaccess.02` — Płaszczyzna danych fabric (quiz, trudność 1; cel 1.3)
- `encor.sdaccess.03` — Płaszczyzna polityk (quiz, trudność 1; cel 1.3)
- `encor.sdaccess.04` — Zarządzanie fabric (quiz, trudność 1; cel 1.3)
- `encor.sdaccess.05` — Fabric edge (quiz, trudność 1; cel 1.3)
- `encor.sdaccess.06` — Fabric border (quiz, trudność 1; cel 1.3)

**encor.sdaccess.stage-2**

- `encor.sdaccess.07` — Control plane node (quiz, trudność 2; cel 1.3)
- `encor.sdaccess.08` — Intermediate node (quiz, trudność 2; cel 1.3)
- `encor.sdaccess.09` — Makrosegmentacja (quiz, trudność 2; cel 1.3)
- `encor.sdaccess.10` — Mikrosegmentacja (quiz, trudność 2; cel 1.3)
- `encor.sdaccess.11` — Rola ISE (quiz, trudność 2; cel 1.3)
- `encor.sdaccess.12` — Anycast gateway (quiz, trudność 2; cel 1.3)

**encor.sdaccess.stage-3**

- `encor.sdaccess.13` — Ruch wewnętrzny działa, zewnętrzny nie (quiz, trudność 3; cel 1.3)
- `encor.sdaccess.14` — Małe pakiety działają (quiz, trudność 3; cel 1.3)
- `encor.sdaccess.15` — Przeniesienie endpointu (quiz, trudność 3; cel 1.3)
- `encor.sdaccess.16` — SGT nie jest szyfrowaniem (quiz, trudność 3; cel 1.3)
- `encor.sdaccess.17` — Integracja z tradycyjną siecią (quiz, trudność 3; cel 1.3)
- `encor.sdaccess.18` — Łączenie ról (quiz, trudność 3; cel 1.3)


Szczegółowa mapa szerokości pokrycia: ENCOR-COVERAGE-AUDIT.md.

## Partia 0.12 — automatyzacja

### Python — odczyt skryptów sieciowych

**encor.python.stage-1**

- `encor.python.01` — Indeks listy (quiz, trudność 1; cel 6.1)
- `encor.python.02` — Wartość słownika (quiz, trudność 1; cel 6.1)
- `encor.python.03` — Liczba elementów (quiz, trudność 1; cel 6.1)
- `encor.python.04` — Porównanie stanu (quiz, trudność 1; cel 6.1)
- `encor.python.05` — Konwersja liczby (quiz, trudność 1; cel 6.1)
- `encor.python.06` — Budowanie komendy (quiz, trudność 1; cel 6.1)

**encor.python.stage-2**

- `encor.python.07` — Filtrowanie interfejsów (quiz, trudność 2; cel 6.1)
- `encor.python.08` — Wartość domyślna (quiz, trudność 2; cel 6.1)
- `encor.python.09` — Górna granica range (quiz, trudność 2; cel 6.1)
- `encor.python.10` — Split pól (quiz, trudność 2; cel 6.1)
- `encor.python.11` — Normalizacja tekstu (quiz, trudność 2; cel 6.1)
- `encor.python.12` — Gałąź else (quiz, trudność 2; cel 6.1)

**encor.python.stage-3**

- `encor.python.13` — Zagnieżdżone dane API (quiz, trudność 3; cel 6.1)
- `encor.python.14` — Warunki łączne (quiz, trudność 3; cel 6.1)
- `encor.python.15` — Append zmienia listę (quiz, trudność 3; cel 6.1)
- `encor.python.16` — Obsługa wyjątku (quiz, trudność 3; cel 6.1)
- `encor.python.17` — Zwracana wartość (quiz, trudność 3; cel 6.1)
- `encor.python.18` — Break kończy pętlę (quiz, trudność 3; cel 6.1)

### JSON — poprawny zapis i struktury danych

**encor.json.stage-1**

- `encor.json.01` — Cudzysłowy JSON (quiz, trudność 1; cel 6.2)
- `encor.json.02` — Wartość logiczna JSON (quiz, trudność 1; cel 6.2)
- `encor.json.03` — Liczba zamiast napisu (quiz, trudność 1; cel 6.2)
- `encor.json.04` — Brak wartości (quiz, trudność 1; cel 6.2)
- `encor.json.05` — Tablica VLAN-ów (quiz, trudność 1; cel 6.2)
- `encor.json.06` — Rozdzielenie pól (quiz, trudność 1; cel 6.2)

**encor.json.stage-2**

- `encor.json.07` — Obiekt zagnieżdżony (quiz, trudność 2; cel 6.2)
- `encor.json.08` — Lista obiektów (quiz, trudność 2; cel 6.2)
- `encor.json.09` — Kolejność w tablicy (quiz, trudność 2; cel 6.2)
- `encor.json.10` — Kolejność kluczy obiektu (quiz, trudność 2; cel 6.2)
- `encor.json.11` — Pusta lista a null (quiz, trudność 2; cel 6.2)
- `encor.json.12` — Escaping cytatu (quiz, trudność 2; cel 6.2)

**encor.json.stage-3**

- `encor.json.13` — JSON a schemat (quiz, trudność 3; cel 6.2)
- `encor.json.14` — Duplikaty nazw (quiz, trudność 3; cel 6.2)
- `encor.json.15` — Minimalny payload interfejsu (quiz, trudność 3; cel 6.2)
- `encor.json.16` — Błąd parsowania (quiz, trudność 3; cel 6.2)
- `encor.json.17` — Dwa poprawne typy (quiz, trudność 3; cel 6.2)
- `encor.json.18` — Komentarze (quiz, trudność 3; cel 6.2)

### YANG — model danych i walidacja

**encor.yang.stage-1**

- `encor.yang.01` — Model danych (quiz, trudność 1; cel 6.3)
- `encor.yang.02` — Model a instancja (quiz, trudność 1; cel 6.3)
- `encor.yang.03` — Leaf (quiz, trudność 1; cel 6.3)
- `encor.yang.04` — Container (quiz, trudność 1; cel 6.3)
- `encor.yang.05` — List (quiz, trudność 1; cel 6.3)
- `encor.yang.06` — Leaf-list (quiz, trudność 1; cel 6.3)

**encor.yang.stage-2**

- `encor.yang.07` — Klucz listy (quiz, trudność 2; cel 6.3)
- `encor.yang.08` — Boolean (quiz, trudność 2; cel 6.3)
- `encor.yang.09` — Config false (quiz, trudność 2; cel 6.3)
- `encor.yang.10` — Namespace (quiz, trudność 2; cel 6.3)
- `encor.yang.11` — Ograniczenie zakresu (quiz, trudność 2; cel 6.3)
- `encor.yang.12` — Enumeration (quiz, trudność 2; cel 6.3)

**encor.yang.stage-3**

- `encor.yang.13` — Model standardowy a natywny (quiz, trudność 3; cel 6.3)
- `encor.yang.14` — Rewizja modułu (quiz, trudność 3; cel 6.3)
- `encor.yang.15` — Walidacja relacji (quiz, trudność 3; cel 6.3)
- `encor.yang.16` — Leafref (quiz, trudność 3; cel 6.3)
- `encor.yang.17` — Lista nie jest zawsze uporządkowana przez użytkownika (quiz, trudność 3; cel 6.3)
- `encor.yang.18` — Granica modelu i protokołu (quiz, trudność 3; cel 6.3)

### Automatyzacja — agent, agentless i kontrola zmian

**encor.orchestration.stage-1**

- `encor.orchestration.01` — Agent na celu (quiz, trudność 1; cel 6.7)
- `encor.orchestration.02` — Agentless (quiz, trudność 1; cel 6.7)
- `encor.orchestration.03` — Przykłady architektur (quiz, trudność 1; cel 6.7)
- `encor.orchestration.04` — Rola inventory (quiz, trudność 1; cel 6.7)
- `encor.orchestration.05` — Playbook (quiz, trudność 1; cel 6.7)
- `encor.orchestration.06` — Transport agentless (quiz, trudność 1; cel 6.7)

**encor.orchestration.stage-2**

- `encor.orchestration.07` — Push i pull (quiz, trudność 2; cel 6.7)
- `encor.orchestration.08` — Stan deklaratywny (quiz, trudność 2; cel 6.7)
- `encor.orchestration.09` — Idempotencja zadania (quiz, trudność 2; cel 6.7)
- `encor.orchestration.10` — Configuration drift (quiz, trudność 2; cel 6.7)
- `encor.orchestration.11` — Koszt modelu agentowego (quiz, trudność 2; cel 6.7)
- `encor.orchestration.12` — Sieć bez możliwości instalacji (quiz, trudność 2; cel 6.7)

**encor.orchestration.stage-3**

- `encor.orchestration.13` — Agent na serwerze proxy (quiz, trudność 3; cel 6.7)
- `encor.orchestration.14` — Tryb check (quiz, trudność 3; cel 6.7)
- `encor.orchestration.15` — Zakres błędu (quiz, trudność 3; cel 6.7)
- `encor.orchestration.16` — Częściowy sukces (quiz, trudność 3; cel 6.7)
- `encor.orchestration.17` — Sekrety automatyzacji (quiz, trudność 3; cel 6.7)
- `encor.orchestration.18` — Weryfikacja zamiaru (quiz, trudność 3; cel 6.7)


## Partia 0.13 — FHRP, czas i PBR

### HSRP i VRRP — wybór bramy i awarie

**encor.fhrp.stage-1**

- `encor.fhrp.01` — Adres bramy hosta (quiz, trudność 1; cel 3.3.c)
- `encor.fhrp.02` — Rola FHRP (quiz, trudność 1; cel 3.3.c)
- `encor.fhrp.03` — Wirtualny adres HSRP (CLI, trudność 1; cel 3.3.c)
- `encor.fhrp.04` — Domyślny priorytet (quiz, trudność 1; cel 3.3.c)
- `encor.fhrp.05` — Wyższy priorytet (CLI, trudność 1; cel 3.3.c)
- `encor.fhrp.06` — Preempt HSRP (quiz, trudność 1; cel 3.3.c)

**encor.fhrp.stage-2**

- `encor.fhrp.07` — Awaria Active bez preempt (quiz, trudność 2; cel 3.3.c)
- `encor.fhrp.08` — Uplink padł, LAN działa (quiz, trudność 2; cel 3.3.c)
- `encor.fhrp.09` — Tracking z dekrementem (CLI, trudność 2; cel 3.3.c)
- `encor.fhrp.10` — Obliczenie skutecznego priorytetu (quiz, trudność 2; cel 3.3.c)
- `encor.fhrp.11` — VRRP IPv4 — klasyczna składnia (CLI, trudność 2; cel 3.3.c)
- `encor.fhrp.12` — Właściciel adresu VRRP (quiz, trudność 2; cel 3.3.c)

**encor.fhrp.stage-3**

- `encor.fhrp.13` — Za mały decrement (quiz, trudność 3; cel 3.3.c)
- `encor.fhrp.14` — Dwie grupy, dwa aktywne routery (quiz, trudność 3; cel 3.3.c)
- `encor.fhrp.15` — Pełny wybór preferowanej bramy (CLI, trudność 3; cel 3.3.c)
- `encor.fhrp.16` — Oba routery zgłaszają Active (quiz, trudność 3; cel 3.3.c)
- `encor.fhrp.17` — VRRP z kontrolą preferencji (CLI, trudność 3; cel 3.3.c)
- `encor.fhrp.18` — Próg i opóźnienie powrotu (quiz, trudność 3; cel 3.3.c)

### NTP i PTP — interpretacja synchronizacji

**encor.time-sync.stage-1**

- `encor.time-sync.01` — Cel NTP (quiz, trudność 1; cel 3.3.a)
- `encor.time-sync.02` — Transport NTP (quiz, trudność 1; cel 3.3.a)
- `encor.time-sync.03` — Znaczenie stratum (quiz, trudność 1; cel 3.3.a)
- `encor.time-sync.04` — Brak synchronizacji (quiz, trudność 1; cel 3.3.a)
- `encor.time-sync.05` — Odczyt ntp server (quiz, trudność 1; cel 3.3.a)
- `encor.time-sync.06` — Strefa czasowa (quiz, trudność 1; cel 3.3.a)

**encor.time-sync.stage-2**

- `encor.time-sync.07` — Wybrane źródło (quiz, trudność 2; cel 3.3.a)
- `encor.time-sync.08` — Reach 377 (quiz, trudność 2; cel 3.3.a)
- `encor.time-sync.09` — Reach 0 (quiz, trudność 2; cel 3.3.a)
- `encor.time-sync.10` — Jawne źródło NTP (quiz, trudność 2; cel 3.3.a)
- `encor.time-sync.11` — Lokalny master (quiz, trudność 2; cel 3.3.a)
- `encor.time-sync.12` — Prefer nie naprawia źródła (quiz, trudność 2; cel 3.3.a)

**encor.time-sync.stage-3**

- `encor.time-sync.13` — PTP grandmaster (quiz, trudność 3; cel 3.3.a)
- `encor.time-sync.14` — Boundary clock (quiz, trudność 3; cel 3.3.a)
- `encor.time-sync.15` — Transparent clock (quiz, trudność 3; cel 3.3.a)
- `encor.time-sync.16` — Domena i profil PTP (quiz, trudność 3; cel 3.3.a)
- `encor.time-sync.17` — Asymetria ścieżki (quiz, trudność 3; cel 3.3.a)
- `encor.time-sync.18` — Nie gwarantuj precyzji z nazwy (quiz, trudność 3; cel 3.3.a)

### PBR — interpretacja polityk routingu

**encor.pbr.stage-1**

- `encor.pbr.01` — Cel PBR (quiz, trudność 1; cel 3.2.d)
- `encor.pbr.02` — Route-map jako polityka (quiz, trudność 1; cel 3.2.d)
- `encor.pbr.03` — Punkt zastosowania (quiz, trudność 1; cel 3.2.d)
- `encor.pbr.04` — Next hop w PBR (quiz, trudność 1; cel 3.2.d)
- `encor.pbr.05` — ACL w match (quiz, trudność 1; cel 3.2.d)
- `encor.pbr.06` — Brak dopasowania (quiz, trudność 1; cel 3.2.d)

**encor.pbr.stage-2**

- `encor.pbr.07` — Route-map deny (quiz, trudność 2; cel 3.2.d)
- `encor.pbr.08` — Wybór według źródła (quiz, trudność 2; cel 3.2.d)
- `encor.pbr.09` — Dwie sekwencje (quiz, trudność 2; cel 3.2.d)
- `encor.pbr.10` — Set next-hop a default next-hop (quiz, trudność 2; cel 3.2.d)
- `encor.pbr.11` — Polityka dla ruchu lokalnego (quiz, trudność 2; cel 3.2.d)
- `encor.pbr.12` — Polityka istnieje bez przypięcia (quiz, trudność 2; cel 3.2.d)

**encor.pbr.stage-3**

- `encor.pbr.13` — Awaria za next hopem (quiz, trudność 3; cel 3.2.d)
- `encor.pbr.14` — Ruch powrotny (quiz, trudność 3; cel 3.2.d)
- `encor.pbr.15` — Analiza konkretnego pakietu (quiz, trudność 3; cel 3.2.d)
- `encor.pbr.16` — Pakiet spoza polityki (quiz, trudność 3; cel 3.2.d)
- `encor.pbr.17` — Weryfikacja działania (quiz, trudność 3; cel 3.2.d)
- `encor.pbr.18` — Granice prostego PBR (quiz, trudność 3; cel 3.2.d)

