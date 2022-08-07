import React from "react";
import ReactDOM from "react-dom/client";

import App from "./App";
import Menu from "./Menu";

import "./style.scss";
import "./react-toggle.css";

const root = ReactDOM.createRoot(document.getElementById("root"));

root.render(
  <React.StrictMode>
    <Menu />
    <App />
  </React.StrictMode>
);

// <Statistc /> and  soon
/*    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320">
      <path
        fill="#393e46"
        fillOpacity="1"
        d="M0,0L24,42.7C48,85,96,171,144,197.3C192,224,240,192,288,165.3C336,139,384,117,432,122.7C480,128,528,160,576,197.3C624,235,672,277,720,293.3C768,309,816,299,864,277.3C912,256,960,224,1008,197.3C1056,171,1104,149,1152,160C1200,171,1248,213,1296,240C1344,267,1392,277,1416,282.7L1440,288L1440,320L1416,320C1392,320,1344,320,1296,320C1248,320,1200,320,1152,320C1104,320,1056,320,1008,320C960,320,912,320,864,320C816,320,768,320,720,320C672,320,624,320,576,320C528,320,480,320,432,320C384,320,336,320,288,320C240,320,192,320,144,320C96,320,48,320,24,320L0,320Z"
      ></path>
    </svg>
*/
