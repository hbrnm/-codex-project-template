# Evaluare comportamentală

[scenarios.json](scenarios.json) conține cazuri de selecție, neactivare și conflict.
Sunt criterii de evaluare, nu scoruri sau dovezi că un model a trecut testele.

## Rulare în mediul real
1. Pornește o sesiune de test într-o copie a proiectului, cu versiunea și modelul notate.
2. Pentru fiecare scenariu, oferă contextul sau fixture-ul necesar și promptul.
3. Observă skillul principal și rezultatul. not_primary indică proceduri care
   nu ar trebui să conducă sarcina, nu o interdicție de consultare justificată.
4. Compară rezultatul cu criteriile acceptance. Notează Trecut, Eșuat sau Neexecutat.
5. Pentru modificări ale unui skill, compară aceleași cazuri înainte și după
   când mediul permite; păstrează variația observată și limitele.
6. Nu efectua acțiuni externe sau plătite numai pentru evaluare fără autorizare.

Tabel recomandat pentru rezultate:
| Caz | Model și versiune | Skill principal | Rezultat | Dovezi și limite |
|---|---|---|---|---|

Testele Python verifică integritatea scenariilor și structura template-ului.
Nu invocă un model, nu simulează un rezultat PASS și nu validează descoperirea
nativă a skillurilor în Cloud.
