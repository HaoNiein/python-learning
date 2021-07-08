"""
Write a program to calculate the credit card balance after one year if a 
person only pays the minimum monthly payment required by the credit card 
company each month.

A summary of the required math is found below:
Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
"""
for k in range(1, 13):                                                         #counting 12 times (12 months) 
    balance = balance *(1-monthlyPaymentRate)*(1+annualInterestRate/12)        #counting  balance 
print ("Remaining balance:", str(round(balance, 2)))
   