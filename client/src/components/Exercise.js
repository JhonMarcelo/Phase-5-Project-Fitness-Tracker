import React, { useState, useEffect } from "react";
import Card from "react-bootstrap/Card";
import ModalForm from "./Forms/ModalForm";
import Button from "react-bootstrap/Button";

function Exercise({ id }) {
  const [exercise, setExercise] = useState([]);
  // LOAD CURRENT USER EXERCISE
  useEffect(() => {
    fetch(`/exercise/${id}`)
      .then((r) => r.json())
      .then((items) => setExercise(items));
  }, []);

  function handleDeleteExercise(exercise_id) {
    const newExerciseList = exercise.filter((ex) => ex.id !== exercise_id);
    setExercise(newExerciseList);
    //Delete the exercise on DB
    fetch(`/exercise/${id}/${exercise_id}`, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
    });
  }
  function handleSubmitForm() {}

  return (
    <div>
      <ul>
        {exercise.map((exercise) => {
          return (
            <>
              <Card key={exercise.id}>
                <Card.Text>
                  <h1>{exercise.exercise_name}</h1>
                  <h2>sets: {exercise.sets}</h2>
                  <h2>reps: {exercise.reps}</h2>
                  <h2>weight: {exercise.weight}</h2>
                </Card.Text>
              </Card>
              <ModalForm onSubmitForm={handleSubmitForm} />
              <Button
                key={exercise.id}
                onClick={() => handleDeleteExercise(exercise.id)}
              >
                Delete
              </Button>
            </>
          );
        })}
      </ul>
    </div>
  );
}

export default Exercise;
