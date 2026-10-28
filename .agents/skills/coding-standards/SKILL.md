---
name: coding-standards
description: "Folosește la implementare și refactorizare pentru a reutiliza codul existent și a evita complexitatea inutilă."
license: "MIT"
---

# Claritate și cea mai mică schimbare completă

Adaptare modificată în română, 2026-10-28. Surse: ecc, ponytail.
Vezi [proveniența și licențele](../../../docs/SOURCES.md).
Se aplică [politica comună](../../../AGENTS.md); acest skill nu o înlocuiește.

1. Citește cerința, convențiile și codul vecin; identifică și apelanții afectați.
2. Caută întâi o soluție existentă în proiect, apoi în platformă sau biblioteca standard,
   apoi în dependențele instalate. Adaugă o dependență numai cu motiv concret.
3. Implementează cea mai mică schimbare care rezolvă complet cererea, inclusiv
   exporturile, configurația, testele și documentația afectate.
4. Folosește nume clare, fluxuri simple și granițe explicite. Evită abstracții pentru
   funcții ipotetice și linii comprimate care cer descifrare.
5. Evită mutarea neașteptată a datelor partajate, respectând idiomurile limbajului.
6. Păstrează validarea, tratarea erorilor, securitatea și accesibilitatea când simplifici.
7. Explică motivele neobișnuite în comentarii; nu comenta mecanic fiecare instrucțiune.
8. Verifică rezultatul cu procedura verification-loop.

Nu impune framework, formatter, format API sau model arhitectural unui proiect
care are alte convenții. Nu transforma „mai puțin cod” în omiterea cerințelor.
Nu activează o personalitate persistentă sau un mod ascuns pentru restul sesiunii.
