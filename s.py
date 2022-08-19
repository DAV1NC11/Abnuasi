import random as randoms


x = (randoms.randint(0, 9))

y = input("Enter a number between 0 and 9: ")

if y == x:
    print('Right')

else:
    print('Wrong')
    print(x)