
#Write a program to accept an integer N and calculate the sum of its digits. Please note N can have maximum 5 digits.

while True:
    N=input("Enter No")   #Accept Number
    try:
        if len(N)>5:        #N can have maximum 5 digits.
            print("Number should be maximum 5 digit")
            continue
        else:
            sum = 0
            for digit in str(N): #Sum of Digits
                sum =sum + int(digit)
            print("Sum of digits=",sum)  #print Sum
            
    except ValueError:
        print("Enter Number Only")
        continue
