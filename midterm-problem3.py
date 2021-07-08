"""
Write a Python function, twoQuadratics, that takes in two sets of coefficients 
and x-values and prints the sum of the results of evaluating two quadratic 
equations. It does not do anything else. 
"""
def evalQuadratic(a, b, c, x):
   '''
   a, b, c: numerical values for the coefficients of a quadratic equation
   x: numerical value at which to evaluate the quadratic.
   '''
   return a*x*x + b*x + c

def twoQuadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    '''
    a1, b1, c1: one set of coefficients of a quadratic equation
    a2, b2, c2: another set of coefficients of a quadratic equation
    x1, x2: values at which to evaluate the quadratics
    '''
    print (evalQuadratic(a1, b1, c1, x1) + evalQuadratic(a2, b2, c2, x2))  