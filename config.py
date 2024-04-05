# Algemene variabelen

vakGrootte = 16 # Geeft aan dat de grootte van elk vak in de game 16x16 is
framerate = 60 # Bepaalt het aantal frame updates per seconde
mapScale = 4 # De schaalverhouding van de map
slot = 0 # De geselecteerde slot bij het opstarten van de game
schermBreedte = 1000 # De breedte van het scherm
schermHoogte = 563 # De hoogte van het scherm

# Lagen

spelerLaag = 3 # De renderlaag waarin de speler zich bevindt
borderLaag = 2 # De laag waarin de mapborders zich bevinden
achtergrondLaag = 1 # De renderlaag waar de achtergrond zich in bevindt

# Speler

spelerSnelheid = 0.3*mapScale # Het aantal pixels die de speler beweegt per movement event
x = 0 # De x coordinaat van de speler
y = 0 # De y coordinaat van de speler
playerSize = 4 # De grootte van de speler

# Inventaris en items

item = ["leeg", "aardbei", "tomaat"] # Alle items in de game
guiScale = 4 # De schaalverhouding van het grafische interface (inventaris)