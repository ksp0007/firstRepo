x=int(input('enter anumber'))
s=0
t=x
while(t>0):
    r=t%10
    s=s*10+r
    t=t//10
print('reverse of it is =%d' %s)    
if(x==s):
    print('the number is palindrome')
else:
    print('the number is not palindrome')
    
