import json
from dataclasses import dataclass
from pathlib import Path

SAVE_FILE = Path("savegame.json")


@dataclass
class Question:
    prompt: str
    options: list[str]
    answer: str
    feedback: str


@dataclass
class Level:
    name: str
    questions: list[Question]


@dataclass
class Period:
    name: str
    levels: list[Level]


def build_periods() -> list[Period]:
    return [
        Period(
            name="Antigüedad",
            levels=[
                Level(
                    name="Civilizaciones Iniciales",
                    questions=[
                        Question(
                            prompt="¿Cuál de estas civilizaciones se desarrolló junto al río Nilo?",
                            options=["Mesopotamia", "Egipto", "China", "Grecia"],
                            answer="Egipto",
                            feedback="Egipto se consolidó gracias a las crecidas del río Nilo.",
                        ),
                        Question(
                            prompt="¿Qué invento es clave en el surgimiento de las ciudades antiguas?",
                            options=["La pólvora", "La escritura", "El motor a vapor", "Internet"],
                            answer="La escritura",
                            feedback="La escritura permitió registrar leyes y transacciones.",
                        ),
                        Question(
                            prompt="¿En qué región surgió la civilización mesopotámica?",
                            options=["Entre los ríos Tigris y Éufrates", "En los Andes", "En la península Ibérica", "En el Sahara"],
                            answer="Entre los ríos Tigris y Éufrates",
                            feedback="Mesopotamia significa ""entre ríos"".",
                        ),
                        Question(
                            prompt="¿Qué cultura aportó el concepto de democracia directa?",
                            options=["Roma", "Grecia", "Fenicia", "Persia"],
                            answer="Grecia",
                            feedback="Atenas es recordada por su democracia directa.",
                        ),
                    ],
                ),
            ],
        ),
        Period(
            name="Independencia y Venezuela",
            levels=[
                Level(
                    name="Campañas Libertadoras",
                    questions=[
                        Question(
                            prompt="¿Quién lideró la Campaña Admirable en 1813?",
                            options=["Simón Bolívar", "José de San Martín", "Francisco Miranda", "Antonio José de Sucre"],
                            answer="Simón Bolívar",
                            feedback="La Campaña Admirable consolidó el liderazgo de Bolívar.",
                        ),
                        Question(
                            prompt="¿Qué batalla aseguró la independencia de Venezuela en 1821?",
                            options=["Carabobo", "Boyacá", "Junín", "Pichincha"],
                            answer="Carabobo",
                            feedback="Carabobo fue decisiva para la independencia venezolana.",
                        ),
                        Question(
                            prompt="¿Cuál era el objetivo principal del Congreso de Angostura?",
                            options=[
                                "Crear un gobierno central para la Gran Colombia",
                                "Restaurar la monarquía española",
                                "Dividir el territorio en virreinatos",
                                "Declarar la guerra a Portugal",
                            ],
                            answer="Crear un gobierno central para la Gran Colombia",
                            feedback="El Congreso de Angostura sentó bases institucionales.",
                        ),
                        Question(
                            prompt="¿Qué figura es conocida como la Libertadora del Libertador?",
                            options=["Manuela Sáenz", "Luisa Cáceres", "Juana Ramírez", "Josefa Camejo"],
                            answer="Manuela Sáenz",
                            feedback="Manuela Sáenz apoyó a Bolívar en momentos clave.",
                        ),
                    ],
                ),
            ],
        ),
    ]


def choose_option(prompt: str, options: list[str]) -> int:
    while True:
        print(f"\n{prompt}")
        for idx, option in enumerate(options, start=1):
            print(f"  {idx}. {option}")
        choice = input("Selecciona una opción: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return int(choice) - 1
        print("Opción inválida. Intenta nuevamente.")


def load_game() -> dict | None:
    if not SAVE_FILE.exists():
        return None
    with SAVE_FILE.open("r", encoding="utf-8") as file_handle:
        return json.load(file_handle)


def save_game(period_index: int, level_index: int, score: int) -> None:
    data = {
        "period_index": period_index,
        "level_index": level_index,
        "score": score,
    }
    with SAVE_FILE.open("w", encoding="utf-8") as file_handle:
        json.dump(data, file_handle, indent=2, ensure_ascii=False)


def play_level(level: Level) -> int:
    lives = 3
    score = 0
    print(f"\nIniciando nivel: {level.name}")
    for question in level.questions:
        if lives == 0:
            break
        answer_index = choose_option(question.prompt, question.options)
        selected = question.options[answer_index]
        if selected == question.answer:
            score += 10
            print("✅ ¡Correcto!", question.feedback)
        else:
            lives -= 1
            print(f"❌ Respuesta incorrecta. {question.feedback}")
            print(f"Vidas restantes: {lives}")
            if lives > 0:
                print("¡Ánimo! Puedes seguir intentándolo.")
    if lives == 0:
        print("El personaje se pone triste, pero puedes intentarlo de nuevo.")
    else:
        print("¡Felicidades! Has completado el nivel.")
    print(f"Puntaje obtenido: {score}")
    return score


def start_new_game(periods: list[Period]) -> None:
    period_index = choose_option(
        "Selecciona el período histórico:",
        [period.name for period in periods],
    )
    levels = periods[period_index].levels
    level_index = choose_option(
        "Selecciona el nivel:",
        [level.name for level in levels],
    )
    score = play_level(levels[level_index])
    save_game(period_index, level_index, score)
    print("Partida guardada.")


def resume_game(periods: list[Period]) -> None:
    data = load_game()
    if data is None:
        print("No hay partidas guardadas.")
        return
    period_index = data.get("period_index", 0)
    level_index = data.get("level_index", 0)
    score = data.get("score", 0)
    print(
        "\nReanudando partida guardada:"
        f"\nPeríodo: {periods[period_index].name}"
        f"\nNivel: {periods[period_index].levels[level_index].name}"
        f"\nPuntaje previo: {score}"
    )
    score += play_level(periods[period_index].levels[level_index])
    save_game(period_index, level_index, score)
    print("Partida actualizada.")


def main() -> None:
    periods = build_periods()
    while True:
        print("\n=== Juego de Historia Universal ===")
        option = choose_option(
            "Menú principal:",
            ["Iniciar nueva partida", "Cargar partida", "Salir"],
        )
        if option == 0:
            start_new_game(periods)
        elif option == 1:
            resume_game(periods)
        else:
            print("Gracias por jugar. ¡Hasta pronto!")
            break


if __name__ == "__main__":
    main()
