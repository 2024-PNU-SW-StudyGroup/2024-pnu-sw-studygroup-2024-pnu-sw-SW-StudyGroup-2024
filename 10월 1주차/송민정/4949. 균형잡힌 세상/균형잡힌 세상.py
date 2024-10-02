while True:
  stack=[]
  ans='yes'
  fron=['[','(']
  s=str(input())
  if s != '.':
    for i in range(len(s)):
      if s[i] in fron:
        stack.append(s[i])

      elif (s[i] == ')'): 
        if (len(stack) != 0) and (stack[-1] == '('):
          stack.pop()
        else:
          print('no')
          ans='no'
          break

      elif (s[i] == ']'):
        if (len(stack) != 0) and (stack[-1] == '['):
          stack.pop()
        else:
          print('no')
          ans='no'
          break
          
    if ans=='no':
      continue
    elif len(stack) == 0:
      print('yes')
    else:
      print('no')
  else:
    break
        