#train the model

model.fit(x, y, epochs = 500)

#model prediction

pred1 = model.predict([87])

print("Prediction: ", pred1) # Prediction:  [[138.29523]]

"""

Epoch 495/500
1/1 [==============================] - 0s 16ms/step - loss: 0.0161
Epoch 496/500
1/1 [==============================] - 0s 11ms/step - loss: 0.0159
Epoch 497/500
1/1 [==============================] - 0s 12ms/step - loss: 0.0157
Epoch 498/500
1/1 [==============================] - 0s 12ms/step - loss: 0.0155
Epoch 499/500
1/1 [==============================] - 0s 13ms/step - loss: 0.0153
Epoch 500/500
1/1 [==============================] - 0s 10ms/step - loss: 0.0150

"""
