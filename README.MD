### Sistema de Reservas – Proyecto FINAL
### PRESENTADO POR: JUAN MADRID PALACIO
### ENLACE DEL REPOSITORIO
-  https://github.com/JuanMadridUSB/ProyectoFinalElectiva.git
### Descripción general
Este proyecto es una aplicación web desarrollada con Python + Django para gestionar un sistema básico de reservas de citas, abarcando operaciones CRUD para Clientes, Empleados, Servicios y Citas. Incluye Bootstrap 5, templates organizados, ModelForms y relaciones entre tablas mediante llaves foráneas.

### Modelos
- Cliente: Representa a la persona que solicita una cita.
  - nombre – Nombre completo del cliente.
  - email – Correo electrónico.
  - telefono – Teléfono de contacto.
- Empleado: Persona que ofrece un servicio o atiende una cita.
  - nombre – Nombre del empleado.
  - especialidad – Área o tipo de servicio que maneja.
- Servicio: Define qué se le puede ofrecer al cliente.
  - nombre – Nombre del servicio.
  - descripcion – Explicación breve.
  - duracion_minutos – Duración estimada del servicio.
- Cita: Representa una reserva o agendamiento con FKs a Cliente, Servicio y Empleado.
  - cliente – FK a Cliente.
  - servicio – FK a Servicio.
  - empleado – FK a Empleado.
  - fecha – Día de la cita.
  - hora – Hora agendada.

### Descripción funcional
- Home: Página inicial con accesos directos a cada módulo.
- Clientes: Listar, crear, editar y eliminar clientes.
- Empleados: Gestión completa de empleados con CRUD.
- Servicios: Registro y CRUD de servicios disponibles.
- Citas: Calendario básico, asignación de cliente + servicio + empleado, registro de fecha y hora, y eliminación.

### Formularios y navegación
Cada módulo cuenta con listado, formulario de registro, formulario de edición y confirmación de eliminación, generados con ModelForms y conectados por urls.py. La navegación entre vistas sigue rutas declaradas en el enrutador de la aplicación. Las páginas utilizan componentes consistentes y estructurados para mantener claridad y usabilidad.

### Instalación y ejecución
1. Clonar o copiar el proyecto en tu máquina y colocarlo en una carpeta de trabajo.
2. Crear el entorno virtual dentro del directorio raíz:
   - ```bash
     python -m venv .venv
     ```
   - Activarlo:
     - Windows:
       ```bash
       .venv\Scripts\activate
       ```
3. Instalar dependencias:
   - ```bash
     pip install django
     ```
4. Aplicar migraciones:
   - ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```
5. Ejecutar servidor:
   - ```bash
     python manage.py runserver
     ```

El sistema queda disponible en: http://127.0.0.1:8000/

### Estructura del proyecto
```text
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
```

