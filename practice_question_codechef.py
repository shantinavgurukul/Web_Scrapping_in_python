# n=int(input("enter the num:-"))
# a=1
# b=0
# i=1
# while(i<=n):
#     c=a+b
#     a=b
#     b=c
#     i=i+1
# print(a)

# def fun(a,b):
#     return(a+b)
#     if(a==1):
#         fun(6,2)
# print(fun(1,2))

# def f():
#     i = 0
#     while(True):
#         return i 

# print(f())


# num=int (input("enter the number"))
# b=1
# c=2
# while(b<=num):
#     i=2
#     while(i<c):
#         if(c%i==0):
#             break
#         i=i+1
#     else:
#         print(c,"is prime number")
#         b=b+1
#     c=c+1
# n=int(input("fgh"))
# a=1
# b=10
# while(a<=n):
#     if (a%2==0):
#         print(a,end="")
#         b=b+10
#     else:
#         a=a+1
#         print(c,end="")




# m=1
# for i in range(1,5):
#     for j in range(i):
#         print(m,end=" ")
#         m=m+1
#     print()
# # print(m)

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end=" ")
#         # m=m+1
#     print()


# a=[1,2,3,4,5,6,7,8,9,10]
# i=0
# c=0
# c2=0
# s=[]
# v=[]
# m=["even"]
# n=[]
# l=[]
# o=[]
# t=["odd"]
# while(i<len(a)):
#     if a[i]%2==0:
#         c=c+1
#         k=a[i]
#         s.append(k)

#     else:
       
#         c2=c2+1
#         b=a[i]
#         v.append(b)
        
#     i=i+1
# n=n+m
# n.append(c)
# n.append(s)
# l=l+t
# l.append(c2)
# l.append(v)
# o.append(n)
# o.append(l)
# print(o)


# n=int(input("enter the number="))
# i=1
# k=[]
# h=[]
# while(i<=n):
#     j=1
#     while(j<=10):
#         a=(i*j)
#         k.append(a)
#         # print(k,end=" ")
#         j=j+1
        
        
#     i=i+1
# print(k)
    

# month=["january","february","march","april","may","june","july","august","september","october","november","december"]
# n=int(input("entee="))
# b=month[n]
# print(b)

binary_number = [1,1,0,1,0]
length = len(binary_number)
a = 1
sum=0
i=0
while(i<length):
    sum= sum+2**i*(binary_number[length-a])
    i=i+1
    a = a+1
print(sum)


