from config import *
from sprites import *
from inventaris import *
import pygame, sys
from pygame.locals import QUIT

class game:
    def __init__(self): # Initialisatie functie van de class game(), initialiseert pygame en verschillende parameters

        self.opgestart = True # Geeft aan dat de game is opgestart

        pygame.init()

        self.gameWindow = pygame.display.set_mode((schermBreedte, schermHoogte)) # g
        self.gameWindow.fill((255, 255, 255))
        #pygame.display.toggle_fullscreen()

        pygame.display.set_caption('Farming sim')

        self.clock = pygame.time.Clock()
        self.clock.tick(framerate)

    def newGame(self): # deze functie wordt aangeropen vanuit de main menu voor het maken van een nieuwe game
        self.spelerSpeelt = True # Bij het aanmaken van een nieuwe game zeggen we dat de speler vanaf dat punt aan het spelen is


    def render(self, inventarisVakken):

        self.gameWindow.blit(player.achtergrond, player.pos)
        self.gameWindow.blit(inventarisGUI, (round(500-(guiScale*115)/2, 0), 450))
        self.gameWindow.blit(player.img, (500-7*playerSize, round(282-playerSize*20.5)))

        if player.inHuis == False:
            self.gameWindow.blit(huisExt, (player.velocity_x+player.pos[0]+300, player.velocity_y+player.pos[1]+200))

        for vak in range(6):
            if item[0] == inventarisVakken[vak]:
                exit;
            else:
                for itemID in range(len(item)):
                    if item[itemID] == inventarisVakken[vak]:
                        self.itemImg = pygame.transform.scale(pygame.image.load("img/items/" + item[itemID] + ".png"),(16*guiScale,16*guiScale))
                        self.gameWindow.blit(self.itemImg, inventaris.vakkenRectangles[vak])
            
            if vak == inventaris.slot:
                self.slotSelect = pygame.transform.scale(pygame.image.load("img/slot.png"),(16*guiScale,16*guiScale))
                self.gameWindow.blit(self.slotSelect, inventaris.vakkenRectangles[vak])
        
        for crops in range(len(crop.zaadLocatie)):
            self.cropImg = pygame.transform.scale(pygame.image.load("img/items/" + crop.zaadSoort[crops] + ".png"),(16*guiScale,16*guiScale))
            self.gameWindow.blit(self.cropImg, (-400, -400))

        pygame.display.update()

    def update(self): # Deze functie update de sprites
        pass


    def main(self, player, inventaris, crop): # De main game loop
        events = pygame.event.get()

        for event in events:
            if event.type == QUIT:
                self.spelerSpeelt = False
                pygame.quit()
                sys.exit()
            else:
                inventaris.update(event)

        player.update()
        self.render(inventaris.inventarisVakken)
        print(inventaris.slot)


inventarisGUI = pygame.transform.scale(pygame.image.load("img/inventaris.png"), (guiScale*115, guiScale*20))
huisExt = pygame.transform.scale(pygame.image.load("img/huisExt.png"), (mapScale*100*1.4, mapScale*100*1.4))

game = game()
game.newGame()
inventaris = inventaris()
player = player(game)

while game.spelerSpeelt:
    game.main(player, inventaris, crop)
