#Write a program to accept a list L1 of N integers. Accept integer M. Multiply each integer in the list by M and generate a new list L2. Print the lists L1 and L2.

N=int(input("Enter integer N:"))  #Enter N integers.
M=int(input("Enter integer M for multiply")) #Accept integer M.

print("Enter",N,"number:")

l1=[int(i)for i in input().split()[:N]] #accept a list L1 of N integers.

l2 = [N * M for N in l1] #Multiply each integer in the list l1 by M


print("L1=",l1,"L2=",l2) #Print list L1 and L2
