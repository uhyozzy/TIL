1. train_test_split()

■ sklearn.model_selection 의 train_test_split 함수
X_train, X_test , y_train , y_test = train_test_split(iris_data.data ,
                      iris_data.target , test_size =0.3, random_state =121)

(설명)
X_train : feature
Y_train : Label
test_size : 전체 데이터에서 테스트 데이터 세트 크기를 얼마로 샘플링 할 것인가를 결정
            (디폴트는 0.25, 25%)
train_size : 전체 데이터에서 학습용 데이터 세트 크기를 얼마로 샘플링 할 것인가를 결정
shuffle : 데이터를 분리하기 전에 데이터를 미리 섞을지 결정, 디폴트는 True, 데이터를 분산시켜서 더 효율적인 학습 및 테스트 데이터 세트를 만드는 데 사용
random_state : 호출할 때마다 동일한 학습/테스트용 데이터 세트를 생성하기 위해 주어지는 난수 값
