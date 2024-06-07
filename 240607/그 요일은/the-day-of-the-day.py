m1, d1, m2, d2 = tuple(map(int, input().split()))
target = str(input())

def daycalc(month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        max_month = 31
    elif month == 2:
        max_month = 29
    else:
        max_month = 30 
    return max_month

ctr = 1

# calculate starting date
if target == "Tue":
    d1 += 1
elif target == "Wed":
    d1 += 2
elif target == "Thu":
    d1 += 3
elif target == "Sat":
    d1 += 4
elif target == "Sun":
    d1 += 5  


while True:
    max_month = daycalc(m1)
    if m1 > m2:
        break
    
    if m1 == m2 and d1 + 7 > d2:
        break

    d1 += 7
    ctr += 1

    if d1 > max_month: 
        m1 += 1
        d1 = d1 - max_month

print(ctr)