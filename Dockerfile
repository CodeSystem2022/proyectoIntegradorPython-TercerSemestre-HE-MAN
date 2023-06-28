# Selecciona la imagen base
FROM python:latest



# Copia los archivos del proyecto al directorio de trabajo del contenedor
COPY main.py /
COPY Contacto.py /
COPY contactoPersonal.py /
COPY ContactoProfesional.py /

# Instala las dependencias

RUN pip install pip install psycopg2-binary
RUN pip install --upgrade pip
RUN pip install datetime
RUN pip install pillow
RUN pip install colorama

#RUN pip install -r requirements.txt
#RUN pip install --upgrade pip


CMD [ "python", "./main.py" ]
