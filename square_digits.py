# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
# 
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
# 
# Note: The function accepts an integer and returns an integer

def square_digits(num):
    square_num = ""
    for number in str(num):
        square = int(number) ** 2
        square_num += str(square)
    return int(square_num)
