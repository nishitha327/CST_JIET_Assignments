from math import floor,sqrt
a = int(input('Enter the number:'))
def stairs(a):

	max_height = floor((-1 + sqrt( 1 + 8 * a)) /  2)
	return max_height

result = stairs(a)
print('the maximum height is ' + str(result))
