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

