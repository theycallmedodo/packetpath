@echo off
setlocal
cd /d "%~dp0"
if not exist "%~dp0serve.mjs" (
 echo Blad: rozpakuj CALY ZIP. Nie uruchamiaj pliku BAT z archiwum.
 pause
 exit /b 1
)
if not exist "%~dp0dist\index.html" (
 echo Brak folderu dist. Rozpakuj cala paczke do jednego folderu.
 pause
 exit /b 1
)
where node >nul 2>nul
if errorlevel 1 (
 echo Zainstaluj Node.js LTS i uruchom ponownie ten plik.
 pause
 exit /b 1
)
node "%~dp0serve.mjs"
pause
