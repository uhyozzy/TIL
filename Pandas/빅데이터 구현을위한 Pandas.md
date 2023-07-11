import pandas as pd
import numpy as np

# 1. Series
```
```
# 2. DataFrame
## 1. 데이터프레임 생성
```
train_data=pd.read_csv("C:/Users/YHJ/Desktop/data/train.csv",
                      index_col='PassengerId',
                      usecols=['PassengerId','Survived','Name','Sex','Age'])
train_data.head()

data = {
    "2015": [9904312, 3448737, 2890451, 2466052],
    "2010": [9631482, 3393191, 2632035, 2000002],
    "2005": [9762546, 3512547, 2517680, 2456016],
    "2000": [9853972, 3655437, 2466338, 2473990],
    "지역": ["수도권", "경상권", "수도권", "경상권"],
    "2010-2015 증가율":[0.0283, 0.0163, 0.0982,0.0141]
}
df3=pd.DataFrame(data)
df3

print(df3.columns)
type(df3.columns)


index=['서울','부산','인천','대구']
df3=pd.DataFrame(data,index=index)
df3.index.name='도시'
df3.columns.name='특성'
df3

train_data.head()

train_data.size

train_data.shape


train_data.info()

train_data.describe()

df3

df3['2010-2015 증가율']*100

df3['2010-2015 증가율']=df3['2010-2015 증가율']*100

df3['2010-2015 증가율']

df3['비고']=['특별시','광역시','특례시','특례시']
df3

del df3['비고']
df3


df3['2005-2015 증가율']=((df3['2015']-df3['2005'])/df3['2005']*100).round(2)
df3


del df3['2005-2015 증가율']
df3

df3.loc['광주']=['호남권',2470000,2456000,2453000,2460000,1.00]
df3

df3.지역

df3[['지역']]

df3[['2010','2015']]

df5=pd.DataFrame(np.arange(12).reshape(3,4))
df5

np.arange(12).reshape(3,4)
```
## 2. 행단위 인덱싱
```
```

## 3. loc, lioc

```python
설정변경코드
- from IPython.core.interactiveshell import InteractiveShell
    InteractiveShell.ast_node_interactivity="all"
- InteractiveShell.ast_node_interactivity:'all'|'last'|'last_expr'|'none'(기본값은 'last_expr')

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity="all"
```

### 데이터 프레임 인덱서 : loc, iloc
- Pandas는 numpy행렬과 같이 쉼표를 사용한(행 인덱스, 열 인덱스)형식의 2차원 인덱싱 지원
- loc : 라벨값 기반의 2차원 인덱싱
- iloc : 순서를 나타내는 정수 기반의 2차원 인덱싱

```python
import pandas as pd
import numpy as np

# 예제DF 생성
# 10-21 범위의 숫자를 value로 갖는 3행 4열의 df

df = pd.DataFrame(np.arange(10,22).reshape(3,4),
                 index=['a','b','c'],
                 columns=["A","B","C","D"])
df

# loc인덱서 사용 

df.loc['a'] #a행의 모든 열 추출 (시리즈로 반환)

df.loc['b':'c'] #여러행 추출
df['b':'c']

df.loc["b"] #시리즈 반환 
df.loc[["b"]] #df 반환

### boolean으로 row 선택하기

df.A>15

df.loc[df.A>15]

# 불리언 시리즈를 반환하는 함수
def sel_row(df):
    return df.A>15

sel_row(df)
df.loc[sel_row(df)]

### loc인덱서 슬라이싱 

df2=pd.DataFrame(np.arange(10,26).reshape(4,4),
                columns=['a','b','c','d'])
df2

df2.loc[1:2] #[초기인덱스값:마지막인덱스값]
df2[1:2] #위치인덱싱 

### loc인덱서 사용 요소 값 접근

df2
df2.loc[0,'a'] #0행, a열에 있는 값 반환

df
df.loc[['a','b']]['A'] #시리즈
df.loc[['a','b'],'A'] #시리즈
df.loc[['a','b'],['A']] #df

### loc를 이용한 indexing정리 

# a행의 모든 열 추출방법

df.loc['a'] #a행 모든 열 추출, 시리즈 반환
df.loc[['a']] #a행 모든 열 추출, df 반환
df.loc['a',:] #a행 모든 열 추출, 시리즈 반환
df.loc[['a'],:] #a행 모든 열 추출, df 반환

# a행의 B,C열 추출 
df.loc['a','B':'C'] #시리즈반환
df.loc[['a']] #df 반환
df.loc[['a'],'B':'C'] #df 반환
df.loc['a',['B','C']] #시리즈 반환

# B행부터 모든행의 A열추출
df.loc['b':'A'] 
df.loc['b':]['A']
df.loc['b':][['A']]
df.loc['b':,['A']]
df.loc['b':,'A':'A']       

# a,b행의 B,D열을 데이터프레임으로 반환
df.loc['a':'b']
df.loc[['a','b']]
df.loc[['a','b']][['B','D']]

df.loc[['a','b'],['B','D']]

## iloc인덱서
- 라벨(name)이 아닌 위치를 나타내는 정수 인덱스만 받음
- 데이터프레임.iloc[행,열]

df
df.iloc[0,1]

# 행과 열 모두 슬라이싱
df.iloc[0:2,1:2]
df.iloc[0:2,1] #시리즈 반환

# 값을 df형태로 추출
df.iloc[2:3,1:2]

# 0행 데이터에서 끝에서 두번째 열부터 끝까지 반환
df
df.iloc[0:1,-2:] #df
df.iloc[0,-2:] #시리즈

df.iloc[[0,1],[1,2]]
```
