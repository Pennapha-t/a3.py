import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Agent:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.radius = 15

    def draw(self):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, int (self.y)), self.radius)

agent = Agent()

running = True
while running:
    screen.fill((0, 0, 0 ))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    agent.draw()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
