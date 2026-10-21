const chat = document.getElementById("chatbot");
const message = document.getElementById("chatbot-message");
const options = document.getElementById("chatbot-options");
const form = document.getElementById("chatbot-form");
const comment = document.getElementById("chatbot-comment");
const score = document.getElementById("chatbot-score");
const status = document.getElementById("chatbot-status");
const retry = document.getElementById("chatbot-retry");

// const BASE_URL = "https://guiafacilmaua.onrender.com";
const BASE_URL = "http://127.0.0.1:8000";

let currentStep = null;
let stepHistory = [];
let drafts = {};
let submissionId;
let sendTarget;
let loading = false;

function createButton(text, action) {
  const button = document.createElement("button");
  button.type = "button";
  button.className = "opcao";
  button.textContent = text;
  button.onclick = action;
  options.appendChild(button);
  return button;
}

function setLoading(value) {
  loading = value;
  form.inert = value;
  options.inert = value;
  retry.disabled = value;
  options.setAttribute("aria-busy", String(value));
}

function updateCounter() {
  document.getElementById("chatbot-counter").textContent = comment.value.length + " / 2000 caracteres";
  submissionId = Date.now() + "-" + Math.random();
}

function showStep() {
  const stepLink = currentStep.link || (currentStep.code === "AM_OFM_03" ? {
    text: "Ver postos da SPTrans",
    subtext: "Abre o site da SPTrans",
    url: "https://www.sptrans.com.br/encontrar-posto?cat=atende",
  } : null);
  message.replaceChildren();
  for (const text of currentStep.messages || [currentStep.message]) {
    const bubble = document.createElement("div");
    bubble.className = "balao";
    bubble.textContent = text;
    message.appendChild(bubble);
  }
  if (stepLink) {
    const link = document.createElement("a");
    link.className = "balao chatbot-link-card";
    link.href = stepLink.url;
    link.target = "_blank";
    link.rel = "noopener noreferrer";

    const title = document.createElement("strong");
    title.textContent = stepLink.text;
    const subtitle = document.createElement("span");
    subtitle.textContent = stepLink.subtext;
    link.append(title, subtitle);
    message.appendChild(link);
  }
  showMedia({ ...currentStep, link: stepLink });
  options.replaceChildren();
  sendTarget = null;

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
    if (option.text.includes("pergunta anterior")) continue;

    if (target === "MENU") {
      createButton(option.text, function () {
        window.location.href = "index.html";
      });
    } else if (option.text === "Enviar" && currentStep.input_type) {
      sendTarget = target;
      const button = createButton("Enviar", null);
      button.type = "submit";
      button.setAttribute("form", "chatbot-form");
    } else if (target) {
      createButton(option.text, function () {
        loadStep(target);
      });
    } else {
      createButton(option.text + " (em breve)", null).disabled = true;
    }
  }

  if (currentStep["next step"]) {
    createButton("Continuar", function () {
      loadStep(currentStep["next step"]);
    });
  }
  if (stepHistory.length > 1) {
    createButton("Voltar à pergunta anterior", function () {
      loadStep(stepHistory[stepHistory.length - 2], true);
    });
  }
  message.focus();
}

async function loadStep(code, goingBack = false) {
  if (loading) return;
  if (currentStep) {
    drafts[currentStep.code] = { comment: comment.value, score: score.value };
  }
  setLoading(true);
  status.textContent = "Carregando...";
  retry.hidden = true;

  try {
    const response = await fetch(`${BASE_URL}/steps/${code}`);
    let step = await response.json();
    if (!response.ok) throw new Error("Etapa não encontrada.");

    if (step.show_with_next && step["next step"]) {
      const nextResponse = await fetch(`${BASE_URL}/steps/${step["next step"]}`);
      const nextStep = await nextResponse.json();
      if (!nextResponse.ok) throw new Error("Etapa não encontrada.");
      step = { ...nextStep, messages: [step.message, nextStep.message] };
    }

    if (goingBack) {
      stepHistory.pop();
    } else {
      stepHistory.push(step.code);
    }
    currentStep = step;
    showStep();
    status.textContent = "";
  } catch (error) {
    status.textContent = "Não foi possível carregar a conversa. Confira a API e os dados do banco.";
    retry.hidden = false;
    retry.onclick = function () {
      loadStep(code, goingBack);
    };
  } finally {
    setLoading(false);
  }
}

async function sendAnswer(event) {
  event.preventDefault();
  if (loading || !form.reportValidity() || !sendTarget) return;

  const answer = {
    submission_id: submissionId,
    step_code: currentStep.code,
    comment: "",
    score: null,
    chat_history: stepHistory.slice(-200),
  };
  if (currentStep.input_type === "comment") {
    answer.comment = comment.value;
  } else {
    answer.score = Number(score.value);
  }

  setLoading(true);
  status.textContent = "Enviando...";
  retry.hidden = true;
  try {
    const response = await fetch(`${BASE_URL}/chatbot/answers`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(answer),
    });
    if (!response.ok) throw new Error("Não foi possível enviar.");
    form.hidden = true;
    options.replaceChildren();
    setLoading(false);
    await loadStep(sendTarget);
  } catch (error) {
    status.textContent = "Não foi possível confirmar o envio. Sua resposta continua preenchida; tente novamente.";
  } finally {
    setLoading(false);
  }
}

function startConversation() {
  const firstSteps = {
    atende: "AM_1",
    "meu-inss": "MI_01",
    feedback: "FB_01",
    menu: "FB_01",
    sugestao: "FB_ES_01",
    reclamacao: "FB_FR_01",
    elogio: "FB_EE_01",
  };
  const service = window.location.hash.slice(1) || chat.dataset.service;
  loadStep(firstSteps[service] || firstSteps[chat.dataset.service]);
}

form.onsubmit = sendAnswer;
comment.oninput = updateCounter;
score.onchange = updateCounter;
startConversation();
