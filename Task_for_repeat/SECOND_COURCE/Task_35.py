m = int(input())
n = int(input())
mat = {input() for _ in range(m)}
inf = {input() for _ in range(n)}
result = (mat ^ inf) | (inf ^ mat)
if len(result) == 0:
    print("NO")
else:
    print(len(result))
