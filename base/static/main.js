document.addEventListener("DOMContentLoaded", function () {
    const createWorkoutBtn = document.getElementById("create-workout-btn");
    const addExerciseBtn = document.getElementById("add-exercise-btn");

    // Отправка запроса на создание тренировки
    createWorkoutBtn.addEventListener("click", async () => {
        const workoutData = {
            name: document.getElementById("workout-name").value,
            description: document.getElementById("workout-description").value,
            difficulty_level: parseInt(document.getElementById("workout-difficulty").value),
            duration_minutes: parseInt(document.getElementById("workout-duration").value)
        };
        
        const response = await fetch("/create_workout/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(workoutData)
        });
        
        const result = await response.json();
        if (result.success) {
            alert("Workout created successfully!");
            document.getElementById("workout-id").value = result.workout_id;
            openExerciseModal();
        }
    });

    // Открытие модального окна для добавления упражнений
    async function openExerciseModal() {
        const exerciseModal = document.getElementById("exercise-modal");
        exerciseModal.style.display = "block";

        const response = await fetch("/get_exercises/");
        const data = await response.json();
        const exerciseSelect = document.getElementById("exercise-select");
        data.exercises.forEach(exercise => {
            let option = document.createElement("option");
            option.value = exercise.id;
            option.text = `${exercise.name} - ${exercise.muscle_group}`;
            exerciseSelect.add(option);
        });
    }

    // Отправка запроса на добавление упражнения к тренировке
    addExerciseBtn.addEventListener("click", async () => {
        const workoutId = document.getElementById("workout-id").value;
        const exerciseData = {
            exercise_id: parseInt(document.getElementById("exercise-select").value),
            sets: parseInt(document.getElementById("exercise-sets").value),
            reps: parseInt(document.getElementById("exercise-reps").value),
            rest_time_seconds: parseInt(document.getElementById("exercise-rest-time").value),
            order: parseInt(document.getElementById("exercise-order").value)
        };
        
        const response = await fetch(`/add_exercise_to_workout/${workoutId}/`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(exerciseData)
        });
        
        const result = await response.json();
        if (result.success) {
            alert("Exercise added successfully!");
        }
    });
});
