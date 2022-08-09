import React from "react";
import Toggle from "react-toggle";

import Menu from "./Menu";

export default class Options extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      nsfwStatus: false,
    };

    this.nsfwToggle = this.nsfwToggle.bind(this);
    this.checkNsfwStatus = this.checkNsfwStatus.bind(this);
  }

  componentDidMount() {
    this.checkNsfwStatus();
  }

  async checkNsfwStatus() {
    let response = await fetch("/api/nsfwStatus");
    let jsoned = await response.json();
    this.setState({
      nsfwStatus: jsoned.nsfwStatus,
    });
  }

  nsfwToggle() {
    this.setState((prevState) => ({
      nsfwStatus: !prevState.nsfwStatus,
    }));
    fetch("/api/nsfw");
  }

  render() {
    return (
      <div>
        <Menu />
        <div id="options" className="Options">
          <h1> nsfw allowed:</h1>
          <div id="toggleWrapper">
            <Toggle
              checked={this.state.nsfwStatus}
              onChange={this.nsfwToggle}
            />
          </div>
        </div>
      </div>
    );
  }
}
