li=[1,-8,2,-6,4,-2]
pos=0
neg=0
for num in li:
 if num >= 0:
  pos +=1
else:
  neg +=1
print('Positive numbers:',pos)
print('Positive numbers:',neg)
print(sum(li))


