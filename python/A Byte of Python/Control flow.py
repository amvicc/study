#!/usr/bin/env python 3

number = 20  # 4*5
runner = True

while runner:
    answer = int(input('Enter result 4*5'))
    if answer == number:
        print('Congratulation! You answered right!')
        runner = False
    else:
        print('You answered wrong!Try again)')
else:
    print('Else-block which after while2')
