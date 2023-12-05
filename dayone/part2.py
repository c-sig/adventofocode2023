import re

num_to_word = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
word_to_num = {v: k for k, v in num_to_word.items()}

def replace_numbers(match):
    return num_to_word[int(match.group(0))]

file_path = "/workspaces/adventofocode2023/dayone/data.txt"

with open(file_path, "r") as file:
    value_list = []

    for line in file:
        line = re.sub(r'\d', replace_numbers, line.strip())

        word_pattern = re.compile(r'(?=(one|two|three|four|five|six|seven|eight|nine))')
        matches = word_pattern.findall(line)

        # Convert matches to numbers
        matches = [word_to_num[match] for match in matches]

        value = str(matches[0]) + str(matches[-1])
        value_list.append(int(value))

    print(sum(value_list))
