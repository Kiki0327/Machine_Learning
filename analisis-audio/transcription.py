# Librerias
import warnings
warnings.filterwarnings('ignore')
import whisper
import os
from datetime import *

def process_transcripcion(path=str, model_name=str):
    """
    Función para transcribir audios.

    Arg:
        path: Ruta en donde se encuentran los audios (archivos con extensión .mp3).
        model_name: Modelo que desea utilizar, las opciones son tiny, base, small, medium, large. 
                    Tenga en cuenta que dependiendo del modelo que eliga la demanda computacional podria ser mayor.

    return:
        Archivo txt con la transcripción del audio.
    """

    # Definiendo ruta y archivos en la ruta
    dirs = os.listdir(path=path)
    dirs = [path+x for x in dirs]
    dirs = [x for x in dirs if x.endswith('.mp3')]
    print(f'Cantidad de archivos:{len(dirs)} \nPrimeros cinco archivos:\n{dirs[:5]}')

    # Cargando modelo IA experto en speech to text
    model = whisper.load_model(model_name)

    # Transcribiendo
    time1 = datetime.now()
    result = model.transcribe(dirs[0])
    time2 = datetime.now()
    print(f'Tiempo de ejecución: {time2 - time1}')

    # Guardando la transcripción
    with open(f"transcriptions/transcription_{model_name}.txt", "w", encoding="utf-8") as file:
        file.write(result['text'])
        print('Transcripción guardada con exito')