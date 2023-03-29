import datetime

#1
print("ex1")

def print_python():
    print("Python")

print_python()

print()

#2
print("ex2")

def print_upper(a):
    print(a.upper())

print_upper("abc")

print()


#3
print("ex3")

def print_number(b):
    for i in range(1, b + 1):
        print(i, end=" ")

print_number(5)

print()

#4
print("ex4")

def print_sum_average(c):
    i = 1
    l = []
    while i <= c:
        l.append(i)
        i += 1
    mean = sum(l) / len(l)
    print(mean)

print_sum_average(5)

print()



#5
print("ex5")

def print_square(d):
    i = 0
    while i <= d - 1:
        j = 0
        while j <= d - 1:
            print("*", end="")
            j += 1
        print()
        i += 1

print_square(3)

print()


#6
print("ex6")

def calc(one, two, three):
    if three == 0:
        kekka = one + two
    elif three == 1:
        kekka = one - two
    elif three == 2:
        kekka = one * two
    elif three == 3:
        if three == 0:
            return
        kekka = int(one / two)
    else:
        return
    print(kekka)

calc(6, 3, 3)

print()

#7
print("ex7")

def hello(a, b = "en"):
    kekka = "hello"
    if b == "jp":
        kekka = "こんにちは"
    print(kekka , a)

hello("aiba", "jp")
hello("aiba") 

print()


#8
print("ex8")

def star():
    return"☆"

print(star())

print()

#9
print("ex9")

def stars():
    return"☆☆☆☆☆"

print(stars())

print()


# #10
print("ex10")

import random

def random_stars():
    kekka = ""
    for a in range(random.randint(1, 5)):
        kekka += ("☆")
    return kekka
    
print(random_stars())

print()



#11
print("ex11")

def print_birth(a):
    year = datetime.datetime.now().year
    kekka = year - a
    if 120 < a or a < 0:
        kekka = "エラー：年齢は０～１２０の範囲です。"
    return kekka

print(print_birth(a = int(input("年齢"))))

print()


#12
print("ex12")

def print_args(*args):
    for arg in args:
        print(arg)

print_args(1,2,3)

print()

#13
print("ex13")

def my_sum(*args):
    return sum(args)

print(my_sum(1,2,3))


print()

#14
print("ex14")

def in_seven(*args):
    return 7 in args

print(in_seven(1,2,3))
print(in_seven(1,7,3))

print()


#15
print("ex15")

def exclamation(*args):
    a = list(args)
    a.append("!")
    return a

print(exclamation("a","b","c"))

print()


#16
print("ex16")

def print_dict(**kwargs): 
    for key, value in kwargs.items():
        print(f"{key}:{value}")

        

print_dict(id=20000, name="smizu", address="神奈川")

print()

#17
print("ex17")

def three_seven():
    i = 1
    while random.randint(0,1000) != 777:
        i += 1
    return i


print(three_seven())

print()


#18
print("ex18")

def mode(*args):
    l1 = []
    d1 = {}
    keys=[]
    if len(args) == 0:
        return
    else: 
        for arg in args:
            l1.append(args.count(arg))
        d1 = dict(zip(args,l1))
        a = max(d1.values())
        for b in d1:
            if d1[b] == a:
                keys.append(b)
        
        return keys
 
print(mode("a","b","c","a","b"))

# 要素値の中で一番大きいもののキーを取り出す



eval("a = 1 + 2")
#↑文字列をコードとして認識することができる




    

    



    



    







