"""
Now write a program that calculates the minimum fixed monthly payment needed 
in order pay off a credit card balance within 12 months. By a fixed monthly 
payment, we mean a single number which does not change each month, but instead 
is a constant amount that will be paid each month.
In this problem, we will not be dealing with a minimum monthly payment rate.

Assume that the interest is compounded monthly according to the balance at the 
end of the month (after the payment for that month is made). The monthly 
payment must be a multiple of $10 and is the same for all months. Notice that 
it is possible for the balance to become negative using this payment 
scheme, which is okay. 
"""
payment = 0                                                        #guessing the payment and starting with $0 payments per month
while balance > 0 :                                                #using while loops to find  found a good minimum monthly payment value 
    newbalance = balance                                            #reset the balance to the initial balance, defining a new variants as the balance  
    for i in range(1,13):                                          #counting 12 times (12 months) 
        newbalance=(newbalance-payment)*(1+annualInterestRate/12)  #counting  balance 
    if newbalance > 0:                                             #if payment cannot meet the balance, payment +$10   
        payment += 10        
    else:                                                          #or stop the program                         
        break
print ("Lowest Payment:", str(guess))