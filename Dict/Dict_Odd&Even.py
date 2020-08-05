a="apple,banana"
s=a.split()
#print(s)

##totalist={}
##for x in s:
##    totalist[x]=s.count(x)
##print(totalist)

mytotalist={x:s.count(x) for x in s}
print (mytotalist)
