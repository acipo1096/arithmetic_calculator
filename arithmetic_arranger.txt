def arithmetic_arranger(problems):
  print(problems)
  res = [eval(i) for i in problems]

  # to break this down, I will split the list into chunks and work with the first problem
  chunk_size = 1
  split_list = list()

  for i in range(0, len(problems), chunk_size):
    split_list.append(problems[i:i + chunk_size])

  problemA = split_list.pop(0)

  # Now, convert the list to a string
  string_list = problemA
  stringA = ' '.join([str(item) for item in string_list])

  # Now split the string to separate number and operator
  splitA = stringA.split(" ", 1)

  # Now print them vertically in order - can maybe be a function later on?
  for i in range(0, len(splitA)):
    print(splitA[i])

  # NEXT STEP - HOW DO I ALIGN AND PRINT DASHES BASED ON NUMBER OF SPACES?

  print(res[0])

  arranged_problems = 0
  return arranged_problems
