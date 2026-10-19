const chat = document.getElementById("chatbot");
const message = document.getElementById("chatbot-message");
const options = document.getElementById("chatbot-options");
const form = document.getElementById("chatbot-form");
const comment = document.getElementById("chatbot-comment");
const score = document.getElementById("chatbot-score");
const status = document.getElementById("chatbot-status");
const retry = document.getElementById("chatbot-retry");

let currentStep;
let stepHistory = [];
let drafts = {};
let submissionId;
let requestNumber = 0;

function createButton(text, action) {
  const button = document.createElement("button");
  button.type = "button";
  button.className = "opcao";
  button.textContent = text;
  button.onclick = action;
  options.appendChild(button);
  return button;
}

function setLoading(loading) {
  form.inert = loading;
  options.inert = loading;
  options.setAttribute("aria-busy", String(loading));
}

function showStep() {
  message.textContent = currentStep.message;
  showMedia(currentStep);
  options.replaceChildren();

  const isComment = currentStep.input_type === "comment";
  const isScore = currentStep.input_type === "score";
  form.hidden = !isComment && !isScore;
  document.getElementById("comment-field").hidden = !isComment;
  document.getElementById("score-field").hidden = !isScore;
  comment.disabled = !isComment;
  comment.required = isComment;
  score.disabled = !isScore;
  score.required = isScore;

  const draft = drafts[currentStep.code] || { comment: "", score: "" };
  comment.value = draft.comment;
  score.value = draft.score;
  updateCounter();

  for (const option of currentStep.options || []) {
    const target = option["next step"];
    if (target === "MENU" || option.text.includes("pergunta anterior")) continue;

    if (option.text === "Enviar" && currentStep.input_type) {
      const button = createButton("Enviar", null);
      button.type = "submit";
      button.setAttribute("form", "chatbot-form");
    } else if (target) {
      createButton(option.text, () => loadStep(target));
    } else {
      createButton(option.text + " (em breve)", null).disabled = true;
    }
  }

  if (currentStep["next step"]) {
    createButton("Continuar", () => loadStep(currentStep["next step"]));
  }
  if (stepHistory.length > 1) {
    createButton("Voltar à pergunta anterior", () => {
      loadStep(stepHistory[stepHistory.length - 2], true);
    });
  }
  message.focus();
}

async function loadStep(code, goingBack = false) {
  if (code === "MENU") {
    window.location.href = "index.html";
    return;
  }
  if (currentStep) {
    drafts[currentStep.code] = { comment: comment.value, score: score.value };
  }
  const request = ++requestNumber;
  setLoading(true);
  status.textContent = "Carregando...";
  retry.hidden = true;

  try {
    const response = await fetch("http://127.0.0.1:8000/steps/" + encodeURIComponent(code));
    const step = await response.json();
    if (!response.ok) throw new Error(step.detail || "Etapa não encontrada.");
    if (request !== requestNumber) return;

    if (goingBack) stepHistory.pop();
    else stepHistory.push(step.code);
    currentStep = step;
    showStep();
    status.textContent = "";
  } catch (error) {
    if (request !== requestNumber) return;
    status.textContent = "Não foi possível carregar a conversa. Confira a API e os dados do banco.";
    retry.hidden = false;
    retry.onclick = () => loadStep(code, goingBack);
  } finally {
    if (request === requestNumber) setLoading(false);
  }
}

async function sendAnswer(event) {
  event.preventDefault();
  if (!form.reportValidity()) return;
  const sendOption = currentStep.options.find(option => option.text === "Enviar");
  if (!sendOption || !sendOption["next step"]) return;

  const request = requestNumber;
  setLoading(true);
  status.textContent = "Enviando...";
  retry.hidden = true;
  try {
    const response = await fetch("http://127.0.0.1:8000/chatbot/answers", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        submission_id: submissionId,
        step_code: currentStep.code,
        comment: currentStep.input_type === "comment" ? comment.value : "",
        score: currentStep.input_type === "score" ? Number(score.value) : null,
        chat_history: stepHistory.slice(-200),
      }),
    });
    if (!response.ok) throw new Error("Não foi possível enviar.");
    if (request !== requestNumber) return;
    form.hidden = true;
    options.replaceChildren();
    await loadStep(sendOption["next step"]);
  } catch (error) {
    if (request === requestNumber) {
      status.textContent = "Não foi possível confirmar o envio. Sua resposta continua preenchida; tente novamente.";
    }
  } finally {
    if (request === requestNumber) setLoading(false);
  }
}

function updateCounter() {
  document.getElementById("chatbot-counter").textContent = comment.value.length + " / 2000 caracteres";
  submissionId = crypto.randomUUID();
}

function startConversation() {
  const firstSteps = {
    atende: "AM_1", "meu-inss": "MI_01", feedback: "FB_01", menu: "FB_01",
    sugestao: "FB_ES_01", reclamacao: "FB_FR_01", elogio: "FB_EE_01",
  };
  const service = window.location.hash.slice(1) || chat.dataset.service;
  stepHistory = [];
  drafts = {};
  currentStep = null;
  form.hidden = true;
  options.replaceChildren();
  loadStep(firstSteps[service] || firstSteps[chat.dataset.service]);
}

form.onsubmit = sendAnswer;
comment.oninput = updateCounter;
score.onchange = () => { submissionId = crypto.randomUUID(); };
window.addEventListener("hashchange", startConversation);
startConversation();
