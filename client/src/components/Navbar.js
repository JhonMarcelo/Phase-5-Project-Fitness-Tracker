import React from "react";
import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";

import { Switch, Route, NavLink } from "react-router-dom";
import Home from "./Home";
import Exercise from "./Exercise";
import About from "./About";

function ColorSchemesExample({ user, setUser }) {
  function handleLogout() {
    fetch("/logout", { method: "DELETE" }).then((r) => {
      if (r.ok) {
        setUser(null);
      }
    });
  }
  return (
    <>
      <Navbar bg="dark" data-bs-theme="dark">
        <Container>
          <Navbar.Brand href="/">Fitness Tracker</Navbar.Brand>
          <Nav className="me-auto">
            <Nav.Link as={NavLink} to={"/home"}>
              Home
            </Nav.Link>
            <Nav.Link as={NavLink} to={"/exercise"}>
              Exercise
            </Nav.Link>
            <Nav.Link as={NavLink} to={"/about"}>
              About
            </Nav.Link>
            <Nav.Link as={NavLink} to={"/"} onClick={handleLogout}>
              Logout
            </Nav.Link>
          </Nav>
        </Container>
      </Navbar>
      <div>
        <Switch>
          <Route exact path="/logout"></Route>
          <Route exact path="/home">
            <Home loggedUser={user.first_name} />
          </Route>
          <Route path="/exercise">
            <Exercise id={user.id} />
          </Route>
          <Route path="/about">
            <About />
          </Route>
          <Route exact path="/">
            <Home loggedUser={user.first_name} />
          </Route>
        </Switch>
      </div>
      <br />
    </>
  );
}

export default ColorSchemesExample;
