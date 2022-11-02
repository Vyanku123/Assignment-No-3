#Write a program to accept an integer N and generate an integer M which is formed by reversing the digits of N.
#Please note N can have maximum 5 digits. Print the numbers N and M. Compare N with M and print the result.

while True:
    N=input("Enter No: ")  #Accept Number
    try:
        if len(N)>5:        #N can have maximum 5 digits.
            print("Number must be less than 5 digit")
            continue
        else:
            M = 0
            N=int(N) #Convert String to number

            O=N #Store Original number

            while(N > 0):
                a = N % 10 #Taking reminder of the number
                M = M * 10 + a 
                N= N // 10  #the floor division // rounds the result the nearest whole number
                
            print("Original number N is",O) #Print Original Number
            print("Reverse number M is ",M) #print Reverse Number
            
    except ValueError:
        print("Enter Number Only")
        continue
    
    if O>M:   #Compare original number with reverse number
        print(" N is greater than M")
    else:
        print("M is greater then N")
