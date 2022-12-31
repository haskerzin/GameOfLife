import pygame
import sys
import numpy as np

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
        self.alive = []
        self.map_cells()

    
    def draw_grid(self):
        for i in range(10, self.width, 10):
            pygame.draw.line(self.screen, self.white, (i, 0), (i, self.height), 1)

        for j in range(10, self.height, 10):
            pygame.draw.line(self.screen, self.white, (0, j), (self.width, j), 1)

    def map_cells(self):
        for i in range(self.width//10):
            for j in range(self.height//10):
                self.cells.append([i,j])

    def distance(self, x, y):
        return np.min(np.absolute(np.array(x) - np.array(y)))

    def check_neighbors(self, cell):
        neighbors = []
        for x in self.alive:
            if self.distance(x, cell) == 1:
                neighbors.append(x)
            if len(neighbors) == 8:
                return len(neighbors)
                break
        
        return len(neighbors)

    
    def update_cells(self):
        for x in self.alive:
            if self.check_neighbors(x) < 2 or self.check_neighbors(x) > 3:
                self.alive.remove(x)

        # Implement the rule 4        


    def draw_alive_cells(self):
        for pos in self.alive:
            pygame.draw.rect(self.screen, self.red, [pos[0]*10, pos[1]*10, 10, 10])
                
            
    
    def draw_screen(self):

        pygame.init()

        # Testing the function with a choice of alive cells:
        self.alive = [(20,20), (21,20), (21,21), (22,20)]
        # self.alive = [(20,20)]


        running = True

        while running:

            self.screen
            self.screen.fill(self.black)
            self.draw_grid()
            self.draw_alive_cells()
            self.update_cells()
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False
            
            pygame.time.wait(3000)

            pygame.display.update()
            self.fpsClock.tick(self.fps)
        
        pygame.quit()
        sys.exit()
