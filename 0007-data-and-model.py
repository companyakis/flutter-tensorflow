# data:)

x = np.array([2 * i - 1 for i in range(10)])

y = np.array([3 * j + 5 for j in range(10)])

print("x values: ", x)

print("y values: ", y)

"""
x values:  [-1  1  3  5  7  9 11 13 15 17]
y values:  [ 5  8 11 14 17 20 23 26 29 32]

"""

#let's create the model

model = keras.Sequential([keras.layers.Dense(units = 1, input_shape = [1])])

model.compile(optimizer = 'sgd', loss = 'mean_squared_error')
