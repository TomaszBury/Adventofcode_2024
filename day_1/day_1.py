# https://adventofcode.com/2024/day/1

# Read the file and convert its contents into a list of lists
data_list_left:list[int] = []
data_list_right:list[int] = []

# Distances
distance:int = 0

# Similarity_score
similarity_score:int = 0


with open('day_1/input.txt', 'r') as file:
    for line in file:
        numbers = line.split()  # Split the line into individual numbers
        data_list_left.append(int(numbers[0]))  # Convert strings to integers and add to the list
        data_list_right.append(int(numbers[1]))  # Convert strings to integers and add to the list

data_list_left.sort()
data_list_right.sort()

for number_left, number_right in zip(data_list_left, data_list_right):
    distance += abs(number_left-number_right)
    similarity_score += number_left * data_list_right.count(number_left)
    print(f'{number_left}\t{number_right} distance: {distance}')

print(f"Similarity score: {similarity_score}")