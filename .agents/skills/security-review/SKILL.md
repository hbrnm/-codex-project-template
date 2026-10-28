---
name: security-review
description: "Folosește la autentificare, autorizare, date personale, secrete, input extern, API-uri, uploaduri și plăți."
license: MIT
---

# Review de securitate

Adaptare din ECC; vezi [proveniența](../../../docs/ECC-SOURCE.md).

1. Identifică datele sensibile, actorii și granițele de încredere ale schimbării.
2. Verifică secretele: fără valori în cod, exemple, loguri sau rezultate de tool.
   Folosește numele variabilelor și setările dedicate ale mediului.
3. Validează datele pe server: tip, dimensiune, format și limite potrivite.
4. Verifică autentificarea și autorizarea pe fiecare operație sensibilă,
   inclusiv accesul la resursele altor utilizatori.
5. Folosește interogări parametrizate; evită interpolarea inputului în SQL,
   comenzi shell, căi și URL-uri. Verifică SSRF și traversarea directoarelor
   unde sunt relevante.
6. Pentru web, verifică escaping-ul, HTML-ul introdus de utilizator, sesiunile,
   cookie-urile, CSRF și CORS conform modelului de autentificare ales.
7. Pentru uploaduri, verifică dimensiunea, conținutul, destinația și permisiunile.
8. Pentru plăți și webhookuri, verifică semnătura, suma, actorul și idempotenta.
9. Evită expunerea datelor în erori și loguri. Aplică limite operațiilor costisitoare.
10. Folosește auditul de dependențe existent, când este disponibil.
    Evaluează rezultatele; nu rula automat actualizări sau remedieri în masă.

Adaugă teste pentru acces neautorizat, input invalid și cazurile sensibile
atinse de schimbare. Nu testa sisteme externe fără autorizare.

Raportează fiecare constatare cu severitate, fișier, impact și remediere.
Marchează verificările inaplicabile. O căutare după șiruri nu este un audit complet.
Nu declara „fără vulnerabilități” pe baza unei verificări parțiale.
