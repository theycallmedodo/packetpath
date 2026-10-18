# Plan rozbudowy treści po 0.13

Stan dostarczony: 576 zadań CCNA, 432 ENCOR i 0 ENARSI. Cel roboczy: 2160 zadań autorskich. Liczby poniżej są budżetem pracy, nie deklaracją pełnego pokrycia ani procentem gotowości do egzaminu.

| Ścieżka | Stan | Cel roboczy | Pozostało |
|---|---:|---:|---:|
| CCNA | 576 | 1080 | 504 |
| ENCOR | 432 | 648 | 216 |
| ENARSI | 0 | 432 | 432 |
| Razem | 1008 | 2160 | 1152 |

Kolejne partie powinny mieć 144–216 zadań, zależnie od możliwości rzetelnego przeglądu, i łączyć nowe tematy z pogłębianiem istniejących. Nie zwiększamy licznika samą podmianą adresów w jednym szablonie.

1. CCNA: Ethernet/ARP/MAC, TCP/UDP, DNS, architektury, okablowanie, diagnostyka fizyczna; rozbudowa IPv6, STP, EtherChannel, NAT i routingu statycznego.
2. CCNA: zaawansowane scenariusze WLAN, bezpieczeństwo i AAA, kontrolery/SDN, Ansible/Terraform, AI w operacjach. Interfejs GUI WLAN wymaga osobnego typu ćwiczenia lub dobrze opisanych scenariuszy.
3. ENCOR v1.2: rozbudować pierwsze 180 zadań; kolejne priorytety to Flexible NetFlow, NETCONF/RESTCONF, security/CoPP, architektury SD-WAN/SDA, multicast, FHRP oraz Python/JSON/YANG. Uzupełnić pełniejsze scenariusze IPsec i ERSPAN.
4. ENARSI: odrębna mapa aktualnego blueprintu; nacisk na rozpoznawanie przyczyn, redystrybucję, filtrację, PBR, VPN i diagnostykę usług.

Dla każdej partii: źródła pierwotne, jawne założenia platformy, cztery sensowne opcje, kontrola braku wieloznaczności, niezależne sprawdzenie obliczeń, przegląd kluczy i scenariuszy. Kontrole strukturalne nie zastępują labu IOS. Należy prowadzić jawny rejestr walidacji laboratoryjnej przed oznaczeniem treści jako przetestowanej na urządzeniu.

Partia 0.8 dostarczyła podstawy Ethernet/ARP/MAC, TCP/UDP, DNS, AAA oraz rozszerzenia IPv6, STP, EtherChannel i NAT. Lista tematów powyżej pozostaje planem dalszego pogłębiania, nie stwierdzeniem braku jakichkolwiek zadań z tych zakresów.

Partia 0.9 dodała 180 ENCOR: 10 działów po 18 zadań. EIGRP jest porównaniem koncepcji zgodnym z 3.2.a; redystrybucja i zaawansowane scenariusze routingu pozostają przede wszystkim planem ENARSI.

Partia 0.10 dodała 72 zadania: Flexible NetFlow, NETCONF, RESTCONF i CoPP. Tematy te wymagają dalszego pogłębiania; kolejne nowe obszary: architektury, multicast oraz Python/JSON/YANG.

Partia 0.11 dodała podstawy i scenariusze multicast, SD-WAN i SD-Access (54 quizy). Następne luki: Python/JSON/YANG, FHRP na poziomie ENCOR, NTP/PTP, pełniejsze security i konfiguracje IPsec; dotychczasowe działy wymagają dalszego pogłębiania.

Partia 0.12 dodała Python/JSON/YANG i agent/agentless (72 quizy). Audyt 47 końcowych celów znajduje się w ENCOR-COVERAGE-AUDIT.md. Największe pozostałe luki: security, infrastruktura L2, PBR, NTP/PTP i API kontrolerów.

Partia 0.13 dodała HSRP/VRRP, NTP/PTP i PBR (54 zadania). Aktualne priorytety następnej sesji zawiera NEXT-SESSION.md. Wcześniejsze listy luk opisują stan na moment danej partii.
