# Decizii pentru reguli care se contrazic

Aceste decizii se aplică variantelor adaptate din template, nu modifică proiectele sursă.
Politica platformei și cererea utilizatorului au prioritate.

| Tensiune între surse | Decizia comună |
|---|---|
| ECC: proces amplu și 80% coverage; Ponytail: schimbare minimă | Acoperim complet cerința cu verificări proporționale riscului. Pragul proiectului decide coverage. |
| ECC: refactor în ciclul TDD; Matt Pocock: refactor în review | Test și remediere pe un comportament; simplificare numai după GREEN, urmată de reverificare. |
| Confirmarea fiecărei interfețe de test; progres autonom | Folosim interfețele și contextul confirmat. Cerem clarificări numai pentru decizii care blochează. |
| Stiluri ferme din taste, frontend-design și diagram-design | Brief-ul, identitatea existentă și accesibilitatea decid. Nu există listă universală de fonturi sau efecte interzise. |
| diagram-design: HTML/SVG; Archify: runtime și schemă proprie | Un singur skill diagramming. Mermaid pentru diagrame simple; artefact autonom pentru interacțiune/export. Niciun runtime extern implicit. |
| Paperclip: orchestrare permanentă; Codex Cloud: capabilități variabile | Preluăm responsabilitatea sarcinilor și dovezile. Aplicația, agenții și programările rămân opționale. |
| REA: analiză de artefacte; proiect cu sursă disponibilă | Întâi analiza sursei cu instrumentele existente. REA numai când întrebarea necesită dovada din artefact sau runtime. |
| Humanizer: rescriere; documentație și cod exact | Rescriem proza, păstrăm faptele, comenzile, codul și țintele linkurilor. |
| Matt: handoff temporar; Cloud: sesiuni separate | Contextul durabil, fără secrete, stă în docs/HANDOFF.md. Notele temporare nu sunt singura sursă de continuitate. |
| Instalare completă versus fișiere autonome | Nu importăm instalatoare sau dependențe ascunse. Fiecare skill adaptat este autonom. |
| Afirmații README versus configurație și execuție | Configurația arată intenția; numai dovezile de execuție confirmă funcționarea. |
| Catalog disponibil versus licențe eterogene | Verificăm componenta concretă. Cataloagele sunt referințe, nu pachete de instalat integral. |

## Cum se rezolvă o contradicție nouă
Identifică cerința, fișierele și regulile în conflict. Verifică autoritatea și
domeniul lor. Aplică politica comună și regula cea mai specifică permisă pentru
implementare. Dacă alegerea afectează material scopul sau datele și rămâne
ambiguă, cere clarificarea necesară. Înregistrează o decizie importantă în ADR.

Nu „rezolva” o contradicție dezactivând teste sau ascunzând eșecuri.
Registrul structural poate detecta dubluri și referințe lipsă; nu poate demonstra
absența tuturor contradicțiilor semantice.
