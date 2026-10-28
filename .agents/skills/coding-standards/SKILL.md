---
name: coding-standards
description: "Folosește pentru implementare, refactorizare sau review general al clarității și convențiilor codului."
license: MIT
---

# Standarde de cod

Adaptare din ECC; sursa și licența sunt în [proveniență](../../../docs/ECC-SOURCE.md).

1. Citește convențiile proiectului și exemplele din vecinătatea fișierelor schimbate.
2. Folosește nume descriptive, funcții concentrate și fluxuri de control clare.
3. Alege cea mai simplă soluție care satisface cerința. Evită abstracțiile speculative.
4. Evită mutarea neașteptată a datelor partajate; respectă idiomurile limbajului.
5. Validează datele la granițele sistemului și tratează erorile fără a pierde cauza.
6. Respectă tipurile, formatterul și instrumentele deja folosite de proiect.
7. Explică deciziile neobișnuite în comentarii; nu descrie mecanic fiecare instrucțiune.
8. Verifică erorile și cazurile limită, nu doar fluxul principal.
9. Pentru UI, verifică etichetele, tastatura, contrastul și dimensiunile mobile.
10. Citește diff-ul final și elimină schimbările fără legătură.

Nu impune React, TypeScript, un format API sau o structură de directoare unui
proiect care folosește alte convenții. Pentru verificarea finală consultă
[verification-loop](../verification-loop/SKILL.md).
