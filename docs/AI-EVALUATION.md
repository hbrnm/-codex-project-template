# Evaluarea funcțiilor AI

Procedură a verification-loop când se schimbă promptul, modelul, căutarea,
contextul sau instrumentele unei funcții AI. Nu se aplică aplicațiilor fără AI.
Aceasta este evaluarea produsului; scenariile din evals testează separat
instrucțiunile agentului care dezvoltă produsul.

1. Definește comportamentul urmărit și un set mic, reprezentativ, de cazuri:
   uz normal, ambiguitate, intrări invalide, context insuficient și erori de
   furnizor. Pentru RAG include surse contradictorii sau absente; pentru un agent
   include instrucțiuni ostile în date externe și acțiuni fără autorizare.
2. Pentru fiecare caz păstrează intrarea fără date sensibile, contextul,
   rezultatul ori criteriul așteptat și severitatea unui eșec. Nu verifica doar
   o propoziție exactă când există mai multe răspunsuri corecte.
3. Stabilește înainte de rulare criteriile și pragurile potrivite produsului:
   corectitudine, susținerea citatelor, respectarea schemei, utilizarea corectă
   a instrumentelor și recunoașterea lipsei informației. Nu inventa praguri universale.
4. Notează versiunea promptului, modelul/versiunea oferită de furnizor,
   parametrii, datele și configurația retrieval. Compară varianta de bază cu
   schimbarea pe aceleași cazuri și condiții. Pentru variabilitate relevantă,
   repetă cazurile în bugetul convenit și raportează distribuția și eșecurile.
5. Folosește verificări deterministe pentru scheme, limite și apeluri de tool;
   review uman cu rubrică pentru sens și utilitate. Dacă folosești un model
   evaluator, documentează-l și verifică un eșantion manual. Scorul lui nu este
   o dovadă independentă de adevăr.
6. Măsoară latența, erorile și consumul raportat. Separă costul măsurat de
   estimarea calculată cu tariful și data sursei; nu inventa consum lipsă.
7. Rulează verificările locale fără apeluri plătite când este posibil.
   Confirmă furnizorul, accesul și bugetul autorizat înaintea unei evaluări live;
   nu porni automat alte modele, servicii sau acțiuni externe reale. Simulează
   instrumentele cu efecte externe și etichetează limitarea simulării.
8. Păstrează cazurile de regresie și compară rezultatul cu baza; nu elimina
   cazurile eșuate ca să crească scorul. Raportează compromisurile și blocajele.

Raport: versiuni, set de cazuri, rubrică, rezultate pe caz și agregate, erori
critice, latență/cost și limite. Marchează evaluarea live Neexecutat dacă nu a
rulat. Testele cu răspunsuri simulate verifică integrarea, nu calitatea modelului.
Un set mic poate găsi regresii; nu demonstrează calitatea în toate situațiile.
