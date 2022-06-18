const img = document.getElementById("icon");
const nameCharacter = document.getElementById("name");
const iterationCount = document.getElementById("compt");

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
      img.src = text.url;
      nameCharacter.textContent = text.name;
      iterationCount.textContent = `iteration count: ${text.iteration}`;
    });
}
