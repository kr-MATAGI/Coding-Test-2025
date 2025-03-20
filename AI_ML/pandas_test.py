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

### 할인 금액 추가
df["할인금액"] = 3000

#### 정렬 ####

# 열을 기준으로
print(df.sort_values(by=["주문금액", "주문일자"], ascending=True))

# 인덱스 기준으로
print(df.sort_index(axis=1, ascending=False))


### 인덱스 설정
print(df.set_index("주문번호"))


### 중복값 확인
print(df.duplicated())

print(df.duplicated(subset="고객명"))

print(df.drop_duplicates(subset="고객명"))


### 산술 연산 ###
df_number = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [10, 20, 30],
    'C': [2.5, 4.5, 1.5]
})

print(df_number/2)
print(df_number.add(10))

df_another = pd.DataFrame({
    'B': [100, 200, 300],
    'C': [25, 45, 15],
    'D': [5, 10, 15] 
})

print(df_number.mul(df_another, fill_value=1))


### 통계 연산
math_score = {
    '이름': ['김철수', '박영희', '이민정', '최재원', '한지민'],
    '학년': ['3학년', '1학년', '1학년', '2학년', '3학년'],
    '점수': [88, 75, 68, 90, 83]
}

df_score = pd.DataFrame(math_score)

print(df_score)

print(df_score["점수"].max())

print(df_score[df_score["학년"] == "3학년"]["점수"].max())

# 괄호 꼭 해주기
print(df_score[(df_score["점수"] >= 75) & (df_score["학년"] == "1학년")])



### 문자열
data = {
    '이름': ['김 철수', '박 영희', '이 민정', '최 재원', '한 지민'],
    '직업': ['개발자', '요리사', '마케터', '작가', '의사']
}
df = pd.DataFrame(data)

print(df)

# 문자열 검색
df["이름_민"] = df["이름"].str.startswith("김")
df["직업_사"] = df["직업"].str.endswith("사")

# 문자열 분리 및 결합
df["성"] = df["이름"].str.split().str.get(0)
df["성2"] = df["이름"].str.split()
df["직업+이름"] = df["직업"].str.cat(df["이름"], sep=" ")

# 문자열 치환 (내부 공백 제거)
df["이름_공백제거"] = df["이름"].str.replace(" ", "")

# 문자열에서 특정 문자 선택
df["이름_마지막"] = df["이름"].str[3]

print(df)


### 데이터 변환
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': ['4', '5', '6'],
    'C': ['7.1', '8.2', '9.3']
})

# 'A' 열의 데이터타입을 문자열(str)로 변경
df['A'] = df['A'].astype(str)
df['B'] = df['B'].astype(int)
df['C'] = df['C'].astype(float)

print(df)
print(df.dtypes)