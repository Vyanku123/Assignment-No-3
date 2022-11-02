#Write a program to a accept a list of N integers. Find the largest and the smallest number in the list and their respective positions in the list.
#Input: N=6, List = (55,3,23,452,82,19)
#Output: Largest integer=452, Position of Largest integer=4, 
#Smallest integer=3, Position of smallest integer=2

a=int(input("Enter value of N:"))

b=[int(i) for i in input().split()[:a]] #Accept numbers till integer N. and convert into list

mi_n=min(b) #Find smallest number from list
ma_x=max(b)  #Find largest number from list

indx_min=b.index(mi_n) #find index of minimum number 
indx_max=b.index(ma_x) #find index of maximum number

print("Largest integer=",ma_x,"Position of Largest integer=",indx_max+1)
print("Smallest integer=",mi_n,"Position of smallest integer=",indx_min+1)
