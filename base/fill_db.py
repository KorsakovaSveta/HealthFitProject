from .models import Exercise, WorkoutExercise
from django.shortcuts import render, redirect

def create_exercise(request):
    # exercises = [
    #     Exercise(
    #         name='Отжимания',
    #         description='Упражнение для тренировки мышц груди, плеч и трицепсов.',
    #         muscle_group='Грудные мышцы',
    #         difficulty=3,
    #         #demonstration_video='https://example.com/pushups'
    #     ),
    #     Exercise(
    #         name='Приседания',
    #         description='Упражнение для тренировки ног и ягодиц.',
    #         muscle_group='Ноги',
    #         difficulty=2,
    #         #demonstration_video='https://example.com/squats'
    #     ),
    #     Exercise(
    #         name='Выпады',
    #         description='Упражнение для тренировки ног и ягодиц с акцентом на баланс.',
    #         muscle_group='Ноги',
    #         difficulty=3,
    #         #demonstration_video='https://example.com/lunges'
    #     ),
    #     Exercise(
    #         name='Планка',
    #         description='Упражнение для укрепления кора и стабилизации тела.',
    #         muscle_group='Пресс',
    #         difficulty=2,
    #         #demonstration_video='https://example.com/plank'
    #     ),
    #     Exercise(
    #         name='Тяга гантели в наклоне',
    #         description='Упражнение для тренировки спины и рук.',
    #         muscle_group='Спина',
    #         difficulty=3,
    #         #demonstration_video='https://example.com/row'
    #     ),
    #     Exercise(
    #         name='Жим штанги лежа',
    #         description='Основное упражнение для тренировки грудных мышц.',
    #         muscle_group='Грудные мышцы',
    #         difficulty=4,
    #         #demonstration_video='https://example.com/benchpress'
    #     ),
    #     Exercise(
    #         name='Подъем ног',
    #         description='Упражнение для тренировки нижней части пресса.',
    #         muscle_group='Пресс',
    #         difficulty=3,
    #         #demonstration_video='https://example.com/legraises'
    #     ),
    #     Exercise(
    #         name='Бёрпи',
    #         description='Комплексное упражнение для всего тела, включающее прыжок и отжимание.',
    #         muscle_group='Все группы мышц',
    #         difficulty=4,
    #         #demonstration_video='https://example.com/burpees'
    #     ),
    #     Exercise(
    #         name='Русские скручивания',
    #         description='Упражнение для тренировки косых мышц живота.',
    #         muscle_group='Пресс',
    #         difficulty=2,
    #         #demonstration_video='https://example.com/russiantwist'
    #     ),
    #     Exercise(
    #         name='Плиометрические приседания',
    #         description='Приседания с прыжком для повышения силы и мощности.',
    #         muscle_group='Ноги',
    #         difficulty=4,
    #         #demonstration_video='https://example.com/jumpingsquats'
    #     ),

    #     Exercise(
    #         name='Мостик',
    #         description='Упражнение для укрепления ягодиц и задней поверхности бедра.',
    #         muscle_group='Ягодицы',
    #         difficulty=2,
    #         #demonstration_video='https://example.com/jumpingsquats'
    #     ),

    #     Exercise(
    #         name='Обратные отжимания',
    #         description='Упражнение для тренировки трицепсов и спины.',
    #         muscle_group='Трицепсы, спина',
    #         difficulty=3,
    #         #demonstration_video='https://example.com/jumpingsquats'
    #     ),

    #     Exercise(
    #         name='Тяга верхнего блока',
    #         description='Упражнение для тренировки широчайших мышц спины.',
    #         muscle_group='Спина',
    #         difficulty=3,
    #         #demonstration_video='https://example.com/jumpingsquats'
    #     ),

    #     Exercise(
    #         name='Жим ногами',
    #         description='Упражнение для проработки ног с использованием тренажера.',
    #         muscle_group='Ноги, ягодицы',
    #         difficulty=4,
    #         #demonstration_video='https://example.com/jumpingsquats'
    #     ),

    #     Exercise(
    #         name='Планка с подъемом ноги',
    #         description='Вариация планки с поднятием ноги для увеличения нагрузки на пресс и ягодицы.',
    #         muscle_group='Пресс, ягодицы',
    #         difficulty=3,
    #         #demonstration_video='https://example.com/jumpingsquats'
    #     ),

    #     Exercise(
    #         name='Кроссфит-скалолаз',
    #         description='Интенсивное кардио-упражнение, имитирующее движение при скалолазании.',
    #         muscle_group='Все группы мышц',
    #         difficulty=4,
    #         #demonstration_video='https://example.com/jumpingsquats'
    #     ),

    #     Exercise(
    #         name='Тренировка с гирей',
    #         description='Упражнения с гирей для развития силы и выносливости',
    #         muscle_group='Все группы мышц',
    #         difficulty=4,
    #         #demonstration_video='https://example.com/jumpingsquats'
    #     ),

    #     Exercise(
    #         name='Боковая планка',
    #         description='Вариация планки, акцентирующая внимание на боковых мышцах живота.',
    #         muscle_group="Косые мышцы живота",
    #         difficulty=3,
    #         #demonstration_video='https://example.com/jumpingsquats'
    #     ),

    #     Exercise(
    #         name='Тяга гантелей к поясу (в наклоне)',
    #         description='Упражнение для проработки спины с использованием гантелей.',
    #         muscle_group="Спина, бицепсы",
    #         difficulty=3,
    #         #demonstration_video='https://example.com/jumpingsquats'
    #     )
    # ]
    
    # Сохранение всех упражнений в базе данных
    # calories = [0.4, 0.3, 0.4, 0.2, 0.5, 0.8, 0.5, 1.4, 0.2, 0.7, 0.3, 0.5, 0.4, 0.9, 0.3, 1.4, 1.0, 0.2, 0.5]
    # for calory, exercise in zip(calories, Exercise.objects.all()):
    #     #exercise = Exercise.objects.get(id=id_exercise)
    #     exercise.calories = calory
    #     exercise.save()
   
    for workout_exercise in WorkoutExercise.objects.all():
        workout_exercise.calories = workout_exercise.reps*workout_exercise.sets*workout_exercise.exercise.calories
        workout_exercise.save()
    return render(request, 'main_page.html')
