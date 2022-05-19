import random
import pygame
import os
pygame.init()
FPS = 60
WIN = pygame.display.set_mode((500,500))
pygame.display.set_caption("Dirty bubble popper")
SCORE_FONT = pygame.font.SysFont('comicsans', 40)

# uses the assets folder to apply graphics to things in the game
Dirty_Bubble = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "bubble.png")),(40,40))
Background = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Bikini Bottom.png")),(500,500))
BUBBLES = []


# draws every object to the window
def draw_window(score):
    WIN.blit(Background,(0,0))
    WIN.blit(score, (50, 400))
    for a in BUBBLES:
        if a[1] > 0:
            WIN.blit(Dirty_Bubble,(a[0],a[1]))
        else:
            BUBBLES.remove(a)
    pygame.display.update()

def update():
    while(len(BUBBLES)<10):
        BUBBLES.append([random.randint(0,500),random.randint(250,500)])

#moves the bubble
def move_bubble(tick):
    for a in BUBBLES:
        a[1] -= 2
        if tick % 10 == 0:
            a[0] += random.randint(-5,5)

def main():
    run = True
    tick = 0
    SCORE = 0
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

        #takes the position of the mouse when clicked and compares it to every bubble in the list to see if it
        #matches position
        if event.type == pygame.MOUSEBUTTONUP or event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            mouse = pygame.Rect(pos[0],pos[1],20,20)
            clicked_sprites = [s for s in BUBBLES if pygame.Rect(s[0],s[1],40,40).colliderect(mouse)]
            for sprites in clicked_sprites:
                SCORE += 1
                BUBBLES.remove(sprites)

        score = SCORE_FONT.render("SCORE: " + str(SCORE), 1, (0, 0, 0))
        update()
        tick += 1
        move_bubble(tick)
        draw_window(score)

if __name__ == '__main__':
    main()
