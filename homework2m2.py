x = 38
print('Hello!')
if x < 0:
    print('Below zero')
print('Good bye! ')

a, b = 10, 5
if a > b:
    print('\na > b')
if a > b and a > 0:
    print('success')
if a > b and (a > 0 or b < 1000):
    print('success too')
if 5 < b and b < 10:
    print('success also')

if '34' > '123':
    print('\nsuccess')
if '123' > '12':
    print('success too')
if [1, 2] > [1, 1]:
    print('success also')

if '6' > 5:
    print('\nsuccess')
if [5, 6] > 5:
    print('success too')
#if '6' != 5:
    print('success also')