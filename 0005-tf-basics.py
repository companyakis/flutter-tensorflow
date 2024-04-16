#slicing

t1 = tf.Variable([[3, 4, 5, 21], [999, 888, 777, 666], [2000, 2010, 2020, 1990]], dtype = tf.float32)

t2 = t1[1][2]

print(t2.numpy()) #777.0
