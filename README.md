# SyntaxColor

El que et comentava era algo tipus això, la wikipedia té diguem 4 clases de contingut, en negreta en blau per les referencies, formules i text normal

![Foto Pantalla](Backpagetion.jpeg)

Extreure el codi html es senzill i hi han moduls de python que tel parsejen;

![Foto Pantalla](parsejen.mp4)

~~Bones Adrià, vale ja miraré quin paquet haig de importar per fer-ho. Però aleshores de conjunts {X,Y} com a dataset que faig servir. La Wikipedia mateixa ?~~

X: El text tal qual, sense labels
Y: Vector de (Paraula,Tipus, paraula,tipus,paraula,tipus)

Aleshores agafes dela wikipedia els articles i prepares per cada article (sols text) el seu vector corresponent.

~~Vaja tan fàcil ? (Bé potser a nivell de programar no ho és tant però és clar) I creus que sortirà quelcom útil ?~~

moduls per fer scrapping a wikipedia:wikipedia, re, reuests i, sobretot, beatutifulSouprequests*

~~I aquestes dades las tindré com dos fitxer o com concretament ?~~

aixó com vulguis
el que jo faria és per cada article
i que clase sigui un nombre per que quedi tot més compacte
un fitxer amb nom [ARTICLE_X].txt que sigui el text tal qual i un que sigui [ARTICLE_Y].csv
csv vol dir comma separated values
y seria basicament: PARAULA, CLASE. PARAULA, CLASE
moduls per fer scrapping a wikipedia
aleshores quan facis la xarxa doncs ja tindrás els fitxers amb les dades
per fer CSVs a python hi ha un módul que es diu CSV pro no et ratllis molt amb això nem fent poc a poc

~~Vale. Entec que farè un programa amb python que fagi tot això de forma automàtica no?~~
Sep.Python o el que vulguis pro si no es python ni javascript jo em moraria.
