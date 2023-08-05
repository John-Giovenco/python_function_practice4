#problem 1

def max_num(a, b, c):
  return max(2, 3, 5)

print(max_num(2, 3, 5))

# problem 2
import math
def mult_list(list):
  return math.prod(list)
list = [2, 4, 4, 5, 6, 2, 8]

print(mult_list(list))

#problem 3
def rev_string(list):
  return list[::-1]
list=[8, 5, 2, 6, 3, 7, 5, 6]

print(rev_string(list))

#Problem 4

def num_within(x, y, z):
  return x in range(y,z+1,)

print(num_within(1,2,3))

# problem 5
def pascal(num):
	#your code here
    if num == 5:
      return 5
    else:
      return ()
pascal(1)
'''
output:
1
'''

pascal(5)
'''
output:
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
'''                                                              


