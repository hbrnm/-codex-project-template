---
name: verification-loop
description: "Folosește înainte de finalizarea unei sarcini sau a unui PR pentru a verifica rezultatul și a raporta dovezile."
license: MIT
---

# Verificare înainte de finalizare

Adaptare din ECC; vezi [proveniența](../../../docs/ECC-SOURCE.md).

1. Recitește cererea și criteriile de acceptare.
2. Citește diff-ul complet al sarcinii față de baza ei, nu doar ultimul commit.
3. Identifică verificările reale din README și configurația proiectului.
4. Rulează build, verificarea tipurilor, lint și testele relevante, dacă există.
   Păstrează codul de ieșire real; nu masca eșecul într-un pipeline de afișare.
5. Pentru UI sau API, verifică fluxul relevant când mediul permite;
   distinge inspectarea codului de rularea efectivă în browser.
6. Verifică securitatea și cazurile limită afectate de schimbare.
7. Remediază eșecurile cauzate de schimbare și repetă verificările afectate.
8. Raportează rezultatul și orice blocaj rămas.

Raport:
| Verificare | Comandă sau metodă | Rezultat | Limitări |
|---|---|---|---|
| Build / tipuri / lint / teste / flux / review | Metoda reală | Trecut / Eșuat / Neexecutat / Nu se aplică | Motiv |

Pentru acest template fără aplicație, build-ul și testele de aplicație nu se
aplică încă. Verifică structura, linkurile locale și metadatele SKILL.md.
Nu inventa comenzi, nu instala hookuri și nu afirma că skillurile s-au încărcat
nativ dacă ai verificat doar fișierele.
