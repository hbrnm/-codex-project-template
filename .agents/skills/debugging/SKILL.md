---
name: debugging
description: "Folosește când un test, build sau flux de utilizator eșuează și trebuie identificată cauza."
license: "MIT"
---

# Depanare bazată pe dovezi

Adaptare modificată în română, 2026-10-28. Surse: addy, rea.
Vezi [proveniența și licențele](../../../docs/SOURCES.md).
Se aplică [politica comună](../../../AGENTS.md); acest skill nu o înlocuiește.

1. Oprește adăugarea funcțiilor afectate și păstrează eroarea, pașii și contextul.
2. Reproduce problema sau notează exact de ce nu se reproduce.
3. Localizează stratul: UI, API, date, integrare, configurație sau test.
4. Redu cazul fără a modifica ori șterge lucrul utilizatorului.
5. Formulează ipoteze verificabile și testează-le pe rând; evită editările speculative în masă.
6. Remediază cauza și verifică apelanții afectați.
7. Adaugă o regresie utilă și repetă fluxul original și verificările conexe.
8. Raportează dovada cauzei, remedierea și incertitudinea rămasă.

Pentru cod sursă disponibil folosește instrumentele obișnuite ale proiectului.
Dacă întrebarea depinde de un binar ori de comportamentul livrat, consultă
architecture-analysis. Nu instala REA sau alte motoare ca parte implicită a depanării.
Nu repeta la nesfârșit un apel extern eșuat cu aceleași condiții.
