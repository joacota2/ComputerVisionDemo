import cv2

def detect_faces(img_path):
    # Cargar el clasificador en cascada para caras
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Cargar la imagen
    img = cv2.imread(img_path)
    if img is None:
        print(f"No se pudo cargar la imagen: {img_path}")
        return

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detectar caras en la imagen
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Dibujar rectángulos alrededor de las caras detectadas
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Mostrar la imagen con las caras detectadas
    cv2.imshow('Faces', img)

    # Espera 10 segundos (10000 milisegundos) antes de cerrar la ventana
    cv2.waitKey(30000)  # 10000 milisegundos = 10 segundos
    
    cv2.destroyAllWindows()

# Ejemplo de uso
detect_faces('data/THE-FACES-RARE-SHOT.png')