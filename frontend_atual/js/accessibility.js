const decreaseButton = document.querySelector('[data-action="decrease-font"]');
const increaseButton = document.querySelector('[data-action="increase-font"]');
const themeButton = document.querySelector('[data-action="toggle-theme"]');
const preferencesStatus = document.getElementById("preferences-status");

let fontSize = 17;
let theme = "light";

try {
  const saved = JSON.parse(localStorage.getItem("guia-preferences"));

  if (saved) {
    if (Number.isInteger(saved.font_size) && saved.font_size >= 15 && saved.font_size <= 25) {
      fontSize = saved.font_size;
    }
    if (saved.theme === "light" || saved.theme === "dark") {
      theme = saved.theme;
    }
  }
} catch (error) {
  preferencesStatus.textContent = "Não foi possível ler as preferências salvas.";
}

function applyPreferences() {
  document.documentElement.style.setProperty("--font-size", fontSize + "px");
  document.documentElement.dataset.theme = theme;
  decreaseButton.disabled = fontSize === 15;
  increaseButton.disabled = fontSize === 25;
  themeButton.setAttribute("aria-pressed", String(theme === "dark"));

  if (theme === "dark") {
    themeButton.setAttribute("aria-label", "Modo claro");
  } else {
    themeButton.setAttribute("aria-label", "Modo escuro");
  }
}

function savePreferences() {
  applyPreferences();

  try {
    localStorage.setItem("guia-preferences", JSON.stringify({
      font_size: fontSize,
      theme: theme,
    }));
    preferencesStatus.textContent = "";
  } catch (error) {
    preferencesStatus.textContent = "A aparência foi alterada, mas o navegador não permitiu salvar.";
  }
}

decreaseButton.addEventListener("click", () => {
  fontSize = Math.max(15, fontSize - 2);
  savePreferences();
});

increaseButton.addEventListener("click", () => {
  fontSize = Math.min(25, fontSize + 2);
  savePreferences();
});

themeButton.addEventListener("click", () => {
  if (theme === "light") {
    theme = "dark";
  } else {
    theme = "light";
  }
  savePreferences();
});

applyPreferences();
