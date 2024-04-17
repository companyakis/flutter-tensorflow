#A simple regression model will be here:) 

# our simple data

x = np.array([-2.0, -1.0, 0.0, 1.5, 2.0, 3.0, 4.0, 5.0])

y = np.array([-5.0, -2.0, 1.0, 5.5, 7.0, 10.0, 13.0, 16.0])

#let's create the model

model = keras.Sequential([keras.layers.Dense(units = 1, input_shape = [1])])

model.compile(optimizer = 'sgd', loss = 'mean_squared_error')
