from datetime import datetime as dt

def chk_input(st):
    q = input('S/E? ')
    if q == 's':
        with open('Log.txt', 'a') as f:
            f.write(f'Start: {dt.today()}\n')
        start = dt.today()
        print(f'Start: {start}')
        chk_input(start)

    if q == 'e':
        print(f'End: {dt.today()}\nElapsed: {dt.today()-st}')
        with open('Log.txt', 'a') as f:
            f.write(f'End: {dt.today()}\n')
            f.write(f'Elapsed: {dt.today()-st}\n\n')
       
chk_input(dt.today())