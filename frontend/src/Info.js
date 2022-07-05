import React from "react";

class Info extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      iteration: 0,
      oldName: this.props.name,
    };

    this.getCharacterNameAndIteration =
      this.getCharacterNameAndIteration.bind(this);
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

  render() {
    return (
      <div id="info">
        <h1 id="name">character name: {this.state.oldName}</h1>
        <h1 id="compt">iteration count: {this.state.iteration}</h1>
      </div>
    );
  }
}

export default Info;
