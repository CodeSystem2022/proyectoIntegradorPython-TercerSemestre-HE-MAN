# proyecto-Integrador-Python-HE-MAN
<table cellspacing="30">
  <tr>
    <td>
      <img src="https://i.pinimg.com/474x/5d/24/be/5d24be6044bbab9b9207c3521405bece.jpg" alt="">
    </td>
    <td>
      <h1>INTEGRANTES:</h1>
      <table border="10">
        <tr>
          <th>NOMBRE:</th>
          <th>APELLIDO:</th>
        </tr>
        <tr>
          <td>Matias</td>
          <td>Michaux</td>
        </tr>
        <tr>
          <td>Emmanuel</td>
          <td>Sbona</td>
        </tr>
        <tr>
          <td>Jorge Agustin</td>
          <td>Loyola</td>
        </tr>
        <tr>
          <td>Fabio Javier</td>
          <td>Flores</td>
        </tr>
        <tr>
          <td>Luciano</td>
          <td>Cortez</td>
        </tr>
        <tr>
          <td>Mauricio</td>
          <td>Cerda</td>
        </tr>
        <tr>
          <td>Fernando Matias</td>
          <td>Cala</td>
        </tr>
        <tr>
          <td>Juan Manuel</td>
          <td>Bresanovich</td>
        </tr>
        <tr>
          <td>Sebastían</td>
          <td>Barros</td>
        </tr>
      </table>
    </td>
  </tr>
</table>


PASOS PARA UTILIZAR LA AGENDA:

# agendapyd

Esta es una aplicación de agenda que te permite gestionar tus contactos. Sigue los pasos a continuación para configurar y ejecutar la aplicación.

## Pasos para ejecutar la aplicación

1. Clona el repositorio a tu máquina local:

   ```bash
   git clone https://github.com/CodeSystem2022/proyectoIntegradorPython-TercerSemestre-HE-MAN.git

2. Abre una terminal y navega hasta el directorio raíz del repositorio clonado.

3.Ejecuta el siguiente comando para iniciar los contenedores de Docker:

   docker-compose up

Esto descargará las imágenes necesarias (pgadmin4, postgres y agendapyd) y creará los contenedores correspondientes.

3. Abre tu navegador web y accede a la siguiente URL: http://localhost:5050

4. Una vez en la página de pgAdmin4, realiza los siguientes pasos:

Haz clic derecho en "Server" y selecciona "Register" > "Server".
En el campo "Name", introduce "postgres".
En la pestaña "Connection", en el campo "Host", introduce "postgres".
En el campo "Maintenance database", introduce "root".
En los campos "Username" y "Password", introduce "root".
Guarda los cambios para establecer la conexión a la base de datos "agenda.db".
Abre una nueva terminal y ejecuta el siguiente comando para iniciar el contenedor de agendapyd en una terminal bash:
  docker run -it --network=agendapyd_mynetwork johnconnor2023/agendapyd /bin/bash

6. Una vez dentro del contenedor, ejecuta el siguiente comando para iniciar la aplicación de agenda:

   python ./main.py

¡Listo! Ahora los contenedores están en funcionamiento y la aplicación de agenda está ejecutándose.

Recuerda que estos pasos asumen que tienes Docker y Docker Compose instalados en tu máquina. Asegúrate de cumplir con los requisitos antes de ejecutar la aplicación. Si tienes algún problema o pregunta, no dudes en abrir un issue en este repositorio.






