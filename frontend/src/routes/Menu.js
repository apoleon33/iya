import React from "react";
import { Link } from "react-router-dom";
import { ImStatsBars, ImGithub, ImHome3 } from "react-icons/im";
import { BsFillGearFill } from "react-icons/bs";

// https://bit.ly/3QJIHAS

export default class Menu extends React.Component {
  constructor(props) {
    super(props);
    this.state = { width: 0, height: 0 };
    this.updateWindowDimensions = this.updateWindowDimensions.bind(this);
  }

  componentDidMount() {
    this.updateWindowDimensions();
    window.addEventListener("resize", this.updateWindowDimensions);
  }

  componentWillUnmount() {
    window.removeEventListener("resize", this.updateWindowDimensions);
  }

  updateWindowDimensions() {
    this.setState({ width: window.innerWidth, height: window.innerHeight });
  }
  render() {
    let app, stats, options, github;
    if (this.state.width < 815) {
      app = <ImHome3 />;
      stats = <ImStatsBars />;
      options = <BsFillGearFill />;
      github = <ImGithub />;
    } else {
      app = <h2>Iya</h2>;
      stats = <h2>Statistics</h2>;
      options = <h2>Options</h2>;
      github = (
        <div>
          Github
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="16"
            height="16"
            fill="currentColor"
            className="bi bi-box-arrow-up-right"
            viewBox="0 0 16 16"
          >
            <path
              fillRule="evenodd"
              d="M8.636 3.5a.5.5 0 0 0-.5-.5H1.5A1.5 1.5 0 0 0 0 4.5v10A1.5 1.5 0 0 0 1.5 16h10a1.5 1.5 0 0 0 1.5-1.5V7.864a.5.5 0 0 0-1 0V14.5a.5.5 0 0 1-.5.5h-10a.5.5 0 0 1-.5-.5v-10a.5.5 0 0 1 .5-.5h6.636a.5.5 0 0 0 .5-.5z"
            />
            <path
              fillRule="evenodd"
              d="M16 .5a.5.5 0 0 0-.5-.5h-5a.5.5 0 0 0 0 1h3.793L6.146 9.146a.5.5 0 1 0 .708.708L15 1.707V5.5a.5.5 0 0 0 1 0v-5z"
            />
          </svg>
        </div>
      );
    }
    return (
      <header className="Menu">
        <Link to="/">{app}</Link>

        <Link to="/statistics">{stats}</Link>

        <Link to="/options">{options}</Link>

        <h2>
          <a
            href="https://github.com/apoleon33/iya"
            target="_blank"
            rel="noreferrer"
          >
            {github}
          </a>
        </h2>
      </header>
    );
  }
}
