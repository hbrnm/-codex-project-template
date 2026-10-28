---
name: code-review
description: "Folosește după schimbări semnificative sau la review de diff și PR pentru a găsi probleme concrete."
license: "MIT"
---

# Review pe cinci dimensiuni

Adaptare modificată în română, 2026-10-28. Surse: addy, ponytail, matt.
Vezi [proveniența și licențele](../../../docs/SOURCES.md).
Se aplică [politica comună](../../../AGENTS.md); acest skill nu o înlocuiește.

1. Citește cerința, convențiile și întregul diff față de baza sarcinii.
2. Verifică corectitudinea: flux principal, erori, limite, concurență și teste.
3. Verifică lizibilitatea: nume, flux, redundanțe și complexitate evitabilă.
4. Verifică arhitectura: responsabilități, interfețe, dependențe și compatibilitate.
5. Verifică securitatea și performanța pe căile afectate.
6. Leagă fiecare constatare de fișier și linie, impact și remediere concretă.
7. Separă blocajele de sugestii; preferința personală de stil nu blochează
   o schimbare corectă care respectă proiectul.
8. Verifică remedierea problemelor importante și repetă verificările afectate.

Păstrează comportamentul când simplifici. O soluție mai scurtă care elimină
validarea sau cerințe este o regresie. Nu afirma că review-ul e independent
dacă a fost făcut de același agent în aceeași conversație. Delegarea este opțională,
numai dacă mediul o suportă și contextul o justifică; nu este activată de acest fișier.
