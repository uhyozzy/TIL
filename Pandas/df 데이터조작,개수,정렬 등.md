> 설정변경 코드 : 변수 명이 두번 이상 출력되어도 모두 콘솔에서 보여줌
```python
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity="all"
```

> 모듈 import
```python
import numpy as np
import pandas as pd
import seaborn as sns #그래프 패키지
```

# pandas 데이터처리 및 변환관련 함수

## 1-1. 데이터 개수 세기
> - count()함수 이용
> - nan값은 세지 않음
> - df : seed이용(seed값이 같으면 동일한 난수 발생)

## 1-2. 시리즈에서 개수 세기
```python
s = pd.Series(range(10))
s[3]=np.nan
s

s.count() #nan 제외

np.random.seed(3)
df1=pd.DataFrame(np.random.randint(5,size=(4,4)))
df1.iloc[2,3]=np.nan
df1
```
```python
# 각열에 대한 원소 개수 변환
# 3열은 결측치 존재
df1.count()


titanic=pd.read_csv("C:/Users/YHJ/Desktop/data/test.csv")
del titanic['Unnamed: 0']
titanic.tail(2)

titanic.to_csv("C:/Users/YHJ/Desktop/data/test.csv") #저장 시키기

titanic.count()

### 카테고리값 세기 
- 시리즈.value_counts()메서드를 사용해 각각의 값이 나온 횟수를 셀 수 있음
- 파라미터 normalize=True를 사용하면 각 값 및 범주형 데이터의 비율을 계산 가능
    
    시리즈.value_counts(normalize=True)
- normalize : 정규화로 범위를 적절하게 조절하는 기능을 함 
   

np.random.seed(1) # 항상 같은 값이 나오게 설정
s2=pd.Series(np.random.randint(6,size=100))
s2.tail() #시리즈 뒷부분 5개 출력 
s2.head() #시리즈 앞부분 5개 출력 
s2.head(10)
len(s2)

s2.value_counts() #0,1,2,3,4,5의 데이터가 몇번 나왔는지
s2.value_counts(normalize=True)

### 범주형 데이터에 value_counts() 함수 적용
- 범주형 데이터 : 관측결과가 몇개의 범주 또는 항목의 형태로 나타나는 자료 ex.성별(남, 여), 선호도(좋다,보통,싫다) 등

titanic['alive'].dtype
titanic['alive'].value_counts()
titanic['alive'].value_counts(normalize=True)*100

# 타이타닉호에 승선한 승객의 남여비율 확인
titanic['sex'].value_counts(normalize=True)*100

### 데이터프레임에 value_counts() 함수 적용
- 행을 하나의 value로 설정하고 동일한 행이 몇번 나타났는지 반환

titanic[['sex','alive']].head(2)
titanic[['sex','alive']].value_counts()

pd.DataFrame(titanic[['sex','alive']].value_counts())
```

## 2. 정렬함수
> - 데이터 정렬 시 사용
> - sort_index(ascending=True/False) : 인덱스를 기준으로 정렬
> - sort_value(ascending=True/False) : 데이터 값을 기준으로 정렬
> - ascending 생략하면 오름차순 정렬 
```python
# 예제 시리즈로 s2사용
s2

s2.value_counts() #반환결과는 빈도값을 기준으로 내림차순 정렬 

s2.value_counts().sort_index() #인덱스 기준으로 정렬
s2.value_counts().sort_values() #빈도값 기준으로 정렬


### 데이터 프레임 정렬
- df.sort_values : 특정 열값 기준 정렬 
    * by인수 사용 : 생략굽ㄹ가
    * by=기준열, by=[기준열1,기준열2]

# 예제 df사용
df1

df1.sort_values(by=0)
df1.sort_values(by=0,ascending=False)
df1.sort_values(by=[0,2]) #우선순위 0열->2열

#예제 df
df = pd.DataFrame({'num_legs':[2,4,4,6],
                  'num_wings':[2,0,0,0]},
                 index=['falcon','dog','cat','ant'])
df

df.sort_index()
```

## 3. 행/열 합계
> - df.sum() 함수 사용
> - 행과 열의 합계를 구할 때는 sum(axis=0/1) , 0이 기본 
```python 
# 예제 df생성
np.random.seed(1)
df2=pd.DataFrame(np.random.randint(10,size=(4,8)))
df2

# 각 행의 합계 구하기 (시리즈 반환)
df2.sum(axis=1)

# 각 열의 합계 구하기 (시리즈 반환)
df2.sum(axis=0)

# 각행의 합계를 표시하는 합계 열 추가
df2['total']=df2[[0,1,2,3,4,5,6,7]].sum(axis=1)
df2

### df의 기본함수
- mean(axis=0/1)
- min(axis=0/1)
- max(axis=0/1)

#각 열의 평균
df2.mean(axis=0)
# 각 행의 최소값
df2.min(axis=1)
```
