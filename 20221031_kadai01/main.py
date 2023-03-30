import sys



print("Ver2 その１------------------------------------")

han = True
while True:   #繰り返しずっと電卓にするため
  try:
    if han:
      dividend = int(input("非除数："))
      han = False
    divisor = int(input("除数："))
    ans = dividend / divisor
    han = False
    print(f"{dividend}/{divisor}={ans}")
    han = True

  except ZeroDivisionError:
    print("0で割ることはできません")
  except ValueError:
    print("整数を入力してください")
  except KeyboardInterrupt:
    sys.exit()





print("Ver2 その2------------------------------------")

while True:
  while True:   #繰り返しずっと電卓にするため
    try:
      dividend = int(input("ひ除数："))
      break
    except ValueError:
      print("整数を入力してください")
    except KeyboardInterrupt:
      sys.exit()

  while True:
    try:
      divisor = int(input("除数："))
      ans = dividend / divisor
      print(f"{dividend} / {divisor} = {ans}")
      break
    except ValueError:
      print("整数を入力してください")
    except ZeroDivisionError:
      print("0で割ることはできません")   
    except KeyboardInterrupt:
          sys.exit()


print("Ver2 その3------------------------------------")


while True:
  try:
    while True:   #繰り返しずっと電卓にするため
      try:
        dividend = int(input("ひ除数："))
        break
      except ValueError:
        print("整数を入力してください")

    while True:
      try:
        divisor = int(input("除数："))
        ans = dividend / divisor
        print(f"{dividend} / {divisor} = {ans}")
        break
      except ValueError:
        print("整数を入力してください")
      except ZeroDivisionError:
        print("0で割ることはできません")
     
  except KeyboardInterrupt:
   sys.exit()
    
    





  









