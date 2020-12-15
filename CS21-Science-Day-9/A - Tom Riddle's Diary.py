n = int(input())
 
names = set()
 
for i in range(n):
    name = input()
    
    if name in names:
        print('YES')
    else:
        print('NO')
    names.add(name)
