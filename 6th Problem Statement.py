#Accept cost price(CP) and Selling price(SP) of an item. Calculate the ammount of PROFIT/LOSS made by the seller and print the
#CP=500, SP=700 PROFIT=200
#CP=500, SP=450 LOSS=50  

while True:
    a=int(input("Enter cost price:"))  #Accept Cost prize
    b=int(input("Enter selling price:"))    #Accept Selling prize
    try:
        if a<0 or b<0:        #Check value must be positive
            print("Enter positive value")
            continue
        else:
            if a<b:
                print("profit is :",b-a)  #For Profit
                break
            else:
                print("loss is :",a-b)   #For loss
                break
            
    except ValueError:
        print("Enter Number Only")
        continue
