import React, { useState, useEffect } from "react";
import Card from "react-bootstrap/Card";

import Button from "react-bootstrap/Button";

function Exercise({ id }) {
  const [exercise, setExercise] = useState([]);

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
            </>
          );
        })}
      </ul>
    </div>
  );
}

export default Exercise;
