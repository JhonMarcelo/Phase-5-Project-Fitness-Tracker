import React, { useState } from "react";

import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";

import { Switch, Route, NavLink } from "react-router-dom";
import Home from "./Home";
import Exercise from "./Exercise";
import About from "./About";
import Authentication from "./Authentication";

function ColorSchemesExample() {
  const [user, setUser] = useState(null);

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
            <Nav.Link as={NavLink} to={"/login"}>
              Login
            </Nav.Link>
          </Nav>
        </Container>
      </Navbar>
      <div>
        <Switch>
          <Route exact path="/">
            <Authentication onLogin={setUser} />
          </Route>

          <Route exact path="/login">
            <Authentication onLogin={setUser} />
          </Route>
          <Route exact path="/home">
            <Home />
          </Route>
          <Route path="/exercise">
            <Exercise />
          </Route>
          <Route path="/about">
            <About />
          </Route>
        </Switch>
      </div>
      <br />
    </>
  );
}

export default ColorSchemesExample;
