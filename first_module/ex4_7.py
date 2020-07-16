#4.7 exercise
def computegrade(grade):
    if grade < 0:
        return print('Bad score')
    elif grade < 0.6:
        return print('F')
    elif grade<0.7:
        return print('D')
    elif grade < 0.8:
        return print('C')
    elif grade < 0.9:
        return print('B')
    elif grade < 1:
        return print('A')
    else:
        return print('Bad score')

grade = input('Type a grade between 0 and 1: ')
try:
    grade = float(grade)
except:
    print('Bad score')
    exit()

computegrade(grade)