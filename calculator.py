a = int(input("How many numbers do you want to enter? "))
numbers = []
i = 0

# Taking input numbers
while i < a:
    num = int(input("Enter the number: ".format(i+1)))
    numbers.append(num)
    i += 1

print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
c = int(input("Choose the arithmetic operation you want to perform: "))

if c == 1:
    result = sum(numbers)
    print("Result of addition:", result)
elif c == 2:
    result = numbers[0]
    j = 1
    while j < len(numbers):
        result -= numbers[j]
        j += 1
    print("Result of subtraction:", result)
elif c == 3:
    result = 1
    j = 0
    while j < len(numbers):
        result *= numbers[j]
        j += 1
    print("Result of multiplication:", result)
elif c == 4:
    result = numbers[0]
    j = 1
    while j < len(numbers):
        if numbers[j] != 0:
            result /= numbers[j]
        else:
            print("Division by zero is not allowed!")
            break
        j += 1
    else:
        print("Result of division:", result)
else:
    print("Invalid selection")
