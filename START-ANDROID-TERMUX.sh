#!/data/data/com.termux/files/usr/bin/bash
# Run from the extracted project in Termux private storage, not /sdcard.
set -euo pipefail
umask 077
cd -- "$(dirname -- "$0")"
for tool in git gh openssl base64; do
  command -v "$tool" >/dev/null || { echo 'Najpierw: pkg install git gh openssl-tool unzip'; exit 1; }
done
gh auth status >/dev/null 2>&1 || { echo 'Najpierw: gh auth login --hostname github.com --git-protocol https --web --scopes repo,workflow'; exit 1; }
test -f package.json && test -f .github/workflows/android-apk.yml
if test -d .git; then
  echo 'Projekt ma już repozytorium. Nie nadpisuję go. Kolejne buildy uruchom w zakładce Actions.'
  exit 1
fi
owner=$(gh api user --jq .login)
read -r -p "Nazwa NOWEGO prywatnego repozytorium [packetpath-android]: " repo
repo=${repo:-packetpath-android}
[[ "$repo" =~ ^[A-Za-z0-9_-]+$ ]] || { echo 'Dozwolone: litery, cyfry, - i _.'; exit 1; }
if gh repo view "$owner/$repo" >/dev/null 2>&1; then
  echo 'Repozytorium już istnieje. Wybierz nową nazwę; nie nadpisuję istniejącego projektu.'
  exit 1
fi
signing_dir="$HOME/.packetpath-signing/${owner}_${repo}"
mkdir -p "$signing_dir"
chmod 700 "$signing_dir"
if ! test -f "$signing_dir/packetpath.p12"; then
  openssl rand -hex 24 | tr -d '\n' > "$signing_dir/store.password"
  openssl req -x509 -newkey rsa:3072 -nodes -sha256 -days 10000 \
    -subj '/CN=PacketPath personal Android signing/' \
    -keyout "$signing_dir/private.pem" -out "$signing_dir/certificate.pem" 2>/dev/null
  openssl pkcs12 -export -name packetpath \
    -inkey "$signing_dir/private.pem" -in "$signing_dir/certificate.pem" \
    -out "$signing_dir/packetpath.p12" -passout "file:$signing_dir/store.password"
  rm "$signing_dir/private.pem" "$signing_dir/certificate.pem"
fi
test -s "$signing_dir/store.password"
git init -b main
git add .
git -c user.name='PacketPath setup' -c user.email='packetpath@localhost' commit -m 'PacketPath 0.14 Android'
gh auth setup-git
gh repo create "$owner/$repo" --private --source=. --remote=origin --push
base64 < "$signing_dir/packetpath.p12" | gh secret set ANDROID_KEYSTORE_BASE64 --repo "$owner/$repo"
gh secret set ANDROID_STORE_PASSWORD --repo "$owner/$repo" < "$signing_dir/store.password"
gh workflow run android-apk.yml --repo "$owner/$repo" --ref main
printf '\nBudowanie uruchomione: https://github.com/%s/%s/actions\n' "$owner" "$repo"
printf 'Zachowaj prywatny klucz i hasło z: %s\nNie wysyłaj ich na czat ani do repozytorium.\n' "$signing_dir"
