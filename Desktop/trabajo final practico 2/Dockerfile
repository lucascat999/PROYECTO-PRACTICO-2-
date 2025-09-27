#Imagen madre 
FROM python:3.11-slim

#Configuracion para poder ver logs de manera correcta
ENV PYTHONBUFFERED=1

#Directorio de trabajo (donde vamos a pararnos)
WORKDIR /crud

#Copiar archivo de dependencias
COPY requirements.txt .

#Instala las dependencias via pip
RUN pip install --no-cache-dir -r requirements.txt

#copiamos codigo fuente del proyecto A
COPY crud/ .

