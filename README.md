# Juego de Historia Universal

## Datos del proyecto
- **Daniel Rivera** (C.I: 31.048.830)
- **José Osorio** (C.I: 30.973.057)
- **Nelson Carrillo** (C.I: 31.611.962)

## ¿De qué va el juego?
Juego de Historia Universal es un reto educativo tipo trivia en el que exploras períodos históricos y respondes preguntas de opción múltiple. Cada categoría representa una etapa de la historia y tu objetivo es completar sus preguntas con la mayor precisión posible, cuidando tu puntaje, el tiempo y tus vidas.

## ¿Cómo se juega?
1. **Elige una categoría**: selecciona el período histórico con el que quieres iniciar.
2. **Responde preguntas**: cada pregunta tiene cuatro opciones, elige la correcta.
3. **Administra tus vidas y tiempo**: si fallas pierdes vidas (según la dificultad). Si el tiempo se agota, también pierdes la pregunta.
4. **Usa comodines estratégicamente**: te permiten obtener pistas, saltar preguntas, investigar por unos segundos o eliminar opciones.
5. **Completa la categoría**: al responder todas las preguntas, puedes continuar con otra categoría.

## Mecánicas principales
- **Puntaje**: cada respuesta correcta suma puntos.
- **Vidas**: los errores reducen vidas; en modos avanzados perder vidas puede terminar la ronda.
- **Tiempo por pregunta**: el temporizador varía por dificultad.
- **Preguntas especiales**: pueden aparecer con reglas de tiempo distintas y premios extra.
- **Guardado**: en la interfaz web puedes guardar y cargar partidas (excepto en modo hardcore).

## Dificultades
- **Principiante**: sin límite de vidas y sin comodines.
- **Fácil**: más vidas, tiempo cómodo y 2 usos por comodín.
- **Normal**: balance entre reto y ayudas, 1 uso por comodín.
- **Difícil**: menos margen de error, sin comodines y con preguntas extra avanzadas.
- **Hardcore**: reglas más estrictas, sin comodines y errores reinician la ronda.

## Comodines
- **Pista**: muestra una pista basada en la respuesta.
- **Saltar**: omite la pregunta actual.
- **Investigar 10s**: te permite salir temporalmente sin penalización.
- **Eliminar 2**: elimina dos opciones incorrectas para dejar solo dos respuestas visibles.

## Metodología del Proyecto
Para el desarrollo del juego educativo sobre Historia Universal enfocado en Venezuela, se selecciona la **metodología en Cascada**, debido a su estructura secuencial, organizada y adecuada para proyectos con requisitos definidos desde el inicio.

Este modelo permite avanzar de manera ordenada a través de las etapas del desarrollo, garantizando que cada fase sea completada, revisada y validada antes de pasar a la siguiente. La metodología en Cascada resulta apropiada para entornos académicos, ya que facilita la planificación, la documentación formal y el control del progreso del proyecto.

## Fases del proyecto

### Fase 1: Análisis de Requisitos
**Objetivo:** Identificar las necesidades educativas, los requerimientos técnicos y los contenidos históricos que formarán parte del juego.

**Actividad Prioritaria:** Recolección de Información Educativa y Técnica

**Tarea 1: Aplicación de Técnica de Recolección de Datos**
Se diseñará y aplicará un instrumento de recolección de datos (cuestionario) dirigido a estudiantes y docentes, con el propósito de conocer:
- Las dificultades en el aprendizaje de Historia Universal.
- El nivel de interés en el uso de juegos educativos.
- Las preferencias en cuanto a dinámicas de aprendizaje digital.

**Estructura sugerida del instrumento:**
- **Sección I:** Datos Generales del Usuario (edad, nivel educativo, frecuencia de uso de tecnología).
- **Sección II:** Aprendizaje de Historia Universal.
  - ¿Considera difícil la asignatura de Historia Universal?
  - ¿Qué temas históricos le resultan más complejos?
- **Sección III:** Juegos Educativos.
  - ¿Le gustaría aprender Historia Universal mediante un juego digital?
  - ¿Qué tipo de retos o actividades le resultan más atractivos?

**Tarea 2: Definición de Requerimientos del Sistema**

**Requerimientos Funcionales:**
- Mostrar niveles organizados por períodos históricos.
- Incluir retos, preguntas y misiones educativas.
- Registrar progreso, puntajes y logros del usuario.
- Mostrar retroalimentación inmediata sobre respuestas.
- Permitir repetir niveles para reforzar el aprendizaje.

**Requerimientos No Funcionales:**
- Interfaz intuitiva y fácil de usar.
- Bajo consumo de recursos del sistema.
- Compatibilidad con equipos de bajos recursos.
- Tiempo de respuesta rápido.
- Diseño visual atractivo y motivador.

### Fase 2: Estudio de Factibilidad
**Objetivo:** Evaluar la viabilidad del proyecto desde los puntos de vista técnico, operativo, económico y social.

**Factibilidad Técnica**
- El proyecto es técnicamente viable debido a la disponibilidad de herramientas accesibles para el desarrollo de juegos educativos, así como a la facilidad de implementación en entornos escolares.

**Factibilidad Operativa**
- El sistema podrá ser utilizado por estudiantes y docentes sin requerir conocimientos técnicos avanzados, gracias a su diseño intuitivo.

**Factibilidad Económica**
- El desarrollo del proyecto implica bajo costo, ya que se utilizarán herramientas gratuitas o de código abierto, minimizando la inversión financiera.

**Factibilidad Psicosocial y Educativa**
El proyecto generará un impacto positivo al:
- Incrementar la motivación de los estudiantes.
- Fortalecer el aprendizaje de la Historia Universal.
- Fomentar el uso responsable de la tecnología.
- Promover el aprendizaje autónomo e interactivo.

### Fase 3: Diseño del Sistema
**Objetivo:** Definir la estructura visual, funcional y navegacional del juego educativo.

**Actividad Prioritaria:** Arquitectura del Juego

**Tarea 1: Diseño del Mapa de Navegación**
**Flujo general del sistema:**
- **Pantalla de Inicio:** pantalla sencilla y llamativa que use imágenes de la Segunda Guerra Mundial con recortes de la Primera Guerra Mundial, batalla de Simón Bolívar y eventos históricos relevantes.
- **Menú Principal:** menú sencillo, igual que la pantalla de inicio, que permita cargar partida guardada e iniciar nueva partida.
- **Selección de Período Histórico:** durante la nueva partida puedes elegir el período en el cual quieres jugar o qué evento histórico deseas seleccionar.
- **Selección de Nivel:** si tienes partidas guardadas puedes repetir niveles y seleccionar hasta donde te hayas quedado.
- **Pantalla de Juego:** selección de preguntas (error si se equivoca de respuesta). Cuatro preguntas, máximo tres vidas y un personaje referente al evento histórico reaccionando a estas; si te equivocas te da ánimos, se pone triste si pierdes y si ganas te felicita.
- **Pantalla de Resultados:** pantalla que muestra los puntos que acumulas después de terminar la ronda.
- **Registro de Puntajes:** los puntajes se registran para desbloquear niveles y comodines dentro del juego.
- **Retorno al Menú Principal:** para regresar al menú principal puede ser desde pausa o si terminas tu nivel y quieres salir estará el botón.

**Tarea 2: Diseño de Interfaz y Mecánicas del Juego**
- Diseño visual atractivo y acorde al público objetivo.
- Sistema de niveles progresivos según la dificultad.
- Retos basados en acontecimientos históricos.
- Sistema de puntos, logros y recompensas.
- Retroalimentación inmediata para reforzar el aprendizaje.

## Restricciones del Sistema
- Limitaciones de hardware en instituciones educativas.
- Tiempo limitado para el desarrollo del proyecto.
- Uso de herramientas gratuitas.
- Contenido histórico limitado a los temas esenciales del programa académico.

## Seguridad del Sistema
- Protección del progreso del usuario.
- Prevención de la alteración de puntajes.
- Restricción de acceso a configuraciones internas del sistema.

## Planificación del Proyecto

| Fase | Actividad | Duración Estimada |
| --- | --- | --- |
| Análisis | Recolección de datos y definición de requerimientos | 1 semana |
| Factibilidad | Evaluación técnica, económica y operativa | 1 semana |
| Diseño | Diseño del sistema y navegación | 2 semanas |
| Desarrollo | Programación del juego | 3 semanas |
| Pruebas | Corrección de errores y validación | 2 semanas |

## Cómo ejecutar el juego
1. Asegúrate de tener Python 3.10 o superior instalado.
2. Ejecuta el juego desde la terminal:

```bash
python main.py
```

El juego guardará tu progreso en `savegame.json`.

## Interfaz web
Para una interfaz moderna, responsive y con estilo Neumorphism puedes abrir el archivo `index.html` en tu navegador. Toda la interfaz (HTML + CSS + JavaScript) está integrada en un solo archivo para que sea fácil de leer, explicar y modificar.

```bash
# Opción simple
open index.html

# Servidor local con Python
python -m http.server 8000
```

Luego visita `http://localhost:8000` en el navegador.

## Interfaz de lujo en Python
Se incluye una versión de escritorio con Tkinter y gestor de partidas guardadas.

```bash
python app_gui.py
```

Las partidas se guardan en `partidas_guardadas.json`.
