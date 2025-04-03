import pandas as pd


'''
     데이터 구조
'''
s = pd.Series([1,2,3,4], ['a','b','c','d'])
print(s)

s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(s['c'])
print(s[['b', 'c']])

s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(s[s > 2])

# 딕셔너리 생성
data_dict = {
    '이름': ['소라', '창훈', '영미'],
    '나이': [25, 30, 35],
    '거주지': ['인천', '순천', '동해']
}

# 딕셔너리를 사용하여 데이터프레임 생성
df_dict = pd.DataFrame(data_dict)

print(df_dict)

'''
    Shape
'''
print('---------------------')
# 고객 데이터를 담은 딕셔너리 생성
data = {
    "이름": ["김철수", "이영희", "박민수"],
    "나이": [25, 32, 19],
    "도시": ["서울", "부산", "대구"]
}

# 딕셔너리를 사용해 데이터프레임 생성
df = pd.DataFrame(data)

# 데이터프레임 출력
print(df)

# 데이터프레임의 shape 속성을 사용하여 행과 열의 수 확인
print("데이터프레임의 차원:", df.shape)
print(df.columns)

# 데이터프레임의 수치 통계 정보 출력
print(df.describe())

print('---------------------')
# loc[]메서드로 첫번째 행 데이터 출력
row = df.loc[0]
print(row)

print('---------------------')
# 리스트로 여러 행(첫번째 행 '0'과 세번째 행 '2') 선택
selected_rows1 = df.loc[[0, 2]]
print(selected_rows1)

print('---------------------')
# 슬라이싱으로 연속된 여러 행(두번째 행 '1'부터 세번째 행 '2'까지) 선택
selected_rows2 = df.loc[1:2]
print(selected_rows2)

print('---------------------')
# df의 모든 행에 대한 "도시" 열 데이터 선택
selected_column = df.loc[:, '도시']
print(selected_column)

print('---------------------')
# 첫번째 행 선택
row = df.iloc[0]

# 두번째 열 선택
column = df.iloc[:, 1]

print(row)
print('------------------------')
print(column)

print('------------------------')
# 데이터프레임 df의 첫번째 행부터 두번째 행까지 선택
selected_rows = df[0:2]
print(selected_rows)

print('------------------------')
# '나이' 열의 값이 '20'보다 큰 행만 선택
filtered_rows1 = df[df['나이'] > 20 ]
print(df['나이'] > 20 )
print(filtered_rows1)

print('------------------------')
# '나이' 열이 20보다 크고 '도시'열의 값이 '서울'이 아닌 행
filtered_rows2 = df[(df['나이'] > 20 ) & (df['도시'] != '서울' )]
print(filtered_rows2)

