# information_systems_integration
University project for the Information Systems Integration course

# Féléves feladat (4.)

## 2.
Készítsen egy alkalmazást, amely 3 kliensből áll. Az első kliens a `/queue/colorQueue` üzenetsorra pont-pont csatlakozással véletlenszerűen *RED*, *GREEN* és *BLUE* paraméterrel ellátott üzeneteket küld 1 másodpercenként. Készítsen három MDB-t amelyek filterrel a `RED`, `GREEN` és a `BLUE` paraméterrel ellátott üzeneteket kapják kizárólag. Az MDB-k véletlenszerűen átlagosan 10 ből 3 szor, rollback-elik az üzenetet, ami így a halott levél csatornára kerül. Minden 10 sikeresen megkapott (nem rollback-elt) üzenet után az MDB-k a `/queue/colorStatistics` sorra küldenek egy üzenetet, ami azt jelzi, hogy 10 (adott színű) üzenetet feldolgoztak. Készítsen egy második klienst, ami a `/queue/colorStatistics` sorrol olvassa a statisztikát és a konzolba kiírja hogy pl. `10 'RED' messages has been processed`. A harmadik kliens a `/queue/DLQ` halott levél csatornáról a konzolon jelzi, ha egy üzenetet nem dolgoztak fel.

## 4.
Készítsen alkalmazást, amely az 2. feladat alapján működik, annyi különbséggel, hogy a kliens egy webszolgáltatás, amely **SOAP**-on keresztül küldi a véletlenszerű színeket a webszolgáltatásnak, és a webszolgáltatás küldi tovább `/queue/colorQueue` üzenetsorra pont-pont csatlakozással az üzeneteket. Az ez utáni teendők megegyeznek az 2.-es feladatban leírtakkal. A lényeges különbség az, hogy a kliens nem kapcsolódik közvetlenül az üzenetsorra, hanem a futó szolgáltatás küldi tovább az üzenetet a sorra.
