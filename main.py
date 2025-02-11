import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Agent with Gravity")
clock = pygame.time.Clock()
FPS = 60

class Agent:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.radius = 30
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 0.5
        self.air_resistance = 0.01

    def update(self):
        self.vx *= (1 - self.air_resistance)
        self.vx += self.ax
        self.vy += self.ay
        self.x += self.vx
        self.y += self.vy

        if self.y + self.radius > HEIGHT:
            self.y = HEIGHT - self.radius
            self.vy = -0.8 * self.vy  
        if self.x > WIDTH:
            self.x = 0            
        elif self.x < 0:
            self.x = WIDTH

    def draw(self):
        pygame.draw.circle(screen, (255, 0, 0), (int(self.x), int(self.y)), self.radius)

agent = Agent()

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        agent.ax = -0.2
    elif keys[pygame.K_RIGHT]:
        agent.ax = 0.2
    else:
        agent.ax = 0  
    if keys[pygame.K_SPACE]:
        agent.vy = -10  

    agent.update()
    agent.draw()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()