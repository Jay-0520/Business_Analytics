from scipy import optimize


# a python script to optimize the algebra problem
'''
Maximize 150*R + 160*N
    subject to
    4*R + 5*N <= 5610
    1.5*R + 2.0*N <= 2200
    1.0*R + 0.8*N <= 1200
    R, N = integer
    R, N >= 0
 
'''

def objective(params):
    R, N = params
    
    # add a negative sign to find the minimum
    return -(135*R + 170*N) 

def constraint1(params):
    R, N = params
    return 5610- 4*R - 5*N

def constraint2(params):
    R, N = params
    return 2200- 1.5*R - 2.0*N

def constraint3(params):
    R, N = params
    return 1200- 1.0*R - 0.8*N


b = [0,100000]
bnds = [b,b]

con1 = {'type': 'ineq', 'fun': constraint1}
con2 = {'type': 'ineq', 'fun': constraint2}
con3 = {'type': 'ineq', 'fun': constraint3}

cons=[con1,con2,con3]

w0 = [1,1]

result = optimize.minimize(objective, w0, method="SLSQP",\
                           bounds= bnds, 
                           constraints = cons)
print(result)

'''
 fun: -190299.99999957348
     jac: array([-135., -170.,    0.])
 message: 'Optimization terminated successfully.'
    nfev: 37
     nit: 10
    njev: 9
  status: 0
 success: True
       x: array([440., 770.])
'''



