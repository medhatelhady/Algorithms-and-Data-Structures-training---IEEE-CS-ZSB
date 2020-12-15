n = int(input())
 
names_count = dict()
for i in range(n):
    name = input()
    
    x = names_count.get(name, 0)
    if x == 0:
        print('OK')
        names_count[name] = 1
    else:
        print(name+str(x))
     
        names_count[name] += 1
