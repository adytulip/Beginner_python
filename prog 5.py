x = int(input('enter first number:'))
y = int(input('enter second number:'))
z = int(input('enter third number:'))

if y>= x <=z:
    if y<=z:
        min,mid,max=x,y,z
    else:
        min,mid,max=x,z,y
elif x>=y<=z:
    if x<=z:
        min,mid,max=y,x,z
    else:
        min,mid,max=y,z,x
elif y>=z<=x:
    if y<=x:
        min,mid,max=z,y,x
    else:
        min,mid,max=z,x,y
print('numbers in ascending order are:',min,mid,max)
        

print('enter a number (numerator): ')
numn = int(input())
print('enter a number (denominator):')
numd = int(input())

if numn%numd==0:
    print('\n' +str(numn)+ 'is divisible by' +str(numd))
else:
    print('\n' + str(numn) + 'is divisible by' +str(numd))
    
