import cv2
import numpy as np

def segment_red_object(img_path):
    # Cargar la imagen
    img = cv2.imread(img_path)
    if img is None:
        print(f"No se pudo cargar la imagen: {img_path}")
        return

    # Convertir la imagen a espacio de color HSV
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Definir rangos de color rojo en HSV
    # El rojo tiene un valor de tono alrededor de 0 o 180 grados, pero debes ajustar estos rangos
    lower_red1 = np.array([0, 70, 50])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 70, 50])
    upper_red2 = np.array([180, 255, 255])

    # Crear máscaras para segmentar el rojo
    mask1 = cv2.inRange(hsv_img, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv_img, lower_red2, upper_red2)
    mask = cv2.bitwise_or(mask1, mask2)

    # Opcional: aplicar una dilatación y erosión para eliminar pequeños ruidos
    mask = cv2.dilate(mask, None, iterations=2)
    mask = cv2.erode(mask, None, iterations=2)

    # Aplicar la máscara a la imagen original
    segmented_img = cv2.bitwise_and(img, img, mask=mask)

    # Mostrar la imagen original y la segmentada
    cv2.imshow('Original', img)
    cv2.imshow('Segmented', segmented_img)
    
    cv2.waitKey(30000)  # Espera hasta que se presione una tecla
    cv2.destroyAllWindows()

# Ejemplo de uso
segment_red_object('data/208II3-850x567.jpg')