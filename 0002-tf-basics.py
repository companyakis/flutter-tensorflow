#reassign

t1 = tf.Variable(101)

t1.assign(1001)

print(t1.numpy()) # 1001

#tf constants

c1 = tf.constant(1001)

print(c1.numpy()) #1001
