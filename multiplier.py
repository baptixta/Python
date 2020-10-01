# Array of numbers
numberlist = []

# Loop getting numbers from input
for item in range(0,4):
    number = float(input("Enter a number: "))
    numberlist.append(number)


factor = float(input("Enter a multiplier: "))

# Function to multiply the numbers from input
def multiplier(numbers, factor):
    result = []
    for item in numbers:
        result.append(item * factor)        
    return result

# Showing on the screen
print(multiplier(numberlist, factor))

