#Write a program to accept a 5 digit integer N and then generates a number M by adding 1 to each digit.

while True:
    N=input("Enter No")   #Accept Number
    try:
        if len(N)==5: #N can have  5 digits.
            l1=[]
            l2=[]
            for i in range(0,len(N)):
                b=int(N[i])
                l1.append(b)   #Seperate that number and appedn in list l1
                
            for i in l1:
                c=i+1
                l2.append(c)#Add 1 into every element of list l1 and append into list l2
            #print(l2)

            for i in range(len(l2)):
                if l2[i]==10:
                    l2[i]=0    #here we replace 10 with 0  ex: l2[i]==10 then we replace with l2[i]=0 
            #print(l2,end="")
                    
            for i in range(0,len(l2)):
                n=l2[i]
                print(l2[i],end="") #we add that number

        else:
            print("Number must be less than 5 digit") #chech where number is 5 digit or not
            continue
    except ValueError:
        print("Enter Number Only")
        continue
