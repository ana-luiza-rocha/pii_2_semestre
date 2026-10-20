function showMedia(step) {
  const media = document.getElementById("chatbot-media");
  media.replaceChildren();

  function getUrl(path) {
    if (!path) return null;
    try {
      const url = new URL(path, window.location.href);
      if (url.protocol === "http:" || url.protocol === "https:") {
        return url.href;
      }
    } catch (error) {
      return null;
    }
    return null;
  }

  const videoUrl = getUrl(step.video_path);
  const websiteUrl = getUrl(step.website_path);

  if (videoUrl) {
    const video = document.createElement("video");
    video.controls = true;
    video.src = videoUrl;
    media.appendChild(video);
  }

  if (websiteUrl) {
    const link = document.createElement("a");
    link.className = "opcao";
    link.textContent = "Abrir site em outra aba";
    link.href = websiteUrl;
    link.target = "_blank";
    link.rel = "noopener noreferrer";
    media.appendChild(link);
  }

  const note = document.createElement("p");
  note.className = "chatbot-note";
  if (!videoUrl && step.message.toLowerCase().includes("vídeo")) {
    note.textContent = "O vídeo deste passo ainda não foi adicionado.";
  } else if (!websiteUrl && /clique no botão|toque no botão/i.test(step.message)) {
    note.textContent = "O link deste passo ainda não foi adicionado.";
  }
  if (note.textContent) media.appendChild(note);
}
