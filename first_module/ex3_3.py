#3.3 exercise
grade = input('Type a grade between 0 and 1 ')
grade = float(grade)
if grade < 0:
    print('Grade out of range')
elif grade < 0.6:
    print('F')
elif grade<0.7:
    print('D')
elif grade < 0.8:
    print('C')
elif grade < 0.9:
    print('B')
elif grade < 1:
    print('A')
else:
    print('Grade out of range')