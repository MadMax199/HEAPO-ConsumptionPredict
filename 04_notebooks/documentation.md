
# Interpretation der Plots
![alt text](image-4.png)

In einem ersten Schritt wurden alle metrischen Variablen und deren Zusammenhang betrachtet. Hierbei wurde sich fokussiert wie das Wetter, der Marktpreis, die Wärmepumpe sowie die PV Einspesiugn den Gesamtverbrauch beeinflussen. 
Die Gurndsätzliche Annahme ist, dass ein zunehmender Verbrauch der Wärmepumpe auch den Gesamtverbrauch erhöhte.Der Verbrauch der Wärmepumpe wird dabei durch kältere Temperaturen erhöht. Diesen Zusammenhang sieht man im ersten Plot deutlich. 
So sinkt bei einem Anstieg der Durchschnitts Temperatur auch der kwh Verbrauch der Wärmepumpe (WP). Auch für den Gesamtverbrauch lässt sich dieser Zusammenhang beobachten. Anhand der Farbskala wird aber auch deutlich, dass sich dieser Zusammenhang besonders in der Heizperiode von Oktober bis März beobachten lässt.Demnsprechend beeinflusst ein höherer Verbrauch der Wärmepumpe auch stärker den Gesamtverbrauch eines Haushaltes wie Plot 3 zeigt. 

Ein weiterer Einflussfaktor bidlet der Preis. Im Zuge der Ukraine Krise kann ein starker Anstieg im Strompreis beobachtet werden (siehe Grafik2). Im Scatterplot wird auich klar, dass ein leicht negativer zusammenhang zwischen dem Preis und dem Vebrrauch vorliegt. Dies scheint sich aber auf hohe Preiswerte in den SommermonatEN zurückführen lassen. Man sieht die Punkte sehr deutlich am unteren Rand der Grafik. 
Dahingegen wirkt die Einspeisung einer PV Anlage negativ auf den Verbrauch. So sinkt der Vebrrauch bei einem Anstieg der PV Einspeisung in den Sommermonaten. Denn bevor Strom in das Netz eingespeist wird, wird es zuerst verbraucht. Somit hat eine PV Anlage in einem Haushalt einen geringeren Nezubezug zur folge. 

![alt text](image-6.png)

Schaut man sich den Zusammenhang der Faktoren auf den Verbrauch noch im Zeiterverlauf genauer an, werden die Interpretationen noch deutlicher. So sieht man deutlich, dass Verbrauchspeaks in der kalten Jahreszeit auftauchenen. Der Anteil der Wärmepumpe spielt dabei allerdings nur eine geringe Rolle wie der letzte Zeitverlauf Plot zeigt. Demnach scheint der Stromverbrauch weniger stark durch den Verbrauch einer Wärmepumpe beeinflusst zu werden. Für die Solareinspeisung und die Preisentwicklung lässt sich wiederum die vorherige Interpretation übernehmen. Der Preispeak im zweiten Halbjahr 2022 ist deutlich zu sehen.

![alt text](image-7.png)

Neben dem Einfluss des Gebäudezustands hat die beheizte Fläche den erwartungsgemäß stärksten positiven Einfluss auf den Verbrauch. Mit jedem Anstieg der Wohnfläche skaliert auch der Energiebedarf, da die zu deckende Transmissionswärmelast linear mit der Gebäudegeometrie wächst.Ergänzend dazu zeigt sich beim Nutzerverhalten ein ähnliches Bild: Eine höhere Anzahl an Bewohnern führt zu einem Anstieg der Grundlast, was primär auf die Warmwasseraufbereitung und den allgemeinen Haushaltsstrom zurückzuführen ist. In der Kombination dieser Faktoren lassen sich so klare Lastprofile ableiten, die als Basis für eine intelligente Steuerung dienen.


![alt text](image-8.png)

Für die Verteilung des Verbrauchs auf die Anzahl der Bewohner wird wiederum ersichtlich, dass der meiste Strom in zwei Personen Haushalten verbraucht wird. Dies ist insofern aber auch nicht verwunderlich, da auch die meisten Haushalte in den Daten Zweipersonen Haushalte sind.


![alt text](image-9.png)

In der Korrelationsanalyse wird deutlich, dass Häuser ohne sanierte Fenster, Fassaden oder Dächer einen systematisch höheren Energieverbrauch aufweisen. Der Sanierungsstatus fungiert hierbei als einer der stärksten negativen Korrelatoren: Je umfassender die thermische Hülle ertüchtigt wurde, desto niedriger liegt das Basisniveau des Strombezugs.Gleichwohl zeigt die Bestandsanalyse, dass der Anteil der sanierten Häuser im Portfolio deutlich geringer ausfällt. Wir verfügen somit über wesentlich weniger Beobachtungen von sanierten Objekten im Vergleich zu jenen im Originalzustand. Diese Ungleichverteilung im Datensatz unterstreicht das enorme Optimierungspotenzial innerhalb der untersuchten Flotte.

![alt text](image-10.png)

Die vorliegende Korrelationsanalyse zeichnet ein präzises Bild der Einflussfaktoren auf den gesamten Strombezug (kwh_received_total) und verdeutlicht die Hebelwirkung technischer sowie baulicher Parameter. Es wird ersichtlich, dass vor allem die Dimensionierung der thermischen Erschließung den stärksten positiven Zusammenhang mit dem Energiebedarf aufweist: Insbesondere die Anzahl und Tiefe der Erdsonden (heatpump_groundsource_brinecircuit_numberofholes / length) korrelieren hochgradig mit einem gesteigerten Strombezug, was auf großvolumige Objekte mit entsprechend hohem Heizlastprofil hindeutet. Flankiert wird dieser Befund durch die Gebäudegröße (building_floorareaheated), die als klassischer Skaleneffekt den Basislastgang nach oben treibt.

Im Gegenzug identifiziert die Analyse die Modernisierung und technologische Effizienz als die entscheidenden negativen Korrelatoren. Ein jüngeres Installationsdatum der Wärmepumpe (heatpump_installation_year) sowie regelmäßige Wartungszyklen, wie die Entkalkung des Warmwasserspeichers (dhw_storage_lastdescaling_year), gehen systematisch mit einem sinkenden Gesamtverbrauch einher. Dies lässt darauf schließen, dass technischer Fortschritt und optimierte Betriebsparameter die Effizienzgewinne direkt in messbare Einsparungen beim Netzbezug übersetzen. Besonders hervorzuheben ist hierbei die Rolle von Photovoltaikanlagen (installation_haspvsystem): Diese fungieren als einer der stärksten Gegenspieler zum Strombezug, da sie durch Eigenstromnutzung das Niveau der extern bezogenen Kilowattstunden signifikant absenken.Somit lässt sich postulieren, dass nicht der Wärmepumpenverbrauch per se den Gesamtverbrauch erklärt, sondern vielmehr der technische Zustand der Wärmepumpe.

Gleichwohl zeigt ein Blick auf die baulichen Sanierungsmaßnahmen wie die Dämmung der Außenwände (building_renovated_walls), dass diese zwar einen mindernden Effekt erzielen, in der Gesamthierarchie der Treiber jedoch hinter den rein anlagentechnischen Faktoren und der PV-Integration zurückbleiben. Diese Gewichtung unterstreicht, dass innerhalb der untersuchten Stichprobe der technologische Standard der Heizungsanlage und die Fähigkeit zur Eigenstromerzeugung derzeit die einflussreichsten Stellschrauben für die energetische Performance darstellen. Während klimatische Variablen wie Außentemperatur und Sonnenscheindauer den Verbrauch erwartungsgemäß saisonal dämpfen, verbleibt das größte gestaltbare Optimierungspotenzial in der konsequenten Erneuerung des Anlagenbestands und dem Ausbau dezentraler Erzeugungskapazitäten.