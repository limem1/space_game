import pygame
import random
import math

pygame.init()
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0,0,0)
# new code !! not used yet !!!
class ResourceManager:
    def __init__(self, path = "."):
        self.path = path
        self.background = self.path + "/background.png"
        self.enemy = self.path + "/chicken.png"
        self.player = self.path + "/space.png"
        self.bullet = self.path + "/bullet.png"


class GameObjectManager:
    def __int__(self):
        self.__resources = ResourceManager()
        self.background = pygame.image.load(self.__resources.background)
        self.enemy = pygame.image.load(self.__resources.enemy)
        self.player = pygame.image.load(self.__resources.player)
        self.bullet = pygame.image.load(self.__resources.bullet)


class Position:
    def __init__(self, object, screen):
        self.object = object
        self.screen = screen
        self.x = 0
        self.y = 0
        self.x_change = 0
        self.y_change = 0

    def set(self, x, y):
        self.x = x
        self.y = y
        set.screen.blit(self.object, (x, y))


class PositionManager:
    def __init__(self, enemyCount):
        self.objects = GameObjectManager()
        self.screen = pygame.display.set_mode((800, 600))
        self.background = Position(self.objects.background, self.screen)
        self.player = Position(self.objects.player, self.screen)
        self.bullet = Position(self.objects.bullet, self.screen)
        self.enemy = []
        self.generateEnemies(enemyCount)

    def generateEnemies(self, count):
        for i in range(count):
            self.enemy.append(Position(self.objects.enemy, self.screen))
# end new code



screen = pygame.display.set_mode((800,600))

background = pygame.image.load("background.png")

playerImg = pygame.image.load("space.png")

playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []


num_of_enimes = 10



for i in range (num_of_enimes) :
     enemyImg.append(pygame.image.load("chicken.png"))
     enemyX.append(random.randint(0,735))
     enemyY.append(random.randint(50,150))
     enemyX_change.append(4)
     enemyY_change.append(40)





bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletx_change =  0
bullety_change =  20
bullet_satet = "ready"
#score
score_value = 0


#text
font = pygame.font.Font('freesansbold.ttf',32)

textX = 10
textY = 10
# game over
over_font = pygame.font.Font('freesansbold.ttf',64)


def game_over_text ():
    over_text = font.render("GAME OVER " , True, blue)

    screen.blit(over_text,200,250 )

def the_score (x,y):
    score = font.render("Score :" + str(score_value),True, black )
    screen.blit(score,(x,y))




def fire_bullet (x,y) :
      global bullet_satet
      bullet_satet = "fire"
      screen.blit(bulletImg,(x+16, y+10))






def player (X,Y) :
     screen.blit(playerImg,(X,Y))

def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))


def iscollision (enemyX, enemyY,bulletX,bulletY) :
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY-bulletY, 2)))
    if distance < 27:
        return True
    else :
        return False



pygame.display.set_caption("Space War")
Icon = pygame.image.load('racing.png')
pygame.display.set_icon(Icon)


running = True
while running :
    screen.fill((0, 0, 0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():

      if event.type == pygame.QUIT:
           running = True
      if event.type == pygame.KEYDOWN :
           if event.key == pygame.K_DOWN :
              playerY_change = -5
           if event.key == pygame.K_UP :
               playerY_change = 5

           if event.key == pygame.K_LEFT:
               playerX_change = -5
           if event.key == pygame.K_RIGHT:
               playerX_change = 5
           if event.key == pygame.K_SPACE :
                bulletY = playerY
                bulletX = playerX
                fire_bullet(bulletX,bulletY)
      if event.type == pygame.KEYUP :
           if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
               playerX_change = 0
           if event.key == pygame.K_DOWN or event.key == pygame.K_UP :
               playerY_change = 0

    playerY -= playerY_change
    playerX += playerX_change
    if playerX <= 0 :
      playerX = 0

    elif playerX   >= 736 :
        playerX = 736

    if playerY <= 0 :
        playerY = 0
    elif playerY >= 536:
        playerY = 536

    for i in range(num_of_enimes):
        if enemyY[i] > 200 :
            for j in range (num_of_enimes):
                enemyY[j] = 2000
            game_over_text()
            break



        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0 :
           enemyX_change[i] = 4
           enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736 :
          enemyX_change[i] = -4
          enemyY[i] += enemyY_change[i]

        coll = iscollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if coll:
            bulletY = 480
            bullet_satet = "ready"
            score_value += 1

            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i],enemyY[i],i)
        if bulletY <= 0 :
           bulletY = 480
           bullet_satet = 'ready'
        if bullet_satet is "fire" :
           fire_bullet(bulletX,bulletY)
           bulletY -= bullety_change

        player(playerX,playerY)
        the_score(textX,textY)
        pygame.display.update()
