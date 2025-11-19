Sistema de Reservas – Proyecto parcialJuanMadrid
Descripción General

Este proyecto es una aplicación web desarrollada con Python + Django, cuyo propósito es gestionar un sistema básico de reservas de citas.
Incluye operaciones CRUD completas para Clientes, Empleados, Servicios y Citas, permitiendo administrar todos los aspectos esenciales de un sistema de agendamiento.

La aplicación utiliza Bootstrap 5, templates organizados, formularios generados mediante ModelForms y relaciones entre tablas mediante llaves foráneas.

Modelos
1. Cliente

Representa a la persona que solicita una cita.
Campos:

nombre – Nombre completo del cliente

email – Correo electrónico

telefono – Teléfono de contacto

2. Empleado

Persona que ofrece un servicio o atiende una cita.
Campos:

nombre – Nombre del empleado

especialidad – Área o tipo de servicio que maneja

3. Servicio

Define qué se le puede ofrecer al cliente.
Campos:

nombre – Nombre del servicio

descripcion – Explicación breve

duracion_minutos – Duración estimada del servicio

4. Cita

Representa una reserva o agendamiento.
Incluye relaciones foráneas con los otros modelos.
Campos:

cliente – FK a Cliente

servicio – FK a Servicio

empleado – FK a Empleado

fecha – Día de la cita

hora – Hora agendada

Descripción Funcional de la Aplicación

El sistema permite administrar todo el flujo de reserva de citas:

Home

Página inicial con accesos directos a cada módulo.

Clientes

Listar clientes

Crear nuevos clientes

Editar clientes

Eliminar clientes

Empleados

Gestión de empleados encargados de las citas

CRUD completo de empleados

Servicios

Registro de servicios disponibles

CRUD completo para gestionar cada servicio

Citas

Calendario básico de reservas

Asignación de cliente + servicio + empleado

Registro de fecha y hora

Eliminación de citas

Cada módulo tiene:

Listado

Formulario de registro

Formulario de edición

Confirmación de eliminación

Todo generado mediante ModelForms y conectado por urls.py.

Instalación y Ejecución
1. Clonar o copiar el proyecto en tu máquina

Coloca el proyecto dentro de una carpeta de trabajo.

2. Crear el entorno virtual

Dentro del directorio raíz:

python -m venv .venv


Activarlo:

.venv\Scripts\activate

3. Instalar dependencias
pip install django

4. Aplicar migraciones
python manage.py makemigrations
python manage.py migrate

5. Ejecutar servidor
python manage.py runserver


El sistema queda disponible en:

http://127.0.0.1:8000/

Estructura del Proyecto
parcialJuanMadrid/
│ manage.py
│
├── parcialJuanMadrid/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── reservas_app/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
│       ├── base.html
│       ├── home.html
│       ├── cliente_*.html
│       ├── empleado_*.html
│       ├── servicio_*.html
│       └── cita_*.html