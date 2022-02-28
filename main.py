from math import fabs
a = float(input('Izrakstīt 1 skaitļu: '))
b = float(input('Izrakstīt 2 skaitļu: '))
c = float(input('Izrakstīt 3 skaitļu: '))
d = float(input('Izrakstīt 4 skaitļu: '))
f = float(input('Izrakstīt 5 skaitļu: '))
def para():
    a1 = a % 2
    b1 = b % 2
    c1 = c % 2
    d1 = d % 2
    f1 = f % 2
    p = 0
    n = 0
    if a1 == 0:
        p += 1
    else:
        n += 1
        
    if b1 == 0:
        p += 1
    else:
        n += 1
        
    if c1 == 0:
        p += 1
    else:
        n += 1
        
    if d1 == 0:
        p += 1
    else:
        n += 1
        
    if f1 == 0:
        p += 1
    else:
        n += 1
    
    if p > n:
        print('Pāra vairak')
    else:
        print("Nepāra vairak")  
para()

def pozitiv():
    poz = 0
    ne = 0
    if a >= 0:
        poz += 1
    else:
        ne += 1
        
    if b >= 0:
        poz += 1
    else:
        ne += 1
        
    if c >= 0:
        poz += 1
    else:
        ne += 1
        
    if d >= 0:
        poz += 1
    else:
        ne += 1
        
    if f >= 0:
        poz += 1
    else:
        ne += 1
    if poz > ne:
        print('Pozītivo vairāk')
    else:
        print("Negatīvo vairāk")
pozitiv()


def divcip():
    q = 0
    t = 0
    if 100 <= fabs(a) < 1000:
        t += 1
    if 10 <= fabs(a) < 100:
        q += 1
    if 100 <= fabs(b) < 1000:
        t += 1
    if 10 <= fabs(b) < 100:
        q += 1
    if 10 <= fabs(c) < 100:
        q += 1
    if 100 <= fabs(c) < 1000:
        t += 1
    if 10 <= fabs(d) < 100:
        q += 1
    if 100 <= fabs(d) < 1000:
        t += 1
    if 10 <= fabs(f) < 100:
        q += 1
    if 100 <= fabs(f) < 1000:
        t += 1
    if q > t:
        print("Divciparu vairak")
    elif q == t:
        print("Vienādi")
    elif t > q:
        print("Trisciparu vairāk")
divcip()