const BASE_URL = "https://guiafacilmaua.onrender.com";
// const BASE_URL = "http://127.0.0.1:8000";

var carregado = false;

function timerInicial() {
  let tempoEsperaDesejavelCarregamento = 3;
  let tempoMaxCarregamento = 55 + tempoEsperaDesejavelCarregamento; // segundos
  let tempoRestante = tempoMaxCarregamento;

  const timer = setInterval(() => {

    if (carregado === true) {
      timer = null;
      document.getElementById("erro-menu").textContent = "Site carregado. Aproveite!";
      clearInterval(timer)
    }

    if (tempoRestante > 0) {
      tempoRestante -= 1;

      if ((tempoMaxCarregamento - tempoRestante) >= tempoEsperaDesejavelCarregamento) {
        document.getElementById("erro-menu").textContent = `Conectando ao site... Tempo estimado: ${tempoRestante} segundos.`;
      }

    } else {
      timer = null;
      document.getElementById("erro-menu").textContent = "Por favor, recarregue a página";
      clearInterval(timer)
    }

  }, 1000) // 1000 milisegundos (1 segundo)
}

async function carregarMenu() {
  try {
    const respostaServicos = await fetch(`${BASE_URL}/services`);
    const respostaSuporte = await fetch(`${BASE_URL}/support`);
    const respostaDescricoes = await fetch(`${BASE_URL}/services/descriptions`);

    if (!respostaServicos.ok || !respostaSuporte.ok || !respostaDescricoes.ok) {
      throw new Error("Erro ao buscar os dados do menu na API");
    }

    const servicos = await respostaServicos.json();
    const suporte = await respostaSuporte.json();
    const descricoes = await respostaDescricoes.json();

    if (!servicos[0] || !servicos[1] || !suporte[0] || !descricoes[0] || !descricoes[1]) {
      throw new Error("A API não retornou todos os dados do menu");
    }

    document.getElementById("nome-atende").textContent = servicos[0];
    document.getElementById("nome-inss").textContent = servicos[1];
    document.getElementById("nome-suporte").textContent = suporte[0];
    document.getElementById("descricao-atende").textContent = descricoes[0];
    document.getElementById("descricao-inss").textContent = descricoes[1];
    carregado = true;

  } catch (erro) {
    console.error(erro);
    document.getElementById("nome-atende").textContent = "Nome indisponível";
    document.getElementById("nome-inss").textContent = "Nome indisponível";
    document.getElementById("nome-suporte").textContent = "Nome indisponível";
    document.getElementById("descricao-atende").textContent = "Descrição indisponível";
    document.getElementById("descricao-inss").textContent = "Descrição indisponível";
    document.getElementById("erro-menu").textContent =
      "Não foi possível carregar o menu. Verifique se a API está ligada e atualize a página.";
  }
}

timerInicial()
carregarMenu();
