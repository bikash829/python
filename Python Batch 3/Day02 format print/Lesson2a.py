a= 5
b=3.2
c= "Hello"

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

p, q, r = 56, 34.2, "Hi"

print (p,q,r)
print("p = %s and q=%s and r=%s" % (p,q,r))

print("p = {0} and q={1} and r={2}".format(p,q,r))
print("p = {2} and q={0} and r={1}".format(p,q,r))
print("p = {} and q={} and r={}".format(p,q,r))

print("p = " + str(p) + " and q= " + str(q) + " and r= " +r)
print("We love {}".format("Nova"))

age = 13
message = "Happy Yeaaaaasin " + str(age) + "th Birthday!"
print(message)