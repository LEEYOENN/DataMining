##20210193 이연 과제-csv파일을 데이터프레임에 평균 1등과 과목1등(중복허용)을 뽑아서 파일작성 과제

import numpy as np
from pandas import Series, DataFrame
scores = []
name = []

with open('name.txt', 'r') as f:
    lines = f.readlines()
    for line in lines :
        name.append(line.strip().split(' ')[1])
with open('midterm.txt', 'r') as f:
    f.readline()
    lines = f.readlines()
    for line in lines :
        data = line.strip().split(',')
        scores.append(data)
for score in scores :
    for i in range(0,4) :
        score[i] = int(score[i])    
#print(scores)

column = ['Korean', 'Mathmatics', 'English', 'Art']
df = DataFrame(scores,name,column)
# print(df)

# # (1)단계 1등학생 출력
avgDf = df.mean(axis='columns')
#print(avgDf)
#print(avgDf.max())


print("평균 1등은 : %s" %avgDf.idxmax())
krMax = df['Korean'].max()
kr1 = df.index[df["Korean"] == krMax]
#print(kr1)

mathMax = df['Mathmatics'].max()
math1 = df.index[df["Mathmatics"] == mathMax]
#print(math1)

engMax = df['English'].max()
eng1 = df.index[df["English"] == engMax]
#print(eng1)

artMax = df['Art'].max()
art1 = df.index[df["Art"] == artMax]
#print(art1)


##(2)단계 파일 쓰기
idx = 0
with open('top.txt', 'w') as f:
    f.write("%s : "%column[0])
    for i in kr1:
        f.write("%s "%str(i))
    f.write('\n')
    f.write("%s : "%column[1])
    for i in math1:
        f.write("%s "%str(i))
    f.write('\n')
    f.write("%s : "%column[2])
    for i in eng1:
        f.write("%s "%str(i))
    f.write('\n')
    f.write("%s : "%column[3])
    for i in art1:
        f.write("%s "%str(i))
    f.write('\n')
        
    
