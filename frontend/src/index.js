import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import App from "./routes/App";
import Info from "./routes/Info";
import Menu from "./routes/Menu";

import "./style.scss";
import "./react-toggle.css";

const root = ReactDOM.createRoot(document.getElementById("root"));

root.render(
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<App />} />
      <Route path="options" element={<Info />} />
      <Route
        path="*"
        element={
          <main>
            <Menu />
            <p>There's nothing here!</p>
          </main>
        }
      />
    </Routes>
  </BrowserRouter>
);
