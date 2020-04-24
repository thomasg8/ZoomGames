import pygame, numpy as np
from random import shuffle
from os import listdir
from time import sleep


class CubeCards():
    def __init__(self, x_s=150, y_s=231, r=1):
        self.round = r

        self.imgs = dict()

        for card in [[c, pygame.transform.scale(pygame.image.load('Cards/'+c),
                (int(x_s), int(y_s)))] for c in listdir('Cards') if '-' in c]:
            self.imgs[card[0].replace('.png',"")] = card[1]

        self.deck = list(self.imgs.keys())
        shuffle(self.deck)
        self.board, self.used = CubeCards.set_board(self.round, self.deck)
        self.remaining = list(set(self.deck) - set(self.used))


        self.m = list()
        for i in range(1, 4-self.round+1):
            row = list()
            for j in range(1, 4-self.round+1):
                x = 25*i + x_s*(i-1)
                y = y_s*(j-1)
                row.append((x,y))
            self.m.append(row)

    def set_board(r, deck):
        n = 4-r ; p=0
        b = np.chararray((n, n), itemsize=4)
        used = [deck[p] for p in range(n*n)]
        for i in range(n):
            for j in range(n):
                b[i,j] = deck[p]
                p+=1
        return b, used

    def choose_card(self, i, j, turn):
        n = 4-self.round
        #for card in self.deck[n*n:]
        old = self.board[int(i), int(j)]
        self.board[int(i),int(j)] = self.deck[n*n+turn]
        self.used.append(self.deck[n*n+turn])
        self.remaining = list(set(self.deck) - set(self.used))
        print(old, 'to', self.board[int(i), int(j)])





def Cube(cards):
    pygame.display.set_caption('Cube')
    window = pygame.display.set_mode((700, 700))

    round_len = len(cards.remaining)
    print(round_len, 'cards remaining')
    piles = np.ones((4-cards.round,4-cards.round))
    myfont = pygame.font.SysFont('Comic Sans MS', 30)



    turn = 0
    for round in [0]:
        running = True
        # Draw Once
        Rect1 = pygame.draw.rect(window, (0, 0, 0),(25, 0, 150, 231))
        Rect2 = pygame.draw.rect(window, (0, 0, 0),(25, 231, 150, 231))
        Rect3 = pygame.draw.rect(window, (0, 0, 0),(25, 462, 150, 231))
        Rect4 = pygame.draw.rect(window, (0, 0, 0),(200, 0, 150, 231))
        Rect5 = pygame.draw.rect(window, (0, 0, 0),(200, 231, 150, 231))
        Rect6 = pygame.draw.rect(window, (0, 0, 0),(200, 462, 150, 231))
        Rect7 = pygame.draw.rect(window, (0, 0, 0),(375, 0, 150, 231))
        Rect8 = pygame.draw.rect(window, (0, 0, 0),(375, 231, 150, 231))
        Rect9 = pygame.draw.rect(window, (0, 0, 0),(375, 462, 150, 231))

        for i in range(4-cards.round):
            for j in range(4-cards.round):
                window.blit(cards.imgs[cards.board[i,j].decode('utf-8')], cards.m[i][j])
        pygame.display.update()
        # Main Loop
        while running:
            # Quit pygame.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and chr(event.key) == 'a':
                    print(piles)
            if turn==round_len:
                running = False

            pos = pygame.mouse.get_pos(); p1, p2, p3 = pygame.mouse.get_pressed()
            if p1:

                if Rect1.collidepoint(pos):
                    print("Rect1")
                    r = 0; c = 0
                    cards.choose_card(r,c, turn); turn+=1; piles[c,r]+=1


                    print('Pile size:', piles[c,r]); print('-'*10)
                    print(len(cards.remaining), 'cards remaining')
                    window.blit(cards.imgs[cards.board[r,c].decode('utf-8')], cards.m[r][c])
                    pygame.display.update()
                if cards.round in [1,2]:
                    if Rect2.collidepoint(pos):
                        r = 0; c = 1
                        cards.choose_card(r,c, turn); turn+=1; piles[c,r]+=1
                        print('Pile size:', piles[c,r]); print('-'*10)
                        print(len(cards.remaining), 'cards remaining')
                        window.blit(cards.imgs[cards.board[r,c].decode('utf-8')], cards.m[r][c])
                        pygame.display.update()


                    elif Rect4.collidepoint(pos):
                        r = 1; c = 0
                        cards.choose_card(r,c, turn); turn+=1; piles[c,r]+=1
                        print('Pile size:', piles[c,r]); print('-'*10)
                        print(len(cards.remaining), 'cards remaining')
                        window.blit(cards.imgs[cards.board[r,c].decode('utf-8')], cards.m[r][c])
                        pygame.display.update()
                    if Rect5.collidepoint(pos):
                        r = 1; c = 1
                        cards.choose_card(r,c, turn); turn+=1; piles[c,r]+=1
                        print('Pile size:', piles[c,r]); print('-'*10)
                        print(len(cards.remaining), 'cards remaining')
                        window.blit(cards.imgs[cards.board[r,c].decode('utf-8')], cards.m[r][c])
                        pygame.display.update()
                if cards.round in [1]:
                    if Rect3.collidepoint(pos):
                        r = 0; c = 2
                        cards.choose_card(r,c, turn); turn+=1; piles[c,r]+=1
                        print('Pile size:', piles[c,r]); print('-'*10)
                        print(len(cards.remaining), 'cards remaining')
                        window.blit(cards.imgs[cards.board[r,c].decode('utf-8')], cards.m[r][c])
                        pygame.display.update()


                    elif Rect6.collidepoint(pos):
                        r = 1; c = 2
                        cards.choose_card(r,c, turn); turn+=1; piles[c,r]+=1
                        print('Pile size:', piles[c,r]); print('-'*10)
                        print(len(cards.remaining), 'cards remaining')
                        window.blit(cards.imgs[cards.board[r,c].decode('utf-8')], cards.m[r][c])
                        pygame.display.update()

                    elif Rect7.collidepoint(pos):
                        r = 2; c = 0
                        cards.choose_card(r,c, turn); turn+=1; piles[c,r]+=1
                        print('Pile size:', piles[c,r]); print('-'*10)
                        print(len(cards.remaining), 'cards remaining')
                        window.blit(cards.imgs[cards.board[r,c].decode('utf-8')], cards.m[r][c])
                        pygame.display.update()

                    elif Rect8.collidepoint(pos):
                        r = 2; c = 1
                        cards.choose_card(r,c, turn); turn+=1; piles[c,r]+=1
                        print('Pile size:', piles[c,r]); print('-'*10)
                        print(len(cards.remaining), 'cards remaining')
                        window.blit(cards.imgs[cards.board[r,c].decode('utf-8')], cards.m[r][c])
                        pygame.display.update()

                    elif Rect9.collidepoint(pos):
                        r = 2; c = 2
                        cards.choose_card(r,c, turn); turn+=1; piles[c,r]+=1
                        print('Pile size:', piles[c,r]); print('-'*10)
                        print(len(cards.remaining), 'cards remaining')
                        window.blit(cards.imgs[cards.board[r,c].decode('utf-8')], cards.m[r][c])
                        pygame.display.update()
                sleep(.5)
