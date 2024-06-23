import pygame   # type: ignore
import sys
import csvReader 

pygame.init()

GRAFFITI_BG = 'images/bp-miller-Xeif8SdEgRU-unsplash.jpg'
DATA_BG = 'images/markus-spiske-iar-afB0QQw-unsplash.jpg'

screen = pygame.display.set_mode((500, 500))
screen.fill((175, 217, 70))
clock = pygame.time.Clock()


background = pygame.image.load(GRAFFITI_BG)
background = pygame.transform.scale(background, (1500, 1500))


font = pygame.font.SysFont('comicsans', 45)
result_font = pygame.font.SysFont('comicsans', 18)
process_text = font.render('Process Data', True, pygame.Color('green')) # (127,92,151)
process_text_rect = process_text.get_rect(center=(250,250))
quit_text = font.render('Quit Application', True, pygame.Color('yellow'), (255,82,82))
quit_text_rect = quit_text.get_rect(center=(250, 250- (process_text_rect.height+25) )) # could also do process_text.height() as it is a surface
result_text = result_font.render('placeholder', True, pygame.Color('Green'), pygame.Color('black'))
result_text_rect = result_text.get_rect(center=(250, 400))

displayResults = False

while True:
    screen.blit(background, (0,0))
    screen.blit(quit_text, quit_text_rect)


    pygame.draw.rect(screen, pygame.Color('purple'), process_text_rect)

    if displayResults:
        screen.blit(result_text, result_text_rect)

    mouse = pygame.mouse.get_pos()
    if process_text_rect.collidepoint(mouse):

        pygame.draw.rect(screen, pygame.Color('red'), process_text_rect)

    screen.blit(process_text, process_text_rect)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_text_rect.collidepoint(mouse):
                    pygame.quit()
                    sys.exit()
                if process_text_rect.collidepoint(mouse):
                    background = pygame.image.load(DATA_BG)             
                    background = pygame.transform.scale(background, (500, 500))
                    
                    # process dataset
                    result = csvReader.processCSV('dataset/cybersecurity_attacks.csv', 'attack type')

                    # display results
                    result_text = result_font.render(result, True, pygame.Color('Green'), pygame.Color('black'))
                    result_text_rect = result_text.get_rect(center=(250, 400))
                    
                    displayResults = True
    pygame.display.update()

    clock.tick(60)
        