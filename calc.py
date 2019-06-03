i = 1
while i <= 10:

    o = input("\n+  -  *  /  ^\nSelect an operator: ")
    x = input("Type a number: ")
    y = input("Type another number: ")

    if o == "/":
        print(float(x) / float(y))
        i += 1
    elif o == "+":
        print(float(x) + float(y))
        i += 1
    elif o == "-":
        print(float(x) - float(y))
        i += 1
    elif o == "*":
        print(float(x) * float(y))
        i += 1
    elif o == "^":
        print(float(x) ** float(y))
        i += 1
    else:
        print("\nIncorrect Operator")

