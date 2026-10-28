# Proveniență ECC

- Sursă: https://github.com/hbrnm/ECC
- Proiect original: https://github.com/affaan-m/ECC
- Commit sursă: `25278e7d7b6cf6e6a4e7a6c8e10f14ff22f0eb5b`
- Data preluării: 2026-10-28
- Licență sursă: MIT; [notificarea originală](../licenses/ECC-MIT.txt).

## Componente și adaptări

Acest template conține rezumate rescrise și adaptate în română, nu o copie
completă sau o instalare ECC. Fișierele SKILL.md sunt autonome și nu necesită
scripturi ECC, resurse partajate externe sau fișiere de metadate opționale.

| Componentă locală | Sursă la commitul fixat |
|---|---|
| coding-standards | .agents/skills/coding-standards/SKILL.md |
| project-planning | agents/planner.md |
| tdd-workflow | .agents/skills/tdd-workflow/SKILL.md și skills/tdd-workflow/SKILL.md |
| security-review | .agents/skills/security-review/SKILL.md |
| verification-loop | .agents/skills/verification-loop/SKILL.md |

Fișierele sursă pot fi consultate la:
https://github.com/hbrnm/ECC/tree/25278e7d7b6cf6e6a4e7a6c8e10f14ff22f0eb5b

Adaptări:
- Planificarea este în conversație. plan-canvas a fost exclus deoarece fluxul
  său folosește un server local și feedback din browser.
- Sunt eliminate presupunerile despre Claude Code, comenzi slash, MCP și hookuri.
- Nu sunt impuse un framework, scripturi npm, servicii sau modele.
- Pragul ECC de coverage 80% nu devine o cerință universală; proiectele își
  documentează pragurile după alegerea tehnologiei.
- Sunt păstrate ciclul test-remediere și raportarea sinceră a dovezilor,
  fără commituri automate pentru fiecare etapă.
- Exemplele specifice de framework sunt înlocuite cu verificări generale.
- Nu se aplică automat actualizări de dependențe sau instalări globale.
- AGENTS.md și documentația sunt adaptate scopului acestui template.

## Evoluția template-ului
Versiunea extinsă combină aceste proceduri cu alte surse. Această pagină
păstrează istoricul inițial ECC; pentru componența curentă, vezi
[SOURCES.md](SOURCES.md) și [registrul](../skills.registry.json).
Planificarea, testarea, standardele și verificarea au fost rescrise pentru
politica comună. Nu mai este un template exclusiv ECC.

## Compatibilitate
Fișierele au metadate name, description și license. Descoperirea nativă,
instrumentele și eventualele interfețe de activare depind de mediul Codex.
Acest repository nu confirmă disponibilitatea subagenților, hookurilor sau MCP.
Citirea explicită a SKILL.md rămâne o procedură manuală, nu o instalare de plugin.

## Actualizare
1. Alege un nou commit ECC și compară numai fișierele sursă relevante.
2. Revizuiește procedurile și dependențele nou introduse.
3. Adaptează selectiv fișierele locale; nu suprascrie regulile proiectului.
4. Păstrează notificarea licenței și actualizează commitul și lista adaptărilor.
5. Verifică linkurile și metadatele; confirmă separat încărcarea în mediul Codex.
6. Revizuiește și integrează schimbările prin fluxul GitHub al proiectului.

Proiectele deja create din template nu primesc automat actualizările acestuia.
