import sklearn
import numpy
import math

from numpy import shape

f = open('/Users/SiriusR/Documents/ee511/hw3/20ng-train-all-terms.txt', "r")
lines = f.readlines()
line0 = lines[0].split()
category = line0[0]
cate_num = numpy.zeros(20)
dictionary = ['a']
j = 0

groups = ['alt.atheism']
# calculate newsgroup
for line in lines:
    strs = line.split()
    if category == strs[0]:
        cate_num[j] += 1
    else:
        category = strs[0]
        j += 1
        cate_num[j] += 1
        groups.append(category)
        # for i in strs:
print(cate_num)
prob_y = cate_num / 11293
# print(prob_y)
print(groups)

number = 0
# construct dictionary
for line in lines:
    number = number + 1
    strs = line.split()
    # print(number)
    for i in strs:
        if i not in dictionary:
            dictionary.append(i)
# print(dictionary)
fg = open('new.txt', "wb")
fg.writelines(["%s\n" % item for item in dictionary])

print(shape(dictionary))
mutual_info = numpy.zeros(shape(dictionary))
