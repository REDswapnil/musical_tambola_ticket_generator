import collections
import random
import sys
from songs import SONG_LIST
from flask import Flask, render_template

app = Flask(__name__)


def generate_single_ticket():

    ticket = []
    col_set = collections.defaultdict(set)

    for _ in range(ROWS):
        row = generate_column()

        for i in range(COLS):
            selected_song = SONG_BRACKETS[i][random.randint(0, 9)]
            while selected_song in col_set[i]:
                selected_song = SONG_BRACKETS[i][random.randint(0, 9)]
            col_set[i].add(selected_song)
            if row[i]:
                row[i] = selected_song
            else:
                row[i] = ""

        ticket.append(row)

    return ticket


def generate_tickets():
    tickets = []
    for i in range(NUMBER_OF_TICKETS):
        tickets.append(generate_single_ticket())
    return tickets


def generate_column():
    col = [False] * COLS
    count = random.sample(list(range(9)), 5)
    for index in count:
        col[index] = True
    return col


@app.route('/')
def hello():
    return render_template('template.html', tickets=generate_tickets())


if __name__ == "__main__":

    NUMBER_OF_TICKETS = 80
    COLS = 9
    ROWS = 3

    SONG_BRACKETS = [
        SONG_LIST[0: 10],
        SONG_LIST[10: 20],
        SONG_LIST[20: 30],
        SONG_LIST[30: 40],
        SONG_LIST[40: 50],
        SONG_LIST[50: 60],
        SONG_LIST[60: 70],
        SONG_LIST[70: 80],
        SONG_LIST[80: 90]
    ]

    if len(sys.argv) <= 1:
        print(f'Running app with number of tickets to generate :: {NUMBER_OF_TICKETS}')
        app.run()
    elif len(sys.argv) == 2:
        NUMBER_OF_TICKETS = int(sys.argv[1])
        print(f'Running app with number of tickets to generate :: {NUMBER_OF_TICKETS}')
        app.run()
    else:
        print('Invalid command line arguments')
        help = f'USE :: python main.py NUMBER_OF_TICKETS'
        print(help)


