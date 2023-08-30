import sys

name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file

test_case = int(input())
for case in range(test_case):
    bina = input()
    tri = input()
    ans = {}
    bina_int = 0
    for i, j in enumerate(bina[::-1]):
        bina_int += int(j) * 2 ** i

    for i in range(len(bina)):
        if 1 << i & bina_int:
            ans[bina_int - (1 << i)] = True
        else:
            ans[bina_int + (1 << i)] = True
    tri_int = 0
    for i, j in enumerate(tri[::-1]):
        tri_int += int(j) * 3 ** i
    is_brake = False
    for i in range(len(tri)):
        this_digit = (tri_int % (3 ** (i + 1)) - tri_int % (3 ** i)) // (3 ** i)
        for j in [0, 1, 2]:
            if j == this_digit:
                pass
            if tri_int - (this_digit * 3 ** i) + (j * 3 ** i) in ans:
                is_brake = True
                return_value = tri_int - (this_digit * 3 ** i) + (j * 3 ** i)
                break
        if is_brake:
            break
    print(f'#{case + 1} {return_value}')




