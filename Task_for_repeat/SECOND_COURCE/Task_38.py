from random import *
tiket = []
while len(tiket) < 7:
    num = randint(1, 49)
    if num not in tiket:
        tiket.append(num)
print(*sorted(tiket))
