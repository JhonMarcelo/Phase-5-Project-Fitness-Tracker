import { useState } from "react";
import Button from "react-bootstrap/Button";
import Modal from "react-bootstrap/Modal";
import Form from "react-bootstrap/Form";

export default function ModalForm({ user_id, onSubmitForm }) {
  const [show, setShow] = useState(false);

  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);

  const [exercise_name, setExercise_name] = useState("");
  const [category, setCategory] = useState("Chest");
  const [sets, setSets] = useState("");
  const [reps, setReps] = useState("");
  const [weight, setWeight] = useState("");

  function handleSubmit(e) {
    e.preventDefault();
    const newExercise = {
      exercise_name: exercise_name,
      target_muscle: category,
      sets: sets,
      reps: reps,
      weight: weight,
    };
    fetch(`/exercise/${user_id}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(newExercise),
    })
      .then((r) => r.json())
      .then((newItem) => onSubmitForm(newItem));
  }

  return (
    <>
      <Button variant="primary" onClick={handleShow}>
        Add Exercise
      </Button>

      <Modal
        show={show}
        onHide={handleClose}
        backdrop="static"
        keyboard={false}
      >
        <Modal.Header closeButton>
          <Modal.Title>Enter New Exercise</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <form id="editmodal" onSubmit={handleSubmit}>
            <Form.Group className="mb-3" controlId="formBasicEmail">
              <Form.Label>Exercise Name</Form.Label>
              <Form.Control
                name="name"
                type="text"
                placeholder="Enter exercise name"
                value={exercise_name}
                onChange={(e) => setExercise_name(e.target.value)}
              />

              <Form.Label>Category</Form.Label>
              <Form.Select
                name="category"
                aria-label="Default select example"
                value={category}
                onChange={(e) => setCategory(e.target.value)}
              >
                <option value="Chest">Chest</option>
                <option value="Back">Back</option>
                <option value="Legs">Legs</option>
                <option value="Shoulder">Shoulder</option>
                <option value="Arms">Arms</option>
                <option value="Abs">Abs</option>
              </Form.Select>
              <Form.Label>Sets</Form.Label>
              <Form.Control
                name="name"
                type="text"
                placeholder="Enter number of sets"
                value={sets}
                onChange={(e) => setSets(e.target.value)}
              />
              <Form.Label>reps</Form.Label>
              <Form.Control
                name="name"
                type="text"
                placeholder="Enter repetition"
                value={reps}
                onChange={(e) => setReps(e.target.value)}
              />
              <Form.Label>Weight</Form.Label>
              <Form.Control
                name="name"
                type="text"
                placeholder="Enter weight"
                value={weight}
                onChange={(e) => setWeight(e.target.value)}
              />
            </Form.Group>
            <Modal.Footer>
              <Button variant="secondary" onClick={handleClose}>
                Close
              </Button>
              <Button variant="primary" type="submit" onClick={handleClose}>
                Submit
              </Button>
            </Modal.Footer>
          </form>
        </Modal.Body>
      </Modal>
    </>
  );
}
