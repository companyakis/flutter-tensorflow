model_file = "simplepredictionmodel.h5"

tf.keras.models.save_model(model, model_file)

lite_converter = tf.lite.TFLiteConverter.from_keras_model(model)

tf_model = lite_converter.convert()

open("simplepredictionmodel.tflite", "wb").write(tf_model)
