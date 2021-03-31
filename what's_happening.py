# This porject will help me to store my thoughts
# It will help me to remember things
# make diary entry and stuff
import pickle
from datetime import datetime

print("type '-h' if you need any help.")

def instrucitons():
    print('\'-t\' for thoughts')
    print('\'-d\' for diary')
    print('\'-s\' for shedules')
    print("'exit' to exit")

while True:
    q = input('what\'s up?:')
    if q == '-h':
        print('"-t" if you have any thoughts and want to store.')
        print('"-d" stands for diary, diray entry kind of stuff.')

#----- Thoughts loop ----------------------------------------------------------
    elif '-t' == q:
        print('"exit" to exit')
        lis = []
        while True: # Loop for thoughts
            thoughts = input('What\'s your thought?: ')
            if thoughts == 'exit':
                break
            elif len(thoughts) >= 5:
                lis.append(thoughts+'('+str(datetime.now())[0:19]+')'+'\n')
        try:
            for i in lis:
                pickle.dump(i, open('thoughts.dat', 'ab'))
            print(pickle.load(open('thoughts.dat', 'rb')))
        except EOFError:
            pass

#---- Diary loop ----------------------------------------------------------
    elif '-d' == q:
        print('"exit" to exit')
        lines = []
        lines.append('\n\n'+'('+str(datetime.now())[0:19]+')'+'\n')
        while True:
            d = input('diary: ')
            if d == 'exit':
                break
            elif len(d) >= 5:
                lines.append(d+'\n')
        try:
            for i in lines:
                pickle.dump(i, open('diary.dat', 'ab'))
            print(pickle.load(open('diary.dat', 'rb')))
        except EOFError:
            pass

#---- Reading part ----------------------------------------------------------
    elif '-r' == q:
        print('-h for help')
        r = input('what do you wanna read: ')
        if r == '-h':
            instrucitons()
            
    elif 'saket' == q:
        print()

    elif q == 'exit': # this will break the code and the program will exit
        break
`1`