import pygame
import sys
import random
import Tkinter

class Draw:

    def __init__(self):
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.DICE_WIDTH = 60
        self.DICE_HEIGHT = 60
        self.DOT_LINE_THICKNESS = 8
        self.DICE_LINE_THICKNESS = 2
        self.DOT_GAP = 18
    def drawOne(self, screen, color, rectTopCornerX, rectTopCornerY):
        pygame.draw.rect(screen, color, pygame.Rect(rectTopCornerX, rectTopCornerY, self.DICE_WIDTH, self.DICE_HEIGHT), self.DICE_LINE_THICKNESS)
        pygame.draw.circle(screen, color, (rectTopCornerX + self.DICE_WIDTH/2, rectTopCornerY + self.DICE_HEIGHT/2), self.DOT_LINE_THICKNESS)
    def drawTwo(self, screen, color, rectTopCornerX, rectTopCornerY):
        pygame.draw.rect(screen, color, pygame.Rect(rectTopCornerX, rectTopCornerY, self.DICE_WIDTH, self.DICE_HEIGHT), self.DICE_LINE_THICKNESS)
        pygame.draw.circle(screen, color, ((rectTopCornerX + self.DICE_WIDTH/2)+self.DOT_GAP, (rectTopCornerY + self.DICE_HEIGHT/2)-self.DOT_GAP), self.DOT_LINE_THICKNESS)
        pygame.draw.circle(screen, color, ((rectTopCornerX + self.DICE_WIDTH/2)-self.DOT_GAP, (rectTopCornerY + self.DICE_HEIGHT/2)+self.DOT_GAP), self.DOT_LINE_THICKNESS)
    def drawThree(self, screen, color, rectTopCornerX, rectTopCornerY):
        pygame.draw.rect(screen, color, pygame.Rect(rectTopCornerX, rectTopCornerY, self.DICE_WIDTH, self.DICE_HEIGHT), self.DICE_LINE_THICKNESS)
        pygame.draw.circle(screen, color, ((rectTopCornerX + self.DICE_WIDTH/2)+self.DOT_GAP, (rectTopCornerY + self.DICE_HEIGHT/2)-self.DOT_GAP), self.DOT_LINE_THICKNESS)
        pygame.draw.circle(screen, color, ((rectTopCornerX + self.DICE_WIDTH/2)-self.DOT_GAP, (rectTopCornerY + self.DICE_HEIGHT/2)+self.DOT_GAP), self.DOT_LINE_THICKNESS)
        pygame.draw.circle(screen, color, ((rectTopCornerX + self.DICE_WIDTH/2), (rectTopCornerY + self.DICE_HEIGHT/2)), self.DOT_LINE_THICKNESS)
    def drawFour(self, screen, color, rectTopCornerX, rectTopCornerY):
        pygame.draw.rect(screen, color, pygame.Rect(rectTopCornerX, rectTopCornerY, self.DICE_WIDTH, self.DICE_HEIGHT), self.DICE_LINE_THICKNESS)
        pygame.draw.circle(screen, color, ((rectTopCornerX + self.DICE_WIDTH/2)+self.DOT_GAP, (rectTopCornerY + self.DICE_HEIGHT/2)-self.DOT_GAP), self.DOT_LINE_THICKNESS)
        pygame.draw.circle(screen, color, ((rectTopCornerX + self.DICE_WIDTH/2)-self.DOT_GAP, (rectTopCornerY + self.DICE_HEIGHT/2)+self.DOT_GAP), self.DOT_LINE_THICKNESS)
        pygame.draw.circle(screen, color, ((rectTopCornerX + self.DICE_WIDTH/2)-self.DOT_GAP, (rectTopCornerY + self.DICE_HEIGHT/2)-self.DOT_GAP), self.DOT_LINE_THICKNESS)
        pygame.draw.circle(screen, color, ((rectTopCornerX + self.DICE_WIDTH/2)+self.DOT_GAP, (rectTopCornerY + self.DICE_HEIGHT/2)+self.DOT_GAP), self.DOT_LINE_THICKNESS)
    def drawFive(self, screen, color, rectTopCornerX, rectTopCornerY):
        pygame.draw.rect(screen, color, pygame.Rect(rectTopCornerX, rectTopCornerY, self.DICE_WIDTH, self.DICE_HEIGHT), self.DICE_LINE_THICKNESS)
        pygame.draw.circle(screen, color, ((rectTopCornerX + self.DICE_WIDTH/2)+self.DOT_GAP, (rectTopCornerY + self.DICE_HEIGHT/2)-self.DOT_GAP), self.DOT_LINE_THICKNESS)
        pygame.draw.circle(screen, color, ((rectTopCornerX + self.DICE_WIDTH/2)-self.DOT_GAP, (rectTopCornerY + self.DICE_HEIGHT/2)+self.DOT_GAP), self.DOT_LINE_THICKNESS)
        pygame.draw.circle(screen, color, ((rectTopCornerX + self.DICE_WIDTH/2)-self.DOT_GAP, (rectTopCornerY + self.DICE_HEIGHT/2)-self.DOT_GAP), self.DOT_LINE_THICKNESS)
        pygame.draw.circle(screen, color, ((rectTopCornerX + self.DICE_WIDTH/2)+self.DOT_GAP, (rectTopCornerY + self.DICE_HEIGHT/2)+self.DOT_GAP), self.DOT_LINE_THICKNESS)
        pygame.draw.circle(screen, color, ((rectTopCornerX + self.DICE_WIDTH/2), (rectTopCornerY + self.DICE_HEIGHT/2)), self.DOT_LINE_THICKNESS)
    def drawSix(self, screen, color, rectTopCornerX, rectTopCornerY):
        pygame.draw.rect(screen, color, pygame.Rect(rectTopCornerX, rectTopCornerY, self.DICE_WIDTH, self.DICE_HEIGHT), self.DICE_LINE_THICKNESS)
        pygame.draw.circle(screen, color, ((rectTopCornerX + self.DICE_WIDTH/2)+self.DOT_GAP, (rectTopCornerY + self.DICE_HEIGHT/2)-self.DOT_GAP), self.DOT_LINE_THICKNESS)
        pygame.draw.circle(screen, color, ((rectTopCornerX + self.DICE_WIDTH/2)-self.DOT_GAP, (rectTopCornerY + self.DICE_HEIGHT/2)+self.DOT_GAP), self.DOT_LINE_THICKNESS)
        pygame.draw.circle(screen, color, ((rectTopCornerX + self.DICE_WIDTH/2)-self.DOT_GAP, (rectTopCornerY + self.DICE_HEIGHT/2)-self.DOT_GAP), self.DOT_LINE_THICKNESS)
        pygame.draw.circle(screen, color, ((rectTopCornerX + self.DICE_WIDTH/2)+self.DOT_GAP, (rectTopCornerY + self.DICE_HEIGHT/2)+self.DOT_GAP), self.DOT_LINE_THICKNESS)
        pygame.draw.circle(screen, color, ((rectTopCornerX + self.DICE_WIDTH/2)+self.DOT_GAP, (rectTopCornerY + self.DICE_HEIGHT/2)), self.DOT_LINE_THICKNESS)
        pygame.draw.circle(screen, color, ((rectTopCornerX + self.DICE_WIDTH/2)-self.DOT_GAP, (rectTopCornerY + self.DICE_HEIGHT/2)), self.DOT_LINE_THICKNESS)

class Dice:
    def __init__(self):
        self.dice = 0
    def roll(self):
        return random.randint(1,6)

class DiceSet:
    def __init__(self):
        self.diceSet = []

class RuleSet:
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


def main():
    print("Yahtzee")
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    rectTopCornerX = 25
    rectTopCornerY = 25
    pygame.init()
    screen = pygame.display.set_mode((600,600))
    screen.fill(WHITE)
    testDice = Draw()
    testDice.drawOne(screen, BLACK, rectTopCornerX, rectTopCornerY)
    testDice.drawTwo(screen, BLACK, rectTopCornerX + 75, rectTopCornerY)
    testDice.drawThree(screen, BLACK, rectTopCornerX + 2*75, rectTopCornerY)
    testDice.drawFour(screen, BLACK, rectTopCornerX + 3*75, rectTopCornerY)
    testDice.drawFive(screen, BLACK, rectTopCornerX + 4*75, rectTopCornerY)
    testDice.drawSix(screen, BLACK, rectTopCornerX + 5*75, rectTopCornerY)
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