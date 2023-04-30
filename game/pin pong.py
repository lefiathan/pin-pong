from pygame import *
font.init()
from random import*


b = randint(0, 1)
r = 0
l = 0


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 2:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 425:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 2:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 425:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        global b
        global l
        global r
        if sprite.collide_rect(ball, player_r):
            self.speed = 5
            self.speed += 2
            b = 1
        if sprite.collide_rect(ball, player_l):
            self.speed = 5
            self.speed += 2
            b = 0
        if sprite.collide_rect(ball, player_l) and player_l.rect.y < self.rect.y:
            self.rect.y += 20
            self.rect.x -= 20
            self.speed = 5
            self.speed += 2
            b = 0
        if sprite.collide_rect(ball, player_r) and player_r.rect.y < self.rect.y:
            self.rect.y += 20
            self.rect.x -= 20
            self.speed = 5
            self.speed += 2
            b = 1
        if sprite.collide_rect(ball, player_l) and player_l.rect.y > self.rect.y:
            self.rect.y -= 20
            self.rect.x += 20
            self.speed = 5
            self.speed += 2
            b = 0
        if sprite.collide_rect(ball, player_r) and player_r.rect.y > self.rect.y:
            self.rect.y -= 20
            self.rect.x += 20
            self.speed = 5
            self.speed += 2
            b = 1
        if self.rect.x < 1:
            l += 1
            b = 0
        if self.rect.x > 650:
            r += 1
            b = 1

        if self.rect.y <= 2 and b == 0:
            self.rect.y += 50
            self.rect.x += 50
        if self.rect.y <= 2 and b == 1:
            self.rect.y += 20
            self.rect.x -= 20
            

            
        if self.rect.y >= 425 and b == 0:
            self.rect.y -= 50
            self.rect.x += 20
        if self.rect.y >= 425 and b == 1:
            self.rect.y -= 50
            self.rect.x -= 20
            
            


        
    def vs(self):
        global b
        if b == 0:
            self.rect.x += self.speed
        if b == 1:
            self.rect.x -= self.speed


def restart():
    global l
    global r
    global b
    keys = key.get_pressed()
    if keys[K_k] and r >= 3 or l >= 3 and keys[K_k]:
        b = randint(0, 1)
        player_l.rect.x = 1
        player_l.rect.y = 300
        player_r.rect.x = 650
        player_r.rect.y = 150
        ball.rect.x = 325
        ball.rect.y = 150
        ball.speed = 5
        r = 0
        l = 0

player_l = Player('racket.png', 1, 300, 5)
player_r = Player('racket.png', 650, 150, 5)
ball = Ball('tenis_ball.png', 325, 150, 5)

win_width = 700
win_height = 500
 
window = display.set_mode((win_width, win_height))
display.set_caption('Лабиринт')
background  = transform.scale(image.load('background.jpg'), (win_width, win_height))
 

 
game = True
finish = False
clock = time.Clock()
FPS = 60
 
font = font.Font(None, 70)
LW = font.render('2 игрок победил!', True, (255, 215, 0))
RW = font.render('1 игрок победил!', True, (180, 0, 0))
res = font.render('нажмите K', True, (180, 0, 180))
 

 
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
 
 
    if not finish:
        window.blit(background, (0, 0))
        player_l.update_l()
        player_r.update_r()
        
 
        player_l.reset()
        player_r.reset()
        ball.reset()

        restart()

        ball.update()
        ball.vs()
        if l >= 3:
            window.blit(LW, (0, 0))
            window.blit(res, (0, 50))
            b = 2
        if r >= 3:
            window.blit(RW, (0, 0))
            window.blit(res, (0, 50))
            b = 2


 
        
 
       
 
        display.update()
        clock.tick(FPS)