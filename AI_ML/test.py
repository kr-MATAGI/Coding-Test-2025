import pandas as pd

df = pd.DataFrame( {
    '이름': ['피카츄','라이츄','리자드','리자몽','꼬부기','어니부기'],
    '속성': ['전기', '전기', '불','불','물',None], 
    '색깔': ['노랑', '노랑', None,'빨강','파랑','파랑'],
    '순위': [ 5, 2, 6, 1, 4, 3] })

df.columns = ['이름', '속성','색깔','순위']

print(df)


print('--------------------')
print(df.iloc[0])
print()
print(df.iloc[[0]])
print()
print(df[0:1])

print('--------------------')
print(df.iloc[2:4])

print('--------------------')
print(df.iloc[2:5,1:3])


print('--------------------')
# df.loc['피카츄', '색깔']='노랑검정'
df['공격력'] = [15, 20, 9, 30, 16, 18 ]
print(df.isnull().sum())


print(df.groupby('순위').mean())