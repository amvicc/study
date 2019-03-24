#!/usr/bin/env python3


def sayHello():
    print('Hello!')


def compare(a, b=0, c=5):
    print(a, b, c)
    if a == b:
        print('Equal')
    if a > b:
        print('a > b')
    if a < b:
        print('a < b')


def total(initial=5, *numbers, **keywords):
    '''First part.

    Second part.'''
    count = initial
    for number in numbers:
        count += number
    for key in keywords:
        count += keywords[key]
    return count


def total2(initial=5, *numbers, extra_number):
    count = initial
    for number in numbers:
        count += number
    count += extra_number
    print(count)


sayHello()
compare(2, 2)
compare(2, 6)
compare(4, 1)
compare(3)
compare(1, c=20)
print(total(10, 1, 2, 3, vegetables=50, fruits=100))
print(total.__doc__)
total2(10, 1, 2, 3, extra_number=50)
