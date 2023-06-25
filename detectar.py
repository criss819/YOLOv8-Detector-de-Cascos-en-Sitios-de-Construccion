from ultralytics import YOLO
import argparse

parser = argparse.ArgumentParser();
parser.add_argument("-modelo", type=str, help="Ingresa nombre del modelo (ubicacion) entrenado entre comillas");
parser.add_argument("-fuente", type=str, help="Ingresa nombre de la imagen/video (ubicacion) para detectar o 1 si deseas usar la cam, todo entre comillas");
args = parser.parse_args();

model = YOLO(args.modelo)

model.predict(source=args.fuente, show=True, save=True, conf=0.5)




