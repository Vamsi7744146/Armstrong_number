#write a program to check first 10 armstrong numbers
num=1
target=10
count=0
while count<target:
    summ=0
    a=len(str(num))
    dummy=num
    while dummy>0:
        rem=dummy%10
        dummy//=10
        summ+=rem**a
    if summ==num:
        print(num)
        count+=1
    num+=1