import tkinter as tk, pygame


def Cube():
    window.destroy()
    import Cube
    print("""\n\n\n\nGavin presents Cube!\nClick on the pile to update the card.
            Press a to see how many cards are in the piles.""")
    for i in range(1,4):
        pygame.init()
        #pygame.font.init()
        cards = Cube.CubeCards(r=i)
        Cube.Cube(cards)
        print("\n\n\n\n\n")

def KingsCup():
    window.destroy()
    import KingsCup
    print("""\n\n\n\nGavin presents Kings Cup!\nClick on the pile to draw.""")
    KC = KingsCup.KingsCup()
    KC.make_board()
    KC.Gameloop()

def RB():
    window.destroy()
    import RideTheBus
    print("""\n\n\n\nGavin presents Ride the Bus!\nClick on the icons to play.
            The rounds are Color, Higher/Lower, Inside/Outside, Suit.""")
    bus = RideTheBus.RideBus()
    bus.Gameloop()


window = tk.Tk()
greeting = tk.Label(text="Select a game"); greeting.pack()


button = tk.Button(text="Cube",width=25, height=5, command=Cube)
button.pack()


button2 = tk.Button(text="Kings Cup",width=25, height=5, command=KingsCup)
button2.pack()

button3 = tk.Button(text="Ride the Bus",width=25, height=5, command=RB)
button3.pack()


window.mainloop()
