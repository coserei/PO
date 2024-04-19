import pygame
from config import *

class inventaris:

    def __init__(self):

        self.inventarisVakken = [data[4], data[5], data[6], data[7], data[8], data[9]]
        #self.vakkenRectangles = [(278,458),(278+76,458),(278+2*76,458),(278+3*76,458),(278+4*76, 458),(278+5*76,458)]
        self.vakkenRectangles = [
        (((infox // 2) - 222), (infoy - 92)),
        (((infox // 2) - 146), (infoy - 92)),
        (((infox // 2) - 70), (infoy - 92)),
        (((infox // 2) + 6), (infoy - 92)),
        (((infox // 2) + 82), (infoy - 92)),
        (((infox // 2) + 158), (infoy - 92))]

        self.vakX = 278

        for vak in range(len(self.inventarisVakken)):
            self.vakkenRectangles.append((self.vakX, 458))
            self.vakX += 76

        self.itemHoeveelheden = [int(data[10]), int(data[11]), int(data[12]), int(data[13]), int(data[14]), int(data[15])]

        #for vak in range(6):
        #    self.inventarisVakken.append(item[0])

        self.slot = slot

    def selectedSlot(self, event):
        if event.type == pygame.MOUSEWHEEL:
            if event.y > 0 and self.slot < 5:
                self.slot += 1
            if event.y < 0 and self.slot > 0:
                self.slot -= 1

    #def pickUp(self):

    #   if interactEvent
    
    def update(self, event):
        self.selectedSlot(event)

        for vak in range(0, len(self.itemHoeveelheden)):
            
            if self.itemHoeveelheden[vak] <= 0:
                self.inventarisVakken[vak] = "leeg"
                self.itemHoeveelheden[vak] = 0
        
        return self.slot, self.itemHoeveelheden, self.inventarisVakken

inventaris = inventaris()

class crop:

    def __init__(self):
        self.zaadX = [0]
        self.zaadY = [0]
        self.cropFase = [0]
        self.zaadSoort = [0]
    
    def cropPlanten(self, playerPos, cropGeplant):
        for crops in range(len(self.zaadX)):
            if cropGeplant == True and (self.zaadX[crops]-self.zaadX[crops-1] > 16*mapScale or len(item) == 1):
                cropGeplant = False
                for zaad in range(len(item)):
                    if inventaris.inventarisVakken[inventaris.slot] == item[zaad] + "Zaad":
                        self.zaadX.append(playerPos[0])
                        self.zaadY.append(playerPos[1])
                        self.zaadSoort.append(item[zaad])
                        inventaris.itemHoeveelheden[inventaris.slot] -= 1
                        return cropGeplant

    def update(self, playerPos, cropGeplant):
        self.cropPlanten(playerPos, cropGeplant)
