from config import *
from sprites import *
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
        self.gameWindow.blit(achtergrond, player.pos)
        self.gameWindow.blit(inventarisGUI, (round(500-(guiScale*115)/2, 0), 450))
        self.gameWindow.blit(player.img, (500-7*4, round(282-4*20.5)))

        for vak in range(6):
            if item[0] == inventarisVakken[vak]:
                exit;
            else:
                for itemID in range(len(item)):
                    print(itemID)
                    if item[itemID] == inventarisVakken[vak]:
                        self.itemImg = pygame.transform.scale(pygame.image.load("img/" + item[itemID] + ".png"),(16*guiScale,16*guiScale))
                        self.gameWindow.blit(self.itemImg, inventaris.vakkenRectangles[vak])
            
            if vak == inventaris.slot:
                self.slotSelect = pygame.transform.scale(pygame.image.load("img/slot.png"),(16*guiScale,16*guiScale))
                self.gameWindow.blit(self.slotSelect, inventaris.vakkenRectangles[vak])

        
        #for zaad in range(player.zaadLocatie):



        pygame.display.update()

    def update(self): # Deze functie update de sprites
        pass


    def main(self, player, inventaris): # De main game loop
        events = pygame.event.get()

        for event in events:
            if event.type == QUIT:
                self.spelerSpeelt = False
                pygame.quit()
                sys.exit()
            else:
                inventaris.selectedSlot(event)

        player.update()
        #player.cropPlanten(inventaris.inventarisVakken, inventaris.itemHoeveelheden)
        self.render(inventaris.inventarisVakken)

class inventaris:

    def __init__(self):

        self.inventarisVakken = []
        self.vakkenRectangles = [(278,458),(278+76,458),(278+2*76,458),(278+3*76,458),(278+4*76, 458),(278+5*76,458)]

        self.itemHoeveelheden = [0, 0, 0, 0, 0, 0]

        for vak in range(6):
            self.inventarisVakken.append(item[0])

        self.slot = slot

    def selectedSlot(self, event):
        print('a')
        if event.type == pygame.MOUSEWHEEL:
            if event.y > 0 and self.slot < 5:
                self.slot += 1
            if event.y < 0 and self.slot > 0:
                self.slot -= 1
            #if event.type == pygame.KEYUP or event.type == pygame.KEYDOWN and event.key == pygame.K_q and self.slot > 0:
            #    self.slot -= 1
            #    print(self.slot)
            #if event.type == pygame.KEYUP or event.type == pygame.KEYDOWN and event.key == pygame.K_e and self.slot < 5:
            #    self.slot += 1
            #    print(self.slot)
        print(self.slot)

    #def pickUp(self):

    #   if interactEvent
    
    def update(self):
        self.selectedSlot()



achtergrond = pygame.transform.scale(pygame.image.load("img/achtergrond.png"), (mapScale*1000, mapScale*563))
inventarisGUI = pygame.transform.scale(pygame.image.load("img/inventaris.png"), (guiScale*115, guiScale*20))

game = game()
game.newGame()
inventaris = inventaris()
player = player(game)

while game.spelerSpeelt:
    game.main(player, inventaris)
