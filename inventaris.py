import pygame
from config import *


class inventaris:

    def __init__(self):

        self.inventarisVakken = ['tomaatZaad', 'tomaatZaad', '', '', '', '', '']
        self.vakkenRectangles = [(278,458),(278+76,458),(278+2*76,458),(278+3*76,458),(278+4*76, 458),(278+5*76,458)]

        self.itemHoeveelheden = [1, 1, 0, 0, 0, 0]

        #for vak in range(6):
        #    self.inventarisVakken.append(item[0])

        self.slot = slot

    def selectedSlot(self, event):
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

    #def pickUp(self):

    #   if interactEvent
    
    def update(self, event):
        self.selectedSlot(event)

        for vak in range(0, len(self.itemHoeveelheden)):
            
            if self.itemHoeveelheden[vak] <= 0:
                self.inventarisVakken[vak] == "leeg"
                self.itemHoeveelheden[vak] == 0
                