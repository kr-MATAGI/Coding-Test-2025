import pandas as pd

# 온라인 쇼핑몰 주문 데이터 생성
data = {
    "주문번호": [1, 2, 3, 4, 5, 6, 7],
    "고객명": ["유재석", "조세호", "유재석", "권상우", "조세호", "권상우", "유재석"],
    "주문금액": [20000, 50000, 15000, 30000, 100000, 25000, 20000],
    "주문일자": ["2024-03-01", "2024-03-01", "2024-03-02", "2024-03-02", "2024-03-03", "2024-03-03", "2024-03-04"],
    "배송지역": ["서울", "부산", "서울", "대구", "부산", "대구", "서울"]
}
df = pd.DataFrame(data)

# 데이터프레임 출력
print(df)
print("-------------")

# 데이터프레임 df에 '배송료' 열을 추가하고 해당 열의 모든 행의 값으로 3000 입력
df['배송료'] = 3000
print(df.head(3))
print("-------------")

# 마지막 열 뒤에 ‘배송상태’ 열을 추가하고 ‘배송완료’ 값을 입력
df.insert(6, '배송상태', '배송완료')
print(df.head(2))
print("-------------")

# 새로운 주문 데이터 행을 추가
new_order = {"주문번호": 8, "고객명": "이무진", "주문금액": 45000, "주문일자": "2024-03-05"}
# 새로운 행 추가
df.loc[7] = new_order

print(df.tail(3))
print("-------------")

# 시리즈 객체 추가
new_series = pd.Series([9, '이상순', 40000, 3000], index=['주문번호', '고객명', '주문금액', '배송료'])
df = pd.concat([df, new_series.to_frame().T], ignore_index=True)

# 딕셔너리 추가
new_dict = {'주문번호': 10, '고객명': '이효리', '주문금액': 35000, '배송료': 3000, '배송상태': '배송중'}
df = pd.concat([df, pd.DataFrame([new_dict])], ignore_index=True)

# 새로운 주문 정보를 포함한 데이터프레임 생성
new_orders_df = pd.DataFrame({'주문번호': [11, 12],
                '고객명': ['김종국', '하하'],
                '주문금액': [25000, 15000],
                '배송료': [3000, 3000]})
df_updated = pd.concat([df, new_orders_df], ignore_index=True)

# 결과 출력
print(df_updated)
print("-------------")

# 결합할 시리즈 생성
concat_series = pd.Series(
  [1000, 2000, 1500, 3000, 5000, 2500, 2000, 1000, 4000],
  name='할인금액'
)

# 데이터프레임과 시리즈를 열 방향으로 결합
df = pd.concat([df, concat_series], axis=1, join='inner')
print(df)

#각 행의 결측치의 개수 확인
missing_values_count2 = df.isnull().sum(axis=1)
print(missing_values_count2)
