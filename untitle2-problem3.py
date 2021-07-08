monthlyInterestRate = annualInterestRate/12
low = balance/12
high = (balance * (1 + monthlyInterestRate)**12)/12.0


while balance > 0.01:
    monthlyPaymentRate = (high + low)/2                  #bisection search       
    nbalance = balance                                   #reset the balance to the initial balance, defining a new variants as the balance  
    for i in range(1,13):                                #counting 12 times (12 months)
        nbalance = nbalance - monthlyPaymentRate + ((nbalance - monthlyPaymentRate) * monthlyInterestRate)
    if nbalance > 0.01:                                  #if nbalance is higher, assigning low as monthlyPaymentRate   
        low = monthlyPaymentRate
    elif nbalance < -0.01:                               #if nbalance is lower, assigning high as monthlyPaymentRate      
        high = monthlyPaymentRate
    else:
        break
print('Lowest Payment:', round(monthlyPaymentRate, 2))