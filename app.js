const SAVE_KEY = "historia-save";

const state = {
  periods: [
    {
      name: "Antigüedad",
      description: "Civilizaciones iniciales y aportes culturales.",
      level: {
        name: "Civilizaciones Iniciales",
        questions: [
          {
            prompt: "¿Cuál de estas civilizaciones se desarrolló junto al río Nilo?",
            options: ["Mesopotamia", "Egipto", "China", "Grecia"],
            answer: "Egipto",
            feedback: "Egipto se consolidó gracias a las crecidas del Nilo.",
          },
          {
            prompt: "¿Qué invento permitió registrar leyes y comercio?",
            options: ["La escritura", "La brújula", "La pólvora", "La rueda"],
            answer: "La escritura",
            feedback: "La escritura impulsó la organización social.",
          },
          {
            prompt: "¿En qué región surgió la civilización mesopotámica?",
            options: [
              "Entre los ríos Tigris y Éufrates",
              "En los Andes",
              "En el Sahara",
              "En la península Ibérica",
            ],
            answer: "Entre los ríos Tigris y Éufrates",
            feedback: "Mesopotamia significa literalmente ""entre ríos"".",
          },
        ],
      },
    },
    {
      name: "Independencia y Venezuela",
      description: "Campañas libertadoras y liderazgos clave.",
      level: {
        name: "Campañas Libertadoras",
        questions: [
          {
            prompt: "¿Quién lideró la Campaña Admirable en 1813?",
            options: ["Simón Bolívar", "Francisco Miranda", "José de San Martín", "Antonio José de Sucre"],
            answer: "Simón Bolívar",
            feedback: "La Campaña Admirable consolidó el liderazgo de Bolívar.",
          },
          {
            prompt: "¿Qué batalla aseguró la independencia de Venezuela en 1821?",
            options: ["Carabobo", "Boyacá", "Junín", "Pichincha"],
            answer: "Carabobo",
            feedback: "Carabobo fue decisiva para la independencia venezolana.",
          },
          {
            prompt: "¿Qué figura es conocida como la Libertadora del Libertador?",
            options: ["Manuela Sáenz", "Luisa Cáceres", "Juana Ramírez", "Josefa Camejo"],
            answer: "Manuela Sáenz",
            feedback: "Manuela Sáenz apoyó a Bolívar en momentos clave.",
          },
        ],
      },
    },
  ],
  currentPeriodIndex: 0,
  currentQuestionIndex: 0,
  lives: 3,
  score: 0,
};

const periodsContainer = document.getElementById("periods");
const periodLabel = document.getElementById("periodLabel");
const levelLabel = document.getElementById("levelLabel");
const livesLabel = document.getElementById("lives");
const scoreLabel = document.getElementById("score");
const questionText = document.getElementById("questionText");
const optionsContainer = document.getElementById("options");
const feedbackText = document.getElementById("feedbackText");
const saveStatus = document.getElementById("saveStatus");

function renderPeriods() {
  periodsContainer.innerHTML = "";
  state.periods.forEach((period, index) => {
    const card = document.createElement("button");
    card.className = "period";
    card.innerHTML = `<strong>${period.name}</strong><span>${period.description}</span>`;
    card.addEventListener("click", () => {
      state.currentPeriodIndex = index;
      state.currentQuestionIndex = 0;
      state.lives = 3;
      state.score = 0;
      updateGame();
    });
    periodsContainer.appendChild(card);
  });
}

function updateStatus() {
  livesLabel.textContent = state.lives;
  scoreLabel.textContent = state.score;
  const period = state.periods[state.currentPeriodIndex];
  periodLabel.textContent = period.name;
  levelLabel.textContent = period.level.name;
}

function updateQuestion() {
  const period = state.periods[state.currentPeriodIndex];
  const question = period.level.questions[state.currentQuestionIndex];
  if (!question) {
    questionText.textContent = "¡Nivel completado!";
    optionsContainer.innerHTML = "";
    feedbackText.textContent = "Felicidades, desbloqueaste el siguiente reto.";
    saveGame();
    return;
  }
  questionText.textContent = question.prompt;
  optionsContainer.innerHTML = "";
  question.options.forEach((option) => {
    const button = document.createElement("button");
    button.className = "option";
    button.textContent = option;
    button.addEventListener("click", () => handleAnswer(option, question, button));
    optionsContainer.appendChild(button);
  });
  feedbackText.textContent = "Selecciona la opción correcta.";
}

function handleAnswer(selected, question, button) {
  const isCorrect = selected === question.answer;
  if (isCorrect) {
    state.score += 10;
    button.classList.add("option--correct");
    feedbackText.textContent = `✅ ${question.feedback}`;
  } else {
    state.lives -= 1;
    button.classList.add("option--wrong");
    feedbackText.textContent = `❌ ${question.feedback} Te quedan ${state.lives} vidas.`;
  }
  updateStatus();
  if (state.lives <= 0) {
    questionText.textContent = "Perdiste las vidas.";
    optionsContainer.innerHTML = "";
    feedbackText.textContent = "El personaje está triste, pero puedes intentarlo de nuevo.";
    saveGame();
    return;
  }
  setTimeout(() => {
    state.currentQuestionIndex += 1;
    updateQuestion();
  }, 700);
}

function updateGame() {
  updateStatus();
  updateQuestion();
}

function saveGame() {
  const payload = {
    currentPeriodIndex: state.currentPeriodIndex,
    currentQuestionIndex: state.currentQuestionIndex,
    lives: state.lives,
    score: state.score,
  };
  localStorage.setItem(SAVE_KEY, JSON.stringify(payload));
  saveStatus.textContent = "Partida guardada correctamente.";
}

function loadGame() {
  const raw = localStorage.getItem(SAVE_KEY);
  if (!raw) {
    saveStatus.textContent = "No hay partida guardada.";
    return false;
  }
  const payload = JSON.parse(raw);
  state.currentPeriodIndex = payload.currentPeriodIndex ?? 0;
  state.currentQuestionIndex = payload.currentQuestionIndex ?? 0;
  state.lives = payload.lives ?? 3;
  state.score = payload.score ?? 0;
  saveStatus.textContent = "Partida cargada.";
  return true;
}

function bindMenu() {
  document.querySelectorAll("[data-action]").forEach((button) => {
    button.addEventListener("click", () => {
      const action = button.dataset.action;
      if (action === "new") {
        state.currentQuestionIndex = 0;
        state.lives = 3;
        state.score = 0;
        updateGame();
        saveStatus.textContent = "Nueva partida iniciada.";
      }
      if (action === "resume") {
        if (loadGame()) {
          updateGame();
        }
      }
      if (action === "scores") {
        saveStatus.textContent = `Puntaje actual: ${state.score}`;
      }
    });
  });
}

renderPeriods();
bindMenu();
updateGame();
