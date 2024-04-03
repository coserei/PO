import pygame
from config import *
import math


# Hitboxes

i = 0
huis1 = pygame.Rect(140 , 270, -175 , -200)
veld1 = pygame.Rect(-160 , 315, -170 , -105)
huis2 = pygame.Rect(-450 , 550, -175 , -200)


# Lijst met hitboxes
hitboxes = [huis1, veld1, huis2]
interactableObjects = [huis1, huis2]

class player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()

        self.game = game

        self.speed = spelerSnelheid
        self.pos = pygame.math.Vector2(x, y)

        self.charImg = []

        self.charImg.append(pygame.image.load('img/char_l.png'))
        self.charImg.append(pygame.image.load('img/char_r.png'))
        
        self.animatieFase = 0
        self.img = pygame.transform.scale(self.charImg[round(self.animatieFase)], (playerSize*14, playerSize*41))

        self.image = pygame.Surface((16, 16))
        self.image.fill((0, 0, 0))

        self.animeerSpeler = False

    def userInput(self):
      self.velocity_x = 0
      self.velocity_y = 0

      keys = pygame.key.get_pressed()
      
      if keys[pygame.K_w]:
        self.velocity_y = self.speed
        self.spelerAnimatie()
      if keys[pygame.K_a]:
        self.velocity_x = self.speed
        self.spelerAnimatie()
      if keys[pygame.K_s]:
        self.velocity_y = -self.speed
        self.spelerAnimatie()
      if keys[pygame.K_d]:
        self.velocity_x = -self.speed
        self.spelerAnimatie()
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

        for j in range(0, (len(interactableObjects) - 1), 1):
            if pygame.Rect.colliderect(self.rect, interactableObjects[j]):
                break
            else:
                j += 1
        if pygame.Rect.colliderect(self.rect, interactableObjects[j]) and keys[pygame.K_e]:
            print("hoi")

    def spelerAnimatie(self):
       self.animeerSpeler = True

    def update(self):
      self.userInput()
      self.move()
      self.rect = pygame.Rect(self.pos[0], self.pos[1], 14, 41)
      self.collideCheck()
      self.interact()
      i = 0
      j = 0
      self.bordercheck()

      if self.animeerSpeler == True:
         self.animatieFase += 1

         if self.animatieFase > 1:
            self.animatieFase = 0
            self.animeerSpeler = False

      self.img = self.img = pygame.transform.scale(self.charImg[self.animatieFase], (playerSize*14, playerSize*41))
      print(self.animatieFase)
    
#class crop:
      
    #def __init__(self):
    #    self.zaadLocatie = []
      
    #def cropPlanten(self, inventarisVakken, itemHoeveelheden):

    #    if keys[pygame.k_q]:
    #        if inventarisVakken[slot] == "aardbeiZaad":
    #            self.zaadLocatie.append(self.pos)
