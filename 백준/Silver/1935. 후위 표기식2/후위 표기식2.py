from decimal import Decimal
n = int(input())
s = input()
stack = []
nums = [int(input()) for _ in range(n)]
dic = {}
for x in s:
    if x.isalpha():
        if x not in dic:
          dic[x] = nums.pop(0)
        top = dic[x]
        stack.append(int(top))
    else:
        b = Decimal(stack.pop())
        a = Decimal(stack.pop())
        num = 0
        if x == '+':
            num = a + b
        if x == '*':
            num = a * b
        if x == '-':
            num = a - b
        if x == '/':
            num = a / b
        stack.append(num)

print(round(num, 2))