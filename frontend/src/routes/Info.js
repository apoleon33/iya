import React from "react";
import Toggle from "react-toggle";

import Menu from "./Menu";

class Info extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      iteration: 0,
      oldName: this.props.name,
      nsfwStatus: false,
    };

    this.getCharacterNameAndIteration =
      this.getCharacterNameAndIteration.bind(this);

    this.nsfwToggle = this.nsfwToggle.bind(this);
  }

  getCharacterNameAndIteration() {
    if (this.state.oldName !== this.props.name) {
      this.setState({
        iteration: this.state.iteration + 1,
        oldName: this.props.name,
      });
    }
  }

  componentDidMount() {
    setInterval(() => this.getCharacterNameAndIteration(), 100);
  }

  nsfwToggle() {
    console.log(this.state.nsfwStatus);
    this.setState((prevState) => ({
      nsfwStatus: !prevState.nsfwStatus,
    }));
    fetch("/api/nsfw");
  }

  render() {
    return (
      <div>
        <Menu />
        <div id="info" className="Info">
          <h1> nsfw allowed:</h1>
          <Toggle
            defaultChecked={this.state.nsfwStatus}
            onChange={this.nsfwToggle}
          />
        </div>
      </div>
    );
  }
}

export default Info;
