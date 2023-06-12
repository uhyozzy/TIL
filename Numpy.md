### 넘파이 실행 : import numpy as np

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
- seed : 난수 발생지점을 조절 가능 
- 시작점이 같으면 항상 같은 난수 표본이 발생하게 됨 

np.random.seed(1)
arr = np.random.rand(10)
print("난수발생 1\n", arr)

```


# 2장. n차원 배열의 인덱싱 
## 2-1) 배열의 index 접근하기 
```
- 인덱스에 접근한다: 배열의 몇번째 원소 값이 무엇인지, 특정한 배열의 값이 무엇인지 탐색하는 과정

(1) 1차원 배열 인덱싱
arr = np.array([0,1,2,3,4,5,6,7,8,9])
arr = np.arange(10)
print(arr)

- 인덱스가 3번째 있는 값 구해보기 (※컴퓨터 프로그래밍 언어에서 인덱스는 1이 아닌 0부터 시작)
print(arr[3])
# 3
- 인덱스가 -1번째 있는 값 구해보기 (※마이너스 값은 뒤부터 읽음)
print(arr[-1])
# 9

(2) 2차원 배열 인덱싱
arr = np.array([[1,2,3,4], 
                [5,6,7,8],
                [9,10,11,12]])
print(arr, arr.shape, arr.ndim)
# 
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]] (3, 4) 2
 
print(arr[0][3]) # 행이 0이고 열이 3번째 인 값 
                 # 4
혹은 print(arr[0,3])으로도 표현 가능

(3) 1차원 배열에서 범위값 탐색 
arr = np.array([0,1,2,3,4,5,6,7,8,9])

- 원소 3부터 8사이의 값 탐색
print(arr[3:8]) # [3,4,5,6,7]

- 원소 3부터 출력
print(arr[3:]) # [3,4,5,6,7,8,9]

- 원소 7미만까지 출력 
print(arr[:7]) # [0,1,2,3,4,5,6]

- -1미만까지 출력 
print(arr[:-1]) # [0,1,2,3,4,5,6,7,8]


(4) 1차원 배열에서 범위값 탐색 
arr = np.array([[1,2,3,4], 
                [5,6,7,8],
                [9,10,11,12]])

- 0번째 행에서 모든 열의 값을 출력
print(arr[0, :]) # [1 2 3 4]

- 특정 열의 모든 값 출력 
print(arr[:, 1]) # [2  6 10]

- 0부터 3미만의 행에 대해서 모든 열에 해당하는 값 => 모든 원소들이 출력
print(arr[:3, :])
# 
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
 
- 2미만까지의 행에서 2번째 열부터 출력 
print(arr[:2, 2:])
#
[[3 4]
 [7 8]]
```


## 2-2) Fancy 인덱싱 
```
- Fancy 인덱싱 : 특정 인덱싱을 여러개 선택해서 배열하는 방법
- 방법 : print시 대괄호 두번 중첩하여 작성

(1) 1차원 배열 
arr = np.array([5, 10, 15, 20, 25, 30])

- 0, 2, 4번째 인덱싱 출력
print(arr[[0, 2, 4]])

(2) 2차원 배열
arr = np.array([[5, 10, 15, 20],
                [25, 30, 25, 40],
                [45, 50, 55, 60]])
                
- 0부터 2행까지, 2열부터 끝까지 출력 
print(arr[[0,2], 2:])  # 처음 값이나 끝값이 없을 때는 ':' 표시 사용
#[[15 20]
 [55 60]]

```


## 2-3) Boolean 인덱싱 
```
- Boolean 인덱싱 : True와 False값을 이용해 배열의 값을 탐색하는 인덱싱
- True에 해당하는 값은 가져오고 False에 해당하는 값은 가져오지 않음

(1) 1차원 배열
arr = np.array([1,2,3,4])
print(arr[[True, False, True, True]])
# [1 3 4]

(2) 2차원 배열 
arr = np.array([[1,2,3,4],
                [5,6,7,8]])
                
- 1행은 가져오지 않고 0행만 가져옴, 열은 전부 다 가져오기 
print(arr[[True, False], True])

```

## 2-4) 조건연산자를 이용하여 인덱싱
```
arr = np.array([[1,2,3,4],
                [5,6,7,8]])
                
- 4보다 큰 원소를 전부 가져오기
print(arr[arr >6])
# [7 8]
```


# 3장. N차원 배열연산법
## 3-1) 배열의 연산1
> 사칙연산, 제곱, 제곱근, 몫, 나머지
```
- 넘파이에서는 파이썬 기본 연산자를 행렬이나 텐서 간에 연산가능 하도록 모듈안에 정의가 되어 있음 
arr1 = np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]]) 
arr2 = np.array([[2,2,2],
                 [2,2,2],
                 [2,2,2]]) 
                 
(1) 사칙연산: 각각 자리에 해당하는 원소끼리 +, -, *, / 됨 
- 덧셈
print(arr1 + arr2) 
혹은
print(np.add(arr1,arr2)) 

- 뺄셈
print(arr1 - arr2) 
혹은
print(np.substract(arr1,arr2))

- 곱셈 
print(arr1 * arr2) 
혹은
print(np.multiply(arr1,arr2))

- 나눗셈
print(arr1 / arr2) 
혹은
print(np.divide(arr1,arr2))

(2) 제곱
- arr1에 대해서 2제곱 하기
print(arr1 ** 2) 

- 자기 자신 제곱하기 
print(np.square(arr1))

(3) 제곱근 
print(np.sqrt(arr1))

(4) 몫
- 각 원소를 2로 나눴을 때 몫 구하기
print(arr1 // 2) 

(5) 나머지
- 각 원소를 2로 나눴을 때 나머지 구하기
print(arr1 % 2)

```

## 3-2) 배열의 연산2
> 내적(dot product), 절댓값, 올림, 반올림, 버림
```

(1) 내적(dot product) = 스칼라 곲, 점곲
- 두 행렬을 곱했을 때 결과값이 스칼라 값이 나오는 연산 

(1-1) 1차원 행렬 
arr1 = np.array([2,3,4])
arr2 = np.array([1,2,3])

print(np.dot(arr1, arr2))
# 20  ---> 2*1 + 3*2 + 4*2 (각각의 원소끼리의 곱의 합)

(1-2) 2차원 행렬 
< dot product 의 연산 과정 > : 벡터의shape에 따라 결과shape도 정해짐
[[a, b]   [[e, f]       [[ae + bg, af + bh]   
 [c, d]]   [g, h]]  =>   [ce + dg, cf + dh]]

arr1 = np.array([[1,2],
                 [4,5]])                 
arr2 = np.array([[1,2],
                 [0,3]])
print(np.dot(arr1,arr2))
#
[[ 1  8]
 [ 4 23]]
 
(2) 절댓값
arr1 = np. array([[1, -2],
                  [-4, 5]])
print(np.abs(arr1))

#
[[1 2]
 [4 5]]

(3) 올림
arr1 = np. array([[1.932, -2.339],
                  [-4.145, 5.206]])
print(np.ceil(arr1))
#
[[ 2. -2.]
 [-4.  6.]]

(4) 내림
print(np.floor(arr1))
#
[[ 1. -3.]
 [-5.  5.]]

(5) 반올림
print(np.round(arr1))
#
[[ 2. -2.]
 [-4.  5.]]
 
(6) 버림 
print(np.trunc(arr1))
#
[[ 1. -2.]
 [-4.  5.]]

```

## 3-3) 배열의 연산3
> min / max / sum / mean / std / cumsum / median
```
arr = np.array([[1, 2, 3], 
                [0, 1, 4])

(1) min : 원소중에 가장 작은 값 출력 
print(np.min(arr)) #0
print(arr.min()) #0
print(arr.min(axis=0)) # [0, 1, 3] 열끼리 비교했을 때 가장 작은 값 출력
print(arr.min(axis=1)) # [1, 0] 행끼리 비교했을 때 가장 작은 값 출력?

(2) max : 원소들 중에 가장 큰 값 출력
print(np.max(arr)) #4
print(arr.max()) #4
print(arr.min(axis=0)) # [1, 2, 4] 열끼리 비교했을 때 가장 큰 값 출력
print(arr.min(axis=1)) # [3, 4] 행끼리 비교했을 때 가장 큰 값 출력

(3) sum : 원소들의 합 출력
print(np.sum(arr)) #11
print(arr.sum()) #11
print(arr.sum(axis=0)) #[1 3 7] 열끼리 더한 값 출력 
print(arr.sum(axis=1)) #[6 5] 행끼리 더한 값 출력

(4) mean : 원소들의 평균값 출력 
print(np.mean(arr)) #1.83
print(arr.mean()) #1.83
print(arr.mean(axis=0)) # [0.5 1.5 3.5]
print(arr.mean(axis=1)) # [2.      1. 6666667] 

(5) std : 원소들의 표준편차 값(분산의 정도를 나타낸 수치)
print(np.std(arr))
print(arr.std())
print(arr.std(axis=0))
print(arr.std(axis=1))

(6) cumsum : 누적합을 계산하는 함수 
print(np.cumsum(arr)) #[1 3 6 6 7 11] 
print(arr.cumsum())  #[1 3 6 6 7 11]  axis를 지정하지 않으면 1차원 배열로 출력
print(arr.cumsum(axis=0))
#
[[1 2 3]
 [1 3 7]]
print(arr.cumsum(axis=1))
#
[[1 3 6]
 [0 1 5]]

(7) median : 중앙값을 출력하는 함수 (원소들을 대소적으로 정렬했을 때 가장 중앙에 있는 값 반환)
arr = np.array([[1, 2, 3], 
                [0, 1, 4],
                [1, 5, 2])
                
print(np.median(arr)) # 1.5
print(arr.median()) #
print(arr.median(axis=0)) # [1, 2, 3]
print(arr.median(axis=1)) # [2, 1, 2]

```

## 3-4) 배열의 연산4
> 비교 연산, 삼각함수 
```
(1) 비교연산
arr1 = np.array([[1, 2, 3]
                 [4, 5, 6]])
arr2 = np.array([[1, 0, 3]
                 [4, -2, 9]])
                 
print(arr1 == arr2)
#[[True False True]
  [True False False]]

print(arr1 > arr2)
#[[False True False]
  [True False True]]
  
print(np.array_equal(arr1, arr2))#arr1의 원소들과 arr2의 원소들이 같은지 비교 
# False

(2) 삼각함수
arr = np.array([[1, 2, 3]
                 [4, 5, 6]])
#sin() : sin값 출력 
print(np.sin(arr))

#cos() : cos값 출력 
print(np.cos(arr))

#tan() : tan값 출력 
print(np.tan(arr))

#pi : 파이 값 출력
print(np.pi) #3.141592...

```


## 3-5) 브로드캐스팅(Broadcasting)
> 배열들의 shape이 다를 때 사용하는 방법 
> 서로다른 행렬은 상대의 shape에 맞춰 확장을 하게 됨 
```
예시1)
arr1 = np.array([[0, 0, 0],
                 [1, 1, 1],
                 [2, 2, 2]])
arr2 = np.array([[5, 6, 7]])
print(arr1 + arr2)
#[[5 6 7]
  [6 7 8]
  [7 8 9]]


예시2) 
arr1 = np.arraY([[1, 1, 1]])
arr2 = np. array([[0],
                  [1],
                  [2]])
print(arr1 + arr2)
#[[1 1 1]
  [2 2 2]
  [3 3 3]]

+) 강의 중 그림 첨부 
```

# 4장. N차원 배열 정렬
## 4-1. 1차원 배열의 정렬
> 정렬 : 오름차순이나 내림차순으로 원소를 나열하는 과정
```
* 1차원 배열 생성 
arr = np.random.randint(10, size = 10)
print(arr)
#[5 0 4 9 1 3 7 6 0 8]

(1) 오름차순 
- 기본적으로는 오름차순 정렬 
pritnt(np.sort(arr))

(2) 내림차순
print(np.sort(arr)[::-1])
--> 단 원본 배열에는 값의 정렬이 유지되지 않음

(3) 정렬된 값을 유지하는 방법
arr = np.sort(arr)
print(arr)

arr.sort() -->재정의된 sort함수 이용 
print(arr)

```

## 4-2. 2차원 배열의 정렬
```
* 2차원 배열 생성
arr = np.random.randint(15, size =(3, 4)
print(arr)
#
[[ 9  3  0 10]
 [ 2  0  1  1]
 [ 8  9 11  9]]
 
 (1) 오름차순
 print(np.sort(arr))
 #
[[ 0  3  9 10]
 [ 0  1  1  2]
 [ 8  9  9 11]]
 
(1-1) 열 기준 오름차순 
print(np.sort(arr, axis=0))
#
[[ 2  0  0  1]
 [ 8  3  1  9]
 [ 9  9 11 10]]
 
(1-2) 행기준 오름차순
 print(np.sort(arr, axis=1))
 #
 [[ 0  3  9 10]
 [ 0  1  1  2]
 [ 8  9  9 11]]
 
(1-3) 2차원 배열을 1차원배열로 정렬하여 오름차순
  print(np.sort(arr, axis=None))
  # [ 0  0  1  1  2  3  8  9  9  9 10 11]
  
(1-4) arsort() : 정렬된 원소의 원래 배열에서의 인덱스(자리 값를 반환
print(np.sort(arr, axis=1))
print(np.argsort(arr, axix=1))
# [[ 0  3  9 10]
 [ 0  1  1  2]
 [ 8  9  9 11]]
[[2 1 0 3]
 [1 2 3 0]
 [0 1 3 2]]

```

# 5장. N차원 배열의 형태 변경
# 5-1. 배열의 형태 변경1
> reshape()
```
(1) 배열의 차원 변경 
- 원래는 1차원
arr = np.arange(12)
print(arr, arr.ndim)
#

- 1차원 -> 2차원 
arr = arr.reshape(3, 4) # 사이즈 같게 설정해야함
print(arr, arr.ndim)
#
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]] 2

