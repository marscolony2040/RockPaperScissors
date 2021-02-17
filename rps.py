import random as rd
import tkinter as tk
import tkinter.ttk as ttk


def rockpaperscissors():
    r = ['rock','paper','scissors']
    s = ['paper', 'scissors', 'rock']

    your_score = 0
    their_score = 0

    while True:
        your_play = input('Enter rock paper or scissors: ')
        their_play = r[rd.randint(0,2)]
        idx = r.index(your_play)
        idy = r.index(their_play)
        if s[idx] == their_play:
            their_score += 1
        if s[idy] == your_play:
            your_score += 1
        print("Your Play: {} | Their Play: {}".format(your_play, their_play))
        print("Your Score: {} | Their Score: {}".format(your_score, their_score))
            


class Home(tk.Tk):

    r = ['rock','paper','scissors']
    s = ['paper', 'scissors', 'rock']

    your_score = 0
    their_score = 0

    def __init__(self):
        tk.Tk.__init__(self)
        tk.Tk.wm_title(self, 'Rock, Paper, Scissors')
        self.geometry('300x80')

        scrFrame = tk.Frame(self)
        scrFrame.pack(side=tk.BOTTOM)
        self.scoreFrame(scrFrame)

        plyFrame = tk.Frame(self)
        plyFrame.pack(side=tk.BOTTOM)
        self.playFrame(plyFrame)

        
        btnFrame = tk.Frame(self)
        btnFrame.pack(side=tk.TOP)
        self.buttonFrame(btnFrame)

    def calculateScore(self, obj):
        their_play = self.r[rd.randint(0, 2)]
        idx = self.r.index(obj)
        idy = self.r.index(their_play)
        if self.s[idx] == their_play:
            self.their_score += 1
        if self.s[idy] == obj:
            self.your_score += 1
        self.theirPlay.configure(text=their_play)
        self.yourScore.configure(text='Your Score: {}'.format(self.your_score))
        self.theirScore.configure(text='Their Score: {}'.format(self.their_score))

    def clearAll(self):
        self.your_score = 0
        self.their_score = 0
        self.yourScore.configure(text='Waiting...')
        self.theirScore.configure(text='Waiting...')
        self.theirPlay.configure(text='Waiting...')
    
    def buttonFrame(self, frame):
        tk.Button(frame, text='Rock', command=lambda: self.calculateScore('rock')).grid(row=1, column=1)
        tk.Button(frame, text='Paper', command=lambda: self.calculateScore('paper')).grid(row=1, column=2)
        tk.Button(frame, text='Scissors', command=lambda: self.calculateScore('scissors')).grid(row=1, column=3)

    def scoreFrame(self, frame):
        self.yourScore = tk.Label(frame, text='Waiting...')
        self.yourScore.grid(row=1, column=1)
        self.theirScore = tk.Label(frame, text='Waiting...')
        self.theirScore.grid(row=1, column=2)
    
    def playFrame(self, frame):
        self.theirPlay = tk.Label(frame, text='Waiting...')
        self.theirPlay.grid(row=1, column=1)
        tk.Button(frame, text='Clear', command=lambda: self.clearAll()).grid(row=1, column=2)


Home().mainloop()
