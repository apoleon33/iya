const img = document.getElementById("icon");
const nameCharacter = document.getElementById("name");
const iterationCount = document.getElementById("compt");
let iteration = 0;

function sendToServer(statusChoice) {
  let data = { status: statusChoice };
  fetch("/choice", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });

  fetch("/image")
    .then(function (response) {
      return response.json();
    })
    .then(function (text) {
      iteration += 1;
      img.src = text.url;
      nameCharacter.textContent = `character name: ${text.name}`;
      iterationCount.textContent = `iteration count: ${iteration}`;
    });
}
