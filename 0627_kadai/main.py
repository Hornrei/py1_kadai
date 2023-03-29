#1

i = 1
while i <= 9:
    j = 1
    while j <= 9:
        kekka = f"{i}*{j} = {i * j}"
        print(f"{kekka:>10}", end="")
        j += 1
    print()

    i += 1

#2
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print(j, end="")
        j += 1
    print()
    i += 1

#3
i = 1
while i <= 5:
    j = 1
    while 6 - j >= i:
        print(j, end="")
        j += 1
    print()
    i += 1

#4
i = 1
while i <= 4:
    j = 1
    while 5 - j >= i:
        print("*", end="")
        j += 1
    print()
    i += 1

#5
i = 1
while i <= 4:
    j = 1
    while j <= 4:
        print("*", end="")
        j += 1
    print()
    i += 1

print()

#6
i = 0
while i <= 3:
    j = 0
    while j < i:
        print("　", end="")
        j += 1
    k = 0
    while k <= 3:
        print("*", end="")
        k += 1
    print()
    i += 1 


#7
i = 0
while i <= 3:
    j = 0
    while j <= 2 - i:
        print("　", end="")
        j += 1
    k = 0
    while k <= 3:
        print("*", end="")
        k += 1
    print()
    i += 1

print()

#8
i = 0
while i < 3:
    j = 0
    while j <= i :
        print("*", end="")
        j += 1
    print()
    i += 1

i = 1
while i <= 2:
    j = 1
    while i <= 3 - j :
        print("*", end="")
        j += 1
    print()
    i += 1

print()



#9


i = 0
while i <= 2:
    j = 0
    while j <= 1 - i:
        print(" ", end="")
        j += 1
    k = 0
    while k <= i * 2:       
        print("*", end="")
        k += 1
    l = 0
    while l <= 1 - i:
        print(" ", end="")
        l += 1
    
    print()
    i += 1





i = 0
while i < 2:
    j = 0
    while j <= i:
        print(" ", end="")
        j += 1
    k = 0
    while k <= 2 - 2 * i:
        print("*", end="")
        k += 1
    l = 0
    while l <= i:
        print(" ", end="")
        l += 1

    print()
    i += 1

print()


#10
i = 1
while i <= 2:
    j = 0
    while j <= 2 - i:
        print(" ", end="")
        j += 1
    
    k = 0
    while k <= i * 2:
        print("*", end="")
        k += 1

    l = 0
    while l <= 2 - i:
        print(" ", end="")
        l += 1
    print()
    i += 1


i = 1
while i <= 3:
    j = 1
    while j <= 7:
        print("*", end="")
        j += 1
    print()
    i += 1


i = 1
while i <= 2:
    j = 0
    while j <= i - 1:
        print(" ", end="")
        j += 1
    
    k = 0
    while k <= 6 - i * 2:
        print("*", end="")
        k += 1

    l = 0
    while l <= i - 1:
        print(" ", end="")
        l += 1
    
    print()
    i += 1



#11
i = 1
while i <= 9:
    j = 1
    while j <= 9:
        kekka = f"{i} * {j} = {i * j}"
        print(f"{kekka:<10}", end="")
        j += 1
    print()

    i += 1


print()



#12
n = int(input("1辺の長さを入力"))
i = 0
while i <= n - 1:
    j = 0
    while j < n - 1 - i:
        print(" ", end="")
        j += 1
    
    k = 0
    while k <= n - 1 + 2 * i:
        print("*", end="")
        k += 1
    
    l = 0
    while l <= n - 1 - i:
        print(" ", end="")
        l += 1
    print()
    i += 1

i = 1
while i <= n - 2:
    j = 1
    while j <= n * 3 - 2:
        print("*", end="")
        j += 1
    print()
    i += 1


i = 0
while i <= n - 1:
    j = 0
    while j < i:
        print(" ", end="")
        j += 1

    k = 0
    while k <  n * 3 - 2 - 2 * i:
        if n == 1:
            break
        print("*", end="")
        k += 1

        

    l = 0
    while j < i:
        print("", end="")
        l += 1
    
    print()
    i += 1