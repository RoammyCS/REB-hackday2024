import pygame
import time
import sys
import random

pygame.init()

# load custom font
custom_font = pygame.font.Font('assets/Minecraftia-Regular.ttf', 100)
eduQuestIcon = pygame.image.load('assets/eduQuestIcon.png')
player1_img = pygame.image.load('assets/mogus_mattright.png')
player2_img = pygame.image.load('assets/mogus_maryright.png')
start_img = pygame.image.load('assets/start_learning.png')
title_img = pygame.image.load('assets/eduQuest.png')
background_img = pygame.image.load('assets/background.jpg')
levelBackground = pygame.image.load('assets/levelBackground.png')
log = pygame.image.load('assets/log.png')
clock = pygame.time.Clock()
FPS = 60
GRAVITY = 1


class Player:
    def __init__(self, x, y, image):
        self.image = pygame.transform.scale(image, (100, 100))
        self.width = 100
        self.height = 100
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
        self.vel_y = 0
        self.flip = False
        self.is_jumping = False
        self.jump_height = 11  # Adjust as needed

    def move(self):
        # reset variable
        dx = 0
        dy = 0

        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            dx -= 10
            self.flip = True
        if key[pygame.K_d]:
            dx += 10
            self.flip = False
        if key[pygame.K_w]:
            player1.jump()

        self.vel_y += GRAVITY
        dy += self.vel_y

        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > 1280:
            dx = 1280 - self.rect.right

        if self.rect.bottom + dy > 720:
            dy = 0

        self.rect.x += dx
        self.rect.y += dy

    def movep2(self):
        # reset variable
        dx = 0
        dy = 0

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= 10
            self.flip = True
        if key[pygame.K_RIGHT]:
            self.rect.x += 10
            self.flip = False
        if key[pygame.K_UP]:
            player2.jump()

        self.vel_y += GRAVITY
        dy = self.vel_y

        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > 1280:
            dx = 1280 - self.rect.right

        if self.rect.bottom + dy > 720:
            dy = 0

        self.rect.x += dx
        self.rect.y += dy

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.vel_y = -self.jump_height

    def apply_gravity(self):
        if self.rect.y < 720 - 150:
            self.vel_y += GRAVITY
            self.rect.y += self.vel_y
        else:
            self.vel_y = 0
            self.rect.y = 720 - 150
            self.is_jumping = False

    def update(self):
        self.move()
        self.apply_gravity()

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), (self.rect.x, self.rect.y))
        pygame.draw.rect(screen, "white", self.rect, 2)


player1 = Player(100, 720 - 150, player1_img)
player2 = Player(200, 720 - 150, player2_img)


class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                print('bob')
                global game_state
                game_state = "startPressed"

        screen.blit(self.image, (self.rect.x, self.rect.y))


start_button = Button(475, 400, start_img, 6)
title_button = Button(375, 100, title_img, 10)

log_group = pygame.sprite.Group()

# settings for screen
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_icon(eduQuestIcon)
pygame.display.set_caption("EduQuest")

# title = custom_font.render("EduQuest", True, "black")
# title_rect = title.get_rect(center=(640, 150))

# waiting = custom_font.render("Waiting...", True, "black")
# waiting_rect = title.get_rect(center=(640, 360))

game_state = "mainMenu"

while True:

    clock.tick(FPS)

    player1.move()
    player2.movep2()
    # Quit Game if Click X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if game_state == "mainMenu":
        screen.blit(background_img, (0, 0))
        start_button.draw()
        title_button.draw()

    elif game_state == "startPressed":
        print('yes')
        screen.blit(background_img, (0, 0))
        screen.blit(levelBackground, (0, 0))
        player1.draw()
        player2.draw()

    pygame.display.update()
