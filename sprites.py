import pygame
from config import *
import math


# Hitboxes

i = 0
huis1 = pygame.Rect(140 , 270, -175 , -200)
veld1 = pygame.Rect(-160 , 315, -170 , -105)
huis2 = pygame.Rect(-450 , 550, -175 , -200)
deur1 = pygame.Rect(1000, 1000, -1000, -1000)

# Lijst met hitboxes
hitboxes = [huis1, veld1, huis2]
interactableObjects = [huis1, huis2, deur1]

class player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()

        self.interactableObjects = interactableObjects
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
        if self.pos[0] > 360:
            self.pos[0] = 360
        elif self.pos[0] < -600:
            self.pos[0] = -600
        elif self.pos[1] > 460:
            self.pos[1] = 460
        elif self.pos[1] < 0:
            self.pos[1] = 0


    def collideCheck(self):
        for i in range(0, (len(hitboxes) - 1), 1):
            if pygame.Rect.colliderect(self.rect, hitboxes[i]):
                break
            else:
                i += 1
        if pygame.Rect.colliderect(self.rect, hitboxes[i]) and self.velocity_x > 0:
            self.pos[0] -= 1
        if pygame.Rect.colliderect(self.rect, hitboxes[i]) and self.velocity_x < 0:
            self.pos[0] += 1
        if pygame.Rect.colliderect(self.rect, hitboxes[i]) and self.velocity_y > 0:
            self.pos[1] -= 1
        if pygame.Rect.colliderect(self.rect, hitboxes[i]) and self.velocity_y < 0:
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
        self.rect = pygame.Rect(self.pos[0], self.pos[1], 14, 41)
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
    
#class crop:
      
    #def __init__(self):
    #    self.zaadLocatie = []
      
    #def cropPlanten(self, inventarisVakken, itemHoeveelheden):

    #    if keys[pygame.k_q]:
    #        if inventarisVakken[slot] == "aardbeiZaad":
    #            self.zaadLocatie.append(self.pos)
