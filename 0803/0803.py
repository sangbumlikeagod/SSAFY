arr = [1, 2, 3]
n = len(arr)
for i in range(1 << n):
    # print(type(i))
    for j in range(n):
        if i & (1 << j):
            # print(j, end=' ')
            pass
    # print()

# print(2 & (1 << 3))
#
# print(1 << 77 + 1 << 2)

lst = [1, 2, 3]
count = len(lst)
for i in range(1, 1 << count):
    ans = 0
    for j in range(count):
        if i & (1 << j):
            # print(lst[j])
            ans += lst[j]
    print(ans)