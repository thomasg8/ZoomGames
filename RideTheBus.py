from Cards import Cards
import numpy as np, pygame
from time import sleep

class RideBus():
    def __init__(self, row_size = 50):
        self.alive = True
        pygame.init()
        self.myfont = pygame.font.SysFont('Anurati', 46)
        self.myfont2 = pygame.font.SysFont('Anurati', 30)
        pygame.display.set_caption('Ride the Bus')
        self.window = pygame.display.set_mode((700, 700))
        self.window.fill((255,255,255))

        self.cards = Cards()
        self.cards.draw_card()
        self.order = ['Color', 'Higher/Lower', 'In/Out', 'Suit']
        self.first, self.second = None, None
        self.board = [self.cards.card_back_img] *4

        self.HL = self.window.blit(self.cards.card_back_img, (170, 175))
        self.Color = self.window.blit(self.cards.card_back_img, (10, 175))
        self.S = self.window.blit(self.cards.card_back_img, (490, 175))
        self.IO = self.window.blit(self.cards.card_back_img, (330, 175))
        #self.HL = pygame.draw.rect(self.window, (100, 0, 0), (170, 175, self.cards.card_width, self.cards.card_height))
        #self.Color = pygame.draw.rect(self.window, (100, 0, 0), (10, 175, self.cards.card_width, self.cards.card_height))
        #self.S = pygame.draw.rect(self.window, (100, 0, 0), (490, 175, self.cards.card_width, self.cards.card_height))
        #self.IO = pygame.draw.rect(self.window, (100, 0, 0), (330, 175, self.cards.card_width, self.cards.card_height))

        WHITE = (255,255,255)
        self.window.blit(self.myfont2.render('Press r to reset the board', False, (0,0,0)),(10, 10))

        #black red
        self.black = pygame.draw.rect(self.window, (0, 0, 0), (10+25+25, 175-45, 50, 35))
        self.red = pygame.draw.rect(self.window, (255, 0, 0), (10+25+25, 175+230+10, 50, 35))
        # higher lower
        self.H = pygame.draw.polygon(self.window, (124, 252, 0), [[170+50, 175-10], [170+100, 175-10], [170+75, 175-35]])
        self.L = pygame.draw.polygon(self.window, (0, 0, 255), [[170+50, 175+240], [170+125-25, 175+240], [170+75, 175+230+35]])
        # Inside Outside
        self.inside = pygame.draw.rect(self.window, WHITE, (330+20, 175-45, 100, 35))
        self.window.blit(self.myfont.render('Inside', False, (0,0,0)),(330+25, 175-40))

        self.outside = pygame.draw.rect(self.window, WHITE, (330+12, 175+10+230, 125, 35))
        self.window.blit(self.myfont.render('Outside', False, (0,0,0)),(330+12, 175+10+230))
        #Suit
        h,s,d,c = [pygame.transform.scale(pygame.image.load('Cards/{}.png'.format(s)), (50, 50))
                    for s in ['hearts', 'spades', 'diamonds', 'clubs']]
        self.hearts = pygame.draw.rect(self.window, WHITE, (490+25, 175-60, 50, 50))
        self.window.blit(h, (490+25, 175-60))

        self.diamonds = pygame.draw.rect(self.window, WHITE, (490+25+50+5, 175-60, 50, 50))
        self.window.blit(d, (490+25+50+5, 175-60))

        self.spades = pygame.draw.rect(self.window, WHITE, (490+25, 175+10+230, 50, 50))
        self.window.blit(s, (490+25, 175+10+230))

        self.clubs = pygame.draw.rect(self.window, WHITE, (490+25+50+5, 175+10+230, 50, 50))
        self.window.blit(c, (490+25+50+5, 175+10+230))

    def set_board(b, window):
        Color = window.blit(b[0], (10, 175))
        HL = window.blit(b[1], (170, 175))
        IO = window.blit(b[2], (330, 175))
        S = window.blit(b[3], (490, 175))


    def HL():
        pass



    def Gameloop(self):
        RideBus.set_board(self.board, self.window)
        pygame.display.update()
        running = True
        while running:
            #print(self.alive)
            # Quit pygame.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and chr(event.key) == 'r':
                    if len(self.cards.remaining)<4:
                        self.cards.shuffle_cards()
                        print("Shuffling Cards")
                    self.board = [self.cards.card_back_img] * 4
                    self.alive = True; self.first, self.second = None, None
                    RideBus.set_board(self.board, self.window)
                    pygame.display.update()


                pos = pygame.mouse.get_pos(); p1, p2, p3 = pygame.mouse.get_pressed()
                if p1:
                    if self.alive:
                        # color
                        if self.board == [self.cards.card_back_img] * 4:
                            if self.black.collidepoint(pos):
                                self.cards.draw_card()
                                self.board[0] = self.cards.imgs[self.cards.active_card]
                                RideBus.set_board(self.board, self.window)
                                if self.cards.active_card.split('-')[1] not in ['C', 'S']:
                                    self.alive = False
                                else:
                                    self.first = int(self.cards.active_card.split('-')[0])

                            elif self.red.collidepoint(pos):
                                self.cards.draw_card()
                                self.board[0] = self.cards.imgs[self.cards.active_card]
                                RideBus.set_board(self.board, self.window)
                                if self.cards.active_card.split('-')[1] not in ['H', 'D']:
                                    self.alive = False
                                else:
                                    self.first = int(self.cards.active_card.split('-')[0])
                        # higher lower
                        elif self.board[1:] == [self.cards.card_back_img] * 3:
                            if self.H.collidepoint(pos):
                                self.cards.draw_card()
                                self.board[1] = self.cards.imgs[self.cards.active_card]
                                RideBus.set_board(self.board, self.window)
                                if self.first > int(self.cards.active_card.split('-')[0]):
                                    self.alive = False
                                else:
                                    self.second = int(self.cards.active_card.split('-')[0])

                            elif self.L.collidepoint(pos):
                                self.cards.draw_card()
                                self.board[1] = self.cards.imgs[self.cards.active_card]
                                RideBus.set_board(self.board, self.window)
                                if self.first < int(self.cards.active_card.split('-')[0]):
                                    self.alive = False
                                else:
                                    self.second = int(self.cards.active_card.split('-')[0])
                        # inside outside
                        elif self.board[2:] == [self.cards.card_back_img] * 2:
                            if self.inside.collidepoint(pos):
                                self.cards.draw_card()
                                self.board[2] = self.cards.imgs[self.cards.active_card]
                                RideBus.set_board(self.board, self.window)
                                if self.first < int(self.cards.active_card.split('-')[0]) < self.second or self.second < int(self.cards.active_card.split('-')[0]) < self.first:
                                    pass
                                else:
                                    self.alive = False

                            elif self.outside.collidepoint(pos):
                                self.cards.draw_card()
                                self.board[2] = self.cards.imgs[self.cards.active_card]
                                RideBus.set_board(self.board, self.window)
                                if self.first < int(self.cards.active_card.split('-')[0]) < self.second or self.second < int(self.cards.active_card.split('-')[0]) < self.first:
                                    self.alive = False
                                else:
                                    pass
                        # suit
                        elif self.board[-1] == self.cards.card_back_img:
                            if self.hearts.collidepoint(pos):
                                self.cards.draw_card()
                                self.board[-1] = self.cards.imgs[self.cards.active_card]
                                RideBus.set_board(self.board, self.window)
                                if self.cards.active_card.split('-')[1] == 'H':
                                    print('You win!')
                                else:
                                    self.alive = False
                            elif self.diamonds.collidepoint(pos):
                                self.cards.draw_card()
                                self.board[-1] = self.cards.imgs[self.cards.active_card]
                                RideBus.set_board(self.board, self.window)
                                if self.cards.active_card.split('-')[1] == 'D':
                                    print('You win!')
                                else:
                                    self.alive = False
                            elif self.spades.collidepoint(pos):
                                self.cards.draw_card()
                                self.board[-1] = self.cards.imgs[self.cards.active_card]
                                RideBus.set_board(self.board, self.window)
                                if self.cards.active_card.split('-')[1] == 'S':
                                    print('You win!')
                                else:
                                    self.alive = False
                            elif self.clubs.collidepoint(pos):
                                self.cards.draw_card()
                                self.board[-1] = self.cards.imgs[self.cards.active_card]
                                RideBus.set_board(self.board, self.window)
                                if self.cards.active_card.split('-')[1] == 'C':
                                    print('You win!')
                                else:
                                    self.alive = False
                    pygame.display.update()
