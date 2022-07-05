import React from "react";
import Info from "./Info";

let [numberOfSmash, numberOfPass] = [[0], [0]];

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      url: "",
    };
    this.smash = this.smash.bind(this);
    this.pass = this.pass.bind(this);
  }

  componentDidMount() {
    fetch("/").then((res) => {
      console.log(res.ok);
    });
    this.getCharacterImg();
  }

  componentWillUnmount() {
    clearInterval(this.timerID);
  }

  smash() {
    let data = { status: true };

    numberOfPass.push(numberOfPass[numberOfPass.length - 1]);
    numberOfSmash.push(numberOfSmash[numberOfSmash.length - 1] + 1);

    fetch("/api/choice", {
      // send results to server.py
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });

    this.getCharacterImg();
  }

  pass() {
    let data = { status: false };

    numberOfPass.push(numberOfPass[numberOfPass.length - 1] + 1);
    numberOfSmash.push(numberOfSmash[numberOfSmash.length - 1]);

    fetch("/api/choice", {
      // send results to server.py
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });

    this.getCharacterImg();
  }

  getCharacterImg() {
    fetch("/api/image").then((res) =>
      res.json().then((data) => {
        // getting a data from api
        this.setState({
          name: data.name,
          url: data.url,
        });
      })
    );
  }

  render() {
    return (
      <div id="mainAndInfoWrapper">
        <main>
          <button onClick={this.pass}>pass</button>
          <p></p>
          <div id="iconWrapper">
            <img
              id="icon"
              src={this.state.url}
              alt={`Failed to render url ${this.state.url} :(`}
            />
          </div>
          <p></p>
          <button onClick={this.smash}>smash</button>
        </main>
        <Info name={this.state.name} />
      </div>
    );
  }
}

/*
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
          <h2 id="averageSex"> </h2>
          <h2 id="preferedCloth"> </h2>
        </div>
      </div>
    </div>
  );
}*/

export default App;
