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

class Agent:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.radius = 15
        self.vx = 0
        self.vy = 0
        self.ax = -0.1
        self.ay = 0.5

    def update(self):
        self.vx += self.ax
        self.vy += self.ay
        self.x += self.vx
        self.y += self.vy

    def draw(self):
        pygame.draw.circle(screen, (255, 0, 0), (int (self.x), int (self.y)), self.radius)

while running:
    screen.fill((0, 0, 0 ))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    agent.update()
    agent.draw()
    pygame.display.flip()
            

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                agent.Jump()

    agent.update()
    agent.draw()

    pygame.display.flip()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        agent.vy = -10
    if keys[pygame.K_LEFT]:
        agent.vx = -10
    if keys[pygame.K_RIGHT]:
        agent.vx = 10
    if agent.right < 0:
        agent.left = WIDTH
    elif agent.left > WIDTH:
        agent.right = 0
    
    agent.update()
    agent.draw()
    pygame.display.flip()

class Agent:
    self.x = WIDTH // 2
    self.y = HEIGHT // 2
    self.vx = 0
    self.vy = 0
    self.ax = 0
    self.ay = 0.5
    self.radius = 20

    def __init__(self):
        self.vx += self.ax
        self.vy += self.ay
        self.x += self.vx
        self.y += self.vy

        if self.y + self.radius > HEIGHT:
            self.y = HEIGHT - self.radius
            self.vy = -0.8 * self.vy
    
    


