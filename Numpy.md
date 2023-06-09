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
- 참고) 리스트의 경우 아래와 같이 범위를 가지는 값 생성 가능
lst = list(range(0,9,2))
print(lst)
# [0, 2, 4, 6, 8]

(1) arr = np.arange()
 - 인자값으로 start, stop, step 값을 가짐
 - stop 미만 값까지 ㅊㄹ력 됨 
 - start 값은 생략가능 0부터 시작
 - step 값도 생략가능 1씩 건너 뜀 

arr = np.arange(3,13,3)
print(arr)
# [ 3  6  9 12]

(2) np.linspace() : 갯수에 따른 균일한 간격의 원소를 출력해 줌 
 - step 값 대신 num값 존재
 - stop 값 포함하여 출력
arr2 = np.linspace(0,100,11)
print(arr2)
# [  0.  10.  20.  30.  40.  50.  60.  70.  80.  90. 100.]


(3) np.logspace() : 지정된 범위에서 균등한 간격으로 log scale만큼 원소를 출력
 - 밑값 지정안할시 상용로그 형식으로 출력 
arr=np.logspace(1, 10, 10, base=2) #base값은 로그의 '밑 값을 의미'
print(arr)
#[   2.    4.    8.   16.   32.   64.  128.  256.  512. 1024.]
```


## 1-5) 난수(랜덤값)로 이루어진 n차원 배열 생성하기 
```
- matplotlib 데이터를 시각화해서 보여줄 수 있는 라이브러리
- 설치 안된 경우 설치하여 실행 (한줄 씩 실행)
!pip install matplotlib
import matplotlib.byplot as plt

- numpy이 안에는 난수를 생성해줄 수 있는 module이 존재

(1) np.random.normal(loc, scalce, size) : 인자값에 따른 난수 추출
- loc=정규분포의 평균, scalce=정규분포의 표준편차, size=추출할 표본의 갯수
arr = np.random.normal(0, 1, 10)
print(arr)
#
[ 0.77384142  1.06027454 -0.60405194  0.22105283 -1.7829051   0.9041896
 -0.3780954   0.62260221  0.91879765 -1.49566152]
 
- 사이즈부분을 shpae으로도 표현 가능
arr = np.random.normal(0, 1, (2,3))
print(arr)
#
[[-0.45319076  0.65354101  0.80636819]
 [-0.87195637  1.22914564 -0.4968285 ]]

+) 이때, 원소의 분포를 시각적으로 알아보고 싶다면? plt.hist 이용!
arr = np.random.normal(0, 1, 1000)
plt.hist(arr, bins=100) #bins: 난수를 몇개의 구간으로 나누어 보여줄지 구분
plt.show()



(2) np.random.rand() : 정규분포에서 0~1사이의 값중 균등한 비율로 표본을 추출하는 함수 
- 인자는 표본 갯수 작성 
arr = np.random.rand(1000)
plt.hist(arr, bins=100)
plt.show()



(3) np.random.randn() : 정규분포에서 -1~1 사이의 값 중 균등한 비율로 표본을 추출하는 함수 
- 인자는 표본 갯수 작성 
arr = np.random.randㅜ(1000)
plt.hist(arr, bins=100)
plt.show()


(4) np.random.randint() : 랜덤한 정수만 출력하는 함수
- 인자 : low값, high값, size (로우값부터 하이값의 미만까지 사이즈의 갯수만큼 출력)
- size에 shape입력 가능
- 인자는 한 개 이상 작성해야함(한개 값은 하이값, 0~하이값 중 하나의 정수 반환)
- plt.hist 이용 가능 
arr = np.random.randint(low=1, high=5, size=10)
print(arr)
# [2 1 3 1 3 4 2 1 2 4]

arr = np.random.randint(low=1, high=5, size=(3, 4))
print(arr)
#
[[2 1 4 4]
 [4 3 3 2]
 [4 4 1 2]]
 
 
arr = np.random.randint(5)
print(arr)
# 1

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

