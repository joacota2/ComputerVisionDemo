import numpy as np
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import os

# Cargar el modelo MobileNetV2 preentrenado
model = MobileNetV2(weights='imagenet')

def classify_image(img_path):
    # Cargar y preparar la imagen
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array_expanded_dims = np.expand_dims(img_array, axis=0)
    processed_img = preprocess_input(img_array_expanded_dims)

    # Realizar la clasificación
    predictions = model.predict(processed_img)

    # Decodificar las predicciones
    results = decode_predictions(predictions, top=3)[0]
    for result in results:
        print(f'{result[1]}: {result[2]*100:.2f}%')


#classify_image('data/208II3-850x567.jpg')

image_directory = 'data/'
for filename in os.listdir(image_directory):
    img_path = os.path.join(image_directory, filename)
    # Verificar si el archivo es una imagen (por ejemplo, .jpg o .png)
    if img_path.lower().endswith(('.png', '.jpg', '.jpeg')):
        print("\n",img_path)
        classify_image(img_path)