a = input()
b = input()
c = input()
l = [a, b, c]

for i in range(len(l)):
    if list(l[i])[0] in ['0','1','2','3','4','5','6','7','8','9']:
        next_num = int(l[i]) + (3-i)
        break

if next_num % 3 == 0 and next_num % 5 == 0:
    print('FizzBuzz')
elif next_num % 3 == 0:
    print('Fizz')
elif next_num % 5 == 0:
    print('Buzz')
else:
    print(str(next_num))