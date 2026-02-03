Bitácora de UX: MapVentura (Act. 3)

1. Micro-interacciones y Manejo de Latencia

En esta actividad, el enfoque principal fue la Visibilidad del Estado del Sistema y la Prevención de Errores, asegurando que el usuario nunca se sienta perdido mientras el sistema procesa información.

2. Decisiones de Diseño

Estados del Marcador (Feedback de Latencia):

Gris (Pendiente): Al hacer clic, el marcador aparece inmediatamente en gris con una animación de pulso. Esto indica que la acción fue recibida pero está en proceso (manejo de "optimistic UI").

Morado (Confirmado): Solo cambia al color de la marca una vez que el servidor (Flask) confirma el guardado.

Prevención de Errores (Diálogo de Confirmación): * Implementamos un popup intermedio que pregunta "¿Guardar este punto?". Esto evita que clics accidentales saturen la base de datos y da control total al usuario (Heurística: "Libertad y Control").

Se incluyó un botón de Cancelar que elimina el marcador temporal de inmediato.

Feedback de Proceso (Toast dinámico):

Durante el fetch, el Toast muestra un icono de carga (spinner) y un mensaje de "Guardando...".

Al finalizar, el mensaje cambia a "¡Punto guardado!" con un icono de éxito, cerrando el ciclo de retroalimentación.

3. Registro de Prompts

Prompt Final Utilizado:

"Escribe un script en JS para Leaflet que:

Ponga un marcador temporal gris inmediatamente al hacer clic.

Abra un popup que pregunte '¿Guardar este punto?' con botones de Guardar y Cancelar.

Al guardar, envíe coordenadas a /guardar_punto usando fetch y muestre un toast de 'Guardando...' con un spinner.

Si el servidor confirma, el marcador cambia a morado y el toast a '¡Punto guardado!'.

Permite borrar el marcador si se cancela."

Refinamientos:

Se añadió una animación CSS pulse para el estado pendiente.

Se ajustó la lógica del fetch para manejar errores de red y revertir el marcador a su estado original si la conexión falla.