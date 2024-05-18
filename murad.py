import qanaqer

a = [1,2,3,4,5,6]
b = qanaqer.filter(a, 3)

c = qanaqer.sort(b)
if qanaqer.isValid(c, '6'):
    print('Test passed!')
else:
    print('Test failed!')