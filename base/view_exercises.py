from django.shortcuts import render
from .models import Exercise
from django.contrib.auth.decorators import login_required

@login_required
def view_exercises(request):
    
    exercises = Exercise.objects.all()
    return render(request, 'Тренировки.html', {'exercises': exercises})