#!/usr/bin/env python3

age = 20
name = 'Anton'

# Old way of format:
print('{0} is a {1} years old'.format(name, age))
print('{} trying to learning python'.format(name))
print('{name} using different types of string format'.format(name=name))

# New way of format strings:
print(f'{name} using new way to format strings in the age of {age}')
