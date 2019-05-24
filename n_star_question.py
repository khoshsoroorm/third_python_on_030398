
star = '*'
space = ' '
number_of_lines = 10
#part 1
for i in range(1, number_of_lines + 1):
    print(star * i)

# part 2
width = number_of_lines * 2 - 1
for i in range(number_of_lines):
    asterisks = star * (2 * i + 1)
    line = asterisks.center(width)
    print(line)

# part 3
 print(number_of_lines*space + star)
 for i in range(1, number_of_lines):
     white_space = space * (number_of_lines - i)
     # asterisks = pattern * (2 * i + 1)
     middle_ws = space * (2 * i - 1)
     line = white_space + star + middle_ws + star
     print(line)

 print((2*number_of_lines+1)*star)

