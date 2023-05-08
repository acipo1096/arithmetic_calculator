def arithmetic_arranger(problems):
  print(problems)
  res = [eval(i) for i in problems]

  # to break this down, I will split the list into chunks and work with the first problem
  chunk_size = 1
  split_list = list()

  for i in range(0, len(problems), chunk_size):
    split_list.append(problems[i:i + chunk_size])

  problemA = split_list.pop(1) + split_list.pop(2)

  # Now, convert the list to a string
  string_list = problemA
  stringA = ' '.join([str(item) for item in string_list])

  # Now split the string to separate number and operator
  # splitA = stringA.split(" ", 2)

  # Splitting string from one line of input - Test 1
  space = ""
  splitA = stringA.split(" ")
  print(splitA)

  # Right alignment works, but there's no need to order based on operand length
  # Splitting string from one line of input - Test 1
  if (len(splitA[0]) > len(splitA[2])):
    spaceLength = len(splitA[0]) - len(splitA[2])
    # Adds the needed number of spaces for the 2nd line based on first operand's length
    for i in range(0, spaceLength, 1):
      space += " "
    splitA[0] = "  " + splitA[0] + '\n'
    splitA[2] = splitA[1] + " " + space + splitA[2]
    print(splitA[0] + splitA[2])
    space = ""

  # Splitting string from one line of input - Test 2
  if (len(splitA[3]) > len(splitA[5])):
    spaceLength = len(splitA[3]) - len(splitA[5])
    for i in range(0, spaceLength, 1):
      space += " "
    splitA[3] = "  " + splitA[3] + '\n'
    splitA[5] = splitA[4] + " " + space + splitA[5]
    print(splitA[3] + splitA[5])

  # Below works, but seeing errors, it doesn't match the output

  # Now print them vertically in order and almost perfectly aligned
  # line1 = splitA[0]
  # line2 = splitA[1]
  # if (len(line1) < len(line2)):
  #   numSpaces = len(line2) - len(line1)
  #   for i in range(0, numSpaces, 1):
  #     print(" ", end="")
  #   print(line1)
  #   print(line2)
  # if (len(line1) > len(line2)):
  #   numSpaces = len(line1) - len(line2)
  #   print(line1)
  #   for i in range(0, numSpaces, 1):
  #     print(" ", end="")
  #   print(line2)

  # Prints the number of hyphens based on which line in problem is longer length
  # if (len(splitA[0]) > len(splitA[1])):
  #   for i in range(0, len(splitA[0]), 1):
  #     print("-", end="")
  # else:
  #   for i in range(0, len(splitA[1]), 1):
  #     print("-", end="")

  # Puts the arranged_problems return on the next line
  # print()
  # print(res[1])

  arranged_problems = 0
  return arranged_problems
