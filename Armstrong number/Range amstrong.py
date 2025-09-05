#write a program to print the armstrong number by given range
LL=int(input())
UP=int(input())
for num in range(LL,UP+1):
    l=len(str(num))
    summ=0
    dummy=num
    while dummy>0:
        rem=dummy%10
        dummy//=10
        summ+=rem**l
    if num==summ:
        print(num)