# MapVentura \| Explora lo Desconocido 🧭

**MapVentura** es una aplicación web de mapeo interactivo enfocada en
entusiastas del senderismo y el ciclismo de montaña (MTB). Su propósito
es facilitar la exploración, visualización y registro de rutas seguras
mediante una interfaz de alto contraste, optimizada para su uso en
exteriores y dispositivos móviles.

La aplicación prioriza la usabilidad, la visibilidad bajo condiciones de
luz intensa y una experiencia de usuario clara e intuitiva.

------------------------------------------------------------------------

## 🚀 Ejecución del proyecto

Sigue los pasos a continuación para ejecutar el proyecto en un entorno
local:

1.  **Clona o descarga el repositorio** en tu equipo.

2.  **Instala las dependencias necesarias** (asegúrate de contar con
    Python instalado):

    ``` bash
    pip install flask
    ```

3.  **Inicia el servidor de desarrollo**:

    ``` bash
    python main.py
    ```

4.  **Abre la aplicación en tu navegador**:

    Accede a: `http://127.0.0.1:5000`

------------------------------------------------------------------------

## 🛠 Stack Tecnológico

-   **Backend:** Python 3, Flask\
-   **Frontend:** HTML5, JavaScript (ES6)\
-   **Estilos:** Tailwind CSS (vía CDN) para un diseño responsivo y
    utilitario\
-   **Mapas:** Leaflet.js con tiles de OpenStreetMap\
-   **Iconografía:** Font Awesome

------------------------------------------------------------------------

## 🎨 Justificación de Diseño y Experiencia de Usuario (UX)

El diseño de MapVentura es el resultado de un proceso iterativo centrado
en la experiencia del usuario y en escenarios de uso reales en
exteriores.

### 1. Estética y Visibilidad

-   **Alto contraste para exteriores:** Se adoptó un modo oscuro (fondos
    `#0f172a`) para reducir el deslumbramiento y la fatiga visual.
-   **Color semántico:** El uso de un morado vibrante genera contraste
    frente a mapas topográficos y entornos naturales, asegurando la
    visibilidad de elementos interactivos como botones y marcadores.

### 2. Ergonomía y Ley de Fitts

-   **Zonas de alcance:** Los controles de zoom se colocaron en la
    esquina inferior derecha, facilitando su uso con el pulgar en
    dispositivos móviles sin obstruir el mapa.
-   **Precisión táctil:** Los botones cuentan con un área mínima de 44
    px, reduciendo errores de interacción durante el movimiento.

### 3. Feedback y Prevención de Errores

-   **Optimistic UI:** Los marcadores aparecen de forma inmediata en
    estado pendiente (gris) y cambian a confirmado (morado) tras la
    respuesta del servidor.
-   **Visibilidad del estado:** Notificaciones tipo *toast* informan
    sobre procesos de carga y confirmación, reduciendo la incertidumbre
    ante la latencia de red.
-   **Control del usuario:** Se incorporan diálogos de confirmación para
    evitar registros accidentales.

### 4. Accesibilidad y Estructura

-   **Vista dual (Split View):** Lista lateral sincronizada con el mapa
    que ofrece una alternativa textual a la navegación espacial.
-   **Navegación asistida:** Uso de atributos ARIA (`aria-label`) para
    compatibilidad con lectores de pantalla.
-   **Interacción cruzada:** La selección de un elemento en la lista
    provoca un desplazamiento suave (*flyTo*) del mapa hacia la
    ubicación correspondiente, mejorando la orientación espacial.

------------------------------------------------------------------------

## 🤖 Créditos a la IA

El desarrollo del código y la documentación fueron co-creados con apoyo
de **Gemini Canvas**.

**Prompt principal utilizado para la estructura base:**

> "Crea una Landing Page HTML para MapVentura con Tailwind. Hero con
> mapa topográfico, título grande y CTA 'Explorar Mapa'. Colores: gris
> oscuro, negro y morado vibrante. Posteriormente, integra un mapa
> interactivo con Leaflet que permita guardar puntos en una base de
> datos temporal con Flask, manejando estados de carga y confirmación
> visual."
