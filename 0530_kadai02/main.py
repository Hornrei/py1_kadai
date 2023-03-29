#Step 1
score = int(input("得点を入力"))
print(score)

#Step 2
if 60 <= score:
    print("合格")


#Step 3
kekka = ""
if 60 <= score:
    kekka = "合格"
else:
    kekka = "不合格"
print(kekka)

#Step 4
message = ""
if 60 <= score:
    kekka = "合格"
    if 80 <= score:
        message = " Great!"
else:
    kekka = "不合格"
   
print(kekka + message)

#Step 5
message = ""
if 60 <= score:
    kekka = "合格"
    if 80 <= score:
        message = " Great!"
else:
    kekka = "不合格"
    if score <= 20:
        message = "　もう少し頑張りましょう"
print(kekka + message)

#Step 6
pw = int(input("パスワードを入力"))
if pw == "pass":
    k = "解除"
else:
    k = "パスワードエラー"
print(k)

#Step 7
import random
r = random.randint(0, 100)
print(f"乱数：{r}")

#Step 8
if r <= 10:
    s = "凶"
else:
    if r <= 40:
        s = "小吉"
    else:
        if r <= 70:
            s = "中吉"
        else:
            if r <= 90:
                s = "吉"
            else:
                s = "大吉"
print(s)

#Step 9
if r <= 10:
    s = "凶"
elif r <= 40:
    s = "小吉"
elif r <= 70:
    s = "中吉"
elif r <= 90:
    s = "吉"
else:
    s = "大吉"
print(s)

#Step 10
age = int(input("年齢を入力"))
if 6 <= age and age <= 22:
    mibun = "学生"
else:
    mibun = "学生でない"

#Step 11
number = int(input("数字"))
if number % 3 == 0 and number % 5 == 0:
    a = "3と5の倍数です"
elif number % 3 == 0:
    a = "3の倍数です"
elif number % 5 ==0:
    a = "5の倍数です"
else:
    a = "3の倍数でも、5の倍数でもありません。"

#Step 12
code = int(input("入力："))
if code == "y" or code == "p":
    b = "ロック解除！"
else:
    b = "解除ならず"

