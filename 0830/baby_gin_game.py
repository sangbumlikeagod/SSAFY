import sys

name = __file__.split('\\')[-1][:-3]
file = open(f'{name}.txt', 'r')
sys.stdin = file


test_case = int(input())


class Player:
    def __init__(self):
        self.card = {}
    def isbabygin(self):
        def is_baby(num, dic):
            if num - 1 in dic and num + 1 in dic:
                return 1
            elif num - 1 in dic and num - 2 * 1 in dic:
                return 1
            elif num + 1 in dic and num + 2 * 1 in dic:
                return 1
            else:
                return 0
        def is_gin(num, dic):
            if dic[num] >= 3:
                return 1
            else:
                return 0
        def is_baby_gin(dic):
            if not dic:
                return 1
            for i in dic:
                if is_baby(i, dic) or is_gin(i, dic):
                    return 1
            return 0
        return is_baby_gin(self.card)
    def draw_card(self, num):
        self.card[num] = self.card.get(num, 0) + 1
        return self.isbabygin()


for num in range(test_case):
    card_set = list(map(int, input().strip().split()))
    player1 = Player()
    player2 = Player()
    return_value = 0
    for i in range(len(card_set)):
        if not i % 2:
            if player1.draw_card(card_set[i]):
                return_value = 1
                break
        else:
            if player2.draw_card(card_set[i]):
                return_value = 2
                break
    print(f'#{num + 1} {return_value}')
