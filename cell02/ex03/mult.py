number = input ("Enter the first number: ")
number2 = input ("Enter the second number: ")
result = int(number) * int(number2)
print("/mult.py: ", result)
if result >0:
    print("The result is positive.")
elif result <0:
    print("The result is negative.")
else:    print("The result is positive and negative.")
