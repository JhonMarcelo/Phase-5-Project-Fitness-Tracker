import React from "react";

function Home({ loggedUser }) {
  return (
    <div>
      <h1>Welcome {loggedUser}</h1>
      <h2>head to exercise to start tracking.</h2>
    </div>
  );
}

export default Home;
