import pygame
import sys
import numpy as np

'''
1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
'''
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
        self.alive_cells = []
        self.active_cells = []
        self.new_cells = []
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
        return np.max(np.absolute(np.array(x) - np.array(y)))

    '''
    Given a cell it checks how many celll in its neighborhood (distance = 1) are alive.

    :returns: number of alive cells in the neighborhood

    :rtype: int 
    '''
    def check_neighbors(self, cell):
        neighbors = []
        for x in self.alive_cells:
            if self.distance(x, cell) == 1:
                neighbors.append(x)
            if len(neighbors) == 8:
                return len(neighbors)
                break
        
        return len(neighbors)

    def draw_alive_cells(self):
        for pos in self.alive_cells:
            pygame.draw.rect(self.screen, self.red, [pos[0]*10, pos[1]*10, 10, 10])

    '''
    Method that generates the neighborhood of a cell given a distance.

    :returns: list of cells of the neighborhood of the cell given considering the defined distante.

    :rtype: list
    '''
    def neighborhood(self, cell, distance):
        neighborhood = []
        x_min = max(0, cell[0] - distance)
        x_max = min(self.width, cell[0] + distance)
        y_min = max(0, cell[1] - distance)
        y_max = min(self.height, cell[1] + distance)

        for i in range(x_min, x_max + 1):
            for j in range(y_min, y_max + 1):
                neighborhood.append((i,j))
        
        # Removing the cell itself from the neighborhood
        neighborhood.remove(cell)
        
        return neighborhood
    
    '''
    Method to enhance performance when applying rule 4. The idea is to minimize the number of cells
    that we need to check its neighbors. It updates the list self.active_cells.
    '''
    def update_active_cells(self):
        active_cells = []
        for x in self.alive_cells:
            if x not in active_cells:
                for y in self.neighborhood(x,1):
                    if y not in active_cells:
                        active_cells.append(y)
        
        # Guaranteeing the alive cells are not in the active_cells
        active_cells = list(set(active_cells) - set(self.alive_cells))
        
        self.active_cells = active_cells

    '''
    Method to generate new alive cells based on the rule 4.
    '''
    def generate_alive_cells(self):

        for x in self.active_cells:
            # print(x, self.check_neighbors(x))
            if self.check_neighbors(x) == 3:
                self.new_cells.append(x)

    def update_alive_cells(self):
        remover = []
        for x in self.alive_cells:
            if self.check_neighbors(x) < 2 or self.check_neighbors(x) > 3:
                remover.append(x)
        
        self.alive_cells = list(set(self.alive_cells) - set(remover))
        # Adding the new cells
        self.alive_cells = self.alive_cells + self.new_cells
        # for y in self.new_cells:
        #     self.alive_cells.append(y)
        # Reseting the self.new_cells
        self.new_cells = []

    '''
    Method that implements the 4 rules
    '''
    def update(self):
        self.generate_alive_cells()
        self.update_alive_cells()
        self.update_active_cells()
        
                
    
    def draw_screen(self):

        pygame.init()

        # Testing the function with a choice of alive cells:
        # self.alive_cells = [(20,20), (21,20), (22,20), (20,21), (22,21), (21,22)]
        self.alive_cells = [(20,20), (21,20), (22,20)]
        self.update_active_cells()
        # print(self.active_cells)

        running = True
        setup_inicial = True

        while running:

            if setup_inicial == True:
                self.screen.fill(self.black)
                self.draw_grid()
                self.draw_alive_cells()
                pygame.time.wait(3000)
                setup_inicial = False

            self.screen.fill(self.black)
            self.draw_grid()
            self.draw_alive_cells()
            self.update()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

            pygame.display.update()

            pygame.time.wait(3000)

            # If all the cells die exit
            if len(self.alive_cells) == 0:
                running = False

            self.fpsClock.tick(self.fps)
        
        pygame.quit()
        sys.exit()
