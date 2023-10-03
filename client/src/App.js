import React, { useEffect, useState } from "react";
import { Switch, Route } from "react-router-dom";
import "./App.css";
import "bootstrap/dist/css/bootstrap.css"; //NEED THIS TO USE BOOTSRAP CSS
import Navbar from "./components/Navbar";

function App() {
  return (
    <div className="App">
      <Navbar />
    </div>
  );
}

export default App;
