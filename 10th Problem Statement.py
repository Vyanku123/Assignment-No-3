#Write a program to accept a list L1 of N integers. Accept integer D.
#Generate list L2 such that it contains only those integers from list L1 which are divisible by D.
#Calculate the size of list L2. Print the list L1, N, D, list L2 and its size.

N=int(input("Enter integer N:"))  #Enter number for how many numbers do you want in list l1
l1=[]
print("Enter",N,"integer:") # Enter those numbers
for i in range(N):
    b=int(input())
    l1.append(b)    #Accept those number and append to  list l1
    
D=int(input("Enter integer D:"))   #Enter number for divide to elements of list l1

l2=[i for i in l1 if i%D==0] #Accept those integers from list L1 which are divisible by D.

print("l1=",l1) #Print list l1
print(" Number of integer N=",N,"D=",D)

print("l2=",l2)  #Print list l2
size=len(l2)
print("Size of L2=",l2)  #Size of L2
