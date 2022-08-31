import React from "react";
import Menu from "./Menu";

class ThunderBolt extends React.Component {
  constructor() {
    super();
    this.state = { name: "", url: "", iteration: 0 };
    this.getBestCharacter = this.getBestCharacter.bind(this);
  }

  componentDidUpdate() {
    if (this.state.iteration === 0) {
      this.getBestCharacter();
      this.setState({ iteration: 1 });
    }
  }

  async getBestCharacter() {
    let response = await fetch("/api/bestCharacter");
    let data = await response.json();
    this.setState({
      name: data.name,
      url: data.url,
    });
  }

  render() {
    return (
      <div className="Thunderbolt">
        <h2>Perhaps {this.state.name} is the perfect choice?</h2>
        <div id="imgWrapper" className="imageWrapper">
          <img
            src={this.state.url}
            className="image"
            alt="failed to render :("
          ></img>
        </div>
      </div>
    );
  }
}

export default class Statistics extends React.Component {
  constructor() {
    super();
    this.data = 0;
    this.state = {
      averageAge: "",
      averageSex: "",
      preferedCloth: "",
      iterationCount: 0,
      preferredHairColor: "",
    };
    this.getData = this.getData.bind(this);
  }

  componentDidMount() {
    this.getData();
  }

  async getData() {
    let response = await fetch("/api/stats");
    this.data = await response.json();
    this.setState({
      averageAge: this.data.averageAge.toLowerCase(),
      averageSex: this.data.averageSex.toLowerCase(),
      iterationCount: this.data.iterationCount,
      preferedCloth: this.data.preferedCloth.toLowerCase(),
      preferredHairColor: this.data.preferredHairColor.toLowerCase(),
    });
  }

  render() {
    return (
      <div>
        <Menu />
        <div className="Statistics">
          <h1 id="textPreferredCharacter">
            Out of the {this.state.iterationCount} character you smashed or
            passed, we can conclude you like {this.state.averageAge}{" "}
            {this.state.averageSex} with {this.data.preferredHairColor} hairs.
          </h1>
          <ThunderBolt />
        </div>
      </div>
    );
  }
}
