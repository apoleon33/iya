import React from "react";
import TinderCard from "react-tinder-card";

import Menu from "./Menu";

let [numberOfSmash, numberOfPass] = [[0], [0]];

const onCardLeftScreen = (myIdentifier) => {
  console.log(myIdentifier + " left the screen");
};

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      url: "",
    };
    this.smash = this.smash.bind(this);
    this.pass = this.pass.bind(this);
    this.onSwipe = this.onSwipe.bind(this);
  }

  componentDidMount() {
    this.getCharacterImg();
  }

  componentWillUnmount() {
    clearInterval(this.timerID);
  }

  onSwipe = (direction) => {
    console.log("You swiped: " + direction);
    if (direction === "right") {
      this.smash();
    } else {
      this.pass();
    }
  };

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
      <div>
        <Menu />
        <div id="mainAndInfoWrapper" className="App">
          <main>
            <TinderCard
              onSwipe={this.onSwipe}
              onCardLeftScreen={() => onCardLeftScreen("fooBar")}
              preventSwipe={["right", "left"]}
              flickOnSwipe={true}
            >
              <div id="iconWrapper" className="imageWrapper">
                <img
                  id="icon"
                  className="image"
                  src={this.state.url}
                  alt={`Failed to render url ${this.state.url} :(`}
                />
                <div id="blurEffect">
                  <h3 id="name">{this.state.name}</h3>
                </div>
              </div>
            </TinderCard>
          </main>
          <div id="buttonWrapper">
            <button onClick={this.pass}>pass</button>
            <button onClick={this.smash}>smash</button>
          </div>
        </div>
      </div>
    );
  }
}

export default App;
