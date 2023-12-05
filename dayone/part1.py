import re

file_path = "/workspaces/adventofocode2023/dayone/data.txt"

with open(file_path, "r") as file:
    value_list = [int(re.sub("[^0-9]", "", line)[0] + re.sub("[^0-9]", "", line)[-1]) for line in file]

print(sum(value_list))
