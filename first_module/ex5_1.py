#5.1 exercise
count = 0
sum = 0
while True:
    num = input("Enter a number: ")
    if num == 'done':
        break

    try:
        num = int(num)
    except:
        print('Invalid input')
        continue
    
    count += 1
    sum += num

print(sum, count, sum/count)