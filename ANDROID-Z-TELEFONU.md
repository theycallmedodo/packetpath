# PacketPath 0.14 — Android z telefonu

Paczka zawiera projekt Android i workflow, nie gotowy APK. Kompilacja odbędzie się na Twoim koncie GitHub. Aplikacja zachowuje 1008 zadań (576 CCNA + 432 ENCOR), interfejs Matrix i odblokowywanie stopni. Zadania są dołączane do APK i wczytywane po jednym stopniu. Linki do dokumentacji Cisco wymagają Internetu.

## 1. Pobierz i przygotuj

Pobierz `PacketPath-v0.14-Android.zip` do folderu Download telefonu. W Termuxie uruchom kolejno:

```bash
pkg update
pkg install git gh openssl-tool unzip
termux-setup-storage
```

Zezwól Termuxowi na dostęp do plików. Potem:

```bash
mkdir -p "$HOME/packetpath-v014"
unzip "$HOME/storage/downloads/PacketPath-v0.14-Android.zip" -d "$HOME/packetpath-v014"
cd "$HOME/packetpath-v014/PacketPath"
```

Jeżeli przeglądarka zmieniła nazwę ZIP, popraw ją w poleceniu. Pracuj w katalogu domowym Termuxa — nie bezpośrednio w Download.

## 2. Zaloguj GitHub

```bash
gh auth login --hostname github.com --git-protocol https --web --scopes repo,workflow
```

Potwierdź logowanie przez przeglądarkę i wpisz wyświetlony jednorazowy kod na stronie GitHuba. Jeżeli przeglądarka się nie otworzy, otwórz wskazany przez CLI adres ręcznie. Nie przesyłaj hasła, tokenu ani kodu na czat. GitHub CLI obsługuje logowanie przez przeglądarkę: https://cli.github.com/manual/gh_auth_login.

## 3. Utwórz repozytorium i uruchom build

```bash
bash START-ANDROID-TERMUX.sh
```

Wpisz nazwę nowego repozytorium lub naciśnij Enter (`packetpath-android`). Skrypt:

- tworzy prywatny klucz podpisujący na telefonie;
- tworzy NOWE prywatne repozytorium na Twoim koncie i wysyła źródła;
- zapisuje klucz i hasło w GitHub Actions Secrets (nie w kodzie);
- uruchamia workflow **Build Android APK** i wyświetla adres jego wyników.

Repozytorium z podaną nazwą nie może już istnieć. Skrypt nie zmienia istniejących repozytoriów. Do prywatnego repozytorium potrzebujesz dostępnego limitu Actions; ewentualne ograniczenie limitu zobaczysz na GitHubie.

Klucz i hasło zostają w `$HOME/.packetpath-signing/LOGIN_REPO/`. Zachowaj oba pliki w bezpiecznej kopii. Usunięcie Termuxa usuwa jego prywatne dane. Zachowanie klucza pozwala aktualizować APK bez zmiany podpisu; nie twórz nowego klucza dla następnych wersji.

## 4. Pobierz i zainstaluj APK

W przeglądarce telefonu otwórz podany link GitHub → **Actions** → **Build Android APK** → uruchomiony build. Po zielonym wyniku w sekcji **Artifacts** pobierz **PacketPath-Android**. Jeśli elementów nie widać, włącz widok komputerowy przeglądarki.

Rozpakuj pobrane archiwum, otwórz `PacketPath-v0.14.apk` i zezwól menedżerowi plików na instalowanie tej aplikacji z tego źródła. Ten plik jest podpisany Twoim kluczem. Nie jest to publikacja w Google Play.

Następny build uruchamiasz w **Actions → Build Android APK → Run workflow**. Workflow ma tylko wyzwalacz ręczny, więc samo wysłanie zmian nie uruchamia płatnej pracy automatycznie. Każdy nowy run otrzymuje wyższy `versionCode`; ponowienie tego samego runu zachowuje numer. Zachowaj repozytorium i klucz dla aktualizacji.

## Postępy i pierwszy test

W zakładce **Twój postęp** są **Eksportuj postępy** i **Wczytaj kopię JSON**. Eksport w Androidzie otwiera systemowe udostępnianie — wybierz miejsce, gdzie chcesz zachować plik. Import wymaga potwierdzenia i zastępuje obecne postępy, nie łączy ich. Wersja komputerowa 0.14 ma te same przyciski i odczytuje zapis poprzedniej wersji, jeśli jest uruchomiona pod tym samym adresem i portem. Zapis z przeglądarki nie pojawi się w APK automatycznie.

Na telefonie sprawdź:

1. W trybie samolotowym otwórz po jednym stopniu CCNA i ENCOR.
2. Rozwiąż quiz i CLI z kilkoma lukami; sprawdź przewijanie kodu i klawiaturę.
3. Wyjdź z aplikacji, otwórz ponownie i sprawdź zapis odpowiedzi.
4. Zakończ stopień wynikiem 5/6 i sprawdź odblokowanie kolejnego.
5. Wyeksportuj kopię i zaimportuj ją ponownie.
6. Sprawdź Wstecz: z ćwiczenia wraca do kampanii, z kampanii minimalizuje aplikację.

Odinstalowanie aplikacji usuwa lokalny zapis. Przed odinstalowaniem wykonaj eksport. Ta wersja nie dodaje kont, synchronizacji chmurowej ani nowych systemów XP/serduszek.

## Gdy coś się zatrzyma

- `gh` nie jest zalogowany: wykonaj ponownie polecenie logowania z punktu 2.
- Push blokuje brak uprawnienia workflow: `gh auth refresh --hostname github.com --scopes repo,workflow`.
- Repo utworzono, ale ustawianie sekretów lub uruchomienie przerwał Internet: nie generuj nowego klucza. W katalogu projektu wykonaj:

```bash
repo=$(gh repo view --json nameWithOwner --jq .nameWithOwner)
signing_dir="$HOME/.packetpath-signing/${repo/\//_}"
base64 < "$signing_dir/packetpath.p12" | gh secret set ANDROID_KEYSTORE_BASE64 --repo "$repo"
gh secret set ANDROID_STORE_PASSWORD --repo "$repo" < "$signing_dir/store.password"
gh workflow run android-apk.yml --repo "$repo" --ref main
```

- Czerwony build: otwórz czerwony krok i prześlij komunikat błędu, bez sekretów. Nie odinstalowuj aplikacji z zapisanymi postępami.

## Weryfikacja tej paczki

W środowisku przygotowania przeszły: czysta instalacja `npm ci`, 27 testów, TypeScript, build Vite i synchronizacja Capacitor Android. Projekt zawiera Gradle Wrapper i ustawienia SDK 36 / Java 21. Workflow weryfikuje podpis APK przed udostępnieniem artefaktu.

Pełna kompilacja Gradle, uruchomienie workflow na Twoim GitHubie oraz test na fizycznym Androidzie nie zostały tu wykonane. Pierwszy build i powyższa lista testów są konieczne przed uznaniem wydania za sprawdzone na telefonie.

Dokumentacja: https://capacitorjs.com/docs/android, https://capacitorjs.com/docs/apis/preferences, https://docs.github.com/en/actions/how-tos/manage-workflow-runs/manually-run-a-workflow.
