import tensorflow as tf
import numpy
from numpy import shape
import csv

'''with open('vector.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    rows = [row for row in reader]
train_samples = [row[0:5000] for row in rows]
train_samples = numpy.array(train_samples, dtype=float)
print(shape(train_samples))'''

f = open('20ng-train-all-terms.txt', "r")
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

y_label = numpy.zeros((11293, 20))
j = 0
counter = cate_num[0]
for i in range(11293):
    if i <= counter:
        y_label[i][j] = 1
    else:
        counter += cate_num[j + 1]
        j += 1
        y_label[i][j] = 1
# print(shape(y_label))


f2 = open('5000.txt', "r")
words = f2.readlines()
print(shape(words))

# representation method 1: use raw_counts
vector = numpy.zeros((11293, 5000), dtype=int)
i = 0
for word in words:
    word = word.strip("\n")
    j = 0
    for line in lines:
        vector[j][i] = line.count(word)
        j += 1
    i = i + 1
print("vector 1 computed")
print(shape(vector))

data = numpy.concatenate((vector, y_label), axis=1)
numpy.random.shuffle(data)
validata = data[0:1129]
print(shape(validata))
traindata = data[1129:11293]
print(shape(traindata))
train_data = traindata[:, 0:5000]
train_label = traindata[:, 5000:5020]
vali_data = traindata[:, 0:5000]
vali_label = traindata[:, 5000:5020]
print(shape(train_label))

x = tf.placeholder(tf.float32, [None, 5000])
y = tf.placeholder(tf.float32, [None, 20])

w = tf.get_variable('w', shape=[5000, 20], dtype=tf.float32)
b = tf.get_variable('b', shape=[20], dtype=tf.float32)

logits = tf.matmul(x, w) + b
probs = tf.sigmoid(logits)
# predictions=tf.argmax(logits,1)

loss = tf.nn.softmax_cross_entropy_with_logits(logits, y)
cost = tf.reduce_mean(loss)
# predictions=tf.argmax(logits,1)

# correct_pred = tf.equal(predictions,tf.argmax(y, 1))
correct_pred = tf.equal(tf.argmax(probs, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

optimizer = tf.train.GradientDescentOptimizer(0.01)
train_op = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.initialize_all_variables())

costs = []

for epoch in range(300):
    start = 0
    end = 0
    for i in range(int((11293 - 1129) / 100)):
        end = start + 100
        c, _ = sess.run([cost, train_op],
                        feed_dict={x: train_data[start:end],
                                   y: train_label[start:end]})
        # print(c)
        costs.append(c)
        start += 100

    acc = sess.run([accuracy],
                   feed_dict={x: vali_data[start:start + 1000],
                              y: vali_label[start:start + 1000]})
    print("epoch:")
    print(epoch)
    print("accuracy on validation set")
    print(acc)

numpy.savetxt('cost1.csv', costs, fmt='%.2e', delimiter=',')
sess.close()

# calculate the accuracy using the second representation
vector2 = numpy.zeros((11293, 5000), dtype=int)
for i in range(5000):
    for j in range(11293):
        if vector[j][i] == 0:
            vector2[j][i] = 1
        else:
            vector2[j][i] = vector[j][i]
print("vector 2 computed")

data = numpy.concatenate((vector, y_label), axis=1)
numpy.random.shuffle(data)
validata = data[0:1129]
print(shape(validata))
traindata = data[1129:11293]
print(shape(traindata))
train_data = traindata[:, 0:5000]
train_label = traindata[:, 5000:5020]
vali_data = traindata[:, 0:5000]
vali_label = traindata[:, 5000:5020]
print(shape(train_label))

sess = tf.Session()
sess.run(tf.initialize_all_variables())

costs2 = []

for epoch in range(300):
    start = 0
    end = 0
    for i in range(int((11293 - 1129) / 100)):
        end = start + 100
        c, _ = sess.run([cost, train_op],
                        {x: train_data[start:end], y: train_label[start:end]})
        # print(c)
        costs2.append(c)
        start += 100

    acc = sess.run([accuracy],
                   {x: vali_data[start:start + 1000], y: vali_label[start:start + 1000]})
    print("epoch:")
    print(epoch)
    print("accuracy on validation set")
    print(acc)

numpy.savetxt('cost2.csv', costs2, fmt='%.2e', delimiter=',')
sess.close()

# calculate the accuracy using the third representation
vector3 = numpy.zeros((11293, 5000))
for i in range(5000):
    for j in range(11293):
        vector3[j][i] = numpy.log(vector[j][i] + 1)
print("vector 3 computed")

data = numpy.concatenate((vector, y_label), axis=1)
numpy.random.shuffle(data)
validata = data[0:1129]
print(shape(validata))
traindata = data[1129:11293]
print(shape(traindata))
train_data = traindata[:, 0:5000]
train_label = traindata[:, 5000:5020]
vali_data = traindata[:, 0:5000]
vali_label = traindata[:, 5000:5020]
print(shape(train_label))

sess = tf.Session()
sess.run(tf.initialize_all_variables())

costs3 = []

for epoch in range(300):
    start = 0
    end = 0
    for i in range(int((11293 - 1129) / 100)):
        end = start + 100
        c, _ = sess.run([cost, train_op],
                        {x: train_data[start:end], y: train_label[start:end]})
        # print(c)
        costs3.append(c)
        start += 100

    acc = sess.run([accuracy],
                   {x: vali_data[start:start + 1000], y: vali_label[start:start + 1000]})
    print("epoch:")
    print(epoch)
    print("accuracy on validation set")
    print(acc)

numpy.savetxt('cost3.csv', costs3, fmt='%.2e', delimiter=',')
sess.close()
