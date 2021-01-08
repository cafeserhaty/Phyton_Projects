numbers=[]
for i in range(0,5):
    numbers.append(input('Enter {}. number:'.format(i+1)))
print('\n')
for i in range(0,5):
    for j in range(0,5-i):
        print(numbers[i],end=' ')
    print('\n')
