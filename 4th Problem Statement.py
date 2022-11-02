#Write a program to accept 5 digit integer N and calculate the sum of its first and fifth digit.

while True:
    N=input("Enter No: ")   #Accept Number 
    try: 
        if len(N)==5:  #Check number is only 5 digit
            
            first_digit = int(N[0])  #First Digit
            last_digit = int(N[-1])  #Last Digit
            
            addition = first_digit + last_digit  #Add first and last digit

            print("Addition of first and last digit is: ",addition) #Print that number
            
        else:
            print("Enter only 5 digit Number") #if number is not 5 digit
            
    except ValueError:
        print("Enter Number Only")
        continue
            
