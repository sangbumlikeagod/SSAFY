
# 1 ~ 10  집합을 만들어 주는 과정
# 요소가 가리키는 값이 부모인걸로
parent = [i for i in range(10)]

def find_set(x):
    if parent[x] == x:
        return x
    
    parent[x] = find_set(parent[x])
    return parent[x]


def union(x, y):
    # 1.같은 집합인가
    x = find_set(x)
    y = find_set(y)
    if x == y:
        # 대표자가 같은 경우를 합치려 할 가능성이 있기 때문에 참아야하는 코드.
        return
    
    #.2. 다른집합이라면 부모를 수정해줘야한다.
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
    
    # 트리 구조라면 같은 구조를 
# 이걸 트리구조로 만든다고.

union(0, 1)
union(1, 3)
print(parent)
t_x = 0
t_y = 2

if find_set(t_x) == find_set(t_y):
    print(f"{t_x} 와 {t_y} 는 같은 집합에 속해 있다")
else:
    print(f"{t_x} 와 {t_y} 는 다른 집합에 속해 있다")