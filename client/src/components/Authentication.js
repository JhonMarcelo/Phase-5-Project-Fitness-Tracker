import React, { useState } from "react";
import Log_in from "./Forms/Login";
import Signup from "./Forms/Signup";

function Authentication({ onLogin }) {
  const [showLogin, setShowLogin] = useState(true);

  return (
    <>
      {showLogin ? (
        <div>
          <Log_in onLogin={onLogin} />
          <p>
            need to signup?
            <button onClick={() => setShowLogin(false)}>Sign up</button>
          </p>
        </div>
      ) : (
        <div>
          <Signup onLogin={onLogin} />
          <p>
            need to login?
            <button onClick={() => setShowLogin(true)}>Log in</button>
          </p>
        </div>
      )}
    </>
  );
}

export default Authentication;
