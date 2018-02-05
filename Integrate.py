from time import time
from pick import pick

# Functions

def f(x):
	return eval(function_string)

def LeftRiemannSums(j):
	sum=0
	for i in range(j):
		sum+=f((i/j)*(end-start)+start)*((end-start)/j)
#		print(sum)
	return sum
def RightRiemannSums(j):
	sum=0
	for i in range(1,j+1,1):
		sum+=f((i/j)*(end-start)+start)*((end-start)/j)
#		print(sum)
	return sum

def TrapezoidalSums(j):
	sum=0
	for i in range(j):
		sum+=0.5*( f((i/j)*(end-start)+start) + f(((i+1)/j)*(end-start)+start) )*((end-start)/(j))
#		print(sum)
	return sum

def MonteCarlo1(j,k): # j=number of slots, k=number of points per slot
	in_dots=0
	out_dots=0
	space=linspace(start,end,j)
	y=vf(space)
	for i in space:
		for l in range(k):
			if random.uniform(0.,max(y))<=f(i):
				in_dots+=1
			else:
				out_dots+=1
	return (in_dots/(out_dots+in_dots))*max(y)*(end-start)

def MonteCarlo2(j,k=100):
	in_d=0
	out_d=0
	h=max(vf(linspace(start,end,k)))
	p=0
	for i in range(j):
		p=[random.uniform(start,end),np.random.uniform(0,h)]
		if p[1]<=f(p[0]):
			in_d+=1
		else:
			out_d+=1
	return (in_d/(out_d+in_d))*h*(end-start)

def exclude(ex,n,strt=0,stp=1):
	'''
	Gives an Integer iterator [0,ex)U(ex,n)
	'''
	return [q for q in range(strt,n,stp) if q!=ex]

def PC(j):
	'''
	Polinomial Coefficient
	'''
	p=1
	for m in exclude(j,k):
		p*=(x-xp[m])/(xp[j]-xp[m])
	return p

def LS():
	'''
	Lagrange Sums
	'''
	p=0
	for i in range(k):
		p+=yp[i]*PC(i)
	return p

# Inputs

print("Demo to numerically integrate numpy real valued functions. \nAll functions have to be written with the x variable. ")
function_string=input("Function: ")
start=float(input("From: "))
end=float(input("To: "))
if (start==end):
	print('\n\n',0)
	quit()

# Pick Method

title = 'Select an Integration Method: '
options = ['Riemman sums','Trapezoid Rule','Monte Carlo 1','Monte Carlo 2',"SymPy Symbolic Integration", "Lagrange Polynomial Interpolation"]
method, indexp = pick(options, title)
print('Method Selected: %s'%(method))

# Riemann sums

if (method=='Riemman sums'):
	from numpy import *
	n=int(input('Number of partitions for the Riemann sums: '))
	print('')
	t1=time()
	print('Left Riemann Sums:  %f'%(LeftRiemannSums(n)))
	print('Right Riemann Sums: %f'%(RightRiemannSums(n)))
	print('Total calculation time: %f'%(time()-t1))

# Trapezoid Rule

if (method=='Trapezoid Rule'):
	from numpy import *
	n=int(input('Number of partitions for the Trapezoid Rule: '))
	print('')
	t1=time()
	print('Result: %f'%(TrapezoidalSums(n)))
	print('Total calculation time: %f'%(time()-t1))

# Monte Carlo 1

if (method=='Monte Carlo 1'):
	from numpy import *
	vf=vectorize(f)
	n=int(input('Number of partitions for Monte Carlo: '))
	m=int(input('Number of points per partition: '))
	print('')
	t1=time()
	print('Result: %f'%(MonteCarlo1(n,m)))
	print('Total calculation time: %f'%(time()-t1))

# Monte Carlo 2

if (method=='Monte Carlo 2'):
	from numpy import *
	vf=vectorize(f)
	n=int(input('Number of dots for Monte Carlo: '))
	print('')
	t1=time()
	print('Result: %f'%(MonteCarlo2(n)))
	print('Total calculation time: %f'%(time()-t1))

# SymPy

if (method=="SymPy Symbolic Integration"):
	from sympy import *
	x=symbols('x')
	g=eval(function_string)
	t1=time()
	G=integrate(g,x)
	print("Indefinite integral",G)
	print("Definite integral",G.subs(x,end)-G.subs(x,start))
	print("Total calculation time: %f"%(time()-t1))

# Lagrange

if (method=="Lagrange Polynomial Interpolation"):
	from sympy import *
	x=symbols('x')
	g=eval(function_string)
	t1=time()
	
	k=int(input("Degree of each Lagrange Polynomial Interpolation: "))
	from numpy import linspace,vectorize
	xp=linspace(start,end,k+1)
	def gfunc(x):
		return eval(str(g))
	vgfunc=vectorize(gfunc)
	yp=vgfunc(xp)
	pol_string=str(expand(LS()))
	def pol(x):
		return eval(pol_string)
	import matplotlib.pyplot as plt
	space=linspace(start,end,100)
	plt.figure()
	plt.plot(space,vgfunc(linspace(start,end,100)))
	plt.plot(space,list(map(pol,space)))
	plt.scatter(xp,list(map(pol,xp)))
	plt.show()
