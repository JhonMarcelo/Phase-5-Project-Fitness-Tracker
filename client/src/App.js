import React, { useEffect, useState } from "react";
import { Switch, Route } from "react-router-dom";
import "./App.css";
import "bootstrap/dist/css/bootstrap.css"; //NEED THIS TO USE BOOTSRAP CSS
import Authentication from "./components/Authentication";

function App() {
  const [data, setData] = useState({});

  useEffect(() => {
    console.log(data);
  }, [data]);

  fetch("/exercise/1")
    .then((r) => r.json())
    .then((data) => setData(data));

  return (
    <div className="App">
      <Authentication />
    </div>
  );
}

export default App;
