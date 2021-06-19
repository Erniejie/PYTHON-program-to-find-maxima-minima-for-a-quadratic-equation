#find maxima minima for a quadratic equation
#Computer Pogramming Tutor, 9th June 2021

# x^2 -2x + 1 =0 as  1-2 1

eqco =input("Enter The Coefficients of  Quadratic Equation:")
coef =list(map(float,eqco.split()))
defe =[]

# Derivating Loop Power of x = length -1-k for k=0 => power =2

for k in range(0,len(coef)):
    # Checking the Power of X if it is 0
    if (len(coef)-k-1!=0):
        defe.append((len(coef)-k-1)*coef[k])
print ("After Differentiation the Equation:" +str(defe[0])+"x%+f"%(defe[1]))

mai = float(-1*defe[1])/defe[0]
if (coef[0])>=0:
    print("The Minima of Given Equation is at x=%f"%mai)
else:
    print("The Maxima of Given Equation is at x=%f"%mai)
    
    

