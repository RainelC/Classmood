
# Classmood

Este proyecto es un Sistema de Monitoreo de Asistencia y Estado de Ánimo de Estudiantes diseñado para automatizar el proceso de pasar lista y monitorear las emociones de los estudiantes durante las clases en línea. El sistema registra automáticamente la asistencia y analiza las expresiones faciales de los estudiantes para proporcionar información en tiempo real sobre su estado de ánimo.


## Tecnologías Utilizadas

**Backend:** FastAPI

**Base de Datos:** MongoDB

**Reconocimiento Facial:** Biblioteca RetinaFace

**Front-End:** HTML, CSS, JS


## Instalación 

1. #### Clonar el repositorio:
```bash
git clone https://github.com/tuusuario/tu-repositorio.git
cd tu-repositorio
```
2. #### Instalar dependencias:
```bash
pip install -r requirements.txt
```
3. #### Dentro de la carpeta del proyecto ejecuta la aplicación: 
```bash
uvicorn main:app --reload
```
    
## Usos

Al ejecutar la aplicación se te brindará una dirección, la cual debes pegar en el navegador y agregando "/docs" al final de esta, para poder ver la documentación completa de la API. Desde ahí podrás probar todos endpoints que conforman la API.

Al abrir el archivo index.html podrá realizar una prueba para crear un estudiante con la información biométrica, en este caso, el rostro del estudiante.

Si deseas probar la función de pasar lista y reconocer las emociones de los estudiantes dirígete al script.js y en la función mostrarCamara() comentar la línea 23 y descomentar la línea 24.

```javascript
procesarCamara();
//setTimeout(attendance_do, 5000)
setTimeout(new_student, 5000)
```



