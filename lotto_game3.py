import random

game = int (input (" 게임수 :   "))
ThisWeekLotto = [0,0,0,0,0,0]             # camel style

for bp in range (0, game) :
          lotto = random.sample (range (1, 46), 6)
          lotto.sort()
          print (lotto)
print ()
for twice in range (0, 6) :           # 0, 1, 2, 3, 4, 5
          ThisWeekLotto[twice] = random.randint (1, 45)

ThisWeekLotto.sort()
print (ThisWeekLotto)
