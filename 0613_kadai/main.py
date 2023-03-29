#1
i = 0
while i < 3:
    print("Hello")
    i += 1

#2
i = 0
while i < 3:
    print(f"NO.{i + 1}")
    i += 1

#3
for i in range(1, 4):
    print(f"NO.{i}")

#4
total = 0
for i in range(1, 11):
    total += i
    i += 1

print(total)

#5
total = 0
n = int(input("総和の上限を入力"))
for i in range(1, n + 1):
    total += i
    i += 1

print(total)


#6
total = 1
i = 10
while 1 <= i:
    total *= i
    i -= 1

print(total)

#7
for i in range(0, 11, 2):
    print(i)

#8
i = 0
kekka = 0
while i <= 10:
    if i % 2 == 0:
        kekka = "□"
    else:
        kekka = "■"
    print(kekka,end = "")
    i += 1

print("")

#9
i = 0
kekka = ""
while i <= 10:
    if i % 2 == 0:
        kekka = "□"
    else:
        kekka = "■"
    
    if i == 5:
        print(kekka)
    else:
        print(kekka,end = "")
    i += 1

print() #改行

i = 0
kekka = ""
while i <= 10:
    if i % 2 == 0:  
        print("白",end="")
    elif i == 5:
        print("黒")
    else:    
        print("黒",end="")
    i += 1


print("")

#10
import random #ランダム関数を使う宣言

r = 0
while r != 77:
    r = random.randint(0, 100)
    print(r)

#11
r = 0
i = 0
while r != 77:
    r = random.randint(0, 100)
    print(r)
    i += 1
print(f"{i}回目")

#12
pw = "PY11"
an = 0
while pw != an:
    an = input("Password")
print("開錠")


#模範解答
while input("Password") != "PY11":
    pass


#13
import random 
r = random.randint(0, 20)
i = 0

while r != i:
    i = int(input("数値を当てて！"))
    if i < r:
        print("もっと大きい")
    elif r < i:
        print("もっと小さい")
    else:
        break
print("正解です")

#14
r = random.randint(0, 20)
i = 0
n = 1
while r != i:
    i = int(input("数値を当てて！"))
    if i < r:
        print("もっと大きい")
        n += 1
    elif r < i:
        print("もっと小さい")
        n += 1
    else:
        break
print(f"正解です\n{n}回目")



    



    

