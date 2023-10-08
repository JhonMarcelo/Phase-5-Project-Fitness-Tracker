// import React, { useEffect, useState } from "react";

import "./App.css";
import "bootstrap/dist/css/bootstrap.css"; //NEED THIS TO USE BOOTSRAP CSS
import Authentication from "./components/Authentication";
import Navbar from "./components/Navbar";

function App() {
  // const [data, setData] = useState({});

  // useEffect(() => {
  //   console.log(data);
  // }, [data]);

  // fetch("/exercise/1")
  //   .then((r) => r.json())
  //   .then((data) => setData(data));

  return (
    <div className="App">
      <Navbar />
    </div>
  );
}

export default App;
