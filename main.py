from config import *
from sprites import *
from inventaris import *
import pygame, sys
from pygame.locals import QUIT

class game:

    # Tijd in uren

    tijd = 12
    dag = 0
    spelerklok = int(tijd)
    white = (255, 255, 255)
    spelgestart = False
    font = pygame.font.SysFont("castillo", 48)
    text = font.render(str(spelerklok) + ":00", True, (255, 255, 255))
    textRect = text.get_rect()

    def __init__(self): # Initialisatie functie van de class game(), initialiseert pygame en verschillende parameters

        pygame.init()

        self.opgestart = True # Geeft aan dat de game is opgestart

        self.gameWindow = pygame.display.set_mode((schermBreedte, schermHoogte)) # g
        self.gameWindow.fill((255, 255, 255))
        #pygame.display.toggle_fullscreen()

        pygame.display.set_caption('Farming sim')

        # Preloading images

        self.slotSelect = pygame.transform.scale(pygame.image.load("img/slot.png"),(16*guiScale,16*guiScale))

        self.clock = pygame.time.Clock()

        self.font = pygame.font.Font('font.ttf', 20)

        self.displayControls = False

    def newGame(self): # deze functie wordt aangeropen vanuit de main menu voor het maken van een nieuwe game
        self.spelerSpeelt = True # Bij het aanmaken van een nieuwe game zeggen we dat de speler vanaf dat punt aan het spelen is


    def render(self, inventarisVakken, zaadX):

        if not (player.shopSchermOpen == True or player.shop2SchermOpen == True):
            print(player.shop2SchermOpen)
            if player.inHuis == False:
                self.gameWindow.blit(huisExt, (player.velocity_x+player.pos[0]+300, player.velocity_y+player.pos[1]+200))
            self.gameWindow.blit(player.achtergrond, player.pos)
            self.gameWindow.blit(player.img, ((infox // 2)-7*playerSize, round((infoy // 2)-playerSize*20.5)))
            if len(zaadX) == 1:
                exit;
            else:
                for crops in range(1, len(crop.zaadX)):
                    self.cropImg = pygame.transform.scale(pygame.image.load("img/items/" + crop.zaadSoort[crops] + "Zaad.png"),(16*guiScale,16*guiScale))
                    self.gameWindow.blit(self.cropImg, (-crop.zaadX[crops]+player.velocity_x+player.pos[0]+(infox // 2)-7*playerSize, -crop.zaadY[crops]+player.velocity_y+player.pos[1]+round((infoy // 2)-playerSize*20.5)))

        self.gameWindow.blit(inventarisGUI, (round((infox // 2)-(guiScale*115)/2, 0), (infoy - 100)))

        for vak in range(6):
            if vak == inventaris.slot:
                self.gameWindow.blit(self.slotSelect, inventaris.vakkenRectangles[vak])

            if item[0] == inventarisVakken[vak]:
                exit;
            else:
                for itemID in range(len(item)):
                    if item[itemID] == inventarisVakken[vak]:
                        self.itemImg = pygame.transform.scale(pygame.image.load("img/items/" + item[itemID] + ".png"),(16*guiScale,16*guiScale))
                        self.gameWindow.blit(self.itemImg, inventaris.vakkenRectangles[vak])
                self.itemCount = self.font.render(str(inventaris.itemHoeveelheden[vak]), True, (0, 0, 0))
                self.gameWindow.blit(self.itemCount, (inventaris.vakkenRectangles[vak]))

        self.coinsAantal = self.font.render('Coins:  ' + str(shop.munten), True, (0, 0, 0))
        self.gameWindow.blit(self.coinsAantal, (5, 30))

        #empty = self.font.render("          ", True, (0, 0, 0))
        #self.gameWindow.blit(empty, self.textRect)
        self.gameWindow.blit(self.text, (5, self.textRect[1]))
        
        self.fps = self.font.render("FPS:" + self.fpsAmount, True, (0, 0, 0))
        self.gameWindow.blit(self.fps, (5, 60))
        pygame.display.update()

    def klok(self): # Deze functie update elke keer als de game update en werkt als klok
        #met 1/3000 zijn de dagen precies 20 minuten op een constante 60 fps
        self.tijd += 1/3000
        if self.tijd > 24:
            self.tijd = 0
            self.dag += 1
        self.spelerklok = str(int(self.tijd))

    def drawKlok(self): #drawt de klok op het scherm
        self.text = self.font.render('Dag: ' + str(self.dag) + "     " + self.spelerklok + ":00", True, (0, 0, 0))
        self.textRect = self.text.get_rect()
        #empty text omdat je anders text over elkaar heen krijgt


    def main(self, player, inventaris): # De main game loop

        events = pygame.event.get()
        button.pauze()

        if self.spelgestart:
            player.update()
            shop.update()
            self.render(inventaris.inventarisVakken, crop.zaadX)
            self.klok()
            self.drawKlok()
            player.cropGeplant = crop.update(player.pos, player.cropGeplant)

        for event in events:
            if event.type == QUIT:
                self.spelerSpeelt = False
                pygame.quit()
            else:
                inventaris.update(event)
            
            pygame.display.flip()
            self.clock.tick(framerate)
            self.fpsAmount = str(round(self.clock.get_fps()))

class shop:
    
    def __init__(self):
        self.munten = 900

        self.itemImages = []

        self.sellButton = pygame.image.load('img/sellButton.png').convert_alpha()
        self.sellButton = pygame.transform.scale(self.sellButton, (28*guiScale, 11*guiScale))

        self.buyButton = pygame.image.load('img/buyButton.png').convert_alpha()
        self.buyButton = pygame.transform.scale(self.buyButton, (24*guiScale, 11*guiScale))

        self.exitButtonShop = pygame.image.load('img/exitButtonShop.png').convert_alpha()
        self.exitButtonShop = pygame.transform.scale(self.exitButtonShop, (27*guiScale, 11*guiScale))

        self.buySelect = 0

        self.buyOptionsRect = []

    def shopOption(self):

        self.imageX = 200
        self.itemImages = []

        if player.shop2SchermOpen:
            self.buyOptions = buyOptions2
        if player.shopSchermOpen:
            self.buyOptions = buyOptions
    
        for items in range(len(self.buyOptions)):
            self.itemImage = pygame.image.load('img/items/'+self.buyOptions[items]+'.png').convert_alpha()
            self.itemImage = pygame.transform.scale(self.itemImage, (16*guiScale, 16*guiScale))
            self.itemImages.append(self.itemImage)

            self.buyOptionsRect.append([self.imageX, 200, 16*guiScale, 16*guiScale])
            self.imageX += 30*guiScale
            
        self.slotImage = pygame.image.load('img/slot.png').convert_alpha()
        self.slotImage = pygame.transform.scale(self.slotImage, (16*guiScale, 16*guiScale))

    def draw(self):

        self.imageX = 200
        game.gameWindow.fill((255,255,255))

        for items in range(len(self.buyOptions)):
            if self.buySelect == items:
                game.gameWindow.blit(self.slotImage,(self.imageX, 200))
            game.gameWindow.blit(self.itemImages[items],(self.imageX, 200))
            self.imageX += 30*guiScale

        game.gameWindow.blit(self.sellButton, (500, 300))
        game.gameWindow.blit(self.buyButton, (700, 300))
        game.gameWindow.blit(self.exitButtonShop, (200, 100))

    def buy(self):
        pos = pygame.mouse.get_pos()
        self.rect = pygame.Rect(700, 300, 24*guiScale, 11*guiScale)

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                if not self.munten <= 0 and (inventaris.inventarisVakken[inventaris.slot] == item[0] or inventaris.inventarisVakken[inventaris.slot] == self.buyOptions[self.buySelect]):
                    inventaris.inventarisVakken[inventaris.slot] = self.buyOptions[self.buySelect]
                    inventaris.itemHoeveelheden[inventaris.slot] += 1
                    self.munten -= 1

    def sell(self):
        pos = pygame.mouse.get_pos()
        self.rect = pygame.Rect(500, 300, 28*guiScale, 11*guiScale)

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                if inventaris.itemHoeveelheden[inventaris.slot] > 0:
                    inventaris.itemHoeveelheden[inventaris.slot] -= 1
                    self.munten += 1

    def buySelector(self):
        pos = pygame.mouse.get_pos()

        for items in range(len(self.buyOptions)):
            self.rect = pygame.Rect(self.buyOptionsRect[items])
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1:
                    self.buySelect = items

    def exit(self):
        pos = pygame.mouse.get_pos()
        self.rect = pygame.Rect(200,100,27*guiScale, 11*guiScale)

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                player.shopSchermOpen = False
                player.shop2SchermOpen = False

    def update(self):
        if player.shopSchermOpen or player.shop2SchermOpen:
            self.shopOption()
            self.buySelector()
            self.buy()
            self.sell()
            self.draw()
            self.exit()

class button():

    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()

        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # Geven de knoppen op het scherm neer
        
        game.gameWindow.blit(self.image, (self.rect.x, self.rect.y))

        if game.displayControls == True:
            game.gameWindow.blit(movementKeys, (infox / 2, infoy * 0.2))
            game.gameWindow.blit(huisBinnenGaan_key, (infox / 2, infoy * 0.4))
            game.gameWindow.blit(huisUitGaan_key, (infox / 2, infoy * 0.6))
            game.gameWindow.blit(cropsOppakken, (infox / 2, infoy * 0.8))

        return action

    def drawButtons():
        if game.spelgestart == False:
            game.gameWindow.fill((255, 255, 255))

            if game.displayControls == False:
                if start_button.draw():
                    game.spelgestart = True
                if exit_button.draw():
                    pygame.quit()
                    sys.exit()
                if controls_button.draw(): 
                    game.displayControls = True  
            if game.displayControls == True:
                if exit_controls.draw():
                    game.displayControls = False 

    def pauze():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            game.spelgestart = False


inventarisGUI = pygame.transform.scale(pygame.image.load("img/inventaris.png"), (guiScale*115, guiScale*20))
huisExt = pygame.transform.scale(pygame.image.load("img/huisExt.png"), (mapScale*100*1.4, mapScale*100*1.4))

game = game()
game.newGame()
player = player(game)
crop = crop()
shop = shop()

movementKeys = pygame.image.load('img/movement_keys.png').convert_alpha()
huisBinnenGaan_key = pygame.image.load('img/huisBinnenGaan_key.png').convert_alpha()
huisUitGaan_key = pygame.image.load('img/huisUitGaan_key.png').convert_alpha()
cropsOppakken = pygame.image.load('img/cropsOppakken.png').convert_alpha()

movementKeys = pygame.transform.scale(movementKeys, (int(185 * 2), int(45 * 2)))
huisBinnenGaan_key = pygame.transform.scale(huisBinnenGaan_key, (int(194 * 2), int(22 * 2)))
huisUitGaan_key = pygame.transform.scale(huisUitGaan_key, (int(166 * 2), int(22 * 2)))
cropsOppakken = pygame.transform.scale(cropsOppakken, (int(166 * 2), int(22 * 2)))

start_img = pygame.image.load('img/start_knop.png').convert_alpha()
exit_img = pygame.image.load('img/exit_knop.png').convert_alpha()
controls_img = pygame.image.load('img/controls_img.png').convert_alpha()

start_button = button((infox // 2) - 100, (infoy // 2) - 100, start_img, 2)
exit_button = button((infox // 2) - 100, (infoy // 2), exit_img, 2)
controls_button = button((infox // 2) - 100, (infoy // 2) + 100, controls_img, 2)
exit_controls = button((infox *0.1), (infoy * 0.1), exit_img, 2)

music = pygame.mixer.music.load("img/muziek.mp3")
pygame.mixer.music.play(-1)

while game.spelerSpeelt:
    button.drawButtons()
    game.main(player, inventaris)
    pygame.display.update()
