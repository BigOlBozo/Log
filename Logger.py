from time import perf_counter as click
from datetime import datetime as dt
from time import sleep
pp = []
cs = []
def check_input():
    if input() == 'p':
        pause_start = dt.today()
        with open('Log.txt', 'a') as f:
            f.write(f'Pause Start: {pause_start}\n')
    if input() == 'o':
        pause_end = dt.today()
        with open('Log.txt', 'a') as f:
            f.write(f'Pause End: {pause_end}\n')
    if input() == 'a':
        pass
    
def chk_input(st):
    q = input('S/E?')
    if q == 'o':
        with open('Log.txt', 'a') as f:
            f.write(f'Start: {dt.today()}\n')
        start = dt.today()
        print(f'Start: {start}')
        chk_input(start)

    if q == 'p':
        print(f'End: {dt.today()}')
        with open('Log.txt', 'a') as f:
            f.write(f'End: {dt.today()}\n')
            f.write(f'Elapsed: {dt.today()-st}\n\n')
       
chk_input(dt.today())