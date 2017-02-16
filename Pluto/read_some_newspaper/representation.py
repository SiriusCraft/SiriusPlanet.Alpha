import numpy
from numpy import shape

f=open('20ng-train-all-terms.txt',"r")
lines=f.readlines()

f2=open('5000.txt',"r")
words=f2.readlines()
print(shape(words))

#representation method 1: use raw_counts
vector=numpy.zeros((11293,5000),dtype=int)
i=0
for word in words:
    word = word.strip("\n")
    j=0
    for line in lines:
        vector[j][i]=line.count(word)
        j+=1
    i=i+1
print("vector 1 computed")
print(shape(vector))


#representation method 2: use binary indicator
vector2=numpy.zeros((11293,5000),dtype=int)
for i in range(5000):
    for j in range(11293):
        if vector[j][i]==0:
            vector2[j][i]=1
        else:
            vector2[j][i] = vector[j][i]
print("vector 2 computed")

#representation method 3: use log-normalized
vector3=numpy.zeros((11293,5000))
for i in range(5000):
    for j in range(11293):
        vector3[j][i]=numpy.log(vector[j][i]+1)
print("vector 3 computed")

numpy.savetxt('vector.csv',vector,fmt='%.0e',delimiter=',')
numpy.savetxt('vector2.csv',vector2,fmt='%.0e',delimiter=',')
numpy.savetxt('vector3.csv',vector3,fmt='%.3e',delimiter=',')