import numpy as np

# 1차원 배열
arr = np.array([1,2,3])
print(arr)



# 2차원 배열
arr = np.array([[1,2,3],[4,5,6]])
print(arr)

type(arr)

tpl=(4,5,6)
arr=np.array(tpl)
print(arr)

arr1 = np.array([1,2,3])
arr2 = np.array([[1,2,3],[4,5,6]])

print(arr1.shape, arr2.shape) # shape :(행,열)
print(arr1.ndim, arr2.ndim)   # ndim : 차원
print(arr1.size, arr2.size)   # size : 원소의 개수