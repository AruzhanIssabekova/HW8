def insertionSort(A):

    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i - 1

        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1

        A[j + 1] = key

    return A

def selectionSort(A):

    n = len(A)
    for i in range(n - 1):
        nMin = i
        for j in range(i + 1, n):
            if A[j] > A[nMin]:
                nMin = j

        if i != nMin:
            A[i], A[nMin] = A[nMin], A[i]


    return A


# 1

# A=list(map(int,input().split()))
# B=insertionSort(A)
# print(B)


# 2

# C=list(map(int,input().split()))
# D=selectionSort(C)
# print(D)


# 3

# N=int(input())
# P=list(map(int,input().split()[:N]))
# SP=selectionSort(P)
# k=N//3
# s=0
# for i in range(k):
#     s=s+P[i]
# print(s)

# 4

# a=list(map(int,input().split()))
# S=sorted(a)
# d=abs(S[1]-S[0])
# for i in range(len(S)):
#     for j in range(i+1,len(S)):
#         dd=abs(S[i] - S[j])
#         if dd < d:
#             Si = S[i]
#             Sj = S[j]
#             d=dd
# print(Si, Sj)

# a=list(map(int,input().split()))
# b=sorted(a)
# a0=[]
# d=b[1]-b[0]
# for i in range(len(b)):
#     c=b[i+1]-b[i]
#     if c<d:
#         d=c
#         a1=b[i]
#         a2=b[i+1]
#     # el:
#     #     a1=b[0]
#     #     a2=b[1]
# print(a1,a2)

a=list(map(int,input().split()))
ai=0
aj=1
d=abs(a[0]-a[1])
for i in range(len(a)):
    for j in range(i+1,len(a)):
        dd=abs(a[i] - a[j])
        if dd<d:
            ai=a[i]
            aj=a[j]
            d=dd
        elif dd<d:
            continue
        elif dd==d:
            ai=a[0]
            aj=a[1]
a0=[]
a0.append(ai)
a0.append(aj)
print(a0)