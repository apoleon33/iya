const img = document.getElementById("icon");
const nameCharacter = document.getElementById("name");
const iterationCount = document.getElementById("compt");
const statAge = document.getElementById("averageAge");

let iteration = 0;
let [numberOfSmash, numberOfPass] = [[0], [0]];
console.log(numberOfPass, numberOfSmash);
var chart = new Chart("myChart", {
  type: "line",

  options: {
    legend: {
      display: true,
    },
    title: {
      display: true,
      text: "choices made for the last 20 characters",
    },
  },
});

function sendToServer(statusChoice) {
  if (statusChoice) {
    numberOfPass.push(numberOfPass[numberOfPass.length - 1]);
    numberOfSmash.push(numberOfSmash[numberOfSmash.length - 1] + 1);
  } else {
    numberOfPass.push(numberOfPass[numberOfPass.length - 1] + 1);
    numberOfSmash.push(numberOfSmash[numberOfSmash.length - 1]);
  }

  let data = { status: statusChoice };
  fetch("/choice", {
    // send results to server.py
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });

  fetch("/image") // get the new image to display with the name
    .then(function (response) {
      return response.json();
    })
    .then(function (text) {
      iteration += 1;
      img.src = text.url;
      nameCharacter.textContent = `character name: ${text.name}`;
      iterationCount.textContent = `iteration count: ${iteration}`;
    });

  fetch("/stats") // get the average age smashed
    .then(function (response) {
      return response.json();
    })
    .then(function (text) {
      if (numberOfPass.length > 50) {
        statistic(numberOfSmash.slice(-20), numberOfPass.slice(-20)); // last 20 elements of the array
        statAge.textContent = `average age smashed: ${text.averageAge}`;
      } else {
        statAge.textContent = "statistics are not available under 50 choice";
      }
    });
}

function statistic(smash, pass) {
  let xValues = [];
  console.log(smash, pass);
  for (let i = 0; i < smash.length; i++) {
    xValues.push(i);
  }
  xValues = xValues.slice(-20);

  chart.data = {
    labels: xValues,
    datasets: [
      {
        label: "smashed",
        data: smash,
        borderColor: "#363B52",
        fill: true,
      },
      {
        label: "passed",
        data: pass,
        borderColor: "#731C22",
        fill: false,
      },
    ],
  };
  chart.update();
}
