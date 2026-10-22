const BASE_URL = "https://guiafacilmaua.onrender.com";
// const BASE_URL = "http://127.0.0.1:8000";

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

carregarMenu();
