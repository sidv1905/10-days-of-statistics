# Enter your code here. Read input from STDIN. Print output to STDOUT
N=int(input())
arr=list(map(int, input().split()))

mean=sum(arr)/N
upper=0
for i in range(N):
    upper=upper+(arr[i]-mean)**2
upper=(upper/N)**0.5

print(round(upper,1))
    

