from Cards import Cards
import numpy as np, pygame
from time import sleep

class KingsCup():
    def __init__(self, row_size = 50):
        self.cards = Cards()
        x = np.random.normal(37, 5, size=1)
        print("End sampled from normal distribution with mu=37 and sigma=5")
        self.end = min(int(x[0]), 51)

        pygame.display.set_caption('Kings Cup')
        self.window = pygame.display.set_mode((700, 700))

        self.rules = {1: 'Waterfall', 2: 'You', 3: 'Me', 4: 'Floor (point)', 5: 'Guys',
                        6: 'Chicks', 7: 'Heaven', 8: 'Mate', 9: 'Rhyme',
                        10: 'Categories', 11: 'Never Have I ever', 12: 'Questions',
                        13: 'Make a Rule'}




    def make_board(self, row_size = 50):
        #pygame.draw.rect(window, (0, 0, 0),(25, 0, 150, 231))

        self.card_rect = pygame.draw.rect(self.window, (100, 0, 0), (10, 10, self.cards.card_width, self.cards.card_height))
        self.window.blit(self.cards.card_back_img, (10,10))



    def Gameloop(self, cdf_values = True):
        pygame.init()
        myfont = pygame.font.SysFont('Anurati', 150); myfont2 = pygame.font.SysFont('Times New Roman', 25)

        textsurface = self.window.blit(myfont2.render('^Click to draw', False, (124,252,0)), (10,self.cards.card_height+20))
        running = True
        self.x = 210; self.y = 0; self.i = 0
        pygame.display.update()
        while running:
            # Quit pygame.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                


            pos = pygame.mouse.get_pos(); p1, p2, p3 = pygame.mouse.get_pressed()
            if p1:
                if self.card_rect.collidepoint(pos):
                    self.i+=1
                    if self.i == self.end:
                        textsurface = myfont.render('GAME OVER', False, (124,252,0))
                        self.window.blit(textsurface,(10,350))
                        pygame.display.update()
                        print("You lost!")
                        sleep(4)
                        running = False
                    else:
                        self.cards.draw_card(); self.y += 30
                        print(self.cards.active_card, self.rules[int(self.cards.active_card.split('-')[0])])
                        if self.y > 400:
                            self.x += 70
                            self.y = 30

                        self.window.blit(self.cards.imgs[self.cards.active_card], (self.x,self.y))
                        pygame.display.update()
                        sleep(.25)
