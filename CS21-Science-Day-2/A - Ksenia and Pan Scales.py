left, right = input().split('|')
 
available = input()
 
for i in available:
    if len(left) > len(right):
        right += i
    else:
        left += i
 
if len(left) == len(right):
    print(left+'|'+right)
else:
    print('Impossible')
