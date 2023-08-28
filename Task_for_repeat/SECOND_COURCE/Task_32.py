from random import *
import string

cap_letter = string.ascii_lowercase
low_letter = string.ascii_uppercase

n = int(input())
password = []
for i in range(n//2):
    password.append(choice(cap_letter))
    password.append((choice(low_letter)))

print(*password, sep='')

from random import *

n = int(input())
password = []
for i in range(n//2):
    password.append(chr(randint(65, 90)))
    password.append(chr(randint(97, 122)))

print(*password, sep='')