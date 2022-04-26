    # import the required libraries from Python
import pathlib
import urllib.request 
import os
import time

 
def descarga():
    image_url = "https://sdo.gsfc.nasa.gov/assets/img/latest/latest_1024_HMIIC.jpg"

    # toma la extension
    file_ext = pathlib.Path(image_url).suffix

    # une el nombre con la extension
    picture_filename = "new" + file_ext

    # especificamos donde guardaremos el archivo
    downloads_path = str(pathlib.Path.home() / "public_html/static/images/")

    # junta el nombre, y el path
    picture_path  = os.path.join(downloads_path, picture_filename)

    # guarda la imagen
    urllib.request.urlretrieve(image_url, picture_path)
    
with open('update_time.conf') as f:
    
    contenido = f.readlines()
    
    a = 0
    
    for line in contenido:
        for i in line:
            if i.isdigit() == True:
                a+= int(i)
    
    while True:
        descarga()
        time.sleep(a)
