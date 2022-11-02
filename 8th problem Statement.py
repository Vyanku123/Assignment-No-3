#Write a program to accept a list of N integers. Accept integer K. Find the Kth smallest number in the list and its position.
#Input: N=8, List= (82,11,55,20,10,67,78,42), K=3
#Output: Kth smallest integer=20, Position of Kth smallest integer=4


a=int(input("enter value of N:")) #Accept list of N integers.
k=int(input("enter value of k:")) # Accept integer K

b=[int(i) for i in input().split()[:a]] #Accept numbers
print("Original List:",b)
c=sorted(b) #Sort list
print("Sorted List:",c) #print Sorted list

m_in=c[k-1] #we substract -1 from kth number cause list count starting from zero. 

i_n=b.index(m_in) #find index of that Kth element

print("Position of Kth smallest integer in original list=",i_n+1)  #we add +1 in kth number cause list count starting from one.
print("Kth smallest integer=",m_in)
