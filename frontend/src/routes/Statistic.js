import React from "react";
import Menu from "./Menu";

export default class Statistics extends React.Component {
  constructor() {
    super();
    this.data = 0;
    this.state = {
      averageAge: "",
      averageSex: "",
      preferedCloth: "",
      iterationCount: 0,
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
      averageAge: this.data.averageAge,
      averageSex: this.data.averageSex,
      iterationCount: this.data.iterationCount,
    });
  }

  render() {
    this.getData();
    return (
      <div>
        <Menu />
        <div className="Statistics">
          <h3>You passed/smashed {this.state.iterationCount} character</h3>
          <h3>most smashed age: {this.state.averageAge}</h3>
          <h3>most smashed sex: {this.state.averageSex}</h3>
        </div>
      </div>
    );
  }
}
