const img = document.getElementById("icon");
const nameCharacter = document.getElementById("name");
const iterationCount = document.getElementById("compt");
const statAge = document.getElementById("averageAge");

let iteration = 0;

var chart = new Chart("myChart", {
  type: "line",

  options: {
    legend: { display: false },
  },
});

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

  fetch("/stats")
    .then(function (response) {
      return response.json();
    })
    .then(function (text) {
      statistic(text.smash, text.pass);
      statAge.textContent = `average age smashed: ${text.averageAge}`;
    });
}

function statistic(smash, pass) {
  let xValues = [];
  for (let i = 0; i < smash.length; i++) {
    xValues.push(i);
  }

  chart.data = {
    labels: xValues,
    datasets: [
      {
        data: smash,
        borderColor: "#363B52",
        fill: true,
      },
      {
        data: pass,
        borderColor: "#731C22",
        fill: false,
      },
    ],
  };
  chart.update();
}
