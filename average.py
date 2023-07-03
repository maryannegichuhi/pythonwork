# create a function that calculates the average of a number'[2.5,6,3,5]

def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average


data = [2.5, 6, 3, 5]
result = calculate_average(data)
print("The average is", result)
