from time import time
import numpy as np
from pick import pick

# Functions

def f(x):
	return eval(function_string)
vf=np.vectorize(f)

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
	space=np.linspace(start,end,j)
	y=vf(space)
	for i in space:
		for l in range(k):
			if np.random.uniform(0.,max(y))<=f(i):
				in_dots+=1
			else:
				out_dots+=1
	return (in_dots/(out_dots+in_dots))*max(y)*(end-start)

def MonteCarlo2(j,k=100):
	in_d=0
	out_d=0
	h=max(vf(np.linspace(start,end,k)))
	p=0
	for i in range(j):
		p=[np.random.uniform(start,end),np.random.uniform(0,h)]
		if p[1]<=f(p[0]):
			in_d+=1
		else:
			out_d+=1
	return (in_d/(out_d+in_d))*h*(end-start)


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
options = ['Riemman sums','Trapezoid Rule','Monte Carlo 1','Monte Carlo 2'] # Lagrange Polynomial Interpolation
method, indexp = pick(options, title)
print('Method Selected: %s'%(method))

# Riemann sums

if (method=='Riemman sums'):
	n=int(input('Number of partitions for the Riemann sums: '))
	print('')
	t1=time()
	print('Left Riemann Sums:  %f'%(LeftRiemannSums(n)))
	print('Right Riemann Sums: %f'%(RightRiemannSums(n)))
	print('Total calculation time: %f'%(time()-t1))

# Trapezoid Rule

if (method=='Trapezoid Rule'):
	n=int(input('Number of partitions for the Trapezoid Rule: '))
	print('')
	t1=time()
	print('Result: %f'%(TrapezoidalSums(n)))
	print('Total calculation time: %f'%(time()-t1))

# Monte Carlo 1

if (method=='Monte Carlo 1'):
	n=int(input('Number of partitions for Monte Carlo: '))
	m=int(input('Number of points per partition: '))
	print('')
	t1=time()
	print('Result: %f'%(MonteCarlo1(n,m)))
	print('Total calculation time: %f'%(time()-t1))

# Monte Carlo 2

if (method=='Monte Carlo 2'):
	n=int(input('Number of dots for Monte Carlo: '))
	print('')
	t1=time()
	print('Result: %f'%(MonteCarlo2(n)))
	print('Total calculation time: %f'%(time()-t1))

