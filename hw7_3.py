'''
   1
  123
 12345
  123
   1
'''
max_line: int = 0
while max_line == 0:
    max_line: int = int(input("nax_line: "))

for number in range(1, max_line + 2, 2):
    spaces: int = (max_line - number) // 2
    print(" " * spaces, end= "")
    for i in range(1, number + 1):
        print(i, end= "")
    print()

for number in range(max_line - 2, 1 -2 , -2):
    spaces: int = (max_line - number) // 2
    print(" " * spaces, end= "")
    for i in range(1, number + 1):
        print(i, end="")
    print()

''''
   *
  ***
 *****
*******
 *****
  ***
   *
'''

max_line: int = 0
while max_line == 0:
    max_line: int = int(input("nax_line: "))

for number in range(1, max_line + 2, 2):
    spaces: int = (max_line - number) // 2
    print(" " * spaces, end= "")
    for i in range(1, number + 1):
        print("*", end= "")
    print()

for number in range(max_line - 2, 1 -2 , -2):
    spaces: int = (max_line - number) // 2
    print(" " * spaces, end= "")
    for i in range(1, number + 1):
        print("*", end="")
    print()