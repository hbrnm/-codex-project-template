# Template pentru proiecte cu Codex Cloud

Bază pentru proiecte noi, cu reguli și cinci skilluri adaptate din ECC.
Nu conține încă o aplicație și nu presupune o tehnologie.

## Creează un proiect
1. În acest repository, activează Settings → General → Template repository.
2. Folosește Use this template → Create a new repository.
3. Acordă conexiunii GitHub acces la noul repository și selectează-l în Codex Cloud.
4. Cere completarea [brief-ului](docs/PROJECT-BRIEF.md), apoi alegerea tehnologiei.
5. După implementarea inițială, completează tabelul comenzilor de mai jos.
   Configurează separat mediul Cloud, secretele și integrările fiecărui proiect.

Exemplu de prim mesaj:

> Citește AGENTS.md și docs/PROJECT-BRIEF.md. Vreau o aplicație pentru [scop].
> Ajută-mă să completez cerințele, propune tehnologia și implementează prima
> funcție verificabilă. Documentează comenzile reale și verificările executate.

## Ce este inclus
- [AGENTS.md](AGENTS.md): instrucțiuni generale pentru lucru și comunicare în română.
- [coding-standards](.agents/skills/coding-standards/SKILL.md): claritate și convenții.
- [project-planning](.agents/skills/project-planning/SKILL.md): planificare în conversație.
- [tdd-workflow](.agents/skills/tdd-workflow/SKILL.md): teste pentru comportament.
- [security-review](.agents/skills/security-review/SKILL.md): verificări de securitate.
- [verification-loop](.agents/skills/verification-loop/SKILL.md): dovezi înainte de finalizare.
- [Șablon PR](.github/pull_request_template.md) și [proveniența ECC](docs/ECC-SOURCE.md).

## Verifică disponibilitatea skillurilor
Pornește o sarcină nouă după integrarea fișierelor și cere:

> Citește AGENTS.md. Identifică skillurile descoperite nativ din .agents/skills/.
> Distinge skillurile oferite de mediu de fișierele pe care le poți doar citi.
> Citește explicit skillul verification-loop și explică ce verificări se aplică acum.

Fișierele sunt în format SKILL.md cu metadate name și description.
Încărcarea efectivă depinde de versiunea și configurația Codex.
Dacă nu există descoperire nativă, cere citirea explicită a fișierului relevant.
Citirea manuală nu confirmă instalarea ca plugin.

## Comenzi ale aplicației
Nu există comenzi de aplicație până la alegerea tehnologiei.
Înlocuiește „Nedefinit” cu comenzi verificate și documentează versiunea runtime-ului.

| Operație | Comandă | Stare |
|---|---|---|
| Instalare | Nedefinit | Tehnologie nealeasă |
| Pornire | Nedefinit | Tehnologie nealeasă |
| Build | Nedefinit | Tehnologie nealeasă |
| Teste | Nedefinit | Tehnologie nealeasă |
| Lint / formatare | Nedefinit | Tehnologie nealeasă |
| Verificare tipuri | Nedefinit | Tehnologie nealeasă |

Nu sunt configurate CI, publicare, hookuri, MCP sau subagenți.
Template-ul copiază fișiere, nu setările Cloud sau secretele.
Procedurile sunt instrucțiuni, nu mecanisme care impun automat verificările.

## Proveniență și licență
Skillurile sunt adaptări documentate din ECC, nu o instalare completă ECC.
Notificarea MIT pentru materialele ECC se păstrează în [licența sursei](licenses/ECC-MIT.txt).
Vezi [sursele și actualizarea](docs/ECC-SOURCE.md).
