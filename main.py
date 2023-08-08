# This entrypoint file to be used in development. Start by reading README.md
from pytest import main

from arithmetic_arranger import arithmetic_arranger

problem_num = input(
  'How many problems do you want to solve (max 5 problems)? ')
print(
  '\nNote: Only include operands - and +, and operator length must not exceed 4.'
)
print('For example: "2321 + 2342" or "12 + 342".')
print()
problems = []
for i in range(int(problem_num)):
  problem = input(f'The problem number {i+1} is: ')
  problems.append(problem)

print()
print(arithmetic_arranger(problems, answer=True))

#print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))

# Run unit tests automatically
#main(['-vv'])
