import React, { useState } from "react";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";

function Signup(onLogin) {
  const [username, setUsername] = useState("");
  const [first_name, setFirst_name] = useState("");
  const [last_name, setLast_name] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState([]);

  function handleSubmit(e) {
    e.preventDefault();
    fetch("/signup", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username,
        first_name,
        last_name,
        password,
      }),
    }).then((r) => {
      if (r.ok) {
        r.json().then((user) => onLogin(user));
      } else {
        r.json().then((err) => setErrors(err.errors));
      }
    });
  }
  return (
    <form onSubmit={handleSubmit}>
      <Form.Label htmlFor="inputPassword5">Username</Form.Label>
      <Form.Control
        type="text"
        id="inputPassword5"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        aria-describedby="passwordHelpBlock"
      />
      <Form.Label htmlFor="inputPassword5">First Namel</Form.Label>
      <Form.Control
        type="text"
        id="inputPassword5"
        value={username}
        onChange={(e) => setFirst_name(e.target.value)}
        aria-describedby="passwordHelpBlock"
      />
      <Form.Label htmlFor="inputPassword5">Last Name</Form.Label>
      <Form.Control
        type="text"
        id="inputPassword5"
        value={username}
        onChange={(e) => setLast_name(e.target.value)}
        aria-describedby="passwordHelpBlock"
      />
      <Form.Label htmlFor="inputPassword5">Password</Form.Label>
      <Form.Control
        type="password"
        id="inputPassword5"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        aria-describedby="passwordHelpBlock"
      />
      <Form.Text id="passwordHelpBlock" muted>
        Your password must be 8-20 characters long, contain letters and numbers,
        and must not contain spaces, special characters, or emoji.
      </Form.Text>
      <br></br>
      <Button variant="primary">Sign up</Button>{" "}
    </form>
  );
}
export default Signup;
