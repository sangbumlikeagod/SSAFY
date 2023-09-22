C = 10
def findmax(lst):
    maxxt = 0
    for i in range((1 << len(lst)) - 1):
        local = 0
        local2 = 0
        for j in range(len(lst)):
 
            if i & 1 << j:
                local += lst[j]
                local2 += lst[j] ** 2

        if local < C:
            maxxt = max(maxxt, local2)

    return maxxt

print(findmax([5, 5, 7]))