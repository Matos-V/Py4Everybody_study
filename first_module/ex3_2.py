#3.2 exercise
hrs = input('Enter hours: ')
try:
    hrs = float(hrs)
except:
    print('Error, please enter numeric input')
    exit()

rate = input('Enter rate: ')
try:
    rate = float(rate)
except:
    print('Error, please enter numeric input')
    exit()


if hrs<= 40:
    pay = hrs*rate
else:
    pay = 40*rate + (hrs-40)*rate*1.5
print(pay)