---
name: tdd-workflow
description: "Folosește pentru logică nouă, remedierea bugurilor și schimbări de comportament care pot fi verificate prin teste."
license: MIT
---

# Dezvoltare ghidată de teste

Adaptare din ECC; vezi [proveniența](../../../docs/ECC-SOURCE.md).

1. Identifică test runner-ul și comanda reală din documentație și configurație.
   Nu presupune npm, Jest, Playwright sau un script ECC absent.
2. Transformă cerința într-un comportament observabil. Pentru un bug,
   construiește un caz de regresie care reproduce cauza.
3. Scrie testul și execută-l înaintea remedierii, când este practic.
4. Confirmă că eșuează din cauza comportamentului vizat, nu din cauza
   dependențelor lipsă ori a unei configurații greșite.
5. Implementează modificarea minimă și repetă același test.
6. Refactorizează păstrând testele verzi. Rulează verificările relevante conexe.
7. Raportează comanda, rezultatul înainte și după și cazurile neacoperite.

Alege teste unitare pentru logică izolată, integrare pentru granițele sistemului
și E2E pentru fluxurile esențiale, în funcție de schimbare.
Testează cazurile de eroare și limitele importante. Izolează datele de test.

Respectă pragurile de coverage existente; dacă nu există, propune o țintă
potrivită după alegerea tehnologiei. Procentul nu înlocuiește verificarea
comportamentului. Nu dezactiva teste ca să obții un rezultat verde.

Nu crea teste artificiale pentru corecturi simple de text. Dacă mediul nu poate
rula testele, raportează blocajul și nu pretinde dovezi RED/GREEN.
Nu crea automat commituri intermediare și nu instala instrumente globale.
