import React from "react";
import { Link } from "react-router-dom";

class Menu extends React.Component {
  render() {
    return (
      <header className="Menu">
        <Link to="/">
          <h2>Iya</h2>
        </Link>

        <Link to="/statistics">
          <h2>statistics</h2>
        </Link>

        <Link to="/options">
          <h2>Options</h2>
        </Link>
      </header>
    );
  }
}

export default Menu;
