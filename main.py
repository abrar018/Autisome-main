import pygame # type: ignore
from button import Button

import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "800,100"  # Set window position
import math
import time

# Initialize Pygame
pygame.init()

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)


# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Pygame")

# Load enemy image
enemy_image = pygame.image.load("player.png")
enemy_x, enemy_y = 250, 100

# Load player image

player_image = pygame.transform.scale(pygame.image.load("assets\knight_front_sitting_nobg.png"),(300,300))
player_x, player_y = 250, 175
hover_amplitude = 30  # Max height of hover
hover_speed = 3   # Speed of hover

pygame.mixer.init()
sound_effect = pygame.mixer.Sound("sound.wav")

# Game loop
running = True
start_time = time.time()

gym=0
read=0
med=0

while running:
    screen.blit(pygame.image.load("assets/forrest.png"),(-250,0))

    pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if GYM_BUTTON.checkForInput(pos):
                gym+=1
            if READ_BUTTON.checkForInput(pos):
                read+=1
            if MEDITATE_BUTTON.checkForInput(pos):
                med+=1
            if GYM_NEGATIVE.checkForInput(pos):
                gym-=1
            if READ_NEGATIVE.checkForInput(pos):
                read-=1
            if MEDITATE_NEGATIVE.checkForInput(pos):
                med-=1


    #sound_effect.play()

    # Calculate hover effect
    elapsed_time = time.time() - start_time
    hover_offset = math.sin(elapsed_time * hover_speed) * hover_amplitude
    player_hover_y = player_y + hover_offset

    # Draw player with hover effect
    screen.blit(player_image, (player_x, player_hover_y))

    screen.blit(get_font(25).render("GYM", True, "Orange"),(100,50))
    screen.blit(get_font(25).render("READ", True, "orange"),(100,80))
    screen.blit(get_font(25).render("MEDITATE", True, "orange"),(100,110))

    GYM_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("assets/plus.png"),(30,30)), pos=(350, 60), 
                            text_input="", font=get_font(10), base_color="#d7fcd4", hovering_color="White")
    READ_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("assets/plus.png"),(25,25)), pos=(350, 90), 
                            text_input="", font=get_font(10), base_color="#d7fcd4", hovering_color="White")
    MEDITATE_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("assets/plus.png"),(25,25)), pos=(350, 120), 
                            text_input="", font=get_font(10), base_color="#d7fcd4", hovering_color="White")
    GYM_NEGATIVE = Button(image=pygame.transform.scale(pygame.image.load("assets/minus.png"),(30,30)), pos=(320, 60), 
                            text_input="", font=get_font(10), base_color="#d7fcd4", hovering_color="White")
    READ_NEGATIVE = Button(image=pygame.transform.scale(pygame.image.load("assets/minus.png"),(25,25)), pos=(320, 90),
                            text_input="", font=get_font(10), base_color="#d7fcd4", hovering_color="White")
    MEDITATE_NEGATIVE = Button(image=pygame.transform.scale(pygame.image.load("assets/minus.png"),(25,25)), pos=(320, 120),
                            text_input="", font=get_font(10), base_color="#d7fcd4", hovering_color="White")

    for button in [GYM_BUTTON, READ_BUTTON, MEDITATE_BUTTON, GYM_NEGATIVE, READ_NEGATIVE, MEDITATE_NEGATIVE]:
            button.changeColor(pos)
            button.update(screen)


    for i in range(gym):
         screen.blit(pygame.transform.scale(pygame.image.load("assets/load.png"),(10,25)),(370+ 15*i, 47))
    for i in range(read):
            screen.blit(pygame.transform.scale(pygame.image.load("assets/load.png"),(10,25)),(370+ 15*i, 77))
    for i in range(med):
            screen.blit(pygame.transform.scale(pygame.image.load("assets/load.png"),(10,25)),(370+ 15*i, 107))

    # Update screen
    pygame.display.flip()

pygame.quit() 
