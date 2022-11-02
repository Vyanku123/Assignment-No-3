a=int(input("Enter number of circles N:")) #Accept How many circles you want

final=[]

for i in range(0,a):
    l3=[]
    x,y=input("Enter co_ordinates of circles N:").split() #Accept Coordinate of circles
    ap=(x,y)
    l3.append(ap)
    
    b=int(input("Enter radius of each circle r:"))  #Accept radious of the circles
    l3.append(b)
    
    area=3.14*b**2
    l3.append(area)   #Calculate area
    
    final.extend([l3])   #extend all informtion to final variable

#bubble sort
def Sort(sub_li):
 l = len(sub_li)
 for i in range(0, l):
  for j in range(0, l-i-2):
   if (sub_li[j][1] > sub_li[j + 1][1]):
    tempo = sub_li[j]
    sub_li[j]= sub_li[j + 1]
    sub_li[j + 1]= tempo
 return sub_li

result=Sort(final)   #put all information to Sort function
print("circle data and area with increasing order:")
for i in range(0,len(final)):
    print("[co-ordinates,radius,Area]=",result[i])
