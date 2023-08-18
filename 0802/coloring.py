import sys

file = open('coloring.txt', 'r')
sys.stdin = file

test_case = int(input())



for num in range(test_case):
    palette = [[0] * 10 for _ in range(10)]
    color_case = int(input())
    for _ in range(color_case):
        sx, sy, lx, ly, color = map(int, input().split())
        for i in range(sx, lx + 1):
            for j in range(sy, ly + 1):
                if palette[i][j] != color and palette[i][j] != 3:
                    palette[i][j] += color

    return_value = 0
    for i in range(10):
        for j in range(10):
            if palette[i][j] == 3:
                return_value += 1


    print(f'#{num + 1} {return_value}')