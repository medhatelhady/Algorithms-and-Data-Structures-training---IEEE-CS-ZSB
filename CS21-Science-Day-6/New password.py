


n, k = map(int, input().split())

letters = 'abcdefghijklmnopqrstuvwxyz'
password = ''

i = 0
while n >0:
    password += letters[i]
    i += 1
    n -= 1
    if i == k:
        i = 0
    
print(password)
        
    
