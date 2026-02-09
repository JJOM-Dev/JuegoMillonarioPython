"""Juego de Historia Universal (consola).

Este archivo mantiene un flujo sencillo para practicar Historia Universal
con preguntas de selección múltiple, sistema de vidas y puntaje.
"""

import json
from dataclasses import dataclass
from pathlib import Path

ARCHIVO_GUARDADO = Path("savegame.json")


@dataclass
class Pregunta:
    enunciado: str
    opciones: list[str]
    respuesta: str
    retroalimentacion: str


@dataclass
class Nivel:
    nombre: str
    preguntas: list[Pregunta]


@dataclass
class Periodo:
    nombre: str
    niveles: list[Nivel]


def construir_periodos() -> list[Periodo]:
    """Crea los periodos históricos con sus niveles y preguntas."""
    return [
        Periodo(
            nombre="Antigüedad",
            niveles=[
                Nivel(
                    nombre="Civilizaciones Iniciales",
                    preguntas=[
                        Pregunta(
                            enunciado="¿Cuál de estas civilizaciones se desarrolló junto al río Nilo?",
                            opciones=["Mesopotamia", "Egipto", "China", "Grecia"],
                            respuesta="Egipto",
                            retroalimentacion="Egipto se consolidó gracias a las crecidas del río Nilo.",
                        ),
                        Pregunta(
                            enunciado="¿Qué invento es clave en el surgimiento de las ciudades antiguas?",
                            opciones=["La pólvora", "La escritura", "El motor a vapor", "Internet"],
                            respuesta="La escritura",
                            retroalimentacion="La escritura permitió registrar leyes y transacciones.",
                        ),
                        Pregunta(
                            enunciado="¿En qué región surgió la civilización mesopotámica?",
                            opciones=[
                                "Entre los ríos Tigris y Éufrates",
                                "En los Andes",
                                "En la península Ibérica",
                                "En el Sahara",
                            ],
                            respuesta="Entre los ríos Tigris y Éufrates",
                            retroalimentacion="Mesopotamia significa ""entre ríos"".",
                        ),
                        Pregunta(
                            enunciado="¿Qué cultura aportó el concepto de democracia directa?",
                            opciones=["Roma", "Grecia", "Fenicia", "Persia"],
                            respuesta="Grecia",
                            retroalimentacion="Atenas es recordada por su democracia directa.",
                        ),
                        Pregunta(
                            enunciado="¿Qué pueblo destacó por el comercio marítimo en el Mediterráneo?",
                            opciones=["Fenicios", "Mayas", "Aztecas", "Incas"],
                            respuesta="Fenicios",
                            retroalimentacion="Los fenicios fueron grandes navegantes y comerciantes.",
                        ),
                        Pregunta(
                            enunciado="¿Qué imperio construyó la Vía Apia y otras calzadas famosas?",
                            opciones=[
                                "Imperio Romano",
                                "Imperio Persa",
                                "Imperio Chino",
                                "Imperio Otomano",
                            ],
                            respuesta="Imperio Romano",
                            retroalimentacion="Roma expandió su red de calzadas para unir el imperio.",
                        ),
                        Pregunta(
                            enunciado="¿Cuál fue un aporte científico de los griegos antiguos?",
                            opciones=["Geometría", "Imprenta", "Electricidad", "Motor de combustión"],
                            respuesta="Geometría",
                            retroalimentacion="Euclides y otros griegos sistematizaron la geometría.",
                        ),
                        Pregunta(
                            enunciado="¿Qué estructura monumental se construyó en Egipto como tumbas reales?",
                            opciones=["Pirámides", "Zigurats", "Anfiteatros", "Catedrales"],
                            respuesta="Pirámides",
                            retroalimentacion="Las pirámides eran tumbas para los faraones.",
                        ),
                        Pregunta(
                            enunciado="¿Qué código legal es uno de los más antiguos de la historia?",
                            opciones=["Código de Hammurabi", "Código Napoleónico", "Leyes de Indias", "Fuero Juzgo"],
                            respuesta="Código de Hammurabi",
                            retroalimentacion="El código de Hammurabi pertenece a Babilonia.",
                        ),
                        Pregunta(
                            enunciado="¿Qué invento chino revolucionó la navegación en la antigüedad?",
                            opciones=["Brújula", "Telescopio", "Imprenta", "Motor a vapor"],
                            respuesta="Brújula",
                            retroalimentacion="La brújula permitió viajes marítimos más precisos.",
                        ),
                    ],
                ),
            ],
        ),
        Periodo(
            nombre="Independencia y Venezuela",
            niveles=[
                Nivel(
                    nombre="Campañas Libertadoras",
                    preguntas=[
                        Pregunta(
                            enunciado="¿Quién lideró la Campaña Admirable en 1813?",
                            opciones=[
                                "Simón Bolívar",
                                "José de San Martín",
                                "Francisco Miranda",
                                "Antonio José de Sucre",
                            ],
                            respuesta="Simón Bolívar",
                            retroalimentacion="La Campaña Admirable consolidó el liderazgo de Bolívar.",
                        ),
                        Pregunta(
                            enunciado="¿Qué batalla aseguró la independencia de Venezuela en 1821?",
                            opciones=["Carabobo", "Boyacá", "Junín", "Pichincha"],
                            respuesta="Carabobo",
                            retroalimentacion="Carabobo fue decisiva para la independencia venezolana.",
                        ),
                        Pregunta(
                            enunciado="¿Cuál era el objetivo principal del Congreso de Angostura?",
                            opciones=[
                                "Crear un gobierno central para la Gran Colombia",
                                "Restaurar la monarquía española",
                                "Dividir el territorio en virreinatos",
                                "Declarar la guerra a Portugal",
                            ],
                            respuesta="Crear un gobierno central para la Gran Colombia",
                            retroalimentacion="El Congreso de Angostura sentó bases institucionales.",
                        ),
                        Pregunta(
                            enunciado="¿Qué figura es conocida como la Libertadora del Libertador?",
                            opciones=[
                                "Manuela Sáenz",
                                "Luisa Cáceres",
                                "Juana Ramírez",
                                "Josefa Camejo",
                            ],
                            respuesta="Manuela Sáenz",
                            retroalimentacion="Manuela Sáenz apoyó a Bolívar en momentos clave.",
                        ),
                        Pregunta(
                            enunciado="¿En qué ciudad se firmó el Acta de Independencia de Venezuela en 1811?",
                            opciones=["Caracas", "Valencia", "Maracaibo", "Cumaná"],
                            respuesta="Caracas",
                            retroalimentacion="El Acta se firmó en Caracas el 5 de julio de 1811.",
                        ),
                        Pregunta(
                            enunciado="¿Qué batalla aseguró la independencia de Ecuador en 1822?",
                            opciones=["Pichincha", "Junín", "Ayacucho", "Boyacá"],
                            respuesta="Pichincha",
                            retroalimentacion="La victoria de Pichincha fue clave para Ecuador.",
                        ),
                        Pregunta(
                            enunciado="¿Qué documento proclamó los derechos del hombre y del ciudadano en 1789?",
                            opciones=[
                                "Declaración de los Derechos del Hombre y del Ciudadano",
                                "Carta Magna",
                                "Constitución de Cádiz",
                                "Edicto de Nantes",
                            ],
                            respuesta="Declaración de los Derechos del Hombre y del Ciudadano",
                            retroalimentacion="Fue un texto fundamental de la Revolución Francesa.",
                        ),
                        Pregunta(
                            enunciado="¿Quién encabezó el proceso de independencia de Haití?",
                            opciones=[
                                "Toussaint Louverture",
                                "Simón Bolívar",
                                "Napoleón Bonaparte",
                                "Bernardo O'Higgins",
                            ],
                            respuesta="Toussaint Louverture",
                            retroalimentacion="Louverture fue líder de la revolución haitiana.",
                        ),
                        Pregunta(
                            enunciado="¿Qué país lideró la Revolución Industrial?",
                            opciones=["Inglaterra", "España", "Portugal", "Rusia"],
                            respuesta="Inglaterra",
                            retroalimentacion="La Revolución Industrial inició en Inglaterra.",
                        ),
                        Pregunta(
                            enunciado="¿Qué organización internacional surgió tras la Segunda Guerra Mundial?",
                            opciones=["ONU", "OTAN", "Unión Europea", "Liga Hanseática"],
                            respuesta="ONU",
                            retroalimentacion="La ONU se fundó en 1945 para promover la paz.",
                        ),
                    ],
                ),
            ],
        ),
    ]


def elegir_opcion(pregunta: str, opciones: list[str]) -> int:
    """Solicita una opción válida al usuario y devuelve el índice seleccionado."""
    while True:
        print(f"\n{pregunta}")
        for indice, opcion in enumerate(opciones, start=1):
            print(f"  {indice}. {opcion}")
        eleccion = input("Selecciona una opción: ").strip()
        if eleccion.isdigit() and 1 <= int(eleccion) <= len(opciones):
            return int(eleccion) - 1
        print("Opción inválida. Intenta nuevamente.")


def cargar_partida() -> dict | None:
    """Lee la partida guardada si existe."""
    if not ARCHIVO_GUARDADO.exists():
        return None
    with ARCHIVO_GUARDADO.open("r", encoding="utf-8") as archivo:
        return json.load(archivo)


def guardar_partida(indice_periodo: int, indice_nivel: int, puntaje: int) -> None:
    """Guarda el estado actual del juego."""
    datos = {
        "period_index": indice_periodo,
        "level_index": indice_nivel,
        "score": puntaje,
    }
    with ARCHIVO_GUARDADO.open("w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=2, ensure_ascii=False)


def jugar_nivel(nivel: Nivel) -> int:
    """Ejecuta las preguntas de un nivel y retorna el puntaje obtenido."""
    vidas = 3
    puntaje = 0
    print(f"\nIniciando nivel: {nivel.nombre}")
    for pregunta in nivel.preguntas:
        if vidas == 0:
            break
        indice_respuesta = elegir_opcion(pregunta.enunciado, pregunta.opciones)
        seleccion = pregunta.opciones[indice_respuesta]
        if seleccion == pregunta.respuesta:
            puntaje += 10
            print("✅ ¡Correcto!", pregunta.retroalimentacion)
        else:
            vidas -= 1
            print(f"❌ Respuesta incorrecta. {pregunta.retroalimentacion}")
            print(f"Vidas restantes: {vidas}")
            if vidas > 0:
                print("¡Ánimo! Puedes seguir intentándolo.")
    if vidas == 0:
        print("El personaje se pone triste, pero puedes intentarlo de nuevo.")
    else:
        print("¡Felicidades! Has completado el nivel.")
    print(f"Puntaje obtenido: {puntaje}")
    return puntaje


def iniciar_nueva_partida(periodos: list[Periodo]) -> None:
    indice_periodo = elegir_opcion(
        "Selecciona el período histórico:",
        [periodo.nombre for periodo in periodos],
    )
    niveles = periodos[indice_periodo].niveles
    indice_nivel = elegir_opcion(
        "Selecciona el nivel:",
        [nivel.nombre for nivel in niveles],
    )
    puntaje = jugar_nivel(niveles[indice_nivel])
    guardar_partida(indice_periodo, indice_nivel, puntaje)
    print("Partida guardada.")


def reanudar_partida(periodos: list[Periodo]) -> None:
    datos = cargar_partida()
    if datos is None:
        print("No hay partidas guardadas.")
        return
    indice_periodo = datos.get("period_index", 0)
    indice_nivel = datos.get("level_index", 0)
    puntaje = datos.get("score", 0)
    print(
        "\nReanudando partida guardada:"
        f"\nPeríodo: {periodos[indice_periodo].nombre}"
        f"\nNivel: {periodos[indice_periodo].niveles[indice_nivel].nombre}"
        f"\nPuntaje previo: {puntaje}"
    )
    puntaje += jugar_nivel(periodos[indice_periodo].niveles[indice_nivel])
    guardar_partida(indice_periodo, indice_nivel, puntaje)
    print("Partida actualizada.")


def main() -> None:
    periodos = construir_periodos()
    while True:
        print("\n=== Juego de Historia Universal ===")
        opcion = elegir_opcion(
            "Menú principal:",
            ["Iniciar nueva partida", "Cargar partida", "Salir"],
        )
        if opcion == 0:
            iniciar_nueva_partida(periodos)
        elif opcion == 1:
            reanudar_partida(periodos)
        else:
            print("Gracias por jugar. ¡Hasta pronto!")
            break


if __name__ == "__main__":
    main()
