
i = 1
while i <= 1000:
    if i % 2 != 0:
        d = ((i ** 3) + 17)
        d = str(i)
        ch = [int(x) for x in d]
        sum_ch = sum(ch)
        d = int(d)
        if sum_ch % 7 == 0:
            print (d)
    i +=1


