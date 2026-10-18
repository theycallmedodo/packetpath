"""Hand-authored release 0.12 content; run once against 0.11. YAML is authoritative."""
import json,re,copy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
cat=json.loads((ROOT/'content/catalog.yaml').read_text())
existing={m['id']:m for m in cat['courses'][-1]['modules']}
all_new=[]
def start(key,title,obj,urls,extend=False):
 global meta,tasks,cards
 meta=(key,title,obj,urls,extend);tasks=[];cards=[]
def base(title,prompt,explain,hint):
 key,title_m,obj,urls,ext=meta;n=len(tasks)+1
 tid=f'encor.{key}.'+('ext.' if ext else '')+f'{n:02}'
 d=([2,3,3] if ext else [1,2,3])[(n-1)//6]
 common=dict(id=tid,revision=1,title=title,skills=[f'{key}.'+re.sub(r'[^a-z0-9]+','-',title.lower()).strip('-')],sources=[dict(title='Dokumentacja Cisco — '+title_m,url=u) for u in urls])
 return dict(common,blueprint_refs=[dict(exam='350-401',version='1.2',objective=obj)],difficulty=d,prompt_md=prompt,hints=[hint or explain],explanation_md=explain,card_id=tid+'.theory')
def card(t,example):
 cards.append({k:t[k] for k in ['revision','title','skills','sources']}|dict(id=t['card_id'],front_md=t['title'],back_md=t['explanation_md'],example=example));tasks.append(t)
def q(title,prompt,answer,wrong,explain,hint=''):
 t=base(title,prompt,explain,hint);n=len(tasks);pos=(n*3+n//6)%4
 opts=[]
 for w in wrong:
  text,reason=w.split('|',1);opts.append(dict(text_md=text,feedback_md=reason))
 opts.insert(pos,dict(text_md=answer,feedback_md=explain));assert len(opts)==4
 for i,o in enumerate(opts):o['id']='ABCD'[i]
 t.update(type='single_choice',options=opts,correct_option_id='ABCD'[pos]);card(t,answer)
def c(title,prompt,template,values,explain,hint=''):
 t=base(title,prompt,explain,hint);blanks=[];example=template
 for i,v in enumerate(values):
  if isinstance(v,str):a=[v];typ='command'
  else:a,typ=v
  blanks.append(dict(id=f'b{i}',label=f'Luka {i+1}',answer_type=typ,accepted=a,width=min(56,max(6,len(a[0])+2)),common_errors={}))
  example=example.replace('{{b'+str(i)+'}}',a[0])
 t.update(type='cli_fill_blank',platform='Cisco IOS / IOS XE; zgodnie z założeniami zadania',template=template,blanks=blanks);card(t,example)
def end():
 key,title,obj,urls,ext=meta;assert len(tasks)==18,(key,len(tasks))
 module=existing.get('encor.'+key) if ext else dict(id='encor.'+key,title=title,description='Od pojęć do analizy i praktycznych scenariuszy.',stages=[])
 if not ext:
  assert module['id'] not in existing
  cat['courses'][-1]['modules'].append(module)
 start_order=len(module['stages'])
 for i in range(3):
  order=start_order+i+1;sid=f'encor.{key}.stage-{order}';path=f'content/encor/{key}/stage-{order}.yaml'
  p=ROOT/path;assert not p.exists(),path;p.parent.mkdir(parents=True,exist_ok=True)
  p.write_text(json.dumps(dict(schema_version=3,id=sid,revision=1,cards=cards[i*6:i*6+6],tasks=tasks[i*6:i*6+6]),ensure_ascii=False,indent=2)+'\n')
  module['stages'].append(dict(id=sid,title=(['Rozszerzenie — zależności','Rozszerzenie — konfiguracja','Rozszerzenie — diagnostyka'] if ext else ['Podstawy','Zastosowanie','Scenariusze'])[i],description='Sześć zadań z teorią i wyjaśnieniem odpowiedzi.',difficulty=tasks[i*6]['difficulty'],order=order,pack_url='/'+path.replace('.yaml','.json'),pack_revision=1,task_count=6,pass_percent=80,requires=[] if order==1 else [f'encor.{key}.stage-{order-1}']))
 all_new.extend(tasks)


def Q(title,prompt,options,explain):
 q(title,prompt,options[0],[x+'|'+explain for x in options[1:]],explain,'Przeanalizuj warunki scenariusza; odpowiedź dotyczy wyłącznie podanych założeń.')
def C(title,prompt,template,values,explain):
 c(title,prompt,template,values,explain,'Zwróć uwagę na tryb konfiguracji i parametry wymienione w poleceniu.')
def save():
 assert len(all_new)==72,len(all_new)
 cat['revision']+=1
 (ROOT/'content/catalog.yaml').write_text(json.dumps(cat,ensure_ascii=False,indent=2)+'\n')
 print('Added',len(all_new),'ENCOR tasks')
BASICS='https://developer.cisco.com/codeexchange/github/repo/CiscoDevNet/netprog_basics'
YANG='https://nso-docs.cisco.com/guides/development/introduction-to-automation/basic-automation-with-python'
ORCH='https://developer.cisco.com/docs/nx-os/configuration-management-and-automation-introduction/'
AGENT='https://developer.cisco.com/docs/nx-os/agent-based-management/'
ANS='https://www.cisco.com/c/en/us/solutions/collateral/data-center-virtualization/application-centric-infrastructure/dc-automation-red-hat-ansible-wp.html'
# Each Python result is written explicitly and independently checked after authoring.
def P(title,code,answer,wrong,explain):
 Q(title,'Jaki wynik wypisze Python 3?\n```python\n'+code+'\n```',[answer]+wrong,explain)
start('python','Python — odczyt skryptów sieciowych','6.1',[BASICS])
P('Indeks listy','ports = ["Gi0/0", "Gi0/1", "Gi0/2"]\nprint(ports[1])','Gi0/1',['Gi0/0','Gi0/2','1'],'Indeksowanie list zaczyna się od zera, więc indeks 1 wskazuje drugi element.')
P('Wartość słownika','device = {"name": "R1", "role": "edge"}\nprint(device["role"])','edge',['R1','role','name'],'Słownik odczytuje wartość przypisaną do klucza role, a nie pozycję elementu.')
P('Liczba elementów','vlans = [10, 20, 30]\nprint(len(vlans))','3',['30','2','60'],'Len zwraca liczbę elementów listy. Nie sumuje wartości VLAN-ów.')
P('Porównanie stanu','state = "up"\nprint(state == "up")','True',['False','up','1'],'Operator == porównuje wartości. Wynikiem jest wartość logiczna True.')
P('Konwersja liczby','vlan = "20"\nprint(int(vlan) + 1)','21',['201','20','TypeError'],'Int zamienia napis z liczbą na liczbę całkowitą, więc + wykonuje dodawanie.')
P('Budowanie komendy','vlan = 30\nprint(f"switchport access vlan {vlan}")','switchport access vlan 30',['switchport access vlan {vlan}','30','f switchport access vlan'],'F-string wstawia wartość zmiennej w miejsce wyrażenia w nawiasach klamrowych.')
P('Filtrowanie interfejsów','states = ["up", "down", "up"]\nprint(sum(1 for state in states if state == "up"))','2',['3','1','0'],'Generator dostarcza jedynkę dla każdego elementu up. Sum zlicza dwa takie stany.')
P('Wartość domyślna','device = {"name": "R1"}\nprint(device.get("role", "unknown"))','unknown',['None','R1','KeyError'],'Dict.get zwraca podany domyślny wynik, jeśli klucza nie ma. Bezpośrednie device["role"] zgłosiłoby KeyError.')
P('Górna granica range','print(list(range(1, 4)))','[1, 2, 3]',['[1, 2, 3, 4]','[0, 1, 2, 3]','[2, 3, 4]'],'Range obejmuje początek, lecz nie obejmuje końca. Tu generuje 1, 2 i 3.')
P('Split pól','line = "Gi0/0 up up"\nprint(line.split()[1])','up',['Gi0/0','[up, up]','0'],'Split bez argumentu rozdziela tekst według białych znaków. Drugi element ma indeks 1.')
P('Normalizacja tekstu','state = " UP \\n"\nprint(state.strip().lower())','up',['UP','True','down'],'Strip usuwa skrajne białe znaki, a lower zamienia litery na małe. Wartości wewnętrzne napisu nie są arbitralnie zmieniane.')
P('Gałąź else','loss = 2\nif loss <= 1:\n    print("OK")\nelse:\n    print("CHECK")','CHECK',['OK','2','OK CHECK'],'Warunek 2 <= 1 jest fałszywy. Wykonana zostaje gałąź else.')
P('Zagnieżdżone dane API','data = {"interfaces": [{"name": "Gi0/0", "mtu": 1500}, {"name": "Gi0/1", "mtu": 9000}]}\nprint(data["interfaces"][1]["mtu"])','9000',['1500','Gi0/1','1'],'Najpierw wybierana jest lista interfaces, następnie jej drugi słownik i pole mtu.')
P('Warunki łączne','iface = {"admin": "up", "oper": "down"}\nprint(iface["admin"] == "up" and iface["oper"] == "up")','False',['True','up','down'],'And wymaga prawdziwości obu porównań. Stan administracyjny up nie oznacza operacyjnego up.')
P('Append zmienia listę','devices = ["R1", "R2"]\nalias = devices\nalias.append("R3")\nprint(len(devices))','3',['2','1','0'],'Alias wskazuje tę samą listę, a append ją modyfikuje. Przypisanie nie tworzy kopii listy.')
P('Obsługa wyjątku','try:\n    print(int("Gi0/0"))\nexcept ValueError:\n    print("invalid")','invalid',['Gi0/0','0','ValueError'],'Konwersja napisu interfejsu na liczbę zgłasza ValueError, który jest obsługiwany w except.')
P('Zwracana wartość','def usable(total):\n    return total - 2\n\nprint(usable(256))','254',['256','2','None'],'Return przekazuje wynik funkcji do wywołującego. To przykład interpretacji kodu; wzór nie opisuje wszystkich wyjątków adresacji IP.')
P('Break kończy pętlę','states = ["up", "down", "up"]\nchecked = 0\nfor state in states:\n    checked += 1\n    if state == "down":\n        break\nprint(checked)','2',['3','1','0'],'Licznik wzrasta także dla drugiego elementu, po czym break kończy pętlę. Trzeci element nie jest sprawdzany.')
end()
start('json','JSON — poprawny zapis i struktury danych','6.2',[BASICS,'https://blogs.cisco.com/developer/intro-to-programmability-3'])
def J(title,prompt,options,explain):
 Q(title,prompt,['`'+x+'`' for x in options],explain)
J('Cudzysłowy JSON','Który zapis jest poprawnym obiektem JSON z nazwą routera?', ['{"name":"R1"}',"{'name':'R1'}",'{name:"R1"}','{"name"="R1"}'],'Klucze oraz napisy JSON używają podwójnych cudzysłowów. Pary klucz–wartość rozdziela dwukropek.')
J('Wartość logiczna JSON','Wybierz poprawny JSON z polem enabled ustawionym na wartość logiczną prawda.', ['{"enabled":true}','{"enabled":True}','{"enabled":"true"}','{"enabled":TRUE}'],'True w Pythonie to true w JSON. Napis "true" jest poprawnym napisem, lecz nie wartością logiczną.')
J('Liczba zamiast napisu','Który JSON przechowuje mtu jako liczbę 1500?', ['{"mtu":1500}','{"mtu":"1500"}','{"mtu":1,500}','{"mtu":01500}'],'Liczba nie ma cudzysłowów ani separatorów tysięcy. W JSON nie zapisuje się liczb z dowolnymi zerami wiodącymi.')
J('Brak wartości','Jak poprawnie zapisać jawny brak wartości nextHop?', ['{"nextHop":null}','{"nextHop":None}','{"nextHop":NULL}','{"nextHop":undefined}'],'JSON używa literału null. None należy do Pythona, a undefined nie jest wartością JSON.')
J('Tablica VLAN-ów','Wybierz tablicę trzech liczb VLAN w polu vlans.', ['{"vlans":[10,20,30]}','{"vlans":{10,20,30}}','{"vlans":(10,20,30)}','{"vlans":"10,20,30"}'],'Tablica JSON używa nawiasów kwadratowych. Napis z przecinkami nie jest tablicą.')
J('Rozdzielenie pól','Który obiekt JSON ma poprawnie rozdzielone name i mtu?', ['{"name":"Gi0/0","mtu":1500}','{"name":"Gi0/0";"mtu":1500}','{"name":"Gi0/0" "mtu":1500}','{"name":"Gi0/0","mtu":1500,}'],'Przecinek rozdziela pola. Standardowy JSON nie dopuszcza końcowego przecinka przed zamknięciem obiektu.')
J('Obiekt zagnieżdżony','API wymaga obiektu interface, który zawiera pole name. Wybierz właściwą strukturę.', ['{"interface":{"name":"Gi0/0"}}','{"interface":"name=Gi0/0"}','{"interface":["name","Gi0/0"]}','{"interface.name":"Gi0/0"}'],'Zagnieżdżony obiekt ma własne nawiasy klamrowe. Klucz zawierający kropkę nie tworzy automatycznie zagnieżdżenia.')
J('Lista obiektów','API oczekuje interfaces jako tablicy obiektów z polem name. Wybierz strukturę.', ['{"interfaces":[{"name":"Gi0/0"},{"name":"Gi0/1"}]}','{"interfaces":{"name":["Gi0/0","Gi0/1"]}}','{"interfaces":["Gi0/0","Gi0/1"]}','{"interfaces":"Gi0/0,Gi0/1"}'],'Każdy element tablicy jest tu obiektem opisującym interfejs. Pozostałe zapisy mają inną strukturę, nawet jeśli są poprawnym JSON.')
Q('Kolejność w tablicy','Czy zmiana kolejności elementów tablicy JSON zawsze zachowuje znaczenie danych?', ['Nie; tablica jest uporządkowana, a znaczenie kolejności zależy też od modelu','Tak, tablice są z definicji nieuporządkowane','Tak, parser zawsze sortuje elementy','Nie, bo tablice nie mogą zawierać więcej niż jednego elementu'],'Tablica zachowuje kolejność. Nie zakładaj, że można dowolnie przestawiać listę akcji lub reguł.')
Q('Kolejność kluczy obiektu','API nie nadaje dodatkowego znaczenia kolejności kluczy. Czy obiekty {"name":"R1","mtu":1500} i {"mtu":1500,"name":"R1"} reprezentują te same pary danych?', ['Tak','Nie, pierwszy klucz zawsze jest identyfikatorem głównym','Nie, drugi zapis zmienia typ mtu','Tak, ale tylko gdy usuniemy cudzysłowy'],'Obiekt jest zbiorem par nazwa–wartość. Nie polegaj na kolejności kluczy jako mechanizmie logiki API.')
J('Pusta lista a null','API wymaga jawnej pustej listy sąsiadów. Jaki zapis odpowiada temu wymaganiu?', ['{"neighbors":[]}','{"neighbors":null}','{"neighbors":{}}','{"neighbors":""}'],'Pusta tablica, null, pusty obiekt i pusty napis to różne wartości i typy.')
J('Escaping cytatu','Opis ma zawierać tekst Port "uplink" wraz z cudzysłowami. Wybierz poprawny JSON.', ['{"description":"Port \\"uplink\\""}','{"description":"Port "uplink""}',"{'description':'Port \"uplink\"'}",'{"description":Port "uplink"}'],'Cudzysłowy wewnątrz napisu JSON trzeba poprzedzić backslashem. Zewnętrzne cudzysłowy nadal wyznaczają granice napisu.')
Q('JSON a schemat','Dokument {"mtu":"duze"} jest poprawny składniowo. Model wymaga liczby całkowitej. Czy dokument spełnia oba wymagania?', ['Nie, poprawna składnia nie oznacza zgodności typu ze schematem','Tak, każda wartość w poprawnym JSON pasuje do każdego modelu','Tak, parser automatycznie zamieni duze na 9000','Nie, JSON nie pozwala na napisy'],'Walidacja składni i walidacja modelu to różne etapy. Tu napis nie spełnia wymaganego typu.')
Q('Duplikaty nazw','Dokument zawiera dwa pola o nazwie mtu z różnymi wartościami. Jaka jest właściwa praktyka?', ['Unikać powtórzonych nazw, bo obsługa przez parsery może się różnić','Zakładać, że każdy parser zawsze wybierze pierwszą wartość','Zakładać, że oba pola utworzą automatycznie tablicę','Używać duplikatów do definiowania priorytetu'],'Unikalne nazwy pól zapewniają przewidywalną wymianę danych. Obsługa duplikatów nie powinna być fundamentem konfiguracji.')
J('Minimalny payload interfejsu','Model zadania wymaga interface jako obiektu z name typu string i enabled typu boolean false. Wybierz poprawny payload.', ['{"interface":{"name":"Gi0/2","enabled":false}}','{"interface":{"name":"Gi0/2","enabled":"false"}}','{"interface":[{"name":"Gi0/2","enabled":false}]}','{"interface":{"name":"Gi0/2","enabled":False}}'],'Trzeba jednocześnie zachować strukturę obiektu, typ napisu oraz typ logiczny. Poprawna składnia to tylko część wymagań.')
Q('Błąd parsowania','Parser wskazuje błąd przy końcu {"name":"R1","roles":["edge","border"}. Co jest niezamknięte?', ['Tablica roles — brakuje ] przed końcową }','Napis R1 — brakuje pierwszego cudzysłowu','Liczba całkowita roles','Obiekt nie może zawierać tablicy'],'Zagnieżdżone nawiasy trzeba zamykać w odwrotnej kolejności. Najpierw tablica, potem obiekt.')
J('Dwa poprawne typy','API wymaga retries jako liczby 3 i reachable jako boolean false. Wybierz poprawny zapis.', ['{"retries":3,"reachable":false}','{"retries":"3","reachable":false}','{"retries":3,"reachable":"false"}','{"retries":3,"reachable":0}'],'Zero i napis "false" nie są tym samym typem co boolean false. API może ściśle walidować te typy.')
Q('Komentarze','Administrator dopisał // uplink do standardowego pliku JSON. Co powinien wiedzieć?', ['Standardowy JSON nie obsługuje komentarzy //','Każdy parser JSON musi ignorować //','Komentarz działa tylko po liczbie','Komentarz zamienia następną wartość w null'],'Niektóre narzędzia przyjmują rozszerzone formaty, ale nie należy zakładać takiej obsługi w standardowym JSON/API.')
end()
start('yang','YANG — model danych i walidacja','6.3',[YANG,BASICS])
Q('Model danych','Jaka jest podstawowa funkcja YANG?', ['Opis struktury, typów i ograniczeń danych zarządzania','Szyfrowanie sesji TLS','Wybór najlepszej ścieżki BGP','Zastąpienie każdej bazy danych plikiem CSV'],'YANG jest językiem modelowania. Nie jest sam protokołem transportowym ani algorytmem szyfrowania.')
Q('Model a instancja','Która para poprawnie rozdziela model i konkretne dane?', ['YANG opisuje model; JSON/XML mogą kodować instancję danych','JSON zawsze jest modelem, YANG zawsze pakietem IP','YANG to wyłącznie wynik show running-config','XML jest transportem TCP, a YANG portem'],'Model określa dopuszczalną strukturę. Instancja zawiera konkretne wartości zgodne z tą strukturą.')
Q('Leaf','Co reprezentuje leaf w YANG?', ['Pojedynczy element danych z określonym typem','Zawsze tablicę obiektów','Wyłącznie komentarz dokumentacyjny','Interfejs fizyczny niezależnie od modelu'],'Leaf może opisywać pojedynczą wartość, np. enabled albo mtu. Jego typ określa dopuszczalne dane.')
Q('Container','Do czego służy container?', ['Grupowania zagnieżdżonych węzłów danych','Wyłącznie uruchamiania kontenera Docker','Wyłącznie szyfrowania jednego leaf','Automatycznego utworzenia nowego VRF'],'Container organizuje hierarchię modelu. Nazwa ta nie oznacza środowiska wirtualizacji aplikacji.')
Q('List','Jak YANG list opisuje np. interfejsy urządzenia?', ['Jako wiele wpisów o wspólnej strukturze','Jako jeden dowolny napis bez struktury','Jako wyłącznie komentarze','Jako obowiązkowo pojedynczy leaf boolean'],'Każdy wpis listy ma strukturę zdefiniowaną w modelu. Klucze mogą identyfikować poszczególne wpisy.')
Q('Leaf-list','Czym leaf-list różni się od list?', ['Leaf-list przechowuje wiele wartości prostego typu, list — wpisy o strukturze','Oba zawsze oznaczają dokładnie jeden napis','Leaf-list służy tylko do IPsec','List nie może mieć żadnych pól potomnych'],'Leaf-list może reprezentować np. kolekcję wartości, a list obiekty takie jak interfejsy z nazwą i parametrami.')
Q('Klucz listy','Model listy interfejsów deklaruje key "name". Do czego służy name?', ['Do jednoznacznego identyfikowania wpisu w tej liście','Do określenia hasła szyfrującego','Do wskazania portu transportowego NETCONF','Do wymuszenia kolejności alfabetycznej wszystkich pakietów'],'Klucz jest częścią tożsamości wpisu listy. Nie jest kluczem kryptograficznym.')
Q('Boolean','Leaf enabled ma type boolean. Która wartość JSON pasuje do tego typu?', ['true','"true" jako napis','"enabled" jako napis','Dowolny obiekt {"state":"up"}'],'Kodowanie musi zachować typ logiczny. Napis o podobnej treści nie staje się automatycznie boolean.')
Q('Config false','Co oznacza config false na węźle YANG?', ['Dane stanu, których nie ustawia się jako konfiguracji przez zwykłą edycję datastore','Wyłączenie całego protokołu NETCONF','Ustawienie każdego boolean na false','Automatyczne usunięcie modelu z urządzenia'],'Config false oznacza dane niekonfiguracyjne, np. obserwowany stan. Odczyt takiego węzła nie uprawnia do jego zapisu.')
Q('Namespace','Dlaczego moduły YANG mają przestrzenie nazw?', ['Aby jednoznacznie rozróżniać nazwy z różnych modułów','Aby zawsze używać jednego VLAN-u zarządzania','Aby ukryć adresy IP w szyfrogramie','Aby wszystkie pola nazywać tak samo bez kwalifikacji'],'Namespace pomaga uniknąć kolizji nazw. Jest ważny przy adresowaniu i kodowaniu elementów modelu.')
Q('Ograniczenie zakresu','Leaf mtu ma type uint16 z range "1280..9216". Czy 1000 jest poprawne dla tego leaf?', ['Nie, mieści się w uint16, ale nie w zawężonym range','Tak, każda liczba uint16 jest dozwolona','Tak, range jest tylko komentarzem','Nie, bo uint16 dopuszcza wyłącznie liczby ujemne'],'Typ bazowy i dodatkowe ograniczenia obowiązują jednocześnie. Range zawęża dopuszczalne wartości.')
Q('Enumeration','Leaf role ma enumeration z wartościami edge i border. Jak należy interpretować zapis role="core"?', ['Jest niezgodny z tym zbiorem dozwolonych wartości','Zawsze zostanie automatycznie zamieniony na edge','Jest dozwolony, bo każda enumeration to dowolny string','Zmienia typ leaf na list'],'Enumeration ogranicza wartości do nazw zdefiniowanych w modelu. Nie zakładaj automatycznych aliasów.')
Q('Model standardowy a natywny','Co trafnie opisuje modele standardowe oraz producenta?', ['Mogą współistnieć; zakres funkcji i wsparcie trzeba sprawdzić na urządzeniu','Model standardowy zawsze zawiera wszystkie funkcje każdego producenta','Modele natywne nigdy nie działają z NETCONF','Tylko modele standardowe mogą używać JSON'],'Standardy ułatwiają przenośność, ale wsparcie i rozszerzenia różnią się między platformami i wersjami.')
Q('Rewizja modułu','Skrypt działał na jednym obrazie, lecz po zmianie wersji urządzenia ścieżka lub pole jest niedostępne. Co należy porównać?', ['Obsługiwane moduły, rewizje, features i deviations','Wyłącznie adres MAC klienta API','Wyłącznie nazwę pliku Pythona','Wyłącznie kolor terminala'],'Obsługa modelu może się zmieniać. Klient powinien znać faktyczny kontrakt udostępniany przez urządzenie.')
Q('Walidacja relacji','Pole pojedynczo ma poprawny typ, ale narusza warunek must wiążący kilka pól. Czy walidator może odrzucić zmianę?', ['Tak, zgodność typu nie wyczerpuje ograniczeń modelu','Nie, każdy poprawny typ unieważnia must','Nie, must jest tylko opisem interfejsu użytkownika','Tak, ale wyłącznie przy HTTP GET'],'Model może narzucać relacje między wartościami. Poprawna składnia i typ nie gwarantują poprawności całej konfiguracji.')
Q('Leafref','Węzeł używa leafref do wskazania wartości w innym miejscu drzewa. Jaki jest zamysł?', ['Modelowanie odwołania do innego węzła danych','Przechowywanie hasła tylko w RAM','Wymuszenie wymiany danych przez UDP','Automatyczne usuwanie obu węzłów'],'Leafref opisuje referencję w modelu. Szczegółowa walidacja istnienia celu zależy od właściwości i kontekstu modelu.')
Q('Lista nie jest zawsze uporządkowana przez użytkownika','Dlaczego klient nie powinien bez sprawdzenia traktować kolejności wpisów każdej listy YANG jako kolejności reguł ACL?', ['Semantykę kolejności określa model, m.in. ordered-by','YANG nigdy nie pozwala modelować kolejności','Każdy serwer zawsze sortuje po adresie IP','XML automatycznie nadaje priorytet pierwszemu wpisowi'],'Kolejność w reprezentacji nie jest uniwersalnym priorytetem. Trzeba odczytać semantykę konkretnej listy.')
Q('Granica modelu i protokołu','Serwer odrzuca zapis oper-state, który w modelu jest config false. Zmiana NETCONF na RESTCONF sama rozwiąże problem?', ['Nie, ograniczenie wynika z modelu danych','Tak, RESTCONF zawsze pozwala pisać wszystkie pola','Tak, JSON automatycznie zmienia config false na true','Nie, bo RESTCONF nie obsługuje modeli'],'Zmiana transportu nie usuwa semantyki modelu. Operacyjny stan odczytuje się, a konfigurację ustawia we właściwych węzłach.')
end()
start('orchestration','Automatyzacja — agent, agentless i kontrola zmian','6.7',[ORCH,AGENT,ANS])
Q('Agent na celu','Co charakteryzuje typowy model agentowy zarządzania konfiguracją?', ['Oprogramowanie agenta uczestniczy w wykonywaniu zadań na zarządzanym węźle','Brak jakiegokolwiek oprogramowania zarządzającego','Wymóg ręcznego wklejania każdego polecenia','Wyłącznie protokół routingu dynamicznego'],'Agent jest elementem architektury narzędzia. Jego obsługa wymaga uwzględnienia instalacji, wersji i uprawnień.')
Q('Agentless','Co oznacza agentless w kontekście Ansible dla wspieranych urządzeń sieciowych?', ['Nie wymaga dedykowanego agenta Ansible na urządzeniu docelowym','Nie wymaga żadnego dostępu sieciowego','Nie wymaga uwierzytelnienia','Nie wymaga żadnego narzędzia po stronie sterującej'],'Narzędzie nadal potrzebuje kontrolera, transportu i dostępu, np. SSH lub API. Brak agenta nie oznacza braku wymagań.')
Q('Przykłady architektur','Które zestawienie opisuje typowe wdrożenia?', ['Ansible — agentless; Puppet/Chef — często agentowe','Ansible — zawsze agent na każdym switchu; Puppet — wyłącznie CSV','Każde narzędzie musi instalować ten sam agent','Puppet i Chef to protokoły data plane'],'To typowe modele, nie zakaz innych trybów i integracji. Konkretną platformę i sposób połączenia trzeba sprawdzić.')
Q('Rola inventory','Do czego służy inventory w typowym workflow Ansible?', ['Określenia zarządzanych hostów, grup i powiązanych zmiennych','Wyłącznie przechowywania rekordów NetFlow','Automatycznego przydzielania numerów AS wszystkim hostom','Zastąpienia protokołu SSH'],'Inventory wyznacza cele i kontekst wykonania. Błędna grupa hostów może skierować poprawną zmianę na niewłaściwe urządzenia.')
Q('Playbook','Jaką rolę pełni playbook Ansible?', ['Opisuje zadania i ich wykonanie dla wskazanych hostów','Jest wyłącznie kopią tablicy routingu','Jest formatem klucza TLS','Zawsze oznacza pojedyncze polecenie systemowe'],'Playbook organizuje automatyzację. Użyte moduły i dane decydują o konkretnych działaniach.')
Q('Transport agentless','Który warunek nadal jest potrzebny w modelu bezagentowym?', ['Wspierany interfejs zarządzania i odpowiednie uprawnienia','Obowiązkowo publiczny adres każdego urządzenia','Wyłączone wszystkie ACL','Identyczny producent wszystkich serwerów aplikacyjnych'],'Agentless nie eliminuje wymagań dostępu. Można używać prywatnych sieci zarządzania i kontrolowanych polityk.')
Q('Push i pull','Które rozróżnienie modeli wykonania jest poprawne?', ['Push: sterujący inicjuje wykonanie; pull: węzeł/agent pobiera żądany stan lub zadania','Push zawsze oznacza UDP, pull zawsze TCP','Push działa wyłącznie bez haseł','Pull oznacza ręczne pobieranie pliku przez operatora'],'To opis kierunku inicjowania pracy, nie automatycznie konkretnego transportu ani pełnej klasyfikacji bezpieczeństwa.')
Q('Stan deklaratywny','Zadanie deklaruje, że VLAN 20 ma istnieć. Czym różni się ten zamiar od bezwarunkowego odtworzenia serii poleceń?', ['Skupia się na stanie docelowym, a narzędzie może porównać go ze stanem obecnym','Zawsze wykonuje reload po każdym uruchomieniu','Nie wymaga odczytu ani walidacji','Automatycznie gwarantuje brak jakichkolwiek błędów'],'Podejście deklaratywne określa rezultat. Jakość implementacji modułu i weryfikacja nadal są istotne.')
Q('Idempotencja zadania','Po pierwszym uruchomieniu konfiguracja już odpowiada celowi. Co powinno zrobić zadanie idempotentne przy ponowieniu?', ['Nie wprowadzać zbędnych zmian tego samego stanu','Zawsze usunąć i odtworzyć całą konfigurację','Zawsze zwiększyć numer VLAN','Zawsze zgłosić błąd tylko dlatego, że stan istnieje'],'Idempotencja ułatwia powtarzanie automatyzacji. Nie gwarantuje jednak, że błędnie określony stan docelowy jest bezpieczny.')
Q('Configuration drift','Co oznacza drift konfiguracji względem zadeklarowanego stanu?', ['Rozbieżność między stanem oczekiwanym a rzeczywistym','Każdy wzrost RTT w sieci','Wyłącznie zmianę adresu DHCP hosta','Obowiązkowo awarię agenta'],'Drift może wynikać np. z ręcznej zmiany lub częściowego wykonania. Narzędzie powinno go wykrywać i obsługiwać zgodnie z polityką.')
Q('Koszt modelu agentowego','Jaki dodatkowy obszar utrzymania zwykle pojawia się przy agentach?', ['Instalacja, zgodność wersji, aktualizacje i zdrowie agentów','Brak możliwości monitorowania','Obowiązkowa rezygnacja z uwierzytelnienia','Brak jakichkolwiek zależności programowych'],'Agent może zapewniać lokalne funkcje, ale sam staje się elementem utrzymania i kontroli dostępu.')
Q('Sieć bez możliwości instalacji','Switch nie pozwala instalować zewnętrznego agenta, ale ma wspierane SSH/API. Który kierunek automatyzacji jest naturalny?', ['Narzędzie bezagentowe lub wspierana integracja/proxy','Rezygnacja z automatyzacji w każdych warunkach','Instalacja dowolnego pakietu mimo braku wsparcia','Wymiana protokołu routingu na narzędzie konfiguracji'],'Brak możliwości instalacji agenta nie wyklucza automatyzacji przez udostępnione interfejsy zarządzania.')
Q('Agent na serwerze proxy','Agent działa na serwerze pośredniczącym, który zarządza urządzeniem przez API. Jaki wniosek jest poprawny?', ['Na urządzeniu może nie być agenta, mimo że rozwiązanie używa agenta na proxy','Cały system jest z definicji pozbawiony agentów','Każdy switch musi wtedy uruchamiać ten sam proces','Proxy eliminuje wymóg uwierzytelnienia do API'],'Architekturę trzeba opisać dla całego rozwiązania i poszczególnych węzłów. Etykiety agent/agentless bez kontekstu mogą upraszczać obraz.')
Q('Tryb check','Czy udany check/dry-run zawsze dowodzi, że rzeczywista zmiana zakończy się identycznie?', ['Nie; zależy od wsparcia modułu i zmian stanu między testem a wykonaniem','Tak, to matematyczna gwarancja dla każdego modułu','Tak, dry-run zawsze wykonuje pełną zmianę produkcyjną','Nie, check nigdy nie ma żadnej wartości'],'Tryb sprawdzający jest pomocny, ale ma ograniczenia. Trzeba znać zachowanie modułów i zweryfikować efekt po wdrożeniu.')
Q('Zakres błędu','Playbook ma poprawną treść, lecz inventory wskazuje wszystkie routery zamiast grupy lab. Co jest głównym ryzykiem?', ['Wykonanie poprawnych zadań na niezamierzonych urządzeniach','Wyłącznie zmiana formatu YAML','Automatyczne odrzucenie przez każdy moduł','Brak ryzyka, bo treść poleceń jest poprawna'],'Poprawność celu jest równie ważna jak poprawność zadania. Ograniczenia grup, limit i etapowanie pomagają kontrolować zakres zmian.')
Q('Częściowy sukces','Automatyzacja zmieniła 8 z 10 urządzeń, a dwa są niedostępne. Co powinien uwzględnić operator?', ['Stan każdego urządzenia, plan ponowienia i spójność zależności','Założyć automatyczny rollback wszystkich dziesięciu','Zgłosić pełny sukces na podstawie większości','Usunąć wyniki wykonania przed ponowieniem'],'Orkiestracja nie gwarantuje transakcji obejmującej całą sieć. Potrzebna jest obsługa błędów i weryfikacja częściowego stanu.')
Q('Sekrety automatyzacji','Gdzie powinny trafiać hasła/tokeny używane przez narzędzie?', ['Do odpowiednio chronionego mechanizmu sekretów, z kontrolą dostępu','Jawnie do publicznego inventory Git','Do opisu interfejsu na każdym routerze','Do nazwy pliku playbooka'],'Automatyzacja powinna chronić poświadczenia i ograniczać uprawnienia. Sam fakt użycia agenta lub agentless nie rozwiązuje zarządzania sekretami.')
Q('Weryfikacja zamiaru','Moduł zwrócił changed=true po modyfikacji routingu. Co jeszcze jest potrzebne do oceny rezultatu?', ['Odczyt stanu i testy osiągalności zgodne z zamiarem zmiany','Nic, changed zawsze oznacza pełną poprawność usługi','Wyłącznie ponowne zapisanie tego samego pliku YAML','Wyłącznie sprawdzenie koloru komunikatu w konsoli'],'Changed opisuje działanie modułu, nie pełne zdrowie sieci. Weryfikuj konfigurację i zachowanie usługi.')
end()
save()
