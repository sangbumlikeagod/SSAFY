def ce(n):
    p = []
    for i in range(3, -1, -1):
        p.append(((n >> (24 - i * 8)) & 0xff)) #
    return p


x = 0x01020304

p = []
print(ce(x))



def ce1(n):
    # print(n)
    # print((n << 24 & 0xff000000) , (n << 8 & 0xff0000))
    # print((n << 24 & 0xff000000) | (n << 8 * 0xff0000) | (n >> 8 & 0xff00) | (n >> 24 & 0xff))
    return (n << 24 & 0xff000000) | (n << 8 & 0xff0000) | (n >> 8 & 0xff00) | (n >> 24 & 0xff)
# 뒤에 두 자리


print(hex(ce1(x)))