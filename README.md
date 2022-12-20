# Proyecto Unidad 05 [Aula 05]
Este es un proyecto de Silabuz Academy del Curso MPTE BE de la Unidad 05.

## Enlace Railway
- **Unidad Django REST Framework** - [Proyecto](https://restproject-production.up.railway.app/login/)



## Proyecto
Se presenta la API de pagos, con os modelos Services, Payment_User, Expired_payments y User, las cuales se hace el uso de JWT para autenticar, permisos para operaciones CRUD, paginaciones, filtros, Throttling además de la documentación generada por Django-Yasg

# API

## Uso de la API como Usuario autenticado

El usuario debe acceder al [registro](https://restproject-production.up.railway.app/register/) para registrarse dentro de la DB

Luego, al [login](https://restproject-production.up.railway.app/login/) para solicitar el Token y saber las credenciales


## Página Principal luego del registro

- Anotar el **User ID** para los campos requeridos en el CRUD
- Copiar el **Token** generado para realizar las operaciones CRUD
- Anotar el **Service ID** para los campos requeridos en el CRUD


## CRUD

Se requiere usar un Cliente API (Insomnia, Postman, Thunder Client, etc.) para enviar el token en el campo Auth - Bearer

## Autor ✒️
- **Jean Franco Tineo** - [tineodev](https://github.com/tineodev)



# Modificar proyecto
Para que el proyecto funcione correctamente, se deben tener en cuenta varios aspectos:
- Contar con una versión de Python y PIP dentro del sistema
- Contar con un módulo de entornos virtuales (virtualenv recomendado)


## Instalación
Iniciar creando el entorno virtual para el despliegue
```py
pip install virtualenv
```

Crear y activar entorno virtual
```bash
virtualenv env

Linux:
source env/bin/activate

Windows:
env\Scripts\activate.bat
```

Instalar requirements.txt
```py
pip install -r requirements.txt
```

Crear archivo <code>SQLite3</code> para la base de datos dentro de <code>django_portfolio</code>
```bash
touch db.sqlite3
```

Crear archivo <code>.env</code> en la carpeta <code>zproject</code> para configurar las variables de entorno
```bash
touch .env
```

Agregue una clave secreta en el archivo <code>.env</code>, como se hace en el ejemplo siguiente
```
SECRET_KEY=This_is_the_password
```

Realice las migraciones correspondientes para las bases de datos
```bash
python manage.py makemigrations
python manage.py migrate
```


## Despliegue 📦

Abrir shell, ubicarse en la carpeta <code>django_portfolio</code>
```bash
python manage.py runserver
```

## Uso de la API como Administrador

El proyecto hace uso del modelo predeterminado User para los usuarios.
Algunas operaciones están limitadas solo para usuarios Admin y/o Usuarios autenticados.

Por lo tanto para acceder a todas las funcionalidades, crear un superusuario

```bash
python manage.py createsuperuser nombre_superusuario
```