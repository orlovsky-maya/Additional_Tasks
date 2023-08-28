m = int(input())
n = int(input())
mat = {input() for _ in range(m)}
inf = {input() for _ in range(n)}
print(len(mat.difference(inf)))