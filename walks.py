from itertools import product
import math

def krp(k):
	r = round(k/math.log(k))
	p = 1/r
	return k,r,p

def weighted_walks(k,r,p,n):
	an = 0
	k_walks = product(range(int(k)),repeat=int((n/2)+1))
	r_walks = product(range(int(r)),repeat=int(n/2))
	all_walks = product(k_walks,r_walks)
	for (kw,rw) in all_walks:
		t = unique_edges(kw,rw,n)
		an += p**t
	return an

def unique_edges(kw,rw,n):
	edges = []
	for i in range(n):
		if i%2==0:
			current_edge = (kw[i/2],rw[i/2])
		else:
			current_edge = (kw[(i+1)/2],rw[(i-1)/2])
		if (current_edge in edges) == False:
			edges.append(current_edge)
	return len(edges)

def binomial(b,a):
	return math.factorial(int(b))/(math.factorial(int(a))*math.factorial(int(b-a)))

def sum_lower_bound(k,r,p,n):
	bound = 0
	for t in range(1,2+n/2):
		bound += binomial(k,t)*r*bnt_val(n,t)*p**t
	return bound

def one_lower_bound(k,r,p,n):
	bound = binomial(k,1+n/2)*r*bnt_val(n,1+n/2)*p**(n/2+1)
	return bound

def bnt_val(n,t):
	bnt = 0
	for j in range(t):
		bnt += (-1)**j*binomial(t,j)*(t-j)**(1+n/2)
	return bnt


a4s = []
b4s = []
c4s = []

for k in range(10,201,10):
	k,r,p = krp(k)
	a4 = weighted_walks(k,r,p,4)
	b4 = sum_lower_bound(k,r,p,4)
	c4 = one_lower_bound(k,r,p,4)
	print str(k) + ' : ' + str([a4,b4,c4])




