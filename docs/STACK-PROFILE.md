# Alegerea procedurilor după tehnologie

Completează după alegerea tehnologiei, în legătură cu [brief-ul](PROJECT-BRIEF.md).
Nu alege un framework, o bază de date sau o platformă doar pentru că există
un skill pentru ele. Acest document nu instalează pachete, pluginuri ori conturi.

| Context confirmat | Ce verificăm | Unde se consemnează |
|---|---|---|
| React/Next.js sau alt UI | Versiuni, componente, accesibilitate, randare și convenții reale | README și instrucțiuni locale relevante |
| API și bază de date | Schema, validare, autorizare, migrații, backup și recuperare după erori | README, teste și ADR când decizia o cere |
| Deployment | Provider, medii, secrete doar prin nume, comenzi, health check și rollback | README și configurația platformei |
| Funcție AI | Furnizor, modele, date, criterii de evaluare și buget | Documentația funcției și evaluările ei |

1. Inspectează manifestele, lockfile-urile și configurația existente. Notează
   versiunile și comenzile efective de instalare, pornire, build, teste și lint.
2. Caută instrucțiunile locale și skillurile disponibile pentru tehnologia
   confirmată. Citește numai ce servește sarcina; verifică documentația oficială
   pentru API-uri sensibile la versiune. Nu presupune instalarea unui skill extern.
3. Refolosește procedurile template-ului. Adaugă un skill specializat numai dacă
   există o responsabilitate repetată distinctă, fără dublarea celor existente.
   Urmează skill-authoring pentru proveniență, licențe, registru și evaluare.
4. Înainte de comenzi cu efecte asupra datelor sau deployment-ului verifică
   mediul țintă și autorizarea. Nu transforma configurarea locală într-o migrare
   sau publicare de producție implicită.
5. Verifică un prim flux complet cu comenzile reale. Până atunci comenzile și
   capabilitățile neconfirmate rămân marcate ca atare.

Pentru template-ul curent tehnologia este nealeasă; verificările de structură
sunt disponibile, iar verificările unei aplicații sunt Nu se aplică.
