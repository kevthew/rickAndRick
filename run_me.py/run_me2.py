
import pygame
import random


pygame.init()
dimensions = (800, 500)

pygame.display.set_caption('Rick and Rick')
screen = pygame.display.set_mode(dimensions)
background_clear = pygame.Surface(dimensions)
background_clear.fill(pygame.Color("#000000"))

difference = pygame.image.load('spot_rick.jpeg')
difference = pygame.transform.scale(difference, dimensions)

rick_pic = pygame.image.load('rick_pic.png')
rick_pic = pygame.transform.scale(rick_pic, dimensions)

clip_rick = pygame.mixer.Sound("clip_rick.ogg")

should_show_first_image = True
sound_effect_timer = random.randrange(5, 12)
played_effect = False

running = True
clock = pygame.time.Clock()
while running:
    time_delta = clock.tick()/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background_clear, (0, 0))  # clear the screen to black each frame
    # play our sound effect after between 5-12 seconds
    if sound_effect_timer < 0.0 and not played_effect:
        clip_rick.play()
        played_effect = True
        should_show_first_image = False
    else:
        sound_effect_timer -= time_delta

    if should_show_first_image:
        screen.blit(difference, (0, 0))
    else:
        screen.blit(rick_pic, (0, 0))
    pygame.display.update()

pygame.quit()             
    
          



