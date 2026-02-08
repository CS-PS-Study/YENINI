import sys
input=sys.stdout.write
A=list(input())

for i in range(len(A)):
    max=i
    for j in range(i+1,len(A)):
        if A[j]>A[max]:
            max=j
    if A[i]<A[max]:
        temp=A[i]
        A[i]=A[max]
        A[max]=temp

for i in range(len(A)):
    input(A[i])