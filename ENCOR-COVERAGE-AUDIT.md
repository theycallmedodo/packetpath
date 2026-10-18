# Audyt zakresu ENCOR — PacketPath 0.13

Źródło zakresu: [Cisco ENCOR 350-401 v1.2](https://learningcontent.cisco.com/documents/marketing/exam-topics/350-401-ENCORE-v1.2.pdf). Audyt własny, nie ocena Cisco.

## Wynik i jego znaczenie

**Przed partią 0.13: 28/47 = 59,6% końcowych podpunktów rozpoczętych. Po tej partii: 31/47 = 66,0%.**

Liczymy końcowe podpunkty (np. 1.2.a i 1.2.b zamiast dodatkowego liczenia ich rodzica 1.2), po jednym punkcie za każdy. To nieważony wskaźnik szerokości biblioteki. Nie stosujemy wag egzaminacyjnych do liczby pytań. Podpunkty nie mają równych rozmiarów ani trudności.

Status „rozpoczęty” wymaga zadania przypisanego do celu lub ręcznie przypisanego podcelu wewnątrz oznaczonego celu nadrzędnego. Samo pojawienie się nazwy technologii w innym pytaniu nie wystarcza. Liczymy wyłącznie kampanię ENCOR; materiał CCNA może pomagać, ale nie zwiększa tu licznika.

**Nie mamy rzetelnego procentu tematów wyczerpanych.** Nie przeprowadzono całościowego audytu głębokości, wymaganych wariantów i labów. Nie nazywamy 66,0% pełnym pokryciem ani gotowością do egzaminu.

## Gdzie wskaźnik jest optymistyczny

- 2.2.b: dużo podstaw GRE, tylko koncepcja IPsec; brak kompletnego labu IPsec.
- 4.3: konfiguracja SPAN/RSPAN, lecz ERSPAN głównie opisowo.
- 4.4: nacisk na ICMP Echo, nie wszystkie operacje SLA.
- 5.3: na razie wąski fragment dotyczący TLS i zaufania certyfikatu.
- 6.2: przed 0.12 jedno pytanie o błędny boolean. Teraz 18 dodatkowych zadań, ale wybór poprawnego JSON nadal nie zastępuje samodzielnego pisania plików.
- 6.5: RESTCONF; brakuje równoważnego pokrycia odpowiedzi Catalyst Center.
- Wiele celów konfiguracji ma poprawne klucze i scenariusze, lecz nie zostało wykonanych na IOS.

## Mapa celów

| Cel | Obszar (skrót redakcyjny) | Status | Moduł / zadanie ENCOR |
|---|---|---|---|
| 1.1.a | Projekt kampusu/chmury | Brak dedykowanego pokrycia | — |
| 1.1.b | Odporność i SSO | Brak dedykowanego pokrycia | — |
| 1.2.a | Płaszczyzny SD-WAN | Rozpoczęty — częściowy | sdwan |
| 1.2.b | Zalety/ograniczenia SD-WAN | Rozpoczęty — częściowy | sdwan |
| 1.3.a | Płaszczyzny SD-Access | Rozpoczęty — częściowy | sdaccess |
| 1.3.b | Integracja tradycyjnego kampusu | Rozpoczęty — częściowy | sdaccess |
| 1.4 | Interpretacja QoS | Rozpoczęty — częściowy | qos-interpret |
| 2.1.a | Hypervisory | Rozpoczęty — częściowy | virtualization |
| 2.1.b | Maszyny wirtualne | Rozpoczęty — częściowy | virtualization |
| 2.1.c | Wirtualne przełączanie | Rozpoczęty — częściowy | virtualization |
| 2.2.a | VRF | Rozpoczęty — częściowy | vrf |
| 2.2.b | GRE/IPsec | Rozpoczęty — częściowy | gre |
| 2.3.a | LISP | Rozpoczęty — częściowy | virtualization |
| 2.3.b | VXLAN | Rozpoczęty — częściowy | virtualization |
| 3.1.a | Diagnostyka trunków | Brak dedykowanego pokrycia | — |
| 3.1.b | Diagnostyka EtherChannel | Brak dedykowanego pokrycia | — |
| 3.1.c | RSTP/MST i ochrona | Brak dedykowanego pokrycia | — |
| 3.2.a | EIGRP/OSPF porównanie | Rozpoczęty — częściowy | routing-compare |
| 3.2.b | OSPFv2/v3 | Rozpoczęty — częściowy | ospf-multi |
| 3.2.c | Bezpośredni eBGP | Rozpoczęty — częściowy | ebgp |
| 3.2.d | PBR | Rozpoczęty — częściowy | pbr |
| 3.3.a | NTP/PTP | Rozpoczęty — częściowy | time-sync |
| 3.3.b | NAT/PAT | Brak dedykowanego pokrycia | — |
| 3.3.c | HSRP/VRRP | Rozpoczęty — częściowy | fhrp |
| 3.3.d | Multicast | Rozpoczęty — częściowy | multicast |
| 4.1 | Narzędzia diagnozy | Brak dedykowanego pokrycia | — |
| 4.2 | Flexible NetFlow | Rozpoczęty — częściowy | netflow |
| 4.3 | SPAN/RSPAN/ERSPAN | Rozpoczęty — częściowy | span |
| 4.4 | IP SLA | Rozpoczęty — częściowy | ip-sla |
| 4.5 | Catalyst Center workflows | Brak dedykowanego pokrycia | — |
| 4.6 | NETCONF/RESTCONF | Rozpoczęty — częściowy | netconf, restconf |
| 5.1.a | Dostęp lokalny/linie | Brak dedykowanego pokrycia | — |
| 5.1.b | AAA | Brak dedykowanego pokrycia | — |
| 5.2.a | ACL | Brak dedykowanego pokrycia | — |
| 5.2.b | CoPP | Rozpoczęty — częściowy | copp |
| 5.3 | Ochrona REST API | Rozpoczęty — częściowy | restconf.18 |
| 5.4.a | Threat defense | Brak dedykowanego pokrycia | — |
| 5.4.b | Endpoint security | Brak dedykowanego pokrycia | — |
| 5.4.c | NGFW | Brak dedykowanego pokrycia | — |
| 5.4.d | TrustSec/MACsec | Brak dedykowanego pokrycia | — |
| 6.1 | Python | Rozpoczęty — częściowy | python |
| 6.2 | JSON | Rozpoczęty — częściowy | json, restconf.16 |
| 6.3 | YANG | Rozpoczęty — częściowy | yang |
| 6.4 | API kontrolerów | Brak dedykowanego pokrycia | — |
| 6.5 | Odpowiedzi REST | Rozpoczęty — częściowy | restconf |
| 6.6 | EEM | Rozpoczęty — częściowy | eem |
| 6.7 | Agent/agentless | Rozpoczęty — częściowy | orchestration |

## Podział na domeny

| Domena | Rozpoczęte / wszystkie podpunkty |
|---|---:|
| Architektura | 5/7 |
| Wirtualizacja | 7/7 |
| Infrastruktura | 7/11 |
| Assurance | 4/6 |
| Security | 2/9 |
| Automatyzacja | 6/7 |

7/7 w wirtualizacji oznacza rozpoczęcie każdego podpunktu, nie ich wyczerpanie. Największe luki: security, L2 na poziomie ENCOR, NAT/PAT w tej kampanii, API kontrolerów i Catalyst Center.

## Licznik treści a zakres

432/648 = 66,7% roboczego budżetu zadań ENCOR. Liczba 648 jest naszym planem autorskim, a nie mianownikiem blueprintu. Nie należy utożsamiać tego wyniku z 66,0% rozpoczętych podpunktów.

W 0.13 przybyły trzy rozpoczęte cele. W FHRP potrzeba dalszych wariantów i weryfikacji laboratoryjnej; NTP/PTP oraz PBR mają po 18 zadań interpretacyjnych, nie pełne laboratoria.
