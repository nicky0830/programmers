n = int(input())
dic = {'l':1, 'r':1, 'n':1 }

for _ in range(n-1):
    check = {'l':0, 'r':0, 'n':0}
    check['l'] = (dic['r'] + dic['n']) 
    check['r'] = (dic['l'] + dic['n']) 
    check['n'] = (dic['r'] + dic['l'] + dic['n']) 
    dic = check

print(sum(dic.values()) % 9901)