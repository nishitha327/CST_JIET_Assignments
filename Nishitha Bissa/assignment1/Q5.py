from math import floor
num= int (input('enter the number'))
def sqrt(num):
        res= floor(num ** 0.5 )
        return res
result =sqrt(num)
print('the square root of the number is ' + str(result))
