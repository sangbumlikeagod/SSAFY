s1 = 'abc'
s2 = 'abc'
s3 = 'def'

s5 = s1[:2] + 'c'

print(s1 is s5)
print(s1 == s5)

s1, s2 = 'ansdfdfasdddddddddddddddddddf', 'ansdfdfasdddddddddddddddddddf'

print(s1 is s2)
s5 = s1[:-1] + s1[-1]
print(s1 is s5)
s6 = s1[:]
print(id(s1), id(s2), id(s5), id(s6))
#
repr()