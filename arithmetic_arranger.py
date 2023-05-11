# Allows me to use Python regular expressions
import re

def arithmetic_arranger(problems, show=False):
  # I start by splitting each problem into chunks
  # Each problem will have its own index in the list
  # Even though problems is also a list, I need to split into chunks in a separate list
  # Splitting into chunks using problems itself splits each number and operand
  # into a different index
  chunk_size = 1
  split_list = []

  for i in range(0, len(problems), chunk_size):
    split_list.append(problems[i:i + chunk_size])

  problemA = []

  for i in range(0, len(split_list), 1):
    problemA += split_list[i]

  # Now, convert the list to a string
  string_list = problemA
  stringA = ' '.join([str(item) for item in string_list])

  # Initalize empty variables to be used later
  answers = ""
  space = ""
  problemSpace = "    "
  dashedLine = ""
  dashedLine2 = ""
  lineLength = []
  lineOne = ""
  lineTwo = ""
  lineThree = ""

  # Now split the string to separate number and operator
  # We then have to remove all the blank characters

  splitA2 = stringA.split(" ")
  splitA = []
  for ele in splitA2:
    if (ele.strip()):
      splitA.append(ele)

  # Check for non-letters
  regex = re.compile("[0-9\+\-\*\/]+")
  for r in range(0, len(splitA), 1):
    result = regex.match(splitA[r]), 0, len(splitA[r])
    # Matches the matched string as opposed to the object returned by .match()
    if (result[0][0] != splitA[r]):
      return 'Error: Numbers must only contain digits.'

  # This will convert the list objects into integers and solve them automatically
  # This must be after the non-letter check, or else program will throw an error
  res = [eval(i) for i in problems]

  # This will iterate through each separate problem in a given list
  for i in range(0, len(splitA) - 1, 3):

    # Now, we have to return error if * or /
    if (splitA[i + 1] == '*' or splitA[i + 1] == '/'):
      return "Error: Operator must be \'+\' or \'-\'."

    # Check for too many operands
    if (i > 12):
      return "Error: Too many problems."

    # Check for too many digits
    if (len(splitA[i]) > 4 or len(splitA[i + 2]) > 4):
      return "Error: Numbers cannot be more than four digits."

    # Evaluates each problem
    # If the length of the first problem is greater than the length of the second
    if (len(splitA[i]) > len(splitA[i + 2])):

      # Adds the needed number of spaces for the 2nd line based on first operand's length
      spaceLength = len(splitA[i]) - len(splitA[i + 2])
      for j in range(0, spaceLength, 1):
        space += " "

      splitA[i] = "  " + splitA[i]
      splitA[i + 2] = splitA[i + 1] + " " + space + splitA[i + 2]
      # If space is not reset, each iteration will add too many spaces
      space = ""

      # Adds each operator and operand to the correct line
      if (i + 3 < len(splitA) - 1):
        lineOne += splitA[i] + problemSpace
      else:
        lineOne += splitA[i]

      if (i + 3 < len(splitA) - 1):
        lineTwo += splitA[i + 2] + problemSpace
      else:
        lineTwo += splitA[i + 2]

      # Calculates the proper number of dashes
      # dashedLine2 is separate because it won't count the spaces between each problem

      for k in range(0, len((splitA[i])), 1):
        dashedLine += "-"
        dashedLine2 += "-"

      lineLength.append(dashedLine2)
      dashedLine2 = ""

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
        dashedLine += "-"
        dashedLine2 += "-"

      lineLength.append(dashedLine2)
      dashedLine2 = ""

      if (i + 3 < len(splitA)):
        dashedLine += problemSpace

  # Calculate problems
  for a in range(0, len(res), 1):
    strLength = len(str(res[a]))
    spaceLength = len(lineLength[a]) - (strLength)
    for s in range(0, spaceLength, 1):
      space += " "

    if (a < len(problemA) - 1):
      lineThree += space + str(res[a]) + problemSpace
    else:
      lineThree += space + str(res[a])

    space = ''

  # Determines whether or not answers will be displayed
  if (show == False):
    arranged_problems = str(lineOne) + '\n' + str(lineTwo) + '\n' + dashedLine
  elif (show == True):
    arranged_problems = str(lineOne) + '\n' + str(
      lineTwo) + '\n' + dashedLine + '\n' + lineThree

  # This allows me to compare my input with the tests
  print(repr(arranged_problems))

  return arranged_problems