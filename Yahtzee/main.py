import pygame
import sys
import random

class Draw:

    def __init__(self):
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.DICE_WIDTH = 60
        self.DICE_HEIGHT = 60
        self.DOT_LINE_THICKNESS = 8
        self.DICE_LINE_THICKNESS = 2
        self.DOT_GAP = 10
    def drawOne(self, screen, color, rectTopCornerX, rectTopCornerY):
        pygame.draw.rect(screen, BLACK, pygame.Rect(rectTopCornerX, rectTopCornerY, self.DICE_WIDTH, self.DICE_HEIGHT), self.DICE_LINE_THICKNESS)
        pygame.draw.circle(screen, BLACK, (rectTopCornerX + self.DICE_WIDTH/2, rectTopCornerY + self.DICE_HEIGHT/2), self.DOT_LINE_THICKNESS)
    def drawTwo(self, screen, color, rectTopCornerX, rectTopCornerY):
        pygame.draw.rect(screen, BLACK, pygame.Rect(rectTopCornerX, rectTopCornerY, self.DICE_WIDTH, self.DICE_HEIGHT), self.DICE_LINE_THICKNESS)
        pygame.draw.circle(screen, BLACK,((rectTopCornerX + self.DICE_WIDTH/2)+self.DOT_GAP, (rectTopCornerY + self.DICE_HEIGHT/2)-dotShift), self.DOT_LINE_THICKNESS)
        pygame.draw.circle(screen, BLACK,((rectTopCornerX + self.DICE_WIDTH/2)-dotShift, (rectTopCornerY + self.DICE_HEIGHT/2)+dotShift), self.DOT_LINE_THICKNESS)

class Dice:
    def __init__(self):
        self.dice = 0
    def roll(self):
        return random.randint(1,6)

class DiceSet:
    def __init__(self):
        self.diceSet = []

class Ruleset:
    def __init__(self):
        print("TO-DO")

class Player:
    def __init__(self):
        self.diceSet = []
        self.keepSet= []
    def getScore(self):
        print("TO-DO")
    def swapDice(self):
        print("TO-DO")
    def keepDice(self):
        print("TO-DO")

class GameWindow:
    def __init__(self):
        print("TO-DO")
    def drawDice(self):
        print("TO-DO")

# Global Variable Declarations
BLACK = (0,0,0)
WHITE = (255,255,255)
# DICE_WIDTH = 60
# DICE_HEIGHT = 60
# DOT_LINE_THICKNESS = 10
# DICE_LINE_THICKNESS = 2

def main():
    print("Yahtzee")
    rectTopCornerX = 100
    rectTopCornerY = 55
    pygame.init()
    screen = pygame.display.set_mode((400,600))
    screen.fill(WHITE)
    testDice = Draw()
    testDice.drawTwo(screen, BLACK, rectTopCornerX, rectTopCornerY)
    # pygame.draw.rect(screen,BLACK,pygame.Rect(rectTopCornerX, rectTopCornerY, DICE_WIDTH, DICE_HEIGHT),DICE_LINE_THICKNESS)
    # pygame.draw.circle(screen,BLACK,(rectTopCornerX + DICE_WIDTH/2, rectTopCornerY + DICE_HEIGHT/2), DOT_LINE_THICKNESS)
    # pygame.display.flip()
    # diceSet = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
    # print("Current dice set: ", diceSet)

    running = True
    while running:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            pygame.display.update()

if __name__ == "__main__":
    main()