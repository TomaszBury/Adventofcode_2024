def read_file_to_list_of_lists(filename) -> list[list[int]]:
    list_of_lists = []

    # Open the file in read mode
    with open(filename, 'r') as file:
        # Read each line in the file
        for line in file:
            # Split the line into string numbers, then convert them to integers
            int_list = [int(num) for num in line.split()]
            # Add the list of integers to the list of lists
            list_of_lists.append(int_list)

    return list_of_lists

# Example usage
filename = 'day_2/input.txt'
reports:list[list[int]] = read_file_to_list_of_lists(filename)
# print(result)

def is_consistent(lst):
    if len(lst) < 2:
        return True
    
    is_increasing = all(x < y for x, y in zip(lst, lst[1:]))
    is_decreasing = all(x > y for x, y in zip(lst, lst[1:]))
    
    return is_increasing or is_decreasing

reports_safe:int = 0
report_safe:int = 0

for report in reports:
    report_safe = 1
    if is_consistent(report):
        for i in range(1,len(report)):
            if abs(report[i-1] - report[i]) <=3:
                report_safe += 1
        
            if report_safe == len(report):
                print(f"report:{report} len:{len(report)} reports_safe:{reports_safe}")
                reports_safe +=1



print(reports_safe)