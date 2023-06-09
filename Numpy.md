import numpy as np

# 1장. N차원 배열 생성
## 1-1) n차원 배열 생성하기 
```
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
```

## 1-2) n차원 배열의 데이터 타입 
```
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
 - 데이터타입이 혼재된 데이터(예)) 튜플,리스트, 문자열 등이 섞여있는 데이터)의 경우 위의 내용 활용 불가 

```

## 1-3) 정해진 형식의 n차원 배열 생성하기  
```
(1) np.zeros() : 모든 원소들이 0으로 된 배열 생성

arr = np.zeros([2,2]) # 대괄호 안에는 행렬 삽입
print(arr)
# [[0. 0.] 
[0. 0.]]

(2) np.ones() : 모든 원소들이 1으로 된 배열 생성

arr = np.ones([3,5]) # 대괄호 안에는 행렬 삽입
print(arr)
# [[1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]]

(3) 
- np.full() : 모든원소들이특정값으로된 배열 생성
arr = np.full((2,3), 5)
print(arr)
# [[5 5 5]
 [5 5 5]]

(4) np.eye(,,k=) : 행이 n, 열이 m이라고 했을 때 n, m shape을 가진 대각원소가 1인 배열 생성 (나머지 요소는 0)
- k값은 대각원소의 출발지점(0부터 출발)
- k값은 생략가능
- m값을 생략하면 n=m인 정방행렬 생성

 arr = np.eye(3, 4, k=0) 
 print(arr) 
# [[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]]
 
 (5) np.zeros_liek() : 원래의 배열과 동일한 shape을 유지한 상태로 원소값을 0으로 바꿈
 arr = np.array([[1,2,3],[4,5,6]])
 arr_z =np.zeros_like(arr)
 print(arr_z)
 #[[0 0 0]
 [0 0 0]]
 
 (6) np.ones_liek() : 원래의 배열과 동일한 shape을 유지한 상태로 원소값을 1으로 바꿈
 arr = np.array([[1,2,3],[4,5,6]])
 arr_z =np.ones_like(arr)
 print(arr_z)
 # [[1 1 1]
 [1 1 1]]

 (7) np.full_liek() : 원래의 배열과 동일한 shape을 유지한 상태로 원소값을 특정값으로 바꿈
 arr = np.array([[1,2,3],[4,5,6]])
 arr_z =np.full_like(arr, 9) #추가로 value 지정
 print(arr_z)
 # [[9 9 9]
 [9 9 9]]
 
```


## 1-4) 특정 범위 값을 가지는 n차원 배열 생성하기 
```
```


## 1-5) 난수로 이루어진 n차원 배열 생성하기 
```
```


## 1-6) 시드(Seed)값을 통한 난수 생성 제어 
```
```


# 2장. n차원 배열의 인덱싱 
## 2-1) 배열의 index 접근하기 
```
```


## 2-2) Fancy 인덱싱 
```
```


## 2-3) Boolean 인덱싱 
```
```

