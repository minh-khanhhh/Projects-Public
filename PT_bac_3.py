#Nhap a, b, c, d
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
d = float(input("Nhập d: "))
#Giai PT
from math import cos, acos, pi, sqrt

if a == 0:
    if b == 0: #PT bac 1
        if c == 0:
            if d == 0:
                print("Phương trình vô số nghiệm")
            else:
                print("Phương trình vô nghiệm")
        else:
            print("Phương trình có nghiệm x:", -d/c)
    else:
        delta = c**2 - 4*b*d
        if delta < 0:
            print("Phương trình vô nghiệm")
        else:
            if delta > 0:
                print("Phương trình có nghiệm: x1 :", (-c+sqrt(delta))/(2*b))
                print("Phương trình có nghiệm: x2 :", (-c-sqrt(delta))/(2*b))
            else:
                print("Phương trình có nghiệm x :", -c/(2*b))
else:
    delta = b**2-3*a*c
    k = (9*a*b*c - 2*b**3 - 27*a**2*d) / (2*sqrt(abs(delta)**3))    
    if delta > 0:
        if abs(k) <= 1:
            print("Phương trình có nghiệm x1: ", (2*sqrt(delta)*cos(acos(k)/3)-b)/(3*a))
            print("Phương trình có nghiệm x2: ", (2*sqrt(delta)*cos(acos(k)/3-2*pi/3)-b)/(3*a))
            print("Phương trình có nghiệm x3: ", (2*sqrt(delta)*cos(acos(k)/3+2*pi/3)-b)/(3*a))
        if abs(k) > 1:
            print("Phương trình có nghiệm x:", (sqrt(delta)*abs(k))/(3*a*k) * (((abs(k)+(k**2-1)**1/2)**1/3)+((abs(k)-(k**2-1)**1/2)**1/3))-b/(3*a))
    if delta == 0:
        print("Phương trình có nghiệm bội x:", (-b+(b**3-27*a**2*d)**1/3)/(3*a))
    if delta < 0:
        print("Phương trình có nghiệm duy nhất x:", (sqrt(abs(delta))/(3*a))*((k+sqrt(k**2+1))**1/3+(k-sqrt(k**2+1))**1/3)-b/(3*a))