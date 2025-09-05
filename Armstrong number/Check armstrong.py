#write a program to check the given number is armstrong number or not 
#153 is armstrong--->taht is equal to the sum of digits each raised to the power of the number of digits 
num=int(input())
a=len(str(num))
summ=0
dummy=num
while dummy>0:
    rem=dummy%10         
    dummy//=10
    summ+=rem**a
if num==summ:
    print('armstrong')
else:
    print('not armstrong')