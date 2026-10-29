# Evaluarea recomandărilor Reddit

Postarea [What Codex skills do you can't live without?](https://www.reddit.com/r/codex/comments/1wjnrod/what_codex_skills_do_you_cant_live_without/)
a fost consultată la 2026-10-29. Comentariile sunt recomandări comunitare,
inclusiv autopromovare, nu rezultate comparative de performanță.

| Recomandare | Acoperire în template | Decizie |
|---|---|---|
| Guide (RunWield) | architecture-analysis cere deja dovezi și distinge observat/dedus/necunoscut | Completat modul fără editări, istoricul relevant și distincția integrat/publicat/activ. |
| Ideator (RunWield) | requirements și project-planning acoperă brief, clarificări și plan | Completată verificarea ipotezelor externe importante înainte de întrebări și PRD la cerere. |
| Anthropic frontend-design, OpenDesign | ui-design include deja ambele surse în registru | Păstrată procedura existentă. |
| Impeccable | ui-design acoperă design, accesibilitate, responsivitate și review | Evaluare ulterioară pe un proiect UI concret; nu instalăm un al doilea proces de design în template-ul fără aplicație. |
| Ponytail | coding-standards, tdd-workflow și code-review îl includ deja | Fără duplicare. |
| Cercetare, îmbunătățire prompturi, ton personal | requirements și clear-writing acoperă părți din aceste nevoi | Fără skill generic suplimentar; tonul personal cere exemple și o cerere concretă. |
| Homelab | Nu există infrastructură de acest fel în template | Specific proiectului; fără integrare. |
| LetMeShowYouSomething | Feedback prin pagină HTML offline | Opțional când există o nevoie concretă de review asincron; fără import de renderer. |

Completările sunt redactate pentru politica acestui template pornind de la
nevoile identificate în discuție. Nu au fost importate fișiere din RunWield,
Impeccable sau LetMeShowYouSomething și nu pretindem că am auditat pachetele lor.
Sursele și licențele adaptărilor existente rămân în registrul curent.
Înaintea unui import viitor trebuie verificate fișierele, commitul, licența,
compatibilitatea Cloud și conflictele cu politica comună.

## Utilizare

> Folosește architecture-analysis: explică de ce există această componentă,
> cu dovezi din cod și istoric, fără să modifici fișiere.

> Folosește requirements: verifică ipotezele importante ale ideii mele și
> scrie un PRD proporțional cu scopul. Nu începe implementarea.

## Verificare

Validatorul și testele structurale se rulează conform AGENTS.md. Au fost adăugate
scenarii pentru analiza fără editări, merge fără dovadă de publicare și cercetare
înainte de interviu. Aceste scenarii nu sunt evaluări comportamentale executate
și nu demonstrează că un model respectă întotdeauna procedura.
