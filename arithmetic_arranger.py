def arithmetic_arranger(problems, answer = False):

  if len(problems) > 5:
    return 'Error: Too many problems.'

  line1 = []
  line2 = []
  line3 = []
  line4 = []
  
  for operation in problems:
    # Split each arithmetic problem into separate components 
    operand1, operator, operand2 = operation.split(" ")

    #Check the operator 
    if operator != "+" and operator != '-':
      return "Error: Operator must be '+' or '-'."

    #Check the operand 
    if len(str(operand1)) >4 or len(str(operand2)) >4:
      return 'Error: Numbers cannot be more than four digits.'

    if not all(char.isdigit() for char in operand1) or not all(char.isdigit() for char in operand2):
      return 'Error: Numbers must only contain digits.'
    
    # Determine the length of the longest operand
    oper_length = len(max(operand1,operand2,key=len))
    
    # Format
    operand1 = operand1.rjust(oper_length+2)
    operand2 = operand2.rjust(oper_length)
    
    line1.append(operand1)
    line2.append(operator + " " + operand2)
    line3.append('-'*(oper_length + 2))

    if answer == True:
      if operator == '+':
        ans = int(operand1) + int(operand2)
      if operator == '-':
        ans = int(operand1) - int(operand2)
      line4.append(str(ans).rjust(oper_length +2))
    
  line1 = "    ".join(line1)
  line2 = "    ".join(line2)
  line3 = "    ".join(line3)
  
  if answer == True:
    line4 = "    ".join(line4)
    arranged_problems = "\n".join([line1,line2,line3,line4]) 

  else:
    arranged_problems = "\n".join([line1,line2,line3])
    

  return arranged_problems