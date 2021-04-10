import sys

string = sys.stdin.readline()
result = 0
temp1 = ''
temp2 = 0
judge = False

for i in range(len(string)):
  # print(temp2, temp1, result)
  if i == len(string) -1:
    temp1 += string[i]
    if judge == False:
      result += int(temp1)

    elif judge == True:
      temp2 += int(temp1)
      result -= temp2 

  elif judge == False:
    if string[i] == '+':
      result += int(temp1)
      temp1 = ''

    elif string[i] == '-':
      judge = True
      result += int(temp1)
      temp1 = ''

    else:
      temp1 += string[i]
  
  elif judge == True:
    if string[i] == '+':
      temp2 += int(temp1)
      temp1 = ''

    elif string[i] == '-':
      temp2 += int(temp1)
      temp1 = ''
      result -= temp2
      temp2 = 0
      
    else:
      temp1 += string[i]


print(result)