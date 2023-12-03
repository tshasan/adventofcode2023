# ok we will accept the calibration document as a txt and read each line.

with open('day1.txt', 'r') as txt:
    total_sum = 0

    for line in txt:
        cleaned = ''

        for char in line:
            if char.isdigit():
                cleaned += char

        if cleaned:  # Check if cleaned is not empty
            if len(cleaned) == 1:
                total_sum += int(cleaned[0]+cleaned[0])
            else :
                total_sum += int(cleaned[0]+cleaned[-1])            
        else: 
            raise ValueError("shit broke")
            

    print("Sum of all the codes is : " + str(total_sum))



