import re

with open("/workspaces/adventofocode2023/dayone/data.txt", "r") as file:
    value_list = []
    for line in file:
        line = re.sub("[^0-9]", "", line)
        line = line[0] + line[-1]
        value_list.append(int(line))
    print(sum(value_list))
        