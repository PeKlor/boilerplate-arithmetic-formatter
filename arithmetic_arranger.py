def arithmetic_arranger(problems, displayanswers=False):

  if len(problems) > 5:
    return "Error: Too many problems."

  firstlinenums = list()
  answers = list()
  secondlinenums = list()
  operands = list()

  k = 0 
  for problem in problems:
    equation = problem.split()
    
    oper = equation[1]
    if oper == "*" or oper == "/":
      return "Error: Operator must be '+' or '-'."
    operands.append(oper)
      
    xdigitcount = 0
    for digit in equation[0]:
      if not (digit >= "0" and digit <= "9"):
        return "Error: Numbers must only contain digits."
      xdigitcount += 1
    if xdigitcount > 4:
      return "Error: Numbers cannot be more than four digits."
    firstlinenums.append( (int(equation[0]), xdigitcount) )

    ydigitcount = 0
    for digit in equation[2]:
      if not (digit >= "0" and digit <= "9"):
        return "Error: Numbers must only contain digits."
      ydigitcount += 1
    if ydigitcount > 4:
      return "Error: Numbers cannot be more than four digits."
    secondlinenums.append( (int(equation[2]), ydigitcount) )

    if oper == "+":
      answers.append(firstlinenums[k][0] + secondlinenums[k][0])
    else:
      answers.append(firstlinenums[k][0] - secondlinenums[k][0])
    k += 1

  firstline = ""
  secondline = ""
  dashline = ""
  answerline = ""
  
  for i in range(len(problems)):
    mostdigits = max(firstlinenums[i][1], secondlinenums[i][1])
    
    firstline += "  " + (mostdigits-firstlinenums[i][1])*" " + str(firstlinenums[i][0])
    secondline += operands[i] + " " + (mostdigits-secondlinenums[i][1])*" " + str(secondlinenums[i][0])
    dashline += "--" + mostdigits*"-"
    answerline += " "
    if int(len(str(answers[i]))) == mostdigits: 
      answerline += " "
    elif int(len(str(answers[i]))) < mostdigits:
      answerline += " " + (mostdigits-int(len(str(answers[i]))))*" "
    answerline += str(answers[i])
    
    if i != len(problems)-1:
      firstline += "    "
      secondline += "    "
      dashline += "    "
      answerline += "    "
    else:
      firstline += "\n"
      secondline += "\n"
      if displayanswers:
        dashline += "\n"

  arranged_problems = firstline + secondline + dashline
  if displayanswers:
    arranged_problems += answerline
  
  return arranged_problems