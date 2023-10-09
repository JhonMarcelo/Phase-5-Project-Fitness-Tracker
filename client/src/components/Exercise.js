import React, { useState, useEffect } from "react";
import Card from "react-bootstrap/Card";
import ModalForm from "./Forms/ModalForm";
import Button from "react-bootstrap/Button";

function Exercise({ id }) {
  const [exercise, setExercise] = useState([]);

  function handleSubmitForm(newExercise) {
    setExercise([...exercise, newExercise]);
  }

  function handleDeleteExercise(exercise_id) {
    const newExerciseList = exercise.filter(
      (exercise) => exercise.id !== exercise_id
    );
    setExercise(newExerciseList);

    fetch(`/exercise/${id}/${exercise_id}`, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
    });
  }

  useEffect(() => {
    fetch(`/exercise/${id}`)
      .then((r) => r.json())
      .then((items) => setExercise(items));
  }, []);

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
              <ModalForm user_id={id} onSubmitForm={handleSubmitForm} />
              <Button onClick={() => handleDeleteExercise(exercise.id)}>
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
