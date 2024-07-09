n = int(input())
fact_arr = [0] * (n+1)
def factorial(num):
    if num== 0:
        fact_arr[0] = 1
    if num == 1:
        fact_arr[1] = 1
    if fact_arr[num] == 0:
        fact_arr[num] = num*factorial(num-1) 
    return fact_arr[num]
answer = 0
for a in str(factorial(n))[::-1]:
    if a == '0':
        answer +=1
    else:
        print(answer)
        break