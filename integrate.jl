s=time()
spl=split(ARGS[1])
expr=spl[1]
a=float(spl[2])
b=float(spl[3])
n=Integer(float(spl[4]))
include_string(string("f(x)=",expr))
l=abs(b-a)
function serie(i)
	return f(a+(i*l)/(n))*(l/n)
end
r=0
for i in 1:n
	r+=serie(i-1)
end
println(r)
println(time()-s)
