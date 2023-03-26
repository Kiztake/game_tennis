from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(width, height))
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
        if keys[K_DOWN] and self.rect.y < win_height - 140:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 140:
            self.rect.y += self.speed
        
back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Game ping-pong")

racket1 = Player("racket.png", 30, win_height//2, 4, 40, 120)
racket2 = Player("racket.png", 520, win_height//2, 4, 40, 120)
ball = GameSprite('tenis_ball.png', 200, win_height//2, 4, 50, 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render("Player 1 lose!!!", True, (180, 0, 0))
lose2 = font.render("Player 2 lose!!!", True, (180, 0, 0))

v_x = 3
v_y = 2

game = True
finish = False
clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    
    if not finish:   
        window.fill(back)

        racket1.update_l()
        racket1.reset()

        racket2.update_r()
        racket2.reset()

        ball.reset()
        ball.rect.x += v_x
        ball.rect.y += v_y

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            v_x *= -1


        if ball.rect.y >= win_height - 50 or ball.rect.y <= 50:
            v_y *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
        elif ball.rect.x >= win_width:
            finish = True
            window.blit(lose2, (200, 200))



    display.update()
    clock.tick(FPS)