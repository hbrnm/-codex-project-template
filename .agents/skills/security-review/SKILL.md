---
name: security-review
description: "Folosește la autentificare, autorizare, date sensibile, input extern, API-uri, uploaduri și plăți."
license: "MIT"
---

# Review de securitate

Adaptare modificată în română, 2026-10-28. Surse: ecc.
Vezi [proveniența și licențele](../../../docs/SOURCES.md).
Se aplică [politica comună](../../../AGENTS.md); acest skill nu o înlocuiește.

1. Identifică actorii, datele sensibile și granițele de încredere ale schimbării.
2. Verifică secretele: fără valori reale în cod, exemple, loguri și răspunsuri.
3. Validează inputul pe server: tip, format, dimensiune și limite.
4. Verifică autorizarea la fiecare operație sensibilă și accesul între utilizatori.
5. Folosește interogări parametrizate. Verifică interpolarea în shell, căi și URL-uri,
   inclusiv SSRF și traversarea directoarelor unde sunt relevante.
6. Pentru web, verifică escaping, HTML extern, sesiuni, cookie-uri, CSRF și CORS
   potrivit modelului de autentificare, fără a impune mecanisme inaplicabile.
7. Pentru fișiere, verifică dimensiunea, conținutul, destinația și permisiunile.
8. Pentru plăți și webhookuri, verifică semnătura, actorul, suma și idempotenta.
9. Evită expunerea datelor în erori și loguri; limitează operațiile costisitoare.
10. Rulează auditul existent când este disponibil. Nu aplica automat actualizări
    sau remedieri în masă ale dependențelor.

Adaugă teste relevante pentru acces neautorizat și input invalid. Nu testa sisteme
externe în afara autorizării. Raportează severitate, locație, impact și remediere.
O căutare după șiruri nu este un audit complet; nu declara absența tuturor
vulnerabilităților după o verificare parțială.
