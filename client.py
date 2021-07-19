"""
Main pygame project.

Houses the following libraries made specifically for the game.
"""

import pygame
from network import Network

pygame.init()

width = 500
height = 500

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pixeller")

class Renderer():
    def update():
        win.fill((255, 255, 255))

    def draw(player):
        player.draw(win)
        
    class Display:
        def update():
            pygame.display.update()

class Utility:
    """
    Utilities required for several things.
    eg. converting data
    """
    def read_pos(string):
        print("string is ")
        print(string)
        string = string.split(",")
        return int(int(string[0]), int(string[1]))
    
    def make_pos(tup):
        return str(tup[0]) + ',' + str(tup[1])

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.vel = .3

        self.rect = (x, y, width, height)
    
    def draw(self, window):
        pygame.draw.rect(win, self.color, self.rect)
    
    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.vel
        
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.vel
        
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y -= self.vel
        
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y += self.vel
        
        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            self.vel = .5
        else:
            self.vel = .3

        self.rect = (self.x, self.y, self.width, self.height)

class Client():
    # the network backend, constantly swaps data between the server and the client.
    network = Network()

    startPos = network.getPos()
    playerList = network.getPlayers() # returns a tuple of players connected.

    entity_plrs = []


    # the player renderable entity.
    print("Player start position is "+str(startPos[0])+", "+str(startPos[1]))
    player = Player(int(startPos[0]), int(startPos[1]), 100, 100, (0, 255, 0))

    newPlayer = Player(int(startPos[0]), int(startPos[1]), 100, 100, (255, 0, 0))
    entity_plrs.append(newPlayer)
        
    
    


    # game logic clock.
    clock = pygame.time.Clock()

    def main(self):
        run = True
        self.clock.tick(60)
        while run:

            #p2Pos = Network.send(Utility.make_pos((self.player.x, self.player.y)))

            #self.player2.x = p2Pos[0]
            #self.player2.y = p2Pos[1]

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()

            Renderer.update()
            self.player.move()
            Renderer.draw(self.player)
            Renderer.draw(self.newPlayer)
            
            Renderer.Display.update()

c = Client()
c.main()