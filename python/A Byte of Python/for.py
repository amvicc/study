#!/usr/bin/env python3

answer = int(input('Enter number to stop:'))

for i in range(1, 100):
    print(i)
    if answer == i:
        break
    else:
        continue
    print('This statement will never printed')
else:
    print('All numbers was printed')
