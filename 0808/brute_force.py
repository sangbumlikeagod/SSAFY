

#   t :

print('가수')
''' 문자열이 이동하는 경우 '''


def string_brute(target, pattern):
    # pattern 만 움직이는 경우
    size_t = len(target)
    size_p = len(pattern)
    idx_t = 0
    idx_p = 0
    for idx in range(size_t - size_p + 1):
        idx_p = 0
        while idx_p < size_p and target[idx + idx_p] == pattern[idx_p] :
            idx_p += 1

        else:
            if idx_p == size_p:
                return True
    else:
        return False

# 아니근데 두방식이 어떻게 다른거냐
# 틀린칸 까지는 갈 필요가 없다면


def string_brute2(target, pattern):
    size_t = len(target)
    size_p = len(pattern)
    t = p = 0
    while t < size_t and p < size_p:
        if target[t] != pattern[p]:
            t -= p
            p = -1
        t += 1
        p += 1
    else:
        if p == size_p:
            return True
        else:
            return False


print(string_brute('fdfsdgkasjfklab', 'ab'))
print(string_brute2('fdfsdgkasjfklab', 'ab'))