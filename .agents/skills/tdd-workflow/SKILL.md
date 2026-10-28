---
name: tdd-workflow
description: "Folosește pentru logică nouă, buguri și schimbări de comportament verificabile prin teste."
license: "MIT"
---

# Teste pe comportament

Adaptare modificată în română, 2026-10-28. Surse: ecc, matt, ponytail.
Vezi [proveniența și licențele](../../../docs/SOURCES.md).
Se aplică [politica comună](../../../AGENTS.md); acest skill nu o înlocuiește.

1. Identifică runner-ul și comanda reală din configurația proiectului.
2. Alege interfața publică relevantă și un comportament observabil din cerință.
   Respectă granițele de test existente; nu cere aprobări repetate pentru alegeri de rutină.
3. Scrie un test mic și execută-l înaintea remedierii, când este practic.
4. Confirmă că eșuează pentru comportamentul vizat. Dependențele lipsă și o
   eroare fără legătură nu reprezintă dovadă RED.
5. Implementează suficient pentru acel test și execută-l din nou.
6. Continuă vertical: un comportament, testul lui, implementarea lui. Nu scrie
   dinainte o suită mare pentru interfețe încă imaginare.
7. Simplifică după GREEN, apoi repetă verificările afectate.
8. Raportează ce garantează testul, comenzile și rezultatele RED/GREEN reale.

Alege unitare, integrare sau E2E după risc. Verifică erorile și limitele importante.
Nu testa metode private sau detalii care se schimbă fără efect asupra utilizatorului.
Valorile așteptate provin din cerință ori exemple independente, nu din repetarea
algoritmului testat. Mock-urile nu trebuie să ascundă exact granița evaluată.

Respectă pragurile de coverage existente. Nu impune 80% tuturor proiectelor și nu
confunda procentul cu utilitatea testelor. Corecturile simple de text nu cer teste
artificiale. Dacă execuția este blocată, raportează blocajul. Nu fabrica RED/GREEN
și nu crea automat commituri intermediare.
