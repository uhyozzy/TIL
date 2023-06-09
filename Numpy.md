import numpy as np

# 1장. N차원 배열 생성

```
1-1) n차원 배열 생성하기 
 1차원 배열
arr = np.array([1,2,3])
print(arr)


 2차원 배열
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

1-2) n차원 배열의 데이터 타입 
- 문자형 확인 방법
arr = np.array([1,2,3], dtype=np.float) #dtype=np.형태 하게되면 문자형 확인 가능
print(arr, arr.dtype) #[1. 2. 3.] float64

arr = np.array([1,2,3], dtype=np.int)
print(arr, arr.dtype) # [1 2 3] int64

arr = np.array([1,0,0], dtype=np.bool)
print(arr, arr.dtype) # [ True False False] bool

- 형변환
arr = np.array([0,1,2,3])
print(arr, arr.dtype)

arr =arr.astype(np.float32)
print(arr, arr.dtype) #[0. 1. 2. 3.] float32

※ 주의
 - 데이터타입이 혼재된 데이터의 경우 위의 내용 활용 불가 

```

