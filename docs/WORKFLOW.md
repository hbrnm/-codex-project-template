# Flux comun

## Alege efortul după sarcină
O corectură simplă: citește, modifică, verifică rezultatul și raportează.
O funcție sau un bug: clarifică rezultatul, implementează incremental și verifică.
Un proiect nou sau o schimbare complexă: brief, plan, implementare, review și dovezi.

| Etapă | Responsabil principal | Rezultat |
|---|---|---|
| Cerințe | requirements | Brief și criterii observabile |
| Plan | project-planning | Pași mici și dependențe |
| Înțelegere sistem | architecture-analysis | Răspuns fără editări, legat de dovezi și istoric disponibil |
| Bug | debugging | Reproducere, cauză, regresie |
| Implementare | coding-standards | Schimbare minimă completă |
| Teste de comportament | tdd-workflow | Dovezi RED/GREEN când sunt posibile |
| Interfață | ui-design | Direcție coerentă și verificare mobilă |
| Diagramă | diagramming | Relații și etichete verificate |
| Review | code-review | Constatări concrete și remedieri |
| Securitate | security-review | Riscuri relevante verificate |
| Finalizare | verification-loop | Rezultate și limite explicite |
| Redactare | clear-writing | Text clar, cu faptele păstrate |
| Skill nou | skill-authoring | Scop distinct și scenarii de evaluare |

Responsabil înseamnă procedura care conduce etapa, nu un proces sau agent pornit automat.
Dacă o sarcină acoperă mai multe etape, folosește procedurile pe rând. De exemplu,
un bug cu logică nouă folosește debugging pentru cauză, tdd-workflow pentru regresie
și verification-loop pentru raportul final.

## Coordonare
Pentru mai multe sarcini reale, folosește o listă cu: obiectiv, responsabil,
fișiere deținute, dependențe, stare și dovadă de finalizare.
Stările sunt planificat → în lucru → verificat; blocat este o stare explicită.
Un agent disponibil poate deține o sarcină independentă. Nu atribui în paralel
editarea acelorași fișiere. În lipsa subagenților, același flux se execută secvențial.
Nu instala Paperclip pentru această convenție.

## Continuitate și decizii
Folosește [HANDOFF.md](HANDOFF.md) la schimbarea sesiunii sau la un blocaj lung.
Documentează o decizie arhitecturală importantă folosind [ADR-TEMPLATE.md](ADR-TEMPLATE.md),
respectând convenția proiectului dacă există deja.
Nu duplica specificații și loguri: folosește linkuri și păstrează faptele actuale.

## Definiția finalizării
- Cerința și criteriile ei sunt acoperite sau limitarea este explicită.
- Diff-ul este relevant; schimbările transversale sunt explicate.
- Verificările potrivite au rezultate reale și eșecurile sunt rezolvate ori raportate.
- Datele și permisiunile rămân în limitele cererii.
- Documentația afectată și contextul necesar continuării sunt actualizate.


## Proceduri specifice proiectului
După alegerea tehnologiei folosește [profilul proiectului](STACK-PROFILE.md).
verification-loop conduce [verificarea web](BROWSER-VERIFICATION.md) și, când
funcția folosește modele, [evaluarea AI](AI-EVALUATION.md). Aceste proceduri nu
înlocuiesc testele comportamentale sau deciziile vizuale din ui-design.
