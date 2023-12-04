def part1(file_path):
    total_sum = 0
    with open(file_path, 'r') as txt:
        for line in txt:
            cleaned = ''
            for char in line:
                if char.isdigit():
                    cleaned += char
            if cleaned:  # Check if cleaned is not empty
                if len(cleaned) == 1:
                    total_sum += int(cleaned[0] + cleaned[0])
                else:
                    total_sum += int(cleaned[0] + cleaned[-1])
    return total_sum

def part2(file_path):
    total_sum = 0
    replace_dict = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e"
    }

    with open(file_path, 'r') as txt:
        for line in txt:
            cleaned = line.lower() # removing this line makes this function not work 
            for word, number in replace_dict.items():
                cleaned = cleaned.replace(word, number)

            cleaned = ''.join([char for char in cleaned if char.isdigit()])
            if cleaned:  # Check if cleaned is not empty
                if len(cleaned) == 1:
                    total_sum += int(cleaned[0] + cleaned[0])
                else:
                    total_sum += int(cleaned[0] + cleaned[-1])
    return total_sum





file_path = 'day1.txt'
print("Part1:", part1(file_path))
print("Part2:", part2(file_path))
