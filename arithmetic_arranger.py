import re


def arithmetic_arranger(problems):
  # res = [eval(i) for i in problems]

  # to break this down, I will split the list into chunks and work with the first problem
  chunk_size = 1
  split_list = list()

  for i in range(0, len(problems), chunk_size):
    split_list.append(problems[i:i + chunk_size])

  problemA = []

  for i in range(0, len(split_list), 1):
    problemA += split_list[i]

  print("This is a list: ", problemA)

  # Now, convert the list to a string
  # AND NOW YOU NEED TO REMOVE ALL NON-DIGITS
  string_list = problemA
  stringC = ' '.join([str(item) for item in string_list])
  print("This is a string: ", stringC)
  stringB = re.sub('[^0-9+-\/\*]', ' ', stringC)
  stringA = stringB
  print("This is a regex string: ", stringA)

  space = ""
  problemSpace = "    "
  dashedLine = ""
  lineOne = ""
  lineTwo = ""

  # Now split the string to separate number and operator
  # Then, we have to remove all the blank characters

  splitA2 = stringA.split(" ")
  splitA = []
  for ele in splitA2:
    if (ele.strip()):
      splitA.append(ele)
  print(splitA)

  problemResult = ''

  # What if I keep the same coding principle but alter the syntax/code used?
  for i in range(0, len(splitA) - 1, 3):
    # Now, we have to return error if * or /
    if (splitA[i + 1] == '*' or splitA[i + 1] == '/'):
      print('Error: Operator must be \'+\' or \'-\'')
      continue

    if (len(splitA[i]) > len(splitA[i + 2])):
      spaceLength = len(splitA[i]) - len(splitA[i + 2])
      # Adds the needed number of spaces for the 2nd line based on first operand's length
      for j in range(0, spaceLength, 1):
        space += " "

      splitA[i] = "  " + splitA[i]
      splitA[i + 2] = splitA[i + 1] + " " + space + splitA[i + 2]
      space = ""

      lineOne += splitA[i] + problemSpace
      lineTwo += splitA[i + 2] + problemSpace

      for k in range(0, len((splitA[i])), 1):
        dashedLine += "-"

      dashedLine += problemSpace

    else:
      spaceLength = len(splitA[i + 2]) - len(splitA[i])
      # Adds the needed number of spaces for the 2nd line based on first operand's length
      for j in range(0, spaceLength, 1):
        space += " "
      splitA[i] = "  " + space + splitA[i]
      splitA[i + 2] = splitA[i + 1] + " " + splitA[i + 2]
      space = ""

      lineOne += splitA[i] + problemSpace
      lineTwo += splitA[i + 2] + problemSpace

      for k in range(0, len((splitA[i + 2])), 1):
        dashedLine += "-"

      dashedLine += problemSpace

  print(" " + lineOne, '\n', lineTwo, '\n', dashedLine)

  # Puts the arranged_problems return on the next line
  # print()
  # print(res[1])

  arranged_problems = 0
  return arranged_problems
