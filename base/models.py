from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Exercise(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    muscle_group = models.CharField(max_length=100)
    difficulty = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], null=True
    )
    demonstration_video = models.URLField(blank=True, null=True, max_length=500)
    demonstration_video_2 = models.URLField(blank=True, null=True, max_length=500)
    calories = models.FloatField()
    equipment = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Workout(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    difficulty_level = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    duration_minutes = models.IntegerField()
    exercises = models.ManyToManyField(Exercise, through='WorkoutExercise')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class WorkoutExercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.IntegerField()
    reps = models.IntegerField()
    rest_time_seconds = models.IntegerField()
    order = models.IntegerField()
    calories = models.FloatField()
    class Meta:
        ordering = ['order']

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    fitness_goal = models.CharField(max_length=200)

class WorkoutLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    duration = models.IntegerField()  # Фактическая продолжительность в минутах
    notes = models.TextField(blank=True)

class ExerciseLog(models.Model):
    workout_log = models.ForeignKey(WorkoutLog, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets_completed = models.IntegerField()
    reps_completed = models.IntegerField()
    weight_used = models.FloatField(null=True, blank=True)
    notes = models.TextField(blank=True)