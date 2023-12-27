#1
a = int(input("tell first number:"))
for i in range(0, a):
    for j in range(0, a):
        print("*", end=" ")
    print()
    #2
a = int(input("tell first number:"))
b = int(input("tell second number:"))
for i in range(0, a * b):
    for j in range(0, a * b):
        print("*", end=" ")
    print()
#3
a = int(input("tell first number:"))
for i in range(0, a + 1):
    for j in range(0, a+ 1):
        if i == 0 or i == a :
            print("*", end=" ")
        elif j == 0 or j == a:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()
    #4
a = int(input("tell first number:"))
b = int(input("tell second number:"))
for i in range(0, a + 1):
    for j in range(0,  b + 1):
        if i == 0 or i == a:
            print("*", end=" ")
        elif j == 0 or j == b:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()



