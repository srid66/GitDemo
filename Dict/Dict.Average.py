s={'english':[23,45,56],'maths':[45,54,67],'science':[23,21,11]}
AverageDict={}
for x,y in s.items():
    AverageDict[x].append (sum(y) / float(len(y)))
