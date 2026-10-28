# Template modular pentru Codex Cloud

Reguli în română și 13 skilluri autonome pentru proiecte noi.
Combină selectiv ECC cu surse comunitare verificate, păstrând o politică comună.
Nu conține încă o aplicație și nu presupune o tehnologie.

## Începe de pe telefon
1. Activează Settings → General → Template repository în GitHub, dacă nu este activ.
2. Alege Use this template → Create a new repository.
3. Acordă conexiunii GitHub acces la noul repository și deschide-l în Codex Cloud.
4. Pornește o sarcină cu mesajul de mai jos.
5. După alegerea tehnologiei, configurează mediul și completează comenzile reale.

> Citește AGENTS.md și docs/PROJECT-BRIEF.md. Vreau să construiesc [descriere].
> Folosește requirements pentru informațiile lipsă, apoi project-planning.
> Selectează numai procedurile relevante și implementează prima funcție verificabilă.
> Explică ce ai verificat și ce rămâne neconfirmat.

## Cum sunt evitate contradicțiile
[AGENTS.md](AGENTS.md) definește politica comună.
[WORKFLOW.md](docs/WORKFLOW.md) distribuie responsabilitățile între etape.
[CONFLICT-RESOLUTION.md](docs/CONFLICT-RESOLUTION.md) documentează alegerile dintre
surse: teste proporționale riscului, schimbare minimă completă, stilul proiectului
prioritar și instrumente externe opționale.

## Skilluri
| Skill | Responsabilitate |
|---|---|
| [coding-standards](.agents/skills/coding-standards/SKILL.md) | Claritate și cea mai mică schimbare completă |
| [project-planning](.agents/skills/project-planning/SKILL.md) | Planificare incrementală |
| [tdd-workflow](.agents/skills/tdd-workflow/SKILL.md) | Teste pe comportament |
| [security-review](.agents/skills/security-review/SKILL.md) | Review de securitate |
| [verification-loop](.agents/skills/verification-loop/SKILL.md) | Dovezi înainte de finalizare |
| [requirements](.agents/skills/requirements/SKILL.md) | Cerințe și criterii de acceptare |
| [debugging](.agents/skills/debugging/SKILL.md) | Depanare bazată pe dovezi |
| [code-review](.agents/skills/code-review/SKILL.md) | Review pe cinci dimensiuni |
| [ui-design](.agents/skills/ui-design/SKILL.md) | Design coerent și verificabil |
| [diagramming](.agents/skills/diagramming/SKILL.md) | Diagrame cu semantică verificabilă |
| [clear-writing](.agents/skills/clear-writing/SKILL.md) | Redactare clară cu păstrarea faptelor |
| [skill-authoring](.agents/skills/skill-authoring/SKILL.md) | Skilluri cu scop și evaluare |
| [architecture-analysis](.agents/skills/architecture-analysis/SKILL.md) | Analiza sistemelor din dovezi |

Registrul verificabil este [skills.registry.json](skills.registry.json).
Selectează un skill principal și consultă altele numai când sunt relevante.

## Documente de proiect
- [Brief](docs/PROJECT-BRIEF.md): rezultat, utilizatori și criterii de acceptare.
- [Brief vizual](docs/DESIGN-BRIEF.md): numai pentru proiecte cu UI.
- [Handoff](docs/HANDOFF.md): continuitate între sesiuni, fără secrete.
- [Șablon ADR](docs/ADR-TEMPLATE.md): decizii importante, când sunt necesare.
- [Șablon PR](.github/pull_request_template.md): rezultat, dovezi și limite.
- [Integrări opționale](docs/OPTIONAL-INTEGRATIONS.md): ce nu este instalat.

## Validarea template-ului
Necesită Python 3.10+; folosește numai biblioteca standard, fără instalare de pachete.

```bash
python3 scripts/validate_template.py
python3 -m unittest discover -s tests -v
```

Validatorul verifică structura, metadatele, registrul, sursele fixate, licențele
înregistrate și linkurile locale. Testele verifică și respingerea unor configurații
defecte. Aceste verificări nu demonstrează absența tuturor contradicțiilor semantice.

[Raportul integrării](docs/REVIEW-REPORT.md) consemnează verificările executate și limitele.

[Scenariile din evals](evals/README.md) verifică selecția și conflictele în sesiuni
reale de agent. Nu sunt prezentate ca rezultate runtime deja obținute.

## Descoperirea în Codex Cloud
Pornește o sarcină nouă după integrare și cere:

> Citește AGENTS.md. Distinge skillurile descoperite nativ de fișierele pe care
> le poți doar citi. Citește explicit verification-loop dacă nu este disponibil nativ.

Formatul SKILL.md nu garantează descoperirea în fiecare interfață.
Citirea explicită este alternativa manuală; nu dovedește instalarea unui plugin.
Template-ul nu activează MCP, hookuri, subagenți, servicii sau programări.

## Comenzi ale viitoarei aplicații
Acestea sunt separate de comenzile validatorului de template.

| Operație | Comandă | Stare |
|---|---|---|
| Instalare | Nedefinit | Tehnologie nealeasă |
| Pornire | Nedefinit | Tehnologie nealeasă |
| Build | Nedefinit | Tehnologie nealeasă |
| Teste aplicație | Nedefinit | Tehnologie nealeasă |
| Lint / tipuri | Nedefinit | Tehnologie nealeasă |

Completează versiunile runtime-ului și comenzile după alegerea tehnologiei.
Secretele și configurațiile Cloud se gestionează separat pentru fiecare proiect.
Nu este configurată publicarea sau o suită CI de aplicație.

## Surse și licențe
Vezi [selecția tuturor surselor](docs/SOURCES.md), [commituri și decizii](sources.lock.json)
și [notificările terților](THIRD-PARTY-NOTICES.md).
Contribuțiile originale sunt MIT; componentele adaptate își păstrează licențele
indicate în skilluri și notificări. [Istoricul ECC](docs/ECC-SOURCE.md) rămâne disponibil.
