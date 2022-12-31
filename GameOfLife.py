import pygame
from sys import exit

# 1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# 2. Any live cell with two or three live neighbours lives on to the next generation.
# 3. Any live cell with more than three live neighbours dies, as if by overpopulation.
# 4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

class Game:

    def __init__(self):

        self.width = 400
        self.height = 400
        self.fpsClock = pygame.time.Clock()
        self.fps = 30
        self.screen = pygame.display.set_mode([self.width, self.height])
        # Colors
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.cells = []

    
    def draw_grid(self):
        for i in range(10, self.width, 10):
            pygame.draw.line(self.screen, self.white, (i, 0), (i, self.height), 1)

        for j in range(10, self.height, 10):
            pygame.draw.line(self.screen, self.white, (0, j), (self.width, j), 1)

    def draw_cells(self):
        for pos in self.cells:
            pygame.draw.rect(self.screen, self.red, [pos[0], pos[1], 10, 10])

    def check_neighbors(self, cell):
        neighbors = 0
        for i in range(cell[0]):
            for j in range(cell[1]):
                
            
    
    def draw_screen(self):

        pygame.init()

        running = True

        while running:

            self.screen
            self.screen.fill(self.black)
            self.draw_grid()
            pygame.draw.rect(self.screen, self.red, [self.width/2, self.height/2, 10, 10])

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

            pygame.display.update()
            self.fpsClock.tick(self.fps)
        
        pygame.quit()
        exit()
