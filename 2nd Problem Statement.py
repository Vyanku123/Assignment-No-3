#Write a program to accept an integer N and generate an integer M which is formed by reversing the digits of N.
#Please note N can have maximum 5 digits.

while True:
    N=input("Enter No: ")  #Accept Number
    try:
        if len(N)>5:        #N can have maximum 5 digits.
            print("Number must be less than 5 digit")
            continue
        else:
            M = 0
            N=int(N) #Convert String to number

            while(N > 0):
                a = N % 10 #Taking reminder of the number
                M = M * 10 + a 
                N= N // 10  #the floor division // rounds the result the nearest whole number
                
            print("reverse number is ",M) #print Reverse Number      

    except ValueError:
        print("Enter Number Only")
        continue
