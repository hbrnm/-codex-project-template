---
name: architecture-analysis
description: "Folosește pentru explicații fără editări despre un proiect existent, ce s-a schimbat sau dacă o funcție este livrată, separând dovezile de ipoteze."
license: "MIT"
---

# Analiza sistemelor din dovezi

Adaptare modificată în română, 2026-10-28. Surse: rea, matt.
Vezi [proveniența și licențele](../../../docs/SOURCES.md).
Se aplică [politica comună](../../../AGENTS.md); acest skill nu o înlocuiește.

1. Definește întrebarea: componente, traseul unei cereri, stocare sau comportament livrat.
2. Pentru sursă disponibilă, citește punctele de intrare, modulele, apelanții,
   configurația și testele relevante înainte de instalarea altor instrumente.
3. Leagă fiecare concluzie de fișier, simbol, test sau observație runtime.
4. Distinge observat, dedus și necunoscut. Nu declara o funcție activă doar
   fiindcă există cod ori configurație pentru ea.
5. Pentru binare, pachete sau comportament care nu poate fi stabilit din sursă,
   propune instrumentul specializat necesar și verifică disponibilitatea lui.
   REA rămâne o integrare opțională; instrucțiunile nu îl instalează.
6. Nu executa implicit fișiere necunoscute și nu extinde analiza la ținte fără autorizare.
7. Livrează traseul relevant și limitele. Folosește diagramming numai dacă ajută.
8. Pentru o decizie majoră, folosește [șablonul ADR](../../../docs/ADR-TEMPLATE.md).

Nu copia un produs întreg când cererea privește o singură funcție.
Separă reconstruirea unui comportament permis de preluarea activelor și identității sale.

## Întrebări despre proiect, fără editări
Pentru „de ce este așa?”, „ce s-a schimbat?” sau „este livrat?”, răspunde fără
modificarea fișierelor, instalări, commituri sau publicare. Nu completa automat
un ADR ori handoff. O cerere explicită de implementare permite trecerea la
procedura relevantă; nu transforma o simplă întrebare într-o remediere.

Restrânge analiza la întrebarea pusă. Consultă documentația și, când sunt
disponibile, git log, git diff sau git blame pentru intervalul relevant.
Istoricul poate explica o decizie; dacă motivul nu este documentat, marchează-l
ca deducție. Citează fișierul și liniile sau commitul pentru concluziile centrale.
Pentru „livrat”, distinge implementat în cod, integrat în branch, publicat și
activ în mediul cerut. Un test local ori un merge nu dovedește publicarea.
Dacă lipsesc istoricul sau accesul runtime, declară exact ce nu poți confirma.

