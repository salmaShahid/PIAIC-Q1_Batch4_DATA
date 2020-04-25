#numpy (numerical )
import numpy as np #sara code np var me agya

# #range(5,9)
# #numpy boht zada faster hay
#
# print(np)
# #range in numpy
# r =np.arange(1,20)
# print(r)
#
# #square with forward or backward loop
# sqr = [item*item for item in r] #backward loop
# print(sqr)
# #for square eof all num
# sq=[]
# for item in r:
#     print(item)#forward
#     sq.append(item*item)
#
# print(sq)


#forward(neeche ki trf)
#backward(aik hi line me)


#multidimensional array
#1d array simple one direction
#multi (rows,column)
#randn(4 row  3 col)
# data = np.random.randn(4,3)
# print(data)

# dat = [2,3,4]
# #4 se mul
# cd = dat*4 #wrong one [2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4]
# print(cd)
#
# f = np.array([2,3,4]) #[ 8 12 16] right one
# c = f *4
# print(c)

# #array shape
# s = np.array([[1,2,3],[4,5,6]])
# print(s.shape) #(2, 3) row,col
# # print(s.ndim) #dime check
# # arr2#2 dim
# #homogeinus arrayy same type of array must in numpy

d = np.zeros(5) #to print zeros
print(d) #[0. 0. 0. 0. 0.]


