with open("day2.txt", 'r') as txt:
    total_sum = 0
    current_game = 0
    fake = 0

    bag = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    for line in txt:
        line = line.rstrip()
        line = line.replace(' ', '')
        line = line.replace(":", ",")
        line = line.replace(";", ",")
        values = line.split(",")

        for x in values:
            x = x.rstrip()

            if "Game" in x:
                x = x.replace("Game", "")
                current_game = x
                fake = 0  # Reset fake flag for a new game
            elif "red" in x:
                x = x.replace("red", "")
                if int(x) <= bag["red"]:
                    pass
                else:
                    fake = 1
            elif "green" in x:
                x = x.replace("green", "")
                if int(x) <= bag["green"]:
                    pass
                else:
                    fake = 1
            elif "blue" in x:
                x = x.replace("blue", "")
                if int(x) <= bag["blue"]:
                    pass
                else:
                    fake = 1
            else:
                print("invalid character", x)

        if fake == 0:
            total_sum += int(current_game)  # Increment the total sum for valid games

print("Total sum of games:", total_sum)




