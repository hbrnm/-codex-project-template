# Surse, selecție și licențe

Au fost examinate toate cele 14 repository-uri din lista atașată, împreună cu
baza ECC existentă. Revizia acoperă README-urile, structura, licențele și fișierele
selectate, nu un audit integral al codului sau testarea tuturor aplicațiilor.
Nu există o măsurătoare care să demonstreze că acest template este „suprem”.

## Ce este preluat

| Sursă | Decizie | Componenta utilă | Adaptare sau limită |
|---|---|---|---|
| [hbrnm/ECC](https://github.com/hbrnm/ECC/tree/25278e7d7b6cf6e6a4e7a6c8e10f14ff22f0eb5b) | Adaptare selectivă | Baza de securitate, planificare și verificare. | Fără instalare globală sau prag universal de coverage. |
| [anthropics/skills](https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44) | Adaptare selectivă | Structura skillurilor, evaluarea lor și designul intenționat. | Fără skillurile documentare source-available sau scripturi Claude. |
| [morluto/rea](https://github.com/morluto/rea/tree/06d1247836b1fc856c4a6ec29e2c81927f445dd9) | Adaptare selectivă | Analiză din dovezi și separarea sursei de comportamentul livrat. | REA și motoarele native rămân opționale. |
| [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail/tree/09c434ab73ca43761c5d8b0c5d341926c2fba710) | Adaptare selectivă | Cea mai mică schimbare completă, cu reutilizarea proiectului. | Fără personalitate persistentă sau minimalism care elimină cerințe. |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills/tree/aeac41d4d005999432bb7312f7ff06383a91d59d) | Adaptare selectivă | Depanare, review multidimensional, surse oficiale și ADR. | Fără proces obligatoriu amplu pentru orice editare. |
| [paperclipai/paperclip](https://github.com/paperclipai/paperclip/tree/cff331f6ca0a652b5e41641c68dfa5fa584c22ae) | Adaptare selectivă | Obiective, responsabilitate, stări și dovezi pentru sarcini. | Aplicația completă, serverul și agenții permanenți nu sunt instalați. |
| [nexu-io/open-design](https://github.com/nexu-io/open-design/tree/d297055b83b6226c2c5e40800bbb4287156c4025) | Adaptare selectivă | Brief vizual și separarea referințelor de deciziile de design. | Fără aplicația completă sau cataloagele sale de active. |
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill/tree/12af471f627f866411b4bd785b19646d3672784c) | Adaptare selectivă | Design potrivit subiectului, distincția pagină/ecran și review pe mobil. | Fără motorul de stil, scripturile Node sau estetica impusă global. |
| [tt-a1i/archify](https://github.com/tt-a1i/archify/tree/d6059331abbddb49bca380ff46dca8ce33158b04) | Adaptare selectivă | Diagrame bazate pe dovezi și alegerea tipului potrivit. | Fără renderer, șabloane ori generare HTML la fiecare răspuns. |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills/tree/be2a406907dbc61b73e6827ded415c96139d13a2) | Referință externă | Catalog pentru descoperirea integrărilor concrete. | Nu copiem catalogul și nu instalăm gateway-uri automat. |
| [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design/tree/0cf73c3fcc56667ad91a9a04c439ac6ccfabc9d1) | Adaptare selectivă | Claritate semantică, etichete și artefacte autonome când sunt utile. | Fără obligativitate HTML/SVG sau restricții estetice universale. |
| [blader/humanizer](https://github.com/blader/humanizer/tree/0ef9fe5bc3572734fd3ae6c448fe00a30cd5dcf0) | Adaptare selectivă | Redactare clară și păstrarea faptelor și a vocii autorului. | Fără exemplele sursei, promisiuni despre detectoare sau rescriere de cod. |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code/tree/e0351d1a1fa569ffe57ac1859ba5c100c848496f) | Referință externă | Referință externă pentru descoperirea resurselor. | Lista nu este copiată, tradusă sau adaptată. |
| [mattpocock/skills](https://github.com/mattpocock/skills/tree/59db609eb1e18aaf59b63284d0e52255aff0c63c) | Adaptare selectivă | Teste la interfețe publice, pași verticali și handoff fără duplicare. | Fără publicare automată de issue-uri sau confirmări de rutină repetate. |
| [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/6c16b23f1bacd0fdf240bb5141ef45e59e82c306) | Adaptare selectivă | Controlul scopului unui diff; exemple AI păstrate ca referințe. | Fără copierea aplicațiilor, chei, modele sau servicii impuse. |

## Evidență verificabilă
[sources.lock.json](../sources.lock.json) fixează commitul, fișierele citite,
licența evaluată și decizia pentru fiecare sursă.
[skills.registry.json](../skills.registry.json) asociază fiecare skill cu sursele sale.
[THIRD-PARTY-NOTICES.md](../THIRD-PARTY-NOTICES.md) păstrează atribuirea și licențele.

Procedurile sunt sinteze adaptate, autonome și modificate în română, nu instalări
ale pachetelor sursă. Nu sunt incluse scripturi, motoare, fonturi, imagini sau alte
active ale surselor. Metadatele de licență ale unui skill combinat reflectă
materialele MIT și/sau Apache-2.0 pe care le adaptează.

## Limite de licențiere
- Nu am preluat skillurile documentare Anthropic cu termeni source-available.
- Catalogul awesome-claude-code, CC-BY-NC-ND-4.0, rămâne referință externă.
- Licența unui catalog nu este o garanție pentru proiectele spre care trimite.
- README-ul exemplului RAG inspectat declară MIT, diferit de licența Apache-2.0
  de la rădăcină. Codul acelui exemplu nu este copiat. Vezi [integrările opționale](OPTIONAL-INTEGRATIONS.md).
- [LICENSE](../LICENSE) acoperă contribuțiile originale ale template-ului;
  materialele terțe își păstrează termenii proprii.

## Actualizare fără suprascriere oarbă
1. Alege sursa și un commit nou, nu o referință mobilă latest.
2. Compară doar componentele folosite și verifică licențele locale și notificările.
3. Verifică suprapunerea cu skillurile existente și politica comună.
4. Adaptează selectiv și actualizează registrul, lockfile-ul și atribuirea.
5. Rulează validarea și testele; evaluează separat comportamentul agentului.
6. Păstrează istoricul și o cale de revenire.

Proiectele create din template nu primesc automat actualizările acestuia.
