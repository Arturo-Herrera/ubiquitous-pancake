Bitácora de UX: MapVentura (Act. 4)

1. Arquitectura de Información y Accesibilidad

En esta actividad, hemos pasado de una interfaz de solo mapa a una vista dual. El objetivo es proporcionar alternativas textuales para la información espacial, mejorando la navegación para todos los usuarios.

2. Decisiones de Diseño

Diseño de Dos Columnas (Split View):

Mapa (Primario): Ocupa la mayor parte de la pantalla para la interacción visual.

Lista de Lugares (Secundario/Accesible): Muestra cada marcador como un elemento de lista con coordenadas. Esto cumple con la necesidad de accesibilidad (lectores de pantalla) y ofrece una forma rápida de revisar los puntos guardados sin navegar por el mapa.

Accesibilidad Web (ARIA):

Se añadieron atributos aria-label a los botones de zoom ("Acercar mapa", "Alejar mapa") y al botón de regreso.

Se definieron roles de application para el mapa y aside para la lista, permitiendo que las tecnologías de asistencia comprendan la estructura de la página.

Interacción Cruzada:

Al hacer clic en un elemento de la lista, el mapa realiza un flyTo (vuelo suave) hacia el marcador y abre su popup. Esto mejora la eficiencia de uso al permitir saltos rápidos entre ubicaciones.

Sincronización: El contador de lugares y la lista se actualizan en tiempo real conforme el usuario confirma o elimina puntos.

3. Registro de Prompts

Prompt Final Utilizado:

"Modifica la interfaz para tener dos columnas: 'Mapa' y 'Lista de Lugares'. Cuando se agregue un marcador en el mapa, debe aparecer también como texto descriptivo en la sección de Lista con sus coordenadas. Asegúrate de que los botones del mapa tengan atributos 'aria-label' descriptivos. Mantén el estilo oscuro y morado."

Refinamientos:

Se ajustó el CSS para que en pantallas pequeñas (móviles) la lista aparezca debajo del mapa de forma responsiva.

Se incluyó una scrollbar personalizada para la lista para mantener la estética oscura sin desentonar con el diseño del sistema.