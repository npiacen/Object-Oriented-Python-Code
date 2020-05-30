# Square class

import pygame
from Shape import *

class Square(Shape):

    def __init__(self, window):
        super().__init__(window, 'Square')
        self.widthAndHeight = random.randrange(10, 100)
        self.rect = pygame.Rect(self.x, self.y, self.widthAndHeight, self.widthAndHeight)

    def clickedInside(self, mousePoint):
        clicked = self.rect.collidepoint(mousePoint)
        return clicked
    
    def area(self):
        theArea = self.widthAndHeight * self.widthAndHeight
        return theArea

    def draw(self):
        pygame.draw.rect(self.window, self.color, (self.x, self.y, self.widthAndHeight, self.widthAndHeight))