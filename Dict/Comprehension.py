#create a dict that contains name as key and count of value as element from below string
a="apple,banana,mango,strawberry,apple,strawberry"
s=a.split(",")
print(s)

##totdict={}
##for x in s:
##    totdict[x]=s.count(x)
##print(totdict)

mytotlist={x:s.count(x) for x in s}
print(mytotlist)
