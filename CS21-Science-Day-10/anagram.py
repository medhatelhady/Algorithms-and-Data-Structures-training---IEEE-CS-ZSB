n = int(input())
 
s = input().lower()
 
if n < 26:
    print('NO')
elif len(set(s)) == 26:
    print('YES')
else:
    print('NO')
