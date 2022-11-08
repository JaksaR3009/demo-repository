# broj = int(input("Unesi broj: "))


# if broj > 0:
#     print("Broj je pozitivan.") 
#     print("Testiranje")
# elif broj < 0:
#     print("Broj je negativan.")
# else:
#     print("Broj je jednak 0.")


# + - * / %
# > < >= <= == !=
# and or not

a = int(input("Unesi broj a: "))
b = int(input("Unesi broj b: "))
c = int(input("Unesi broj c: "))

# if a < b and a < c:
#     print(a)
# elif b < a and b < c:
#     print(b)
# else:
#     print(c)

if a < b:
    if a < c:
        print(a)
    else:
        print(c)
else:
    if b < c:
        print(b)
    else:
        print(c)
    