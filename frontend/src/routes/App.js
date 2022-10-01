import React from "react";
import TinderCard from "react-tinder-card";
import { BsXLg, BsSuitHeartFill } from "react-icons/bs";

import Footer from "./Footer";
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
      origin: "",
    };
    this.smash = this.smash.bind(this);
    this.pass = this.pass.bind(this);
    this.onSwipe = this.onSwipe.bind(this);
  }

  componentDidMount() {
    this.getCharacterImg();
    document.addEventListener("keyup", this.keyboardEvents.bind(this));
  }

  componentWillUnmount() {
    clearInterval(this.timerID);
    document.removeEventListener("keyup", this.keyboardEvents.bind(this));
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
          origin: data.origin,
        });
      })
    );
  }

  keyboardEvents(event) {
    switch (event.key) {
      case "ArrowLeft":
        this.pass();
        break;
      case "ArrowRight":
        this.smash();
        break;
      default:
        console.log(event.key);
        return;
    }
  }

  render() {
    return (
      <div id="wrap">
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
                  <h3 id="name" className="textOnImage">
                    {this.state.name} from {this.state.origin}
                  </h3>
                </div>
              </div>
            </TinderCard>
          </main>
          <div id="buttonWrapper">
            <button onClick={this.pass} id="cross-button">
              {" "}
              <BsXLg id="cross-icon" />
            </button>
            <button onClick={this.smash} id="valid-button">
              <BsSuitHeartFill id="valid-icon" />
            </button>
          </div>
        </div>
        <Footer />
      </div>
    );
  }
}

export default App;
