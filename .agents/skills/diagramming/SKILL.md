---
name: diagramming
description: "Folosește când relațiile, fluxurile sau stările sunt explicate mai clar printr-o diagramă."
license: "MIT AND Apache-2.0"
---

# Diagrame cu semantică verificabilă

Adaptare modificată în română, 2026-10-28. Surse: archify, diagram-design.
Vezi [proveniența și licențele](../../../docs/SOURCES.md).
Se aplică [politica comună](../../../AGENTS.md); acest skill nu o înlocuiește.

1. Definește întrebarea și publicul. Pentru o listă simplă folosește o listă sau un tabel.
2. Extrage entitățile și relațiile din dovezi. Pentru cod, indică fișierele și traseul;
   pentru o propunere, etichetează explicit elementele propuse.
3. Alege tipul potrivit: arhitectură, secvență, flux, stări sau model de date.
4. Pentru o diagramă mică în documentație folosește Mermaid dacă este suficient.
   Pentru un artefact interactiv ori de export folosește HTML/SVG autonom când este util.
5. Păstrează același sens între text și diagramă: direcții, condiții, limite, chei
   și relații trebuie să reflecte dovezile.
6. Folosește etichete clare și stilul proiectului. Separă vederile când densitatea
   împiedică lectura; nu elimina relații esențiale pentru un număr arbitrar de noduri.
7. Verifică etichetele, muchiile, suprapunerile și lizibilitatea pe telefon.
   Dacă nu ai renderer sau browser, notează limita.
8. Livrează artefactul și explicația scurtă a ceea ce demonstrează.

Nu pretinde că ai rulat validatorul Archify sau exportul diagram-design:
aceste motoare nu sunt incluse. Nu încărca date private în renderere externe.
Nu genera automat o pagină HTML pentru fiecare răspuns.
