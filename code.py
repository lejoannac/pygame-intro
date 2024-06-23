import pygame   # type: ignore
import sys
import csvReader 

pygame.init()

GRAFFITI_BG = 'images/bp-miller-Xeif8SdEgRU-unsplash.jpg'
DATA_BG = 'images/markus-spiske-iar-afB0QQw-unsplash.jpg'

screen = pygame.display.set_mode((500, 500))
screen.fill((175, 217, 70))
clock = pygame.time.Clock()

# load & scale the image
background = pygame.image.load(GRAFFITI_BG)
background = pygame.transform.scale(background, (1500, 1500))

# getting a system font
font = pygame.font.SysFont('comicsans', 45)
result_font = pygame.font.SysFont('comicsans', 18)