arr = arr.reshpae(3, -1) # shape값에 -1을 입력하면 자동으로 4로 입력됨
                         # 자동으로 size를 맞출 수 있도록 설정 
                         # 단, shape의 두 원소 모두 -1로 설정은 불가
print(arr)
#
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]] 2




- 1차원 -> 3차원
arr = arr.reshape((2, 3, 2))
print(arr, arr.ndim)
#
 [[ 6  7]
  [ 8  9]
  [10 11]]] 3

- 4차원도 마찬가지

```

# 5-2. 배열의 형태 변경2
> resize(), ravel()
```
(1) resize()
- resize함수는 reshape함수와 동일하지만 원본 데이터를 변경시킨다는 차이점이 있음
- resize함수에서 변경할 shape을 지정해줘야 함 

arr = np.arange(12)
print(arr)
# [ 0  1  2  3  4  5  6  7  8  9 10 11]

arr.resize(3, 4)
print(arr)
# [[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
 
(2) ravle()
- 1차원 배열로 변경
arr = arr.ravel()
print(arr)
# [ 0  1  2  3  4  5  6  7  8  9 10 11]

```

# 5-3. 배열의 형태 변경3
> expand_dims(), squeeze()
```
arr = np.array([1,2])
print(arr, arr.shape)
# [1 2] (2,)

(1) expand_dims()
- 입력한 exis값을 기준으로 차원을 추가하는 함수
arr = np.expand_dims(arr, axis =0)
pritnt(arr, arr.shape)
# [[1 2]] (1, 2) --> row값을 기준으로 차원 추가 

arr = np.expand_dims(arr, axis =1)
pritnt(arr, arr.shape) 
# [[1]
 [2]] (2, 1)  --> columm값을 기준으로 차원 추가 

(2) squeeze()
- 배열의 축을 제거하여 한차원씩 차원을 축소하는 함수
arr = np.array([[1,2]])
print(arr, arr.shape, arr.ndim)
# [[1 2]] (1, 2) 2

arr = np.squeeze(arr, axis=0)
print(arr, arr.shape, arr.ndim)
# [1 2] (2,) 1

- 3차원 제거 
예시1)
arr = np.array([[[1],
                 [2],
                 [3]]])
print(arr, arr.shape, arr.ndim)
#[[[1]
  [2]
  [3]]] (1, 3, 1) 3

arr =np.squeeze(arr, axis=0) #--> x축 제거 
print(arr, arr.shape, arr.ndim)
#[[1]
 [2]
 [3]] (3, 1) 2

예시2)
arr = np.array([[[1, 2, 3]]])
print(arr, arr.shape, arr.ndim)
# [[[1 2 3]]] (1, 1, 3) 3

arr =np.squeeze(arr, axis=1) #--> y축 제거 
print(arr, arr.shape, arr.ndim)
# [[1 2 3]] (1, 3) 2

```

# 5-4. 전치행렬(Transpose Matrix)
```



```

# 6장. N차원 배열의 병합 
# 6-1. 배열에 원소 추가 및 삭제 
```



```
# 6-2. 배열 간의 병합  
```



```
# 6-3. 배열 분할
```



```
