---
name: verification-loop
description: "Folosește înainte de finalizarea unei sarcini sau a unui PR pentru a verifica rezultatul și limitele sale."
license: "MIT AND Apache-2.0"
---

# Dovezi înainte de finalizare

Adaptare modificată în română, 2026-10-28. Surse: ecc, llm-apps.
Vezi [proveniența și licențele](../../../docs/SOURCES.md).
Se aplică [politica comună](../../../AGENTS.md); acest skill nu o înlocuiește.

1. Recitește cererea și criteriile de acceptare.
2. Citește diff-ul complet al sarcinii față de baza potrivită, nu doar ultimul commit.
3. Leagă fiecare fișier schimbat de cerință: păstrează dacă este necesar, separă
   dacă poate fi livrat independent, justifică dacă schimbarea transversală e indispensabilă.
   Numele fișierului sau numărul de linii sunt indicii, nu probe de lipsă de relevanță.
4. Identifică și rulează comenzile reale de build, tipuri, lint și teste relevante.
   Păstrează codul de ieșire real; nu ascunde eșecuri prin pipeline-uri de afișare.
5. Verifică fluxul UI/API afectat când mediul permite; inspectarea codului nu
   este echivalentă cu execuția în browser sau cu o tranzacție completă.
6. Aplică review-ul și verificările de securitate relevante.
7. Remediază eșecurile cauzate de schimbare și repetă verificările afectate.
8. Raportează fiecare verificare: metoda sau comanda, rezultatul și limita.

Folosește stările Trecut, Eșuat, Neexecutat și Nu se aplică. Nu inventa PASS.
Pentru template fără aplicație verifică structura, metadatele, manifestul,
proveniența și linkurile cu python3 scripts/validate_template.py.
Build-ul și testele aplicației nu se aplică până la alegerea tehnologiei.
Descoperirea nativă a skillurilor se confirmă separat într-o sesiune Codex;
validarea fișierelor nu demonstrează comportamentul agentului.
