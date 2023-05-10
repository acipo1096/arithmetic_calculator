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
  stringA = ' '.join([str(item) for item in string_list])
  # print("This is a string: ", stringC)
  # stringB = re.sub('[^0-9+-\/\*]', ' ', stringC)
  # stringA = stringB
  # print("This is a regex string: ", stringA)

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

  # Check for non-letters
  regex = re.compile("[0-9\+\-\*\/]+")
  for r in range(0, len(splitA), 1):
    print("The current iteration value is: ", splitA[r])
    result = regex.match(splitA[r]), 0, len(splitA[r])
    # Matches the matched string as opposed to the object returned by .match()
    if (result[0][0] != splitA[r]):
      # print(splitA[r])
      return 'Error: Numbers must only contain digits.'

  # What if I keep the same coding principle but alter the syntax/code used?
  for i in range(0, len(splitA) - 1, 3):
    print("i+3 is: ", i + 3)
    print("Length is: ", len(splitA))

    # Now, we have to return error if * or /
    if (splitA[i + 1] == '*' or splitA[i + 1] == '/'):
      return "Error: Operator must be \'+\' or \'-\'."

    # Check for too many operands
    if (i > 12):
      return "Error: Too many problems."

    # Check for too many digits
    print("The length of splitA[i+2] is: ", len(splitA[i + 2]))
    print("splitA is: ", splitA[i + 2])
    if (len(splitA[i]) > 4 or len(splitA[i + 2]) > 4):
      return "Error: Numbers cannot be more than four digits."

    if (len(splitA[i]) > len(splitA[i + 2])):
      spaceLength = len(splitA[i]) - len(splitA[i + 2])
      # Adds the needed number of spaces for the 2nd line based on first operand's length
      for j in range(0, spaceLength, 1):
        space += " "

      splitA[i] = "  " + splitA[i]
      splitA[i + 2] = splitA[i + 1] + " " + space + splitA[i + 2]
      space = ""

      if (i + 3 < len(splitA) - 1):
        lineOne += splitA[i] + problemSpace
      else:
        lineOne += splitA[i]

      if (i + 3 < len(splitA) - 1):
        lineTwo += splitA[i + 2] + problemSpace
      else:
        lineTwo += splitA[i + 2]

      for k in range(0, len((splitA[i])), 1):
        print("k is: ", k)
        dashedLine += "-"

      if (i + 3 < len(splitA)):
        dashedLine += problemSpace

    else:
      spaceLength = len(splitA[i + 2]) - len(splitA[i])
      # Adds the needed number of spaces for the 2nd line based on first operand's length
      for j in range(0, spaceLength, 1):
        space += " "
      splitA[i] = "  " + space + splitA[i]
      splitA[i + 2] = splitA[i + 1] + " " + splitA[i + 2]
      space = ""

      if (i + 3 < len(splitA) - 1):
        lineOne += splitA[i] + problemSpace
      else:
        lineOne += splitA[i]

      if (i + 3 < len(splitA) - 1):
        lineTwo += splitA[i + 2] + problemSpace
      else:
        lineTwo += splitA[i + 2]

      for k in range(0, len((splitA[i + 2])), 1):
        print("k is: ", k)
        dashedLine += "-"

      if (i + 3 < len(splitA)):
        dashedLine += problemSpace
  # Puts the arranged_problems return on the next line
  # print()
  # print(res[1])

  arranged_problems = str(lineOne) + '\n' + str(lineTwo) + '\n' + dashedLine
  print(repr(arranged_problems))

  return arranged_problems
