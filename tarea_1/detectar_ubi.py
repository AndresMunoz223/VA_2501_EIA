from ultralytics import YOLO
import cv2
from icecream import ic

# import re

# Cargar los modelos
plate_model = YOLO("bestPlate.pt")  # Modelo para detectar la placa
char_model = YOLO("bestSegAll.pt")  # Modelo para segmentar y clasificar caracteres

# Ruta de la imagen
image_path = "placas/00-01-56_001_AAA000.jpg"

# Leer la imagen original
image = cv2.imread(image_path)

# 1. Detectar la placa en la imagen
plate_results = plate_model(image)

# Extraer la región de la placa detectada
for result in plate_results:
    for box in result.boxes:
        # Coordenadas de la placa detectada
        x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
        
        # Recortar la región de la placa
        plate_roi = image[y1:y2, x1:x2]

        # Mostrar la placa detectada (opcional)
        # cv2.imshow("Placa detectada", plate_roi)

        # 2. Detectar y clasificar los caracteres en la placa
        char_results = char_model(plate_roi)

        # Mostrar el texto de la placa en consola
        ic(char_results)

        # Inicializar la placa como un texto vacío
        plate_text = ""

        # Crear una lista para almacenar los caracteres y sus coordenadas
        characters = []

        for char_result in char_results:
            for char_box in char_result.boxes:
                # Coordenadas de cada carácter
                cx1, cy1, cx2, cy2 = map(int, char_box.xyxy[0].tolist())
                
                # Clasificación del carácter
                char_label = char_result.names[int(char_box.cls[0])]

                # Mostrar el texto de la placa en consola
                print(f"Letra: {char_label}")

                # Agregar el carácter y sus coordenadas a la lista
                characters.append({'label': char_label, 'x1': cx1, 'y1': cy1, 'x2': cx2, 'y2': cy2})

        # Ordenar los caracteres según la coordenada 'x1' para asegurarse de que estén en orden de izquierda a derecha
        characters_sorted = sorted(characters, key=lambda x: x['x1'])

        # Dibujar los caracteres ordenados en la imagen original
        for char in characters_sorted:
            # Obtener las coordenadas del cuadro delimitador de cada carácter
            cx1, cy1, cx2, cy2 = char['x1'], char['y1'], char['x2'], char['y2']
            
            # Obtener el texto del carácter
            char_label = char['label']
            
            # Agregar el carácter al texto de la placa
            plate_text += char_label

            # Dibujar el cuadro del carácter en la imagen de la placa
            cv2.rectangle(plate_roi, (cx1, cy1), (cx2, cy2), (0, 255, 0), 2)
            cv2.putText(
                image,
                char_label,
                (x1+cx1, y1+cy1 - 10),  # Ajustar la posición del texto
                cv2.FONT_HERSHEY_SIMPLEX,
                1.0,  # Escala de la fuente
                (0, 255, 0),  # Color verde
                2,  # Grosor del texto
                cv2.LINE_AA,
            )

        # Escribir la placa en la imagen original
        cv2.putText(
            image,
            f"Placa: {plate_text}",
            (x1, y1 - 50),  # Posición de la placa en la imagen original
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2,
            cv2.LINE_AA,
        )

# Mostrar la imagen original con la placa detectada y texto
cv2.imshow("Detección de placas", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
