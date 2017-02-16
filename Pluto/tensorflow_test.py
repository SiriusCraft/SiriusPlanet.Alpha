import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib as plt

data = pd.read_csv('http://statweb.stanford.edu/~tibs/ElemStatLearn/datasets/zip.train.gz', compression='gzip',
                   header=None, sep=' ')
data.head()
tf.reset_default_graph()
# define placeholder
x = tf.placeholder(tf.float32, shape=[None, 256], name='x')
y = tf.placeholder(tf.int32, shape=[None, 256], name='y')

# define variables
w = tf.get_variable('w', shape=[256, 10], dtype=tf.float32)
b = tf.get_variable('b', shape=[10], dtype=tf.float32)

logits = tf.matmul(x, w) + b
probs = tf.sigmoid(logits)
predictions = tf.argmax(logits, 1)

loss = tf.nn.sparse_softmax_cross_entropy_with_logits(logits, y)
cost = tf.reduce_mean(loss)

optimizer = tf.train.GradientDescentOptimizer(0.1)
train_op = optimizer.minimize(cost)

session = tf.Session()

session.run(tf.initialize_all_variables())
# session.run(b)
cost = []
for i in range(1, 100):
    c = session.run([cost, train_op], {x: data.values[:, 1:-1], y: data[0]})
    cost.append(c)
# plt.plot(cost)


preds = session.run(predictions, {x: data.values[:, 1:-1]})
(preds == data[0]).sum() / float(len(data))
