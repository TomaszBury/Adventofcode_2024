import re

def read_input_file(filename) -> list[str]:
    with open(filename, 'r') as file:
        content = file.read()
    
    # Regular expression to match 'mul(int,int)'
    pattern = r'mul\(\d+,\d+\)'

    # Split the content based on the pattern
    split_content = re.findall(pattern, content)

    return split_content

def calculate_mul(mul_file) -> int:
    result:int = 0
    pattern = r'mul\((\d+),(\d+)\)'
    
    for item in mul_file:
        match = re.match(pattern, item)
        if match:
            num1, num2 = int(match.group(1)), int(match.group(2))
            result += num1 * num2
    
    return result
        

input_file = read_input_file("day_3/input.txt")

result = calculate_mul(input_file)

print(result)