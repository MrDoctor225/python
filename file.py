a = 0
b = 1
i = 0
count = 2
d = 2
while i < 49:
    a += b
    b += a

    while a % d != 0 and d < a-1:
        d += 1
    if a % d == 0:
        count += 1
    if count == 2:
        print(' ' + str(a))
    count = 2
    d = 2
    while b % d != 0 and d < b-1:
        d += 1
    if b % d == 0:
        count += 1
    if count == 2:
        print(' ' + str(b))
    count = 2
    d = 2
    # print(' ' + str(a))
    # print(' ' + str(b))
    i += 1