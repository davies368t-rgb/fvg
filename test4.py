import pygame

pygame.init()

bg_color = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480

display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My first game screen")

test = pygame.Surface([200,200])
test.fill(red)

text = pygame.font.Font(None,36).render("Test",True,pygame.Color("red"))
text_rect = text.get_rect(center=(SCREEN_WIDTH // 2,SCREEN_HEIGHT // 2))

def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display_surface.fill(bg_color)
        pygame.draw.rect(display_surface,(0,255,0),pygame.Rect(SCREEN_WIDTH // 2-50,SCREEN_HEIGHT // 2-30,100,60))
        display_surface.blit(text,text_rect)

        pygame.display.flip()

        clock.tick(30)
    
    pygame.quit()

if __name__ == "__main__":
    game_loop()