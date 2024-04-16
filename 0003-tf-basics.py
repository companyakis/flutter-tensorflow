#specify data type

t1 = tf.Variable([[3, 4, 5], [999, 888, 777], [2000, 2010, 2020]], dtype = tf.float32)

print(t1.numpy())

print("**********")

t2 = tf.constant(-500, dtype = tf.float64)

print(t2.numpy())

"""
[[   3.    4.    5.]
 [ 999.  888.  777.]
 [2000. 2010. 2020.]]
**********
-500.0
"""
