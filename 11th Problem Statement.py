#Write a program to accept cardinality of set A as N, and cardinality of set B as M. Then accept elements of set A and set B.
#Generate set C which is union of set A and set B, set D which is intersection set of set A and Set B.
#Print set A, B, C, D, Cardinality of set C, Cardinality of set D.

N=int(input("Enter cardinality of set A:")) #cardinality of a set is the total number of unique elements in a set.
M=int(input("Enter cardinality of set b:"))

a=set([int(i) for i in input("Enter set A:").split()[:N]]) #Enter all elements for set A
b=set([int(i) for i in input("Enter set B: ").split()[:M]])  #Enter all elements for set B

c=a.union(b) #A union B
d=a.intersection(b) #A intersection B

print("set a=",a)
print("set b=",b)

print("set c=",c ,"cardinality of set c:",len(c))  #Print Cardinality for sec C
print("set d=",d ,"cardinality of set c:",len(d))  #Print Cardinality for sec D
