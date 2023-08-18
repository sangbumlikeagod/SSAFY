

'''
2차원 배열
'''
power = [[i for i in range(4)] for _ in range(4)]
print(power)

'''

행 위주 순회

'''

row, column = 4, 4

for i in range(row):
    for j in range(column):
        print(power[i][j], end=' ')

print()
'''
열 위주의 순회
'''

for i in range(column):
    for j in range(row):
        print(power[j][i], end=' ')

'''
지그재그 순회
'''
print()

for idx in range(row):
    for j in range(column):
        print(power[idx][j + (column - 2 * j - 1) * (idx % 2)], end=' ')


