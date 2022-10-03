num1 = float(input("Number: "))
operator = str(input("Operator: "))
num2 = float(input("Number: "))

operatorDict = {
    "+" : num1 + num2,
    "-" : num1 - num2,
    "*" : num1 * num2,
    "/" : num1 / num2,
    "%" : num1 % num2,
    "^" : num1 ** num2
}

result = operatorDict.get(operator)

if result != None:
    print(num1 , operator , num2 , "=" , result)
else:
    print("Invalid operator")
