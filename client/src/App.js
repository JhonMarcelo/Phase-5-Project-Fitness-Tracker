import React, { useEffect, useState } from "react";

import "./App.css";
import "bootstrap/dist/css/bootstrap.css"; //NEED THIS TO USE BOOTSRAP CSS
import Authentication from "./components/Authentication";
import Navbar from "./components/Navbar";

function App() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    fetch("/check_session").then((r) => {
      if (r.ok) {
        r.json().then((user) => {
          setUser(user);
        });
      }
    });
  }, []);
  console.log(user);
  if (!user) return <Authentication onLogin={setUser} />;

  return (
    <div className="App">
      <Navbar user={user} setUser={setUser} />
    </div>
  );
}

export default App;
