import tensorflow as tf

#create tensors

t1 = tf.Variable(101)

print(t1)

print("**********")

print(type(t1))

print("**********")

print(t1.shape) 

print("**********")

print(t1.numpy())

print("**********")

t2 = tf.Variable([3, 5])

print(t2)

print("**********")

print(t2.shape) 

print("**********")

print(t2.numpy())

print("**********")

t3 = tf.Variable([[5, 9], [22, 43]])

print(t3)

print("**********")

print(t3.shape) 

print("**********")

print(t3.numpy())

"""
<tf.Variable 'Variable:0' shape=() dtype=int32, numpy=101>
**********
<class 'tensorflow.python.ops.resource_variable_ops.ResourceVariable'>
**********
()
**********
101
**********
<tf.Variable 'Variable:0' shape=(2,) dtype=int32, numpy=array([3, 5], dtype=int32)>
**********
(2,)
**********
[3 5]
**********
<tf.Variable 'Variable:0' shape=(2, 2) dtype=int32, numpy=
array([[ 5,  9],
       [22, 43]], dtype=int32)>
**********
(2, 2)
**********
[[ 5  9]
 [22 43]]
"""
