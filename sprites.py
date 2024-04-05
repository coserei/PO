import pygame
from config import *
import math

class player(pygame.sprite.Sprite):

    #hitboxes
    collideCount = 0
    interactCount = 0
    huis1 = pygame.Rect(0, 0, 0, 0)
    veld1 = pygame.Rect(0, 0, 0, 0)
    huis2 = pygame.Rect(500, 500, 1000, 1000)
    deur1 = pygame.Rect(1000, 1000, -1000, -1000)

    #borders
    borderhuis = [500, 500, 1000, 1000]
    borderbuiten = [500, 500, 1000, 1000]

    #lijst met hitboxes
    hitboxeshuis = [huis1]
    hitboxesbuiten = [huis1, veld1, huis2]
    interactableObjects = [huis1, huis2, deur1]

    #plek
    hitboxes = hitboxesbuiten
    borders = borderbuiten

    achtergrond = pygame.image.load("img/achtergrond.png")

    def __init__(self, game):
        super().__init__()

        self.game = game

        self.speed = spelerSnelheid
        self.pos = pygame.math.Vector2(x, y)

        self.charImg = []

        self.charImg.append(pygame.image.load('img/char_l1.png'))
        self.charImg.append(pygame.image.load('img/char_l2.png'))

        self.charImg.append(pygame.image.load('img/char_r1.png'))
        self.charImg.append(pygame.image.load('img/char_r2.png'))
        
        self.animatieFase = 0
        self.img = pygame.transform.scale(self.charImg[round(self.animatieFase)], (playerSize*17, playerSize*40))

        self.image = pygame.Surface((16, 16))
        self.image.fill((0, 0, 0))

        self.animeerSpeler = False

    def userInput(self):
      self.velocity_x = 0
      self.velocity_y = 0

      keys = pygame.key.get_pressed()

      if keys[pygame.K_d]:
        self.velocity_x = -self.speed
        self.spelerAnimatie('rechts')
      if keys[pygame.K_w]:
        self.velocity_y = self.speed
        self.spelerAnimatie('boven')
      if keys[pygame.K_a]:
        self.velocity_x = self.speed
        self.spelerAnimatie('links')
      if keys[pygame.K_s]:
        self.velocity_y = -self.speed
        self.spelerAnimatie('onder')
        #diagonaal bewegen moet even snel zijn, denk aan de 1, 1, wortel 2 driehoek
      if self.velocity_x != 0 and self.velocity_y != 0:
          self.velocity_x = self.velocity_x / math.sqrt(2)
          self.velocity_y = self.velocity_y / math.sqrt(2)

    def move(self):
      self.pos += pygame.math.Vector2(self.velocity_x, self.velocity_y)

    def bordercheck(self):
        if self.pos[0] > 472:
            self.pos[0] = 472
        elif self.pos[0] < -mapScale*992+473+17*playerSize:
            self.pos[0] = -mapScale*992+473+17*playerSize
        elif self.pos[1] > 282-(playerSize/2*40):
            self.pos[1] = 282-(playerSize/2*40)
        elif self.pos[1] < -992*mapScale+282+(playerSize/2*40):
            self.pos[1] = -992*mapScale+282++(playerSize/2*40)
        
        print(self.pos)

    def collideCheck(self):
        for self.collideCount in range(0, (len(self.hitboxes) - 1), 1):
            if pygame.Rect.colliderect(self.rect, self.hitboxes[self.collideCount]):
                break
            else:
                self.collideCount += 1
        if pygame.Rect.colliderect(self.rect, self.hitboxes[self.collideCount]) and self.velocity_x > 0:
            self.pos[0] -= 1
        if pygame.Rect.colliderect(self.rect, self.hitboxes[self.collideCount]) and self.velocity_x < 0:
            self.pos[0] += 1
        if pygame.Rect.colliderect(self.rect, self.hitboxes[self.collideCount]) and self.velocity_y > 0:
            self.pos[1] -= 1
        if pygame.Rect.colliderect(self.rect, self.hitboxes[self.collideCount]) and self.velocity_y < 0:
            self.pos[1] += 1

    def interact(self):

        keys = pygame.key.get_pressed()

        for self.interactCount in range(0, (len(self.interactableObjects) - 1), 1):
            if pygame.Rect.colliderect(self.rect, self.interactableObjects[self.interactCount]):
                break
            else:
              self.interactCount += 1
        if pygame.Rect.colliderect(self.rect, self.interactableObjects[0]) and keys[pygame.K_e]:
            self.achtergrond = pygame.image.load("img/huis.png")
            self.hitboxes = self.hitboxeshuis
            self.borders = self.borderhuis
            self.pos[0] = 200
            self.pos[1] = 200
        if pygame.Rect.colliderect(self.rect, self.interactableObjects[1]) and keys[pygame.K_e]:
            self.achtergrond = pygame.image.load("img/huis.png")
            self.hitboxes = self.hitboxeshuis
            self.borders = self.borderhuis
            self.pos[0] = 200
            self.pos[1] = 200
        if pygame.Rect.colliderect(self.rect, self.interactableObjects[2]) and keys[pygame.K_q] and self.hitboxes == self.hitboxeshuis:
            self.achtergrond = pygame.image.load("img/achtergrond.png")
            self.hitboxes = self.hitboxesbuiten
            self.borders = self.borderbuiten
            self.pos[0] = 44
            self.pos[1] = 10

    def spelerAnimatie(self, richting):
        self.animeerSpeler = True
        self.richting = richting
       
    def update(self):
        self.userInput()
        self.move()
        self.rect = pygame.Rect(self.pos[0], self.pos[1], 17*playerSize, 40*playerSize)
        self.collideCheck()
        self.interact()
        self.collideCount = 0
        self.interactCount = 0
        self.bordercheck()

        if self.animeerSpeler == True:
            self.animatieFase += 0.0045

            if self.animatieFase > 1 and self.richting == 'links':
                self.animatieFase = 0
                self.animeerSpeler = False
            if self.animatieFase > 3 and self.richting == 'rechts':
                self.animatieFase = 2
                self.animeerSpeler = False
            if self.animatieFase > 1 and self.richting == 'onder': # Moeten nog textures voor worden gemaakt
                self.animatieFase = 0
                self.animeerSpeler = False
            if self.animatieFase > 1 and self.richting == 'boven': # Moeten nog textures voor worden gemaakt
                self.animatieFase = 0
                self.animeerSpeler = False

            self.img = pygame.transform.scale(self.charImg[round(self.animatieFase)], (playerSize*17, playerSize*40))
    
class crop:
      
    def __init__(self):
        self.zaadLocatie = []
      
    def cropPlanten(self, inventarisVakken, slot):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_q]:
            if inventarisVakken[slot] == "aardbei":
                self.zaadLocatie.append(self.pos)
                print()


