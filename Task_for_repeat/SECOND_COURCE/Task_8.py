dic_dnk = {'G':'C',
           'C':'G',
           'T':'A',
           'A':'U'}
dnk = list(input())
for elem in dnk:
    print(dic_dnk[elem], end='')