import "./style.css";

const button = document.querySelector<HTMLButtonElement>("#draw-button");
const resultArea = document.querySelector<HTMLDivElement>("#result");
const historyButton = document.querySelector<HTMLButtonElement>("#history-button");
const historyArea = document.querySelector<HTMLDivElement>("#history");

// おみくじを引く
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

// 履歴を見る
historyButton?.addEventListener("click", async () => {
  const response = await fetch("http://127.0.0.1:8000/history");
  const data = await response.json();

  if (historyArea) {
    historyArea.innerHTML = "<h2>これまでの占い</h2>";
    for (const item of data) {
      historyArea.innerHTML += `
        <div class="history-item">
          <span class="history-result">${item.result}</span>
          <span class="history-date">${item.created_at}</span>
        </div>
      `;
    }
  }
});