# Scenariusze praktyczne

Każdy wiersz pliku `.txt` to ręcznie opracowany przypadek: tytuł, obserwacje,
rozpoznanie, działanie, dowód weryfikacji i zasada. Separator: `|`.
Cztery pytania dotyczą różnych decyzji w tym samym przypadku. Są rozłożone
między sekcjami, aby odpowiedź z jednego pytania nie podpowiadała następnego.
Dystraktory pochodzą z innych przypadków tego samego działu; informacja zwrotna
wiąże je z ich właściwym kontekstem. Nie generujemy wariantów przez podmianę IP.

`python scripts/authoring/expand_scenarios.py` dopisuje tylko nowe paczki.
Dotychczasowe paczki, ID, rewizje i zależności pozostają nienaruszone.
Przy poprawkach edytuj źródła scenariuszy i ponownie uruchom skrypt.
