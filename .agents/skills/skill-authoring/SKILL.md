---
name: skill-authoring
description: "Folosește când creezi, modifici sau evaluezi un skill din acest template."
license: "Apache-2.0"
---

# Skilluri cu scop și evaluare

Adaptare modificată în română, 2026-10-28. Surse: anthropic.
Vezi [proveniența și licențele](../../../docs/SOURCES.md).
Se aplică [politica comună](../../../AGENTS.md); acest skill nu o înlocuiește.

1. Definește o singură responsabilitate, intrările, rezultatul și când skillul
   trebuie sau nu trebuie selectat.
2. Verifică registrul existent; extinde un responsabil existent înainte de a crea un duplicat.
3. Scrie SKILL.md cu name, description și license în formatul scalar al template-ului.
   Descrierea trebuie să indice concret sarcinile pentru care skillul este relevant.
4. Păstrează procedura scurtă; include resurse locale numai dacă sunt necesare.
   Niciun fișier nu trebuie să depindă de un checkout extern.
5. Înregistrează sursele, commiturile, licențele și adaptările.
6. Actualizează registrul și adaugă scenarii de selecție și de neactivare.
7. Rulează validatorul structural și testele lui.
8. Evaluează separat rezultatele agentului pe scenarii reprezentative: utilitate,
   corectitudine, selecție greșită și contradicții. Compară cu varianta fără skill
   când mediul permite. Notează rezultate reale, nu scoruri presupuse.
9. Ajustează și păstrează istoricul modificărilor.

Scenariile din evals sunt criterii pentru evaluare comportamentală; trecerea
validatorului nu demonstrează performanța agentului. Nu lansa automat alte modele
sau evaluări plătite. Acest skill nu include scripturile Anthropic.
