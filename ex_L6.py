a = 200
b = 33
c = 500
if a > b or a > c:  # and or not
  print("at leastone of the conditions is true")





x = 41
if x >10:
  print("Above ten, ")
  if x > 20:
      print("and also above twenty!" )
  else:
      print("but not above 20.")





day = int(input("please num 1-7: "))
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("today is a weekday")
    case 6 | 7:
        print("i love weekends")
    case _:
        print("please input num 1-7.")























fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
print("------------------------------------")
for i in range(0,3):
    print(fruits[i])
