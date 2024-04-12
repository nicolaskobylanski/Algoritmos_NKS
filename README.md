# Sistema de Gestión Hotelera

Este script en Python implementa un sistema simple de gestión hotelera. Permite a los usuarios administrar habitaciones de hotel, empleados y reservas de huéspedes a través de una interfaz de línea de comandos.

## Cómo funciona

El script proporciona un menú principal con opciones para la gestión del hotel, la gestión de empleados, la gestión de habitaciones y para salir del sistema. Cada opción del menú conduce a submenús donde se pueden realizar acciones específicas.

- **Gestión del Hotel**: Permite a los usuarios agregar o eliminar habitaciones, agregar o eliminar empleados, hacer check-in o check-out de huéspedes.
- **Gestión de Empleados**: Permite a los usuarios ver los detalles de los empleados, actualizar las posiciones de los empleados y actualizar los salarios de los empleados.
- **Gestión de Habitaciones**: Proporciona opciones para verificar la disponibilidad de habitaciones, hacer check-in de huéspedes en habitaciones y hacer check-out de huéspedes de habitaciones.

El script se ejecuta continuamente en un bucle hasta que el usuario elige salir del sistema.

## Cómo utilizar

1. Ejecuta el script.
2. Sigue las indicaciones para navegar a través de los menús y realizar las acciones deseadas.
3. Usa las opciones proporcionadas para gestionar las habitaciones del hotel, los empleados y las reservas de huéspedes.

## Estructura del Script

- **Hotel.py**: Define la clase Hotel con métodos para gestionar las operaciones del hotel.
- **Room.py**: Define la clase Room con atributos y métodos relacionados con las habitaciones del hotel.
- **Employee.py**: Define la clase Employee con atributos y métodos relacionados con los empleados del hotel.
- **main.py**: Script principal que proporciona la interfaz de línea de comandos y orquesta la interacción entre el usuario y el sistema de gestión hotelera.

## Nota

- Este script proporciona una demostración básica de un sistema de gestión hotelera. Para un entorno de producción, serían necesarias características adicionales, manejo de errores y medidas de seguridad.
- El script asume una interfaz de línea de comandos simple. Para una interfaz más amigable para el usuario, se podría desarrollar una interfaz gráfica de usuario (GUI) o una interfaz web.

**Descargo de responsabilidad:** Este script es solo para fines de demostración y puede requerir modificaciones adicionales para casos de uso del mundo real.
