# Bulls and cows
Druhý závěrečný projekt na Python Akademii od Engeta

## Popis projektu
Tento projekt je hra, která je postavená na hádání 4 ciferného čísla. 

## Pravidla a popis hry
Hra náhodně vygeneruje 4 tajné číslice a úkolem uživatele je napsat do konzole správné číslice a ve správném pořadí.

Hra po zadání čísla vypíše počet `bulls` a `cows`.<br>
1 `bull` = pokud uživatel uhodne jak číslo, tak jeho umístění<br>
1 `cow` = pokud uživatel uhodne číslo, ale ne jeho umístění

Hra končí ve chvíli, kdy uživatel uhodne všechny bulls.<br>
`4 bulls / 0 cow`

Zadané číslo musí splňovat:
 - Číslo musí mít 4 znaky.<br>
 - Číslo nesmí začínat nulou.<br>
 - V čísle nesmí být duplicity (čísla se nesmí opakovat).

Součástí hry jsou:<br>
 - Popis hry a pravidla<br>
 - Statistiky odehraných her 

## Ukázka hry
Spuštění hry:
```
Ahoj hráči!
Vítám tě ve hře Bulls and cows.
V hlavním menu zvol na klávesnici jednu z možností.
------------------------------------------------------
Hlavní menu:
 1 - Nová hra
 2 - Popis hry a pravidla
 3 - Statistiky
 q - Konec hry
------------------------------------------------------
Zvol menu (1/2/3/q):
```
Ukázka úspěšně dokončené hry:
```
------------------------------------------------------
Pro předčasné ukončení hry zmáčkni klávesu: q
------------------------------------------------------
Pojďme hrát.
------------------------------------------------------
Zadej 4ciferné číslo: 1234
1 bull / 1 cow
------------------------------------------------------
Zadej 4ciferné číslo: 1385
3 bulls / 0 cow
------------------------------------------------------
Zadej 4ciferné číslo: 1395
4 bulls / 0 cow
------------------------------------------------------
Správně, uhodl jsi tajné číslo.
Počet pokusů: 3
Odehraný čas:   0 hod : 0 min : 38 sek
------------------------------------------------------
Pro návrat do hlavního menu zadej písmeno q:
```
Ukázka statistik odehraných her:
```
Start hry: 09.10.2022 13:20:18, Dokončeno: Ano, Počet pokusů: 3, Odehraný čas: 0 hod : 0 min : 38 sek
Start hry: 09.10.2022 13:22:17, Dokončeno: Ano, Počet pokusů: 7, Odehraný čas: 0 hod : 2 min : 12 sek
Start hry: 09.10.2022 13:26:28, Dokončeno: Ne
```

