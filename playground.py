
# 언패킹으로 받으면 저걸로 받네
a, *b = [1, 2]
print(a, b)

#
# for i in range(5):
#     for j in range(4):
#         print(j)
#         pass
#         break
#     else:
#         break
#     print(i)
# else:
#     print('1111')

i = 0

while i < 5:
    j = 0
    while j < 4:
        break
        print(j)
        j += 1
    else:
        break
    i += 1
    print(i)
else:
    print('나왔음')