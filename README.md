# YOLOv8 Detector de Cascos en Sitios de Construcción!

YOLOv8 es un modelo que se basa en el éxito de las versiones anteriores de YOLO e introduce nuevas características y mejoras para aumentar aún más el rendimiento y la flexibilidad. YOLOv8 está diseñado para ser rápido, preciso y fácil de usar, lo que lo convierte en una excelente opción para una amplia gama de tareas de detección y seguimiento de objetos, segmentación de instancias, clasificación de imágenes y estimación de poses.

Este repositorio brinda un modelo entrenado para la detección de cascos en sitios de construcción, usando una modificación del Hard-Hat Dataset del Harvard Data-Verse (Eliminando algunas clases innecesarias de alrededor de 200 imágenes), en cuanto a la división del dataset, se adoptó una estrategia comúnmente utilizada, dividiendo en conjuntos de entrenamiento y validación, con una proporción del 75% y 25% respectivamente, garantizando una evaluación adecuada del rendimiento del modelo en diferentes escenarios.

Los pasos a seguir para poder iniciar la detección de objetos en videos, imágenes o de una webcam son los siguientes (La creación del entorno asume que Anaconda esté instalado en la computadora):


## Creación y activación de entorno

Para el uso de YOLOv8 se requiere versiones superiores a Python 3.8 y PyTorch 1.7
```
conda create -n yolov8_custom python=3.10
```
```
conda activate yolov8_custom
```

## Instalación de paquetes

```
pip install ultralytics
```
```
pip install argparse
```
## Dataset (Opcional)

Si deseas el dataset modificado, se encuentra en el repositorio, con el formato correcto que pide YOLO.



## Descargar el Modelo Entrenado

El modelo entrenado es [hardhatv2.pt](https://www.mediafire.com/file/64s3qg23nzxkb4i/hardhatv2.rar/file), es necesario para poder detectar los cascos dentro de las construcciones, al ser muy pesado no lo puedo subir al repositorio, sin embargo, si esta el link de descarga.

## Iniciar el Detector

Lo puedes hacer directamente desde el entorno creado, usando este código:
```
yolo task=detect mode=predict model=hardhatv2.pt show=true conf=0.5 source="" save=true
```
En source va el nombre o la ubicación de la imagen/video a detectar, en caso se desee usar una cam, se tendría que poner el numero "0", en caso tengas mas de una cam conectada solo cambia el numero ("1", "2", etc.).

En caso se desee usar Python y argparse, aquí esta el código:
```
from ultralytics import YOLO
import argparse

parser = argparse.ArgumentParser();
parser.add_argument("-modelo", type=str, help="Ingresa nombre del modelo (ubicacion) entrenado entre comillas");
parser.add_argument("-fuente", type=str, help="Ingresa nombre de la imagen/video (ubicacion) para detectar o 1 si deseas usar la cam, todo entre comillas");
args = parser.parse_args();

model = YOLO(args.modelo)

model.predict(source=args.fuente, show=True, save=True, conf=0.5)
```

## Entrenar Modelo (Opcional)

Si deseas entrenar tu mismo el modelo y usar el dataset modificado, se usa este código en el entorno creado:
```
yolo task=detect mode=train epochs=50 data=data.yaml model=yolov8m.pt imgsz=640 batch=8
```
Epochs es la cantidad de veces que se va a analizar datos, aprender de ellos y utilizar estos puntos de aprendizaje para identificar patrones de interés.

Data.yaml es un archivo que se encuentra dentro del dataset modificado, este archivo contiene la ubicación de las imágenes de entrenamiento y validación al igual que las clases que va a aprender.

Si deseas mas información, aquí esta el repositorio principal de [YOLOv8](https://github.com/ultralytics/ultralytics)
