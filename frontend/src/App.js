import "./style.scss";

function App() {
  return (
    <main>
      <button onclick="sendToServer(false)">pass</button>
      <p></p>
      <div id="iconWrapper">
        <img id="icon" src="{{imgUrl}}" alt="a waifu" />
      </div>
      <p></p>
      <button onclick="sendToServer(true)">smash</button>
    </main>
  );
}

function Info() {
  return (
    <div id="info">
      <h1 id="name">character name:</h1>
      <h1 id="compt">iteration count:</h1>
    </div>
  );
}

function Statistic() {
  return (
    <div id="stats">
      <h1>Statistics:</h1>
      <div id="statWrapper">
        <div id="chartWrapper">
          <canvas id="myChart"></canvas>
        </div>
        <div id="textStatistic">
          <h2 id="averageAge">statistics are not available under 50 choice</h2>
          <h2 id="averageSex"></h2>
          <h2 id="preferedCloth"></h2>
        </div>
      </div>
    </div>
  );
}

export { App, Info, Statistic };
