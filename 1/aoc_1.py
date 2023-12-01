print("AoC is ready! Lets roll!")

result = 0
first_digit = -1
last_digit = -1
index = -1
tmp = ""

word_to_number = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'zero': '0'}

with open('input_2.txt') as f:
    lines = f.readlines()
    lines += "\n"
    for line in lines:
        index = -1
        for char in line:
            index += 1
            tmp_index = index
            while tmp not in word_to_number or len(tmp) > 5:
                if tmp_index >= len(line):
                    break
                tmp += line[tmp_index]
                tmp_index += 1
                
            if tmp in word_to_number:
                insert = word_to_number.get(tmp)
                if (insert.isnumeric() and first_digit == -1):
                    first_digit = insert
                elif (insert.isnumeric()):
                    last_digit = insert
            elif (char != "\n"):
                if (char.isnumeric() and first_digit == -1):
                    first_digit = char
                elif (char.isnumeric()):
                    last_digit = char
            else:
                if (last_digit == -1):
                    last_digit = first_digit
                result += (int(first_digit + last_digit)) 
                print("TEST",int(first_digit + last_digit))
                first_digit = -1
                last_digit = -1
            tmp = ""
            

            
print(result)
