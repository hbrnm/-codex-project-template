# Verificarea unui flux web complet

Procedură a verification-loop pentru o funcție web modificată. ui-design decide
direcția vizuală; această procedură verifică rezultatul executat.
Template-ul nu conține o aplicație sau un browser instalat.

1. Identifică mediul, versiunea testată, URL-ul și criteriul de acceptare.
   Folosește comenzile reale din proiect și instrumentul disponibil, de exemplu
   suita Playwright existentă. Confirmă disponibilitatea browserului înainte să
   pretinzi execuția; un răspuns HTTP 200 nu dovedește funcționarea interfeței.
2. Alege fluxul afectat și date demonstrative izolate. Folosește un cont de test
   și mediul de dezvoltare/test. Nu efectua plăți, mesaje reale ori modificări
   ale datelor de producție fără autorizarea acelei operații.
3. Execută acțiunea în browser și urmărește rezultatul vizibil, cererea API,
   statusul și răspunsul relevant. Inspectează consola și cererile eșuate;
   nu păstra tokenuri, cookie-uri sau date personale în raport.
4. Dacă fluxul salvează date, verifică rezultatul după reîncărcare și, când
   este relevant, într-o sesiune nouă. Coroborează cu o citire autorizată din
   API/stocare când accesul există. Un toast sau un mock nu dovedește persistența
   reală. Dacă lipsește accesul la un strat, marchează limita fără a inventa probe.
5. Verifică erorile importante: date invalide, eroare API, acces neautorizat,
   încărcare și lipsa rezultatelor, după ce afectează schimbarea. Folosește
   simulări numai în mediul de test și etichetează ce a fost simulat.
6. Pentru UI afectat verifică desktop și mobil la 360, 390 și 430 px, tastatură,
   focus, etichete, overflow, contrast și mișcare redusă. O captură nu dovedește
   accesibilitatea; adaugă interacțiuni și verificările automate disponibile.
7. Păstrează capturi sau rezultate de teste numai în locul convenit de proiect,
   fără date sensibile. Curăță numai datele de test create de tine, când este sigur.

Raportează: mediu și versiune, flux, pași, rezultat așteptat/observat, dovadă,
stare și limitări. Distinge testul local, cu mock și pe deployment real.
Dacă lipsește browserul, execută verificările posibile și marchează browserul
Neexecutat; explică ce rămâne de verificat. Nu declara fluxul complet Trecut
când o parte necesară nu a fost verificată. Pentru o aplicație fără UI se aplică
API și stocare, iar browserul este Nu se aplică.
