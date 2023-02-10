from PIL import Image
import pytesseract
import re

"""Validar lenguajes de tesseract
print(pytesseract.get_languages())
"""

"""Se va a leer la primera imagen que es el acta de la carpeta donde se extrajeron las imagenes del pdf"""
imagen = Image.open('/home/cso/Desktop/pyverify/inpng/SINIESTRO_0.png')

"""RESULTAODS DE LA LECTURA"""
ocr_result = pytesseract.image_to_string(imagen, lang='spa')

"""
Se guarda el texto en un txt
"""
text_file=open("textouno1.txt","w")
text_file.write(ocr_result)


