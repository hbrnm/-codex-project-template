---
name: ui-design
description: "Folosește la UI nou, redesign și review vizual pentru a transforma brief-ul în alegeri concrete și accesibile."
license: "MIT AND Apache-2.0"
---

# Design coerent și verificabil

Adaptare modificată în română, 2026-10-28. Surse: anthropic, open-design, taste.
Vezi [proveniența și licențele](../../../docs/SOURCES.md).
Se aplică [politica comună](../../../AGENTS.md); acest skill nu o înlocuiește.

1. Citește brief-ul, designul existent și referințele furnizate. Distinge pagina de
   prezentare de ecranul de lucru; au densități și scopuri diferite.
2. Refolosește identitatea și componentele proiectului înaintea unor preferințe noi.
3. Completează [brief-ul vizual](../../../docs/DESIGN-BRIEF.md): public, acțiune
   principală, paletă, tipografie, spațiere, compoziție, stări și constrângeri.
4. Separă ce este observat sau furnizat de ceea ce propui. Alege o direcție coerentă
   potrivită subiectului; nu combina arbitrar stiluri pentru a părea original.
5. Folosește conținut real. Nu inventa testimoniale, clienți, numere sau rezultate.
   Marchează datele demonstrative. Păstrează proveniența și drepturile imaginilor.
6. Implementează responsiv, cu semantică, etichete, focus, tastatură, contrast și
   preferința pentru mișcare redusă. Efectele trebuie să ajute utilizatorul.
7. Când browserul este disponibil, verifică la 360, 390 și 430 px și pe desktop:
   overflow, lizibilitate, interacțiuni, stări de încărcare, gol și eroare.
8. Compară rezultatul cu brief-ul și corectează problemele; raportează ce ai văzut
   efectiv și ce ai evaluat doar din cod.

Nu există interdicții universale asupra cardurilor, umbrelor, fonturilor,
gradientelor sau Mermaid. Cererea și sistemul vizual al proiectului decid.
Nu copia logo-uri și alte elemente protejate din referințe fără drepturi.
Nu presupune existența scripturilor Taste, a browserului ori a OpenDesign.

## De la brief la ecran
Pentru UI nou sau redesign semnificativ, schițează înainte de cod un plan compact:
culori și roluri, familii și scară tipografică, spațiere, aliniere și compoziție.
Reutilizează tokenurile existente; pentru un proiect nou definește valori concrete.
Verifică planul față de brief și corectează alegerile care nu au o justificare
în conținut ori în nevoile publicului. Nu cere o aprobare suplimentară pentru
alegeri reversibile deja autorizate și nu impune acest pas unei corecturi mici.

Tipografia trebuie să păstreze o ierarhie lizibilă și lungimi de rând potrivite.
Numerotarea exprimă o ordine reală; animația explică o schimbare sau atrage
atenția justificat. Verifică suprascrierile CSS care anulează spațierea intenționată.
Numește acțiunile concret și consecvent între buton și confirmare. Pentru eroare
spune ce s-a întâmplat și ce poate face utilizatorul; pentru starea goală indică
următorul pas. Evită termenii de implementare în interfața utilizatorului.

Compară capturile cu brief-ul când ai browser; păstrează dovezile și limitele
conform [procedurii de verificare](../../../docs/BROWSER-VERIFICATION.md).

