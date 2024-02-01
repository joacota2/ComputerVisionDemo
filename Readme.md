
---

# Proyecto de Visión por Computadora

Este proyecto demuestra tres aspectos fundamentales de la visión por computadora: detección de objetos, segmentación de imágenes y clasificación de imágenes. Cada uno de estos componentes utiliza diferentes técnicas y herramientas de visión por computadora para procesar y analizar imágenes.

## Componentes del Proyecto

- **Detección de Objetos**: Detecta y marca objetos dentro de una imagen, como rostros humanos.
- **Segmentación de Imágenes**: Separa y destaca partes específicas de una imagen, como segmentar un coche rojo del fondo.
- **Clasificación de Imágenes**: Clasifica imágenes en categorías predefinidas basándose en su contenido, como diferenciar entre imágenes de gatos y perros.

## Requisitos

Este proyecto requiere Python 3.x y varias bibliotecas de visión por computadora y procesamiento de imágenes, incluidas OpenCV, TensorFlow y Keras. Para la aceleración por GPU en tareas de clasificación de imágenes, es posible que necesites una configuración adicional relacionada con CUDA y cuDNN.

### Dependencias Principales

- Python 3.x
- OpenCV
- TensorFlow / Keras
- NumPy

## Configuración del Entorno de Ejecución

### Aceleración por GPU con CUDA

Para aprovechar la aceleración por GPU, asegúrate de tener una tarjeta gráfica compatible con CUDA y de que los controladores de NVIDIA, CUDA Toolkit y cuDNN estén instalados y configurados correctamente en tu sistema.

1. **Controladores de NVIDIA**: Asegúrate de tener instalados los últimos controladores de NVIDIA compatibles con tu GPU.

2. **CUDA Toolkit**: Instala la versión de CUDA Toolkit que sea compatible con la versión de TensorFlow que estás utilizando. Consulta la [tabla de compatibilidad de TensorFlow](https://www.tensorflow.org/install/source#linux) para elegir la versión adecuada.

3. **cuDNN**: Descarga e instala la biblioteca NVIDIA cuDNN compatible con la versión instalada de CUDA Toolkit. Sigue las instrucciones proporcionadas en el [sitio web de NVIDIA](https://developer.nvidia.com/cudnn) para configurar cuDNN.

### Verificación de la Configuración de CUDA

Después de instalar CUDA y cuDNN, verifica que TensorFlow pueda reconocer la GPU ejecutando el siguiente fragmento de código en Python:

```python
import tensorflow as tf

if tf.test.gpu_device_name():
    print('GPU encontrada:', tf.test.gpu_device_name())
else:
    print("GPU no encontrada, utilizando CPU en su lugar.")
```

Si TensorFlow no detecta la GPU, revisa la instalación y configuración de CUDA y cuDNN.

## Instalación

Primero, clona este repositorio en tu máquina local:

```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
```

Luego, crea y activa un entorno virtual (opcional pero recomendado):

```bash
python3 -m venv venv
# En Windows
venv\Scripts\activate
# En macOS y Linux
source venv/bin/activate
```

Instala las dependencias necesarias:

```bash
pip install -r requirements.txt
```

## Uso

### Detección de Objetos

Para ejecutar el ejemplo de detección de objetos:

```bash
python det.py
```

### Segmentación de Imágenes

Para ejecutar el ejemplo de segmentación de imágenes:

```bash
python seg.py
```

### Clasificación de Imágenes

Para ejecutar el ejemplo de clasificación de imágenes:

```bash
python clas.py
```
