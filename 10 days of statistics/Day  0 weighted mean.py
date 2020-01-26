
N=int(input())
X=list(map(int, input().split()))
W=list(map(int, input().split()))

sum1=0

for i in range(len(W)):
    sum1=sum1+W[i]*X[i]

print(round(sum1/sum(W),1))
