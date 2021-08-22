#Declaring list
numbers = []

#Loop to fill the list
for i in range(100):
    numbers.append(i)
print(numbers)

#Loop to remove even numbers
for num in numbers:
    if(num % 2 == 0):
        numbers.remove(num)
print(numbers)