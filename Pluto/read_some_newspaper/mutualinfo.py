import sklearn
import numpy
import math

from numpy import shape


f=open('/Users/SiriusR/Documents/ee511/read_some_newspaper/20ng-train-all-terms.txt',"r")
lines=f.readlines()
line0=lines[0].split()
category=line0[0]
cate_num=numpy.zeros(20)
dictionary=['a']
j=0

groups=['alt.atheism']
#calculate newsgroup
for line in lines:
    strs=line.split()
    if category == strs[0]:
        cate_num[j]+=1
    else:
        category=strs[0]
        j+=1
        cate_num[j]+=1
        groups.append(category)
    #for i in strs:
print(cate_num)
prob_y=cate_num/11293
#print(prob_y)
print(groups)

f2=open('new.txt',"r")
lines2=f2.readlines()
print(shape(lines2))

mutual_info=numpy.zeros(shape(lines2))
#calculate frequency and mutual information
counter=0
for word in lines2:
    word=word.strip("\n")
    #print(word)
    #print(word)
    start=0
    x_all=0
    prob_x_y = numpy.zeros(20)
    prob_x2_y = numpy.zeros(20)
    for i in range(20):
        x_y=0
        end=int(start+cate_num[i])
        for line in lines[start:end]:
            if word in line:
                x_y+=1
        x_all=x_all+x_y
        prob_x_y[i]=(float(x_y+1))/(11293+20)
        prob_x2_y[i] = (float(cate_num[i] - x_y+1)) / (11293+20)
        start=int(start+cate_num[i])
    prob_x=float(x_all)/11293
    #print(x_all)

    for j in range(20):
        mutual_info[counter]=mutual_info[counter]+prob_x_y[j]*numpy.log2(prob_x_y[j]/(prob_x*prob_y[j]))
    for j in range(20):
        mutual_info[counter]=mutual_info[counter]+prob_x2_y[j]*numpy.log2(prob_x2_y[j]/((1-prob_x)*prob_y[j]))
    #print(mutual_info[counter])
    counter+=1
    if counter % 1000 ==0:
        print(counter)
        #print(mutual_info)
fg = open('mutualinfo.txt', "wb")
fg.writelines(["%s\n" % item for item in mutual_info])


