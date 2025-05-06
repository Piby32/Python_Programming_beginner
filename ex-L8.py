def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(9))
''''''''''''''''''''''''''''''''''''''
cars = ["ford", "volvo", "bmw"]
print(cars[0])
print(cars[1])
print(cars[2])
print(cars)

for i in range(0,3):
    print(cars[i])
    
for i in cars:
    print(i)
'''''''''''''''''''''''''''''''''''''''
cars.append("Honda")
print(cars)

cars.pop(1)
print(cars)

cars.remove("volvo")
print(cars)
''''''''''''''''''''''''''''''''''''''''
i_array=[]
for i in range(0,3):
    i_array.append(int(input("please input a num")))
print(i_array)
