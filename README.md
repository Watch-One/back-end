# Backend de WatchOne
Version de python usada para desarrollar el proyecto: 3.9

### Pasos para ejecutar el proyecto:
- Instalar las dependencias necesarias: ``` pip install -r requirements.txt ```
- Agregar variables de entorno, copiar ```.env.template``` y cambiarle el nombre a ```.env```, luego poner los datos necesarios para acceder a la base de datos MySQL y si prefiere cambiarle la SECRET_KEY, para hacer pruebas la que ya esta de ejemplo está bien.
- Para iniciar el proyecto ejecutar el siguiente comando desde la raíz del proyecto:
  ```
    python -m uvicorn app:app --port 8000
  ```
  (Si el puerto le da problemas lo puede cambiar)
- Listo, puede acceder y hacer pruebas con la API desde la dirección: ``` http://localhost:8000/docs ``` o el puerto con el que haya ejecutado el comando.