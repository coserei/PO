import pygame
pygame.init()

infox = int(pygame.display.get_desktop_sizes()[0][0])
infoy = int(pygame.display.get_desktop_sizes()[0][1])

save = open("Saved.txt")
data = save.readlines()

# Algemene variabelen

vakGrootte = 16 # Geeft aan dat de grootte van elk vak in de game 16x16 is
framerate = 60 # Bepaalt het aantal frame updates per seconde
mapScale = 4 # De schaalverhouding van de map
slot = 0 # De geselecteerde slot bij het opstarten van de game
schermBreedte = infox # De breedte van het scherm
schermHoogte = infoy # De hoogte van het scherm

# Lagen

spelerLaag = 3 # De renderlaag waarin de speler zich bevindt
borderLaag = 2 # De laag waarin de mapborders zich bevinden
achtergrondLaag = 1 # De renderlaag waar de achtergrond zich in bevindt

# Speler

spelerSnelheid = 1*mapScale # Het aantal pixels die de speler beweegt per movement event
x = float(data[0]) # De x coordinaat van de speler
y = float(data[1]) # De y coordinaat van de speler
playerSize = 4 # De grootte van de speler

# Inventaris en items

item = ["leeg", "appel", "banaan", "kers", "peer", "tomaat", "appelZaad", "banaanZaad", 
        "kersZaad", "peerZaad", "tomaatZaad", "bed1", "bed2", "bed3" "kaars1", "kaars2", 
        "kaars3", "muur1", "muur2", "muur3"] # Alle items in de game
guiScale = 4 # De schaalverhouding van het grafische interface (inventaris)

buyOptions = ["appelZaad", "banaanZaad", "kersZaad", "peerZaad", "tomaatZaad"] # Buy opties voor de farm shop
buyOptions2 = ["bed1", "bed2", "bed3", "kaars1", "kaars2", "kaars3", "muur1", "muur2", "muur3"] # Buy opties voor de huis shop

houseScale = 3
