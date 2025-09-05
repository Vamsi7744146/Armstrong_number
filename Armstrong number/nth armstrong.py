#write a program to print 10th armstrong number
num=1
target=11
count=0
while count<target:
    summ=0
    a=len(str(num))
    dummy=num
    while dummy>0:
        rem=dummy%10
        summ+=rem**a
        dummy//=10
    if summ==num:
        count+=1
        if count==target:
            print(num)
    num+=1