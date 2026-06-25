import "./style.css";

const button = document.querySelector<HTMLButtonElement>("#draw-button");
const resultArea = document.querySelector<HTMLDivElement>("#result");

button?.addEventListener("click", async () => {
  const response = await fetch("http://127.0.0.1:8000/fortune");
  const data = await response.json();

  if (resultArea) {
    resultArea.innerHTML = `
      <p class="result-title">${data.result}</p>
      <p class="result-message">${data.message}</p>
    `;
  }
});