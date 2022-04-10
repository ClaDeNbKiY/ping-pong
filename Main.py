from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, heidth):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(width, heidth))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_heidth - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -=  self.speed
        if keys[K_s] and self.rect.y < win.heidth - 80:
            self.rect.y += self.speed


back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_heidth))
window.fill(back)

game = True

finish = False
clock = time.Clock()
FPS = 60

racket1 = Player("racket.png",30,200,4,50,150)
racket2 = Player("racket.png", 520,200,4,50,150)
ball = GameSprite("tennis_ball.png",200,200,4,50,50)

font.init()
font = font.Font(NONE, 35)
lose1 = font.render("PLAYER 1 LOSE", True, (180, 0, 0))
lose2 = font.render("PLAYER 2 LOSE", True, (180, 0, 0))

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        window.fill(back)
        racket1.update_1()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.y > win_heidth-50 or ball.rect.y < 0:
            speed_y *= -1
