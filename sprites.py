import pygame
from config import *
import math
import random

class player(pygame.sprite.Sprite):

    # Hitboxes

    collideCount = 0
    interactCount = 0
    huis1 = pygame.Rect(1000, 1000, -2000, -2000)
    veld1 = pygame.Rect(0, 0, 0, 0)
    huis2 = pygame.Rect(500, 500, 1000, 1000)
    deur1 = pygame.Rect(1000, 1000, -1000, 0)
    veld2 = pygame.Rect(0, 0, -3000, -3000)
    shop1 = pygame.Rect(0, 0, -3000, -3000)
    shop2 = pygame.Rect(0, 0, -3000, -3000)

    save = open("Saved.txt")
    data = save.readlines()

    # Borders

    borderhuis = [500, 500, 1000, 1000]
    borderbuiten = [500, 500, 1000, 1000]

    hitboxessave = data[20]

    # Lijst met hitboxes

    hitboxeshuis = [huis1]
    hitboxesbuiten = [huis1, veld1, huis2]
    interactableObjects = [huis1, huis2, deur1, veld2, shop1, shop2]

    # Plek

    if hitboxessave == "hitboxesbuiten":
        hitboxes = hitboxesbuiten
    else:
        hitboxes = hitboxeshuis

    borders = [int(data[16]), int(data[17]), int(data[18]), int(data[19])]

    def __init__(self, game):
        super().__init__()

        self.zaadSoort = []
        self.zaadLocatie = []

        self.cropGeplant = False

        self.game = game

        self.speed = spelerSnelheid
        self.pos = pygame.math.Vector2(x, y)

        self.charImg = {
            'links': [pygame.image.load('img/char_l1.png'), pygame.image.load('img/char_l2.png')],
            'rechts': [pygame.image.load('img/char_r1.png'), pygame.image.load('img/char_r2.png')],
            'boven': [pygame.image.load('img/char_down1.png'), pygame.image.load('img/char_down2.png')],
            'onder': [pygame.image.load('img/char_up1.png'), pygame.image.load('img/char_up2.png')]
        }
        
        self.animatieFase = 0
        self.richting = 'onder'
        player.img = self.charImg[self.richting][0]

        self.image = pygame.Surface((16, 16))
        self.image.fill((0, 0, 0))

        self.animeerSpeler = False

        self.shopSchermOpen = False
        self.shop2SchermOpen = False

        self.boomX = []
        self.boomY = []

        for bomen in range(20):
            boomX = random.randint(2, 60) * 16 * mapScale
            boomY = random.randint(2, 44) * 16 * mapScale
            collision = False
            for hitX, hitY in zip(self.boomX, self.boomY):
                if abs(hitX - boomX) < 300 and abs(hitY - boomY) < 300:
                    collision = True
                    break

            if not collision:
                self.boomX.append(boomX)
                self.boomY.append(boomY)

        self.animatieTijd = 1/15

        self.inHuis = bool(int(data[25]))

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
        pygame.key.set_repeat(1000)

        for self.interactCount in range(0, (len(self.interactableObjects) - 1), 1):
            if pygame.Rect.colliderect(self.rect, self.interactableObjects[self.interactCount]):
                break
            else:
              self.interactCount += 1
        if pygame.Rect.colliderect(self.rect, self.interactableObjects[0]) and keys[pygame.K_e]:
            self.hitboxes = self.hitboxeshuis
            self.borders = self.borderhuis
            self.inHuis = True
        if pygame.Rect.colliderect(self.rect, self.interactableObjects[0]) and keys[pygame.K_q]:
            self.hitboxes = self.hitboxes
            self.borders = self.borders
            self.inHuis = False
        if pygame.Rect.colliderect(self.rect, self.interactableObjects[3]) and keys[pygame.K_b]:
            self.cropGeplant = True
        if pygame.Rect.colliderect(self.rect, self.interactableObjects[4]) and keys[pygame.K_t]:
            self.shopSchermOpen = True
        if pygame.Rect.colliderect(self.rect, self.interactableObjects[4]) and keys[pygame.K_u]:
            self.shop2SchermOpen = True
            

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

        if self.animeerSpeler:

            self.animatieFase += self.animatieTijd

            self.maximumFase = 2 #if self.richting in ['links', 'rechts'] else 3

            if self.animatieFase >= self.maximumFase:
                self.animatieFase = 0

            self.index = int(self.animatieFase)
        
        else:

            self.index = 0

        self.img = pygame.transform.scale(self.charImg[self.richting][self.index], (playerSize*17, playerSize*40))
        self.animeerSpeler = False
