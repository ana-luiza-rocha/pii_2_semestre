const CATEGORIAS = {
  saude: {
    nome: "Saúde",
    icone: '<svg viewBox="0 0 24 24"><path d="M9 3h6v6h6v6h-6v6H9v-6H3V9h6z"/></svg>',
    perguntas: [
      "Como baixar o app e-Saúde SP?",
      "Como agendar uma consulta?",
      "Como ver o cartão de vacinação?",
      "Como marcar um exame?",
    ],
  },
  dinheiro: {
    nome: "Dinheiro",
    icone: '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M15 9.5c-.5-1-1.7-1.5-3-1.5-1.7 0-3 .9-3 2.2 0 3 6 1.5 6 4.3 0 1.3-1.3 2.2-3 2.2-1.4 0-2.6-.6-3-1.7M12 6v2M12 16v2"/></svg>',
    perguntas: [
      "Como fazer um Pix?",
      "Como consultar meu saldo?",
      "Como pagar um boleto pelo celular?",
      "Como evitar golpes?",
    ],
  },
  carro: {
    nome: "Carro",
    icone: '<svg viewBox="0 0 24 24"><path d="M4 16v-4l2-5h12l2 5v4zM4 12h16"/><circle cx="8" cy="16" r="1.5"/><circle cx="16" cy="16" r="1.5"/></svg>',
    perguntas: [
      "Como consultar multas?",
      "Como pagar o IPVA?",
      "Como renovar a CNH?",
    ],
  },
  apps: {
    nome: "Aplicativos",
    icone: '<svg viewBox="0 0 24 24"><rect x="7" y="2" width="10" height="20" rx="2"/><path d="M11 18h2"/></svg>',
    perguntas: [
      "Como baixar um aplicativo?",
      "Como atualizar um aplicativo?",
      "Como criar uma conta gov.br?",
      "Como pedir um carro por aplicativo?",
    ],
  },
};

const PERGUNTA_INICIAL = "Com o que você quer ajuda hoje?";
const PERGUNTA_FORMATO = "Você quer ver um vídeo ou um texto?";
const RESPOSTAS = {
  "Vídeo": "Aqui vai o vídeo com o passo a passo. (exemplo)",
  "Texto": "Aqui vai o passo a passo em texto. (exemplo)",
};

// elementos
const telaHome = document.getElementById("tela-home");
const telaChat = document.getElementById("tela-chat");
const listaCategorias = document.getElementById("categorias");
const listaPerguntas = document.getElementById("perguntas");
const conversa = document.getElementById("conversa");
const campoBusca = document.getElementById("busca");

// telas
function mostrarTela(tela) {
  telaHome.classList.toggle("ativa", tela === telaHome);
  telaChat.classList.toggle("ativa", tela === telaChat);
}

// home
function criarCategorias() {
  for (const [chave, categoria] of Object.entries(CATEGORIAS)) {
    const botao = document.createElement("button");
    botao.className = "categoria";
    botao.dataset.chave = chave;
    botao.setAttribute("aria-pressed", "false");
    botao.innerHTML = categoria.icone + "<span>" + categoria.nome + "</span>";
    botao.addEventListener("click", () => alternarCategoria(chave));
    listaCategorias.appendChild(botao);
  }
}

function alternarCategoria(chave) {
  const botoes = listaCategorias.querySelectorAll(".categoria");
  const estavaAberta = listaCategorias
    .querySelector('[data-chave="' + chave + '"]')
    .getAttribute("aria-pressed") === "true";

  // fecha tudo
  botoes.forEach((b) => b.setAttribute("aria-pressed", "false"));
  listaPerguntas.innerHTML = "";
  listaPerguntas.classList.remove("aberta");

  if (estavaAberta) return;

  // abre a categoria clicada
  listaCategorias
    .querySelector('[data-chave="' + chave + '"]')
    .setAttribute("aria-pressed", "true");

  CATEGORIAS[chave].perguntas.forEach((texto) => {
    const item = document.createElement("li");
    const botao = document.createElement("button");
    botao.textContent = texto;
    botao.addEventListener("click", () => iniciarChat(texto));
    item.appendChild(botao);
    listaPerguntas.appendChild(item);
  });
  listaPerguntas.classList.add("aberta");
}

// o chat
function adicionarMensagem(texto, autor) {
  const mensagem = document.createElement("div");
  mensagem.className = "msg " + autor; // "bot" ou "eu"
  mensagem.textContent = texto;
  conversa.appendChild(mensagem);
  mensagem.scrollIntoView({ block: "end" });
}

function adicionarOpcoes(opcoes) {
  const caixa = document.createElement("div");
  caixa.className = "opcoes";

  opcoes.forEach((texto) => {
    const botao = document.createElement("button");
    botao.textContent = texto;
    botao.addEventListener("click", () => {
      caixa.remove();
      adicionarMensagem(texto, "eu");
      setTimeout(() => adicionarMensagem(RESPOSTAS[texto], "bot"), 400);
    });
    caixa.appendChild(botao);
  });

  conversa.appendChild(caixa);
  caixa.scrollIntoView({ block: "end" });
}

function iniciarChat(pergunta) {
  conversa.innerHTML = "";
  mostrarTela(telaChat);

  adicionarMensagem(PERGUNTA_INICIAL, "bot");
  adicionarMensagem(pergunta, "eu");

  setTimeout(() => {
    adicionarMensagem(PERGUNTA_FORMATO, "bot");
    adicionarOpcoes(["Vídeo", "Texto"]);
  }, 400);
}

// busca
function buscar() {
  const texto = campoBusca.value.trim();
  if (!texto) return;
  campoBusca.value = "";
  iniciarChat(texto);
}
//p clicar la
document.getElementById("btn-buscar").addEventListener("click", buscar);
campoBusca.addEventListener("keydown", (e) => {
  if (e.key === "Enter") buscar();
});
document.getElementById("btn-voltar").addEventListener("click", () => mostrarTela(telaHome));

//tamanho da letra
let tamanhoLetra = 17;

function mudarLetra(passo) {
  tamanhoLetra = Math.min(26, Math.max(13, tamanhoLetra + passo));
  document.body.style.fontSize = tamanhoLetra + "px";
}

document.getElementById("btn-contraste").addEventListener("click", () => {
  document.body.classList.toggle("escuro");
});

document.getElementById("btn-aumentar").addEventListener("click", () => mudarLetra(2));
document.getElementById("btn-diminuir").addEventListener("click", () => mudarLetra(-2));

//inicio
criarCategorias();
