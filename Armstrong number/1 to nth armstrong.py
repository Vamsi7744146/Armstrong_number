#print 6th to 10th armstrong number
num=1
count=0
while count<10:
    summ=0
    l=len(str(num))
    dummy=num
    while dummy>0:
        rem=dummy%10
        summ+=rem**l
        dummy//=10
    if summ==num:
        count+=1
        if count>=6:
            print(num)
    num+=1