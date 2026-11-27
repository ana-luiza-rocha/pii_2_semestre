const chat = document.getElementById("chatbot");
const message = document.getElementById("chatbot-message");
const options = document.getElementById("chatbot-options");
const form = document.getElementById("chatbot-form");
const comment = document.getElementById("chatbot-comment");
const scoreStars = document.getElementById("chatbot-score-stars");
const scoreAviso = document.getElementById("chatbot-score-aviso");
const scoreValue = document.getElementById("chatbot-score-value");
const status = document.getElementById("chatbot-status");
const retry = document.getElementById("chatbot-retry");

const BASE_URL = location.hostname === "localhost" || location.hostname === "127.0.0.1"
  ? ""
  : "https://guiafacilmaua.onrender.com";

let currentStep = null;
let stepHistory = [];
let drafts = {};
let selectedScore = "";
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

function updateStarRating() {

  if (!scoreStars) {
    return
  }

  const rating = Number(selectedScore);
  for (const button of scoreStars.querySelectorAll("button")) {
    const value = Number(button.dataset.score);
    button.querySelector("span").textContent = selectedScore && value <= rating ? "★" : "☆";
    button.setAttribute("aria-pressed", String(value === rating && Boolean(selectedScore)));
  }
  if (selectedScore) {
    scoreValue.textContent = rating * 20 + "%";
  } else {
    scoreValue.textContent = "0%";
  }
}

function showStep() {
  const stepVideo = currentStep.video_path || (currentStep.code === "AM_OFM_01"
    ? "videos/Obter_ficha_medica_atende_mais.mp4"
    : null);
  const stepLink = currentStep.link || null;
  message.replaceChildren();
  document.getElementById("chatbot-aviso").hidden = currentStep.input_type !== "comment";
  const rotulo = document.getElementById("rotulo-comentario");
  if (currentStep.input_type === "score") {
    rotulo.textContent = "Seu comentário";
  } else if (currentStep.code === "FB_ES_01") {
    rotulo.textContent = "Sua sugestão";
  } else if (currentStep.code === "FB_FR_01") {
    rotulo.textContent = "Sua reclamação";
  } else if (currentStep.code === "FB_EE_01") {
    rotulo.textContent = "Seu elogio";
  } else {
    rotulo.textContent = "Sua mensagem";
  }
  for (const text of currentStep.messages || [currentStep.message]) {
    let frase = text;
    if (frase === "Conte para a gente o que você acha que pode melhorar no Guia Fácil") {
      frase = frase + ".";
    }
    const bubble = document.createElement("div");
    bubble.className = "balao";
    bubble.textContent = frase;
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
  showMedia({ ...currentStep, video_path: stepVideo, link: stepLink });
  options.replaceChildren();
  sendTarget = null;

  const isComment = currentStep.input_type === "comment";
  const isScore = currentStep.input_type === "score";
  form.hidden = !isComment && !isScore;
  document.getElementById("comment-field").hidden = !isComment && !isScore;
  document.getElementById("score-field").hidden = !isScore;
  scoreAviso.textContent = "";
  scoreAviso.hidden = true;
  comment.disabled = !isComment && !isScore;
  comment.required = isComment;

  const draft = drafts[currentStep.code] || { comment: "", score: "" };
  comment.value = draft.comment;
  selectedScore = draft.score;
  updateStarRating();
  updateCounter();

  for (const option of currentStep.options || []) {
    const target = option["next step"];
    if (option.text === "Continuar" && target === currentStep["next step"]) continue;
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
  const hasHomeOption = (currentStep.options || []).some(function (option) {
    return option["next step"] === "MENU";
  });
  if (stepHistory.length > 1 && !hasHomeOption) {
    createButton("Voltar à pergunta anterior", function () {
      loadStep(stepHistory[stepHistory.length - 2], true);
    });
  }
  message.focus();
}

async function loadStep(code, goingBack = false) {
  if (loading) return;
  if (currentStep) {
    drafts[currentStep.code] = { comment: comment.value, score: selectedScore };
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

    if (step.message === "Precisa de ajuda com mais alguma coisa?") {
      let destino = "";
      for (const option of step.options || []) {
        if (option.text === "Não") {
          destino = option["next step"];
        }
      }
      if (destino) {
        const resposta = await fetch(`${BASE_URL}/steps/${destino}`);
        const seguinte = await resposta.json();
        if (!resposta.ok) throw new Error("Etapa não encontrada.");
        step = seguinte;
      }
    }

    if (step.message === "Espero ter ajudado! Se precisar novamente, estarei por aqui! Até a próxima!") {
      step.message = "Espero ter ajudado! Se precisar novamente, estarei por aqui. Até a próxima!";
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
    status.textContent = "Não conseguimos carregar a conversa... Tente atualizar a página daqui 15 segundos."
    retry.hidden = false;
    retry.onclick = function () {
      loadStep(code, goingBack);
    };
  } finally {
    setLoading(false);
  }
}

async function sendAnswer() {
  if (loading || !form.reportValidity() || !sendTarget) return;

  const answer = {
    submission_id: submissionId,
    step_code: currentStep.code,
    comment: "",
    score: null,
    chat_history: stepHistory.slice(-200),
  };
  if (currentStep.input_type === "comment" || currentStep.input_type === "score") {
    answer.comment = comment.value;
  }
  if (currentStep.input_type === "score") {
    answer.score = Number(selectedScore);
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

const confirmacao = document.getElementById("confirmacao");

function abrirConfirmacao() {
  const perguntas = {
    FB_ES_01: "Deseja enviar esta sugestão?",
    FB_FR_01: "Deseja enviar esta reclamação?",
    FB_EE_01: "Deseja enviar este elogio?"
  };
  const avaliacao = currentStep.input_type === "score";
  if (avaliacao) {
    document.getElementById("confirmacao-titulo").textContent = "Deseja enviar esta avaliação?";
    document.getElementById("confirmacao-texto").textContent = "Você poderá voltar e alterar a avaliação antes de enviar.";
  } else {
    document.getElementById("confirmacao-titulo").textContent = perguntas[currentStep.code];
    document.getElementById("confirmacao-texto").textContent = "Você poderá voltar e alterar o texto antes de enviar.";
  }
  document.getElementById("icone-sugestao").hidden = currentStep.code !== "FB_ES_01";
  document.getElementById("icone-reclamacao").hidden = currentStep.code !== "FB_FR_01";
  document.getElementById("icone-elogio").hidden = currentStep.code !== "FB_EE_01";
  document.getElementById("icone-avaliacao").hidden = !avaliacao;
  confirmacao.classList.add("aberto");
  document.getElementById("confirmar-voltar").focus();
}

function fecharConfirmacao() {
  confirmacao.classList.remove("aberto");
  comment.focus();
}

function pedirEnvio(event) {
  event.preventDefault();
  if (loading || !form.reportValidity() || !sendTarget) return;
  if (currentStep.input_type === "score" && !selectedScore) {
    status.textContent = "";
    scoreAviso.textContent = "Escolha uma nota de 1 a 5 estrelas.";
    scoreAviso.hidden = false;
    return;
  }
  if ((currentStep.input_type === "comment" || currentStep.input_type === "score") && confirmacao) {
    abrirConfirmacao();
    return;
  }
  sendAnswer();
}

if (confirmacao) {
  document.getElementById("confirmar-voltar").onclick = fecharConfirmacao;
  document.getElementById("confirmar-enviar").onclick = function () {
    confirmacao.classList.remove("aberto");
    sendAnswer();
  };
  confirmacao.onclick = function (event) {
    if (event.target === confirmacao) {
      fecharConfirmacao();
    }
  };
}

form.onsubmit = pedirEnvio;
comment.oninput = updateCounter;
const botoesNota = document.querySelectorAll("#chatbot-score-stars button");
for (const botao of botoesNota) {
  botao.onclick = function () {
    if (loading) return;
    selectedScore = botao.dataset.score;
    updateStarRating();
    updateCounter();
    status.textContent = "";
    scoreAviso.textContent = "";
    scoreAviso.hidden = true;
  };
}
startConversation();
