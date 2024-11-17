from .models import Exercise, WorkoutExercise
from django.shortcuts import render, redirect

def create_exercise(request):
    exercises = [
        Exercise(
            name ='Классические отжимания',
            description = 'В этом упражнении работает грудь и трицепс. Так же, если не хватает сил для полноценных отжиманий, то можно отжиматься с колен.',
            muscle_group = 'Грудные мыщцы',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BE%D1%82%D0%B6%D0%B8%D0%BC%D0%B0%D0%BD%D0%B8%D1%8F-%D0%BA%D0%BB%D0%B0%D1%81%D1%81%D0%B8%D0%BA.gif',
            demonstration_video_2 = 'https://makefitness.pro/wp-content/uploads/2020/02/%D0%BE%D1%82%D0%B6-%D1%81-%D0%BA%D0%BE%D0%BB%D0%B5%D0%BD-1.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Отжимания от стульев',
            description = 'В этом упражнении работает грудь и трицепс.',
            muscle_group = 'Грудные мыщцы',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2019/10/%D0%9E%D1%82%D0%B6%D0%B8%D0%BC%D0%B0%D0%BD%D0%B8%D1%8F-%D0%BE%D1%82-%D1%81%D1%82%D1%83%D0%BB%D1%8C%D0%B5%D0%B2-2-%D1%81%D1%82%D1%83%D0%BB%D0%B0-%D0%9A%D0%BE%D0%BB%D1%8F.gif',
            demonstration_video_2 = 'https://makefitness.pro/wp-content/uploads/2019/10/%D0%9E%D1%82%D0%B6%D0%B8%D0%BC%D0%B0%D0%BD%D0%B8%D1%8F-%D0%BE%D1%82-%D1%81%D1%82%D1%83%D0%BB%D1%8C%D0%B5%D0%B2-%D0%BE%D1%81%D0%BB%D0%BE%D0%B6%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5-3-%D1%81%D1%82%D1%83%D0%BB%D0%B0-%D0%9A%D0%BE%D0%BB%D1%8F.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

         Exercise(
            name ='Отжимания ноги на возвышенности',
            description = 'В этом упражнении больше работает трицепс.',
            muscle_group = 'Грудные мыщцы',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/09/%D0%BE%D1%82%D0%B6%D0%B8%D0%BC%D0%B0%D0%BD%D0%B8%D1%8F-%D0%BD%D0%BE%D0%B3%D0%B8-%D0%BD%D0%B0-%D0%B2%D0%BE%D0%B7%D0%B2%D1%8B%D1%88%D0%B5%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D0%B8.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Отжимания узким хватом',
            description = 'В этом упражнении больше работает трицепс.',
            muscle_group = 'Грудные мыщцы',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BE%D1%82%D0%B6-%D1%83%D0%B7%D0%BA%D0%B8%D0%B5.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Отжимания лучника',
            description = 'В этом упражнении работает грудь и трицепс.',
            muscle_group = 'Грудные мыщцы',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BE%D1%82%D0%B6%D0%B8%D0%BC%D0%B0%D0%BD%D0%B8%D1%8F-%D0%BB%D1%83%D1%87%D0%BD%D0%B8%D0%BA%D0%B0.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Отжимания с подносом колена',
            description = 'В этом упражнении работает грудь и трицепс.',
            muscle_group = 'Грудные мыщцы',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BE%D1%82%D0%B6-%D1%81-%D0%BF%D0%BE%D0%B4%D0%BD%D0%BE%D1%81%D0%BE%D0%BC-%D0%BA%D0%BE%D0%BB%D0%B5%D0%BD%D0%B0-%D0%B2-%D0%BD%D0%B8%D0%B6%D0%BD%D0%B5%D0%B9-%D1%82%D0%BE%D1%87%D0%BA%D0%B5.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Кик отжимания',
            description = 'В этом упражнении работает грудь и трицепс.',
            muscle_group = 'Грудные мыщцы',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BA%D0%B8%D0%BA-%D0%BE%D1%82%D0%B6%D0%B8%D0%BC%D0%B0%D0%BD%D0%B8%D1%8F.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Жим гантель лежа (общая грудь)',
            description = 'В этом упражнении работает грудь и трицепс.',
            muscle_group = 'Грудные мыщцы',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%B6%D0%B8%D0%BC-%D0%B3%D0%B0%D0%BD%D1%82%D0%B5%D0%BB%D0%B5%D0%B9-%D0%BB%D1%91%D0%B6%D0%B0-1.gif',
            calories = 0.4,
            equipment = 'С гантелями'
        ),

        Exercise(
            name ='Жим гантель под положительным углом (верх груди)',
            description = 'В этом упражнении работает грудь и трицепс.',
            muscle_group = 'Грудные мыщцы',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%B6%D0%B8%D0%BC-%D0%B3%D0%B0%D0%BD%D1%82%D0%B5%D0%BB%D0%B5%D0%B9-%D0%BD%D0%B0-%D0%BD%D0%B0%D0%BA%D0%BB%D0%BE%D0%BD%D0%BE%D0%B9.gif',
            calories = 0.4,
            equipment = 'С гантелями'
        ),

        Exercise(
            name ='Жим гантель под отрицательным углом (низ грудных мышц)',
            description = 'В этом упражнении работает грудь и трицепс.',
            muscle_group = 'Грудные мыщцы',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%B6%D0%B8%D0%BC-%D0%B3%D0%B0%D0%BD%D1%82%D0%B5%D0%BB%D0%B5%D0%B9-%D0%BF%D0%BE%D0%B4-%D0%BE%D1%82%D1%80%D0%B8%D1%86%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%BC-%D1%83%D0%B3%D0%BB%D0%BE%D0%BC-%D0%BB%D1%91%D0%B6%D0%B0.gif',
            calories = 0.4,
            equipment = 'С гантелями'
        ),

       Exercise(
            name ='Разведение гантель лежа',
            description = 'В этом упражнении работает грудь и трицепс.',
            muscle_group = 'Грудные мыщцы',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%80%D0%B0%D0%B7%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B3%D0%B0%D0%BD%D1%82%D0%B5%D0%BB%D0%B5%D0%B9-%D0%BB%D1%91%D0%B6%D0%B0.gif',
            calories = 0.4,
            equipment = 'С гантелями'
        ),

        Exercise(
            name ='Разведение гантель лежа под положительным углом (верх груди)',
            description = 'В этом упражнении работает грудь и трицепс.',
            muscle_group = 'Грудные мыщцы',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%80%D0%B0%D0%B7%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B3%D0%B0%D0%BD%D1%82%D0%B5%D0%BB%D0%B5%D0%B9-%D0%BB%D1%91%D0%B6%D0%B0-%D0%BD%D0%B0-%D0%BD%D0%B0%D0%BA%D0%BB%D0%BE%D0%BD%D0%BE%D0%B9-%D1%81%D0%BA%D0%B0%D0%BC%D1%8C%D0%B5.gif',
            calories = 0.4,
            equipment = 'С гантелями'
        ),

        Exercise(
            name ='Разведение гантель лежа под отрицательным углом (низ грудных мышц)',
            description = 'В этом упражнении работает грудь и трицепс.',
            muscle_group = 'Грудные мыщцы',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%B6%D0%B8%D0%BC-%D0%B3%D0%B0%D0%BD%D1%82%D0%B5%D0%BB%D0%B5%D0%B9-%D0%BB%D1%91%D0%B6%D0%B0-%D0%BD%D0%B0-%D1%81%D0%BA%D0%B0%D0%BC%D1%8C%D0%B5-%D0%BF%D0%BE%D0%B4-%D0%BE%D1%82%D1%80%D0%B8%D1%86%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%BC-%D1%83%D0%B3%D0%BB%D0%BE%D0%BC.gif',
            calories = 0.4,
            equipment = 'С гантелями'
        ),

        Exercise(
            name ='Пуловер с гантелей',
            description = 'В этом упражнении работает грудь и трицепс.',
            muscle_group = 'Грудные мыщцы',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/09/%D0%BF%D0%BE%D0%BB%D0%BE%D0%B2%D0%B5%D1%80-%D1%81-%D0%B3%D0%B0%D0%BD%D1%82%D0%B5%D0%BB%D0%B5%D0%B9.gif',
            calories = 0.4,
            equipment = 'С гантелями'
        ),

        Exercise(
            name ='Жим штанги лежа',
            description = 'В этом упражнении работает грудь и трицепс.',
            muscle_group = 'Грудные мыщцы',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%B6%D0%B8%D0%BC-%D1%88%D1%82%D0%B0%D0%BD%D0%B3%D0%B8-%D0%BB%D0%B5%D0%B6%D0%B0.gif',
            calories = 0.4,
            equipment = 'Со штангой'
        ),

        Exercise(
            name ='Жим штанги лежа  под положительным углом (верх грудных мышц)',
            description = 'В этом упражнении работает грудь и трицепс.',
            muscle_group = 'Грудные мыщцы',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%B6%D0%B8%D0%BC-%D0%BD%D0%B0-%D0%BD%D0%B0%D0%BA%D0%BB%D0%BE%D0%BD%D0%BE%D0%B9.gif',
            calories = 0.4,
            equipment = 'Со штангой'
        ),

        Exercise(
            name ='Жим штанги лежа под отрицательным углом (низ грудных мышц)',
            description = 'В этом упражнении работает грудь и трицепс.',
            muscle_group = 'Грудные мыщцы',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%B6%D0%B8%D0%BC-%D1%88%D1%82%D0%B0%D0%BD%D0%B3%D0%B8-%D0%BB%D1%91%D0%B6%D0%B0-%D0%B3%D0%BE%D0%BB%D0%BE%D0%B2%D0%BE%D0%B9-%D0%B2%D0%BD%D0%B8%D0%B7.gif',
            calories = 0.4,
            equipment = 'Со штангой'
        ),

        Exercise(
            name ='Отжимания с резиной',
            description = 'В этом упражнении работает грудь и трицепс.',
            muscle_group = 'Грудные мыщцы',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BE%D1%82%D0%B6%D0%B8%D0%BC%D0%B0%D0%BD%D0%B8%D0%B5-%D1%81-%D1%80%D0%B5%D0%B7%D0%B8%D0%BD%D0%BA%D0%BE%D0%B9.gif',
            calories = 0.4,
            equipment = 'С резиной'
        ),

        Exercise(
            name ='Отжимания на брусьях',
            description = 'В этом упражнении работает грудь и трицепс.',
            muscle_group = 'Грудные мыщцы',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/03/%D0%BE%D1%82%D0%B6%D0%B8%D0%BC%D0%B0%D0%BD%D0%B8%D1%8F-%D0%BD%D0%B0-%D0%B1%D1%80%D1%83%D1%81%D1%8C%D1%8F%D1%85-%D0%B4%D0%BB%D1%8F-%D0%B3%D1%80%D1%83%D0%B4%D0%B8.gif',
            calories = 0.4,
            equipment = 'На брусьях'
        ),

        Exercise(
            name ='Гиперэкстензия лежа',
            description = 'В этом упражнении работают поясничные мышцы.',
            muscle_group = 'Мышцы спины',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%B3%D0%B8%D0%BF%D0%B5%D1%80%D1%8D%D0%BA%D1%81%D1%82%D0%B5%D0%BD%D0%B7%D0%B8%D1%8F.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Повороты корпуса',
            description = 'В этом упражнении работают поясничные мышцы и частично задействованы широчайшие мышцы.',
            muscle_group = 'Мышцы спины',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BF%D0%BE%D0%B2%D0%BE%D1%80%D0%BE%D1%82%D1%8B-%D0%BA%D0%BE%D1%80%D0%BF%D1%83%D1%81%D0%B0-%D0%BB%D0%B5%D0%B6%D0%B0.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Пловец',
            description = 'В этом упражнении работают поясничные мышцы и широчайшие мышцы.',
            muscle_group = 'Мышцы спины',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BF%D0%BB%D0%B0%D0%B2%D0%B5%D1%86-%D0%B1%D0%B5%D0%B7-%D0%BD%D0%BE%D0%B3.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Приведение локтей лежа',
            description = 'В этом упражнении работают поясничные мышцы и широчайшие мышцы.',
            muscle_group = 'Мышцы спины',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BF%D1%80%D0%B8%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-%D0%BB%D0%BE%D0%BA%D1%82%D0%B5%D0%B9-%D0%BB%D0%B5%D0%B6%D0%B0-1.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Тяга гантель в наклоне',
            description = 'В этом упражнении работают широчайшие мышцы.',
            muscle_group = 'Мышцы спины',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%82%D1%8F%D0%B3%D0%B0-%D0%B3%D0%B0%D0%BD%D1%82%D0%B5%D0%BB%D0%B5%D0%B9-%D0%B2-%D0%BD%D0%B0%D0%BA%D0%BB%D0%BE%D0%BD%D0%B5.gif',
            calories = 0.4,
            equipment = 'С гантелями'
        ),

        Exercise(
            name ='Тяга гантель в упоре',
            description = 'В этом упражнении работают широчайшие мышцы и нет нагрузки на поясницу.',
            muscle_group = 'Мышцы спины',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%82%D1%8F%D0%B3%D0%B0-%D0%B3%D0%B0%D0%BD%D1%82%D0%B5%D0%BB%D0%B5%D0%B9-%D0%BB%D1%91%D0%B6%D0%B0-%D0%BD%D0%B0-%D1%81%D0%BA%D0%B0%D0%BC%D1%8C%D0%B5.gif',
            calories = 0.4,
            equipment = 'С гантелями'
        ),

        Exercise(
            name ='Шраги',
            description = 'В этом упражнении работают трапециевидные мышцы.',
            muscle_group = 'Мышцы спины',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%88%D1%80%D0%B0%D0%B3%D0%B8-%D1%81-%D0%B3%D0%B0%D0%BD%D1%82%D0%B5%D0%BB%D1%8F%D0%BC%D0%B8.gif',
            calories = 0.4,
            equipment = 'С гантелями'
        ),

        Exercise(
            name ='Мертвая тяга',
            description = 'В этом упражнении работают поясничные мышцы и ягодицы.',
            muscle_group = 'Мышцы спины',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BC%D0%B5%D1%80%D1%82%D0%B2%D0%B0%D1%8F-%D1%82%D1%8F%D0%B3%D0%B0-%D1%81-%D0%B3%D0%B0%D0%BD%D1%82%D0%B5%D0%BB%D1%8F%D0%BC%D0%B8.gif',
            calories = 0.4,
            equipment = 'С гантелями'
        ),

        Exercise(
            name ='Тяга штанги в наклоне',
            description = 'В этом упражнении работают широчайшие мышцы.',
            muscle_group = 'Мышцы спины',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%82%D1%8F%D0%B3%D0%B0-%D1%88%D1%82%D0%B0%D0%BD%D0%B3%D0%B8-%D0%B2-%D0%BD%D0%B0%D0%BA%D0%BB%D0%BE%D0%BD%D0%B52.gif',
            calories = 0.4,
            equipment = 'Со штангой'
        ),

        Exercise(
            name ='Тяга штанги в наклоне обратным хватом',
            description = 'В этом упражнении работают широчайшие мышцы.',
            muscle_group = 'Мышцы спины',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%82%D1%8F%D0%B3%D0%B0-%D1%88%D1%82%D0%B0%D0%BD%D0%B3%D0%B8-%D0%B2-%D0%BD%D0%B0%D0%BA%D0%BB%D0%BE%D0%BD%D0%B5-%D0%BE%D0%B1%D1%80%D0%B0%D1%82%D0%BD%D1%8B%D0%BC-%D1%85%D0%B2%D0%B0%D1%82%D0%BE%D0%BC.gif',
            calories = 0.4,
            equipment = 'Со штангой'
        ),

        Exercise(
            name ='Классическая становая тяга',
            description = 'В этом упражнении преимущественно работают низ спины и ноги.',
            muscle_group = 'Мышцы спины',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BA%D0%BB%D0%B0%D1%81%D1%81%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F-%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%B0%D1%8F-%D1%82%D1%8F%D0%B3%D0%B0.gif',
            calories = 0.4,
            equipment = 'Со штангой'
        ),

        Exercise(
            name ='Становая тяга «сумо»',
            description = 'В этом упражнении преимущественно работают низ спины и ноги.',
            muscle_group = 'Мышцы спины',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%B0%D1%8F-%D1%81%D1%83%D0%BC%D0%BE.gif',
            calories = 0.4,
            equipment = 'Со штангой'
        ),

        Exercise(
            name ='Наклоны со штангой',
            description = 'В этом упражнении работают поясничные мышцы.',
            muscle_group = 'Мышцы спины',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BD%D0%B0%D0%BA%D0%BB%D0%BE%D0%BD%D1%8B-%D1%81%D0%BE-%D1%88%D1%82%D0%B0%D0%BD%D0%B3%D0%BE%D0%B92.gif',
            calories = 0.4,
            equipment = 'Со штангой'
        ),

        Exercise(
            name ='Шраги',
            description = 'В этом упражнении работает верх спины.',
            muscle_group = 'Мышцы спины',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%88%D1%80%D0%B0%D0%B3%D0%B8-%D1%81%D0%BE-%D1%88%D1%82%D0%B0%D0%BD%D0%B3%D0%BE%D0%B9.gif',
            calories = 0.4,
            equipment = 'Со штангой'
        ),

        Exercise(
            name ='Подтягивания широким хватом',
            description = 'В этом упражнении работают широчайшие и трапециевидные мышцы.',
            muscle_group = 'Мышцы спины',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%9F%D0%BE%D0%B4%D1%82%D1%8F%D0%B3%D0%B8%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F-%D1%88%D0%B8%D1%80%D0%BE%D0%BA%D0%B8%D0%BC-%D1%85%D0%B2%D0%B0%D1%82%D0%BE%D0%BC.gif',
            calories = 0.4,
            equipment = 'На турнике'
        ),

        Exercise(
            name ='Тяга в наклоне',
            description = 'В этом упражнении работают широчайшие и ромбовидные мышцы.',
            muscle_group = 'Мышцы спины',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%82%D1%8F%D0%B3%D0%B0-%D0%BA-%D0%BF%D0%BE%D1%8F%D1%81%D1%83-%D0%B2-%D0%BD%D0%B0%D0%BA%D0%BB%D0%BE%D0%BD%D0%B5-1.gif',
            calories = 0.4,
            equipment = 'С резиновыми петлями'
        ),

        Exercise(
            name ='Тяга в наклоне одной рукой поочередно',
            description = 'В этом упражнении работают широчайшие мышцы.',
            muscle_group = 'Мышцы спины',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%82%D1%8F%D0%B3%D0%B0-%D0%BA-%D0%BF%D0%BE%D1%8F%D1%81%D1%83-%D0%BE%D0%B4%D0%BD%D0%BE%D0%B9-%D1%80%D1%83%D0%BA%D0%BE%D0%B9.gif',
            calories = 0.4,
            equipment = 'С резиновыми петлями'
        ),

        Exercise(
            name ='Наклоны вперед',
            description = 'В этом упражнении работают широчайшие и ромбовидные мышцы.',
            muscle_group = 'Мышцы спины',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BD%D0%B0%D0%BA%D0%BB%D0%BE%D0%BD%D1%8B-%D0%B2%D0%BF%D0%B5%D1%80%D0%B5%D0%B4-1.gif',
            calories = 0.4,
            equipment = 'С резиновыми петлями'
        ),

        Exercise(
            name ='Шраги',
            description = 'В этом упражнении работает верх спины.',
            muscle_group = 'Мышцы спины',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%88%D1%80%D0%B0%D0%B3%D0%B8-2.gif',
            calories = 0.4,
            equipment = 'С резиновыми петлями'
        ),

        Exercise(
            name ='Классический подъем гантель на бицепс стоя',
            description = 'В этом упражнении работает бицепс.',
            muscle_group = 'Мышцы рук',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BF%D0%BE%D0%B4%D1%8A%D1%91%D0%BC-%D0%B3%D0%B0%D0%BD%D1%82%D0%B5%D0%BB%D0%B5%D0%B9-%D0%BD%D0%B0-%D0%B1%D0%B8%D1%86%D0%B5%D0%BF%D1%81.gif',
            calories = 0.4,
            equipment = 'С гантелями'
        ),

        Exercise(
            name ='Подъем гантель на бицепс с супинацией',
            description = 'В этом упражнении работает бицепс.',
            muscle_group = 'Мышцы рук',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BF%D0%BE%D0%B4%D1%8A%D1%91%D0%BC-%D0%B3%D0%B0%D0%BD%D1%82%D0%B5%D0%BB%D0%B5%D0%B9-%D0%BD%D0%B0-%D0%B1%D0%B8%D1%86%D0%B5%D0%BF%D1%81-%D1%81-%D1%81%D1%83%D0%BF%D0%B8%D0%BD%D0%B0%D1%86%D0%B8%D0%B5%D0%B9.gif',
            calories = 0.4,
            equipment = 'С гантелями'
        ),

        Exercise(
            name ='Подъем на бицепс сидя, с упором в бедро',
            description = 'В этом упражнении работает бицепс.',
            muscle_group = 'Мышцы рук',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BF%D0%BE%D0%B4%D1%8C%D1%91%D0%BC-%D0%B3%D0%B0%D0%BD%D1%82%D0%B5%D0%BB%D0%B5%D0%B9-%D1%81%D0%B8%D0%B4%D1%83-%D1%81-%D1%83%D0%BF%D0%BE%D1%80%D0%BE%D0%BC-%D0%B2-%D0%B1%D0%B5%D0%B4%D1%80%D0%BE.gif',
            calories = 0.4,
            equipment = 'С гантелями'
        ),

        Exercise(
            name ='Сгибания рук в упоре о скамью',
            description = 'В этом упражнении работает бицепс.',
            muscle_group = 'Мышцы рук',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BF%D0%BE%D0%B4%D1%8A%D1%91%D0%BC-%D0%B3%D0%B0%D0%BD%D1%82%D0%B5%D0%BB%D0%B5%D0%B9-%D0%B2-%D1%83%D0%BF%D0%BE%D1%80%D0%B5.gif',
            calories = 0.4,
            equipment = 'С гантелями'
        ),

        Exercise(
            name ='Подъем гантель на бицепс сидя на скамье',
            description = 'В этом упражнении работает бицепс.',
            muscle_group = 'Мышцы рук',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BF%D0%BE%D0%B4%D1%8A%D1%91%D0%BC-%D0%B3%D0%B0%D0%BD%D1%82%D0%B5%D0%BB%D0%B5%D0%B9-%D1%81%D0%B8%D0%B4%D1%8F-%D0%BD%D0%B0-%D1%81%D0%BA%D0%B0%D0%BC%D1%8C%D0%B5.gif',
            calories = 0.4,
            equipment = 'С гантелями'
        ),

        Exercise(
            name ='Подъем на бицепс с упором о скамью',
            description = 'В этом упражнении работает бицепс.',
            muscle_group = 'Мышцы рук',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BF%D0%BE%D0%B4%D1%8A%D1%91%D0%BC-%D0%BD%D0%B0-%D0%B1%D0%B8%D1%86%D0%B5%D0%BF%D1%81-%D0%B3%D0%B0%D0%BD%D1%82%D0%B5%D0%BB%D0%B5%D0%B9-%D1%81-%D1%83%D0%BF%D0%BE%D1%80%D0%BE%D0%BC-%D0%BE%D0%B1-%D1%81%D0%BA%D0%B0%D0%BC%D0%B5%D0%B9%D0%BA%D1%83.gif',
            calories = 0.4,
            equipment = 'С гантелями'
        ),

        Exercise(
            name ='Французский жим с гантелями стоя',
            description = 'В этом упражнении работает трицепс.',
            muscle_group = 'Мышцы рук',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%84%D1%80%D0%B0%D0%BD%D1%86%D1%83%D0%B7%D0%BA%D0%B8%D0%B9-%D0%B6%D0%B8%D0%BC-%D1%81%D1%82%D0%BE%D1%8F-%D1%81-%D0%B3%D0%B0%D0%BD%D1%82%D0%B5%D0%BB%D0%B5%D0%B9.gif',
            calories = 0.4,
            equipment = 'С гантелями'
        ),

        Exercise(
            name ='Французский жим с гантелями сидя',
            description = 'В этом упражнении работает трицепс.',
            muscle_group = 'Мышцы рук',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%84%D1%80%D0%B0%D0%BD%D1%86%D1%83%D0%B7%D0%BA%D0%B8%D0%B9-%D0%B6%D0%B8%D0%BC-%D1%81-%D0%B3%D0%B0%D0%BD%D1%82%D0%B5%D0%BB%D0%B5%D0%B9-%D1%81%D0%B8%D0%B4%D1%8F.gif',
            calories = 0.4,
            equipment = 'С гантелями'
        ),

        Exercise(
            name ='Французский жим с гантелями лёжа (с 2 гантелями)',
            description = 'В этом упражнении работает трицепс.',
            muscle_group = 'Мышцы рук',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%84%D1%80%D0%B0%D0%BD%D1%86%D1%83%D0%B7%D0%BA%D0%B8%D0%B9-%D0%B6%D0%B8%D0%BC-%D0%BB%D1%91%D0%B6%D0%B0-%D1%81-%D0%B3%D0%B0%D0%BD%D1%82%D0%B5%D0%BB%D1%8F%D0%BC%D0%B8.gif',
            calories = 0.4,
            equipment = 'С гантелями'
        ),  

        Exercise(
            name ='Разгибание руки из-за головы',
            description = 'В этом упражнении работает трицепс.',
            muscle_group = 'Мышцы рук',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%80%D0%B0%D1%88%D0%B8%D0%B1%D0%B0%D0%BD%D0%B8%D0%B5-%D1%80%D1%83%D0%BA%D0%B8-%D1%81-%D0%B3%D0%B0%D0%BD%D1%82%D0%B5%D0%BB%D0%B5%D0%B9-%D0%B8%D0%B7-%D0%B7%D0%B0-%D0%B3%D0%BE%D0%BB%D0%BE%D0%B2%D1%8B.gif',
            calories = 0.4,
            equipment = 'С гантелями'
        ), 

        Exercise(
            name ='Разгибание руки с гантелей в наклоне',
            description = 'В этом упражнении работает трицепс.',
            muscle_group = 'Мышцы рук',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%80%D0%B0%D0%B7%D0%B3%D0%B8%D0%B1%D0%B0%D0%BD%D0%B8%D0%B5-%D1%80%D1%83%D0%BA%D0%B8-%D0%B2-%D0%BD%D0%B0%D0%BA%D0%BB%D0%BE%D0%BD%D0%B5.gif',
            calories = 0.4,
            equipment = 'С гантелями'
        ), 

        Exercise(
            name ='Молоток',
            description = 'В этом упражнении работает предплечье.',
            muscle_group = 'Мышцы рук',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BC%D0%BE%D0%BB%D0%BE%D1%82%D0%BE%D0%BA-%D1%81-%D0%B3%D0%B0%D0%BD%D1%82%D0%B5%D0%BB%D1%8F%D0%BC%D0%B8.gif',
            calories = 0.4,
            equipment = 'С гантелями'
        ), 

        Exercise(
            name ='Подъем гантель с упором о скамью',
            description = 'В этом упражнении работает предплечье.',
            muscle_group = 'Мышцы рук',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BF%D0%BE%D0%B4%D1%8A%D1%91%D0%BC-%D0%B3%D0%B0%D0%BD%D1%82%D0%B5%D0%BB%D0%B5%D0%B9-%D0%BD%D0%B0-%D0%BF%D1%80%D0%B5%D0%B4%D0%BF%D0%BB%D0%B5%D1%87%D1%8C%D0%B5-%D1%81-%D1%83%D0%BF%D0%BE%D1%80%D0%BE%D0%BC-%D0%BE%D0%B1-%D1%81%D0%BA%D0%B0%D0%BC%D1%8C%D1%8E.gif',
            calories = 0.4,
            equipment = 'С гантелями'
        ), 

        Exercise(
            name ='Узкие отжимания',
            description = 'В этом упражнении работает трицепс.',
            muscle_group = 'Мышцы рук',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BE%D1%82%D0%B6-%D1%83%D0%B7%D0%BA%D0%B8%D0%B5.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Разгибания рук в обратной пленке',
            description = 'В этом упражнении работает трицепс.',
            muscle_group = 'Мышцы рук',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%80%D0%B0%D0%B7%D0%B3%D0%B8%D0%B1%D0%B0%D0%BD%D0%B8%D1%8F-%D1%80%D1%83%D0%BA-%D0%BE%D1%82-%D0%BF%D0%BE%D0%BB%D0%B0-%D0%B2-%D0%BE%D0%B1%D1%80%D0%B0%D1%82%D0%BD%D0%BE%D0%B9-%D0%BF%D0%BB%D0%B0%D0%BD%D0%BA%D0%B5.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Отжимания спиной к скамье или стулу',
            description = 'В этом упражнении работает трицепс.',
            muscle_group = 'Мышцы рук',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BE%D1%82%D0%B6%D0%B8%D0%BC%D0%B0%D0%BD%D0%B8%D1%8F-%D1%81%D0%BF%D0%B8%D0%BD%D0%BE%D0%B9-%D0%BA-%D1%81%D0%BA%D0%B0%D0%BC%D1%8C%D0%B5.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Сгибания на бицепс',
            description = 'В этом упражнении работает бицепс.',
            muscle_group = 'Мышцы рук',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%81%D0%B3%D0%B8%D0%B1%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BD%D0%B0-%D0%B1%D0%B8%D1%86%D0%B5%D0%BF%D1%81-%D0%B4%D0%B2%D1%83%D0%BC%D1%8F-%D1%80%D1%83%D0%BA%D0%B0%D0%BC%D0%B8.gif',
            calories = 0.4,
            equipment = 'С резиновыми петлями'
        ),

        Exercise(
            name ='Сгибания на бицепс поочередно каждой рукой',
            description = 'В этом упражнении работает бицепс.',
            muscle_group = 'Мышцы рук',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%81%D0%B3%D0%B8%D0%B1%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BD%D0%B0-%D0%B1%D0%B8%D1%86%D0%B5%D0%BF%D1%81-%D0%BE%D0%B4%D0%BD%D0%BE%D0%B9-%D1%80%D1%83%D0%BA%D0%BE%D0%B9-1.gif',
            calories = 0.4,
            equipment = 'С резиновыми петлями'
        ),

        Exercise(
            name ='Сгибания на бицепс в наклоне',
            description = 'В этом упражнении работает бицепс.',
            muscle_group = 'Мышцы рук',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%81%D0%B3%D0%B8%D0%B1%D0%B0%D0%BD%D0%B8%D1%8F-%D0%BD%D0%B0-%D0%B1%D0%B8%D1%86%D0%B5%D0%BF%D1%81-%D0%B4%D0%B2%D1%83%D0%BC%D1%8F-%D1%80%D1%83%D0%BA%D0%B0%D0%BC%D0%B8-%D0%B2-%D0%BD%D0%B0%D0%BA%D0%BB%D0%BE%D0%BD%D0%B5.gif',
            calories = 0.4,
            equipment = 'С резиновыми петлями'
        ),

        Exercise(
            name ='Сгибания на бицепс в наклоне одной рукой',
            description = 'В этом упражнении работает бицепс.',
            muscle_group = 'Мышцы рук',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%81%D0%B3%D0%B8%D0%B1%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BD%D0%B0-%D0%B1%D0%B8%D1%86%D0%B5%D0%BF%D1%81-%D0%B2-%D0%BD%D0%B0%D0%BA%D0%BB%D0%BE%D0%BD%D0%B5.gif',
            calories = 0.4,
            equipment = 'С резиновыми петлями'
        ),

        Exercise(
            name ='Молотковые сгибания',
            description = 'В этом упражнении работает предплечье.',
            muscle_group = 'Мышцы рук',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%81%D0%B3%D0%B8%D0%B1%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BD%D0%B0-%D0%B1%D0%B8%D1%86%D0%B5%D0%BF%D1%81-%D0%B2-%D1%81%D1%82%D0%B8%D0%BB%D0%B5-%D0%BC%D0%BE%D0%BB%D0%BE%D1%82%D0%BA%D0%BE%D0%BC.gif',
            calories = 0.4,
            equipment = 'С резиновыми петлями'
        ),

        Exercise(
            name ='Молотковые сгибания одной рукой',
            description = 'В этом упражнении работает предплечье.',
            muscle_group = 'Мышцы рук',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%81%D0%B3%D0%B8%D0%B1%D0%B0%D0%BD%D0%B8%D1%8F-%D0%BD%D0%B0-%D0%B1%D0%B8%D1%86%D0%B5%D0%BF%D1%81-%D1%81%D1%82%D0%BE%D1%8F-%D0%BC%D0%BE%D0%BB%D0%BE%D1%82%D0%BA%D0%BE%D0%BC.gif',
            calories = 0.4,
            equipment = 'С резиновыми петлями'
        ),

        Exercise(
            name ='Молотковые сгибания в наклоне',
            description = 'В этом упражнении работает предплечье.',
            muscle_group = 'Мышцы рук',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%81%D0%B3%D0%B8%D0%B1%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BD%D0%B0-%D0%B1%D0%B8%D1%86%D0%B5%D0%BF%D1%81-%D0%B2-%D0%BD%D0%B0%D0%BA%D0%BB%D0%BE%D0%BD%D0%B5-%D0%BC%D0%BE%D0%BB%D0%BE%D1%82%D0%BE%D0%BC.gif',
            calories = 0.4,
            equipment = 'С резиновыми петлями'
        ),

        Exercise(
            name ='Разгибания из-за головы',
            description = 'В этом упражнении работает трицепс.',
            muscle_group = 'Мышцы рук',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%80%D0%B0%D0%B7%D0%B3%D0%B8%D0%B1%D0%B0%D0%BD%D0%B8%D0%B5-%D1%80%D1%83%D0%BA-%D0%B2%D0%B2%D0%B5%D1%80%D1%85-%D0%B8%D0%B7-%D0%B7%D0%B0-%D0%B3%D0%BE%D0%BB%D0%BE%D0%B2%D1%8B.gif',
            calories = 0.4,
            equipment = 'С резиновыми петлями'
        ),

        Exercise(
            name ='Разгибания из-за плеч',
            description = 'В этом упражнении работает трицепс.',
            muscle_group = 'Мышцы рук',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%80%D0%B0%D0%B7%D0%B3%D0%B8%D0%B1%D0%B0%D0%BD%D0%B8%D1%8F-%D0%BD%D0%B0-%D1%82%D1%80%D0%B8%D1%86%D0%B5%D0%BF%D1%81-%D0%B2%D0%BF%D0%B5%D1%80%D0%B5%D0%B4-%D0%B8%D0%B7-%D0%B7%D0%B0-%D0%BF%D0%BB%D0%B5%D1%87.gif',
            calories = 0.4,
            equipment = 'С резиновыми петлями'
        ),

        Exercise(
            name ='Разгибания руки в наклоне',
            description = 'В этом упражнении работает трицепс.',
            muscle_group = 'Мышцы рук',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%80%D0%B0%D0%B7%D0%B3%D0%B8%D0%B1%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BD%D0%B0-%D1%82%D1%80%D0%B8%D1%86%D0%B5%D0%BF%D1%81-%D0%B2-%D0%BD%D0%B0%D0%BA%D0%BB%D0%BE%D0%BD%D0%B5-1.gif',
            calories = 0.4,
            equipment = 'С резиновыми петлями'
        ),

        Exercise(
            name ='Разгибания руки с резинкой',
            description = 'В этом упражнении работает трицепс.',
            muscle_group = 'Мышцы рук',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/04/%D1%80%D0%B0%D0%B7%D0%B3%D0%B8%D0%B1%D0%B0%D0%BD%D0%B8%D0%B5-%D1%80%D1%83%D0%BA%D0%B8-%D0%BD%D0%B0-%D1%82%D1%80%D0%B8%D1%86%D0%B5%D0%BF%D1%81-%D1%81%D1%82%D0%BE%D1%8F.gif',
            calories = 0.4,
            equipment = 'С фитнес-резинкой'
        ),

        Exercise(
            name ='Сгибания с резинкой',
            description = 'В этом упражнении работает трицепс.',
            muscle_group = 'Мышцы рук',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/04/%D1%81%D0%B3%D0%B8%D0%B1%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BD%D0%B0-%D0%B1%D0%B8%D1%86%D0%B5%D0%BF%D1%81.gif',
            calories = 0.4,
            equipment = 'С фитнес резинкой'
        ),

        Exercise(
            name ='Тяга штанги обратным хватом',
            description = 'В этом упражнении работает бицепс.',
            muscle_group = 'Мышцы рук',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%82%D1%8F%D0%B3%D0%B0-%D1%88%D1%82%D0%B0%D0%BD%D0%B3%D0%B8-%D0%B2-%D0%BD%D0%B0%D0%BA%D0%BB%D0%BE%D0%BD%D0%B5-%D0%BE%D0%B1%D1%80%D0%B0%D1%82%D0%BD%D1%8B%D0%BC-%D1%85%D0%B2%D0%B0%D1%82%D0%BE%D0%BC.gif',
            calories = 0.4,
            equipment = 'Со штангой'
        ),

        Exercise(
            name ='Подъем штанги на бицепс',
            description = 'В этом упражнении работает бицепс.',
            muscle_group = 'Мышцы рук',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BF%D0%BE%D0%B4%D1%8A%D0%B5%D0%BC-%D1%88%D1%82%D0%B0%D0%BD%D0%B3%D0%B8-%D0%BD%D0%B0-%D0%B1%D0%B8%D1%86%D0%B5%D0%BF%D1%81.gif',
            calories = 0.4,
            equipment = 'Со штангой'
        ),

        Exercise(
            name ='Подъем штанги с упором о скамью',
            description = 'В этом упражнении работает бицепс.',
            muscle_group = 'Мышцы рук',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%B1%D0%B8%D1%86%D0%B5%D0%BF%D1%81-%D1%81%D0%BE-%D1%88%D1%82%D0%B0%D0%BD%D0%B3%D0%BE%D0%B9-%D0%BB%D0%B5%D0%B6%D0%B0-%D0%BD%D0%B0-%D1%81%D0%BA%D0%B0%D0%BC%D1%8C%D0%B5.gif',
            calories = 0.4,
            equipment = 'Со штангой'
        ),

        Exercise(
            name ='Жим лежа узким хватом',
            description = 'В этом упражнении работает трицепс.',
            muscle_group = 'Мышцы рук',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%B6%D0%B8%D0%BC-%D1%88%D1%82%D0%B0%D0%BD%D0%B3%D0%B8-%D0%BB%D0%B5%D0%B6%D0%B0-%D1%83%D0%B7%D0%BA%D0%B8%D0%BC-%D1%85%D0%B2%D0%B0%D1%82%D0%BE%D0%BC.gif',
            calories = 0.4,
            equipment = 'Со штангой'
        ),

        Exercise(
            name ='Французский жим лежа',
            description = 'В этом упражнении работает трицепс.',
            muscle_group = 'Мышцы рук',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%84%D1%80%D0%B0%D0%BD%D1%86%D1%83%D0%B7%D1%81%D0%BA%D0%B8%D0%B9-%D0%B6%D0%B8%D0%BC-%D1%81%D0%BE-%D1%88%D1%82%D0%B0%D0%BD%D0%B3%D0%BE%D0%B9-%D0%BB%D0%B5%D0%B6%D0%B0.gif',
            calories = 0.4,
            equipment = 'Со штангой'
        ),

        Exercise(
            name ='Французский жим сидя',
            description = 'В этом упражнении работает трицепс.',
            muscle_group = 'Мышцы рук',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%84%D1%80%D0%B0%D0%BD%D1%86%D1%83%D0%B7%D0%BA%D0%B8%D0%B9-%D0%B6%D0%B8%D0%BC-%D1%81%D0%B8%D0%B4%D1%8F.gif',
            calories = 0.4,
            equipment = 'Со штангой'
        ),

        Exercise(
            name ='Французский жим стоя',
            description = 'В этом упражнении работает трицепс.',
            muscle_group = 'Мышцы рук',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%84%D1%80%D0%B0%D0%BD%D1%86%D1%83%D0%B7%D0%BA%D0%B8%D0%B9-%D0%B6%D0%B8%D0%BC-%D1%81%D1%82%D0%BE%D1%8F.gif',
            calories = 0.4,
            equipment = 'Со штангой'
        ),

        Exercise(
            name ='Подъем штанги на бицепс обратным хватом',
            description = 'В этом упражнении работает предплечье.',
            muscle_group = 'Мышцы рук',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BF%D0%BE%D0%B4%D1%8A%D0%B5%D0%BC-%D1%88%D1%82%D0%B0%D0%BD%D0%B3%D0%B8-%D0%BD%D0%B0-%D0%B1%D0%B8%D1%86%D0%B5%D0%BF%D1%81-%D0%BE%D0%B1%D1%80%D0%B0%D1%82%D0%BD%D1%8B%D0%BC-%D1%85%D0%B2%D0%B0%D1%82%D0%BE%D0%BC.gif',
            calories = 0.4,
            equipment = 'Со штангой'
        ),

        Exercise(
            name ='Подтягивания обратным хватом',
            description = 'В этом упражнении работает бицепс.',
            muscle_group = 'Мышцы рук',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%9F%D0%BE%D0%B4%D1%82%D1%8F%D0%B3%D0%B8%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F-%D0%BE%D0%B1%D1%80%D0%B0%D1%82%D0%BD%D1%8B%D0%BC-%D1%85%D0%B2%D0%B0%D1%82%D0%BE%D0%BC.gif',
            calories = 0.4,
            equipment = 'На турнике'
        ),

        Exercise(
            name ='Подтягивания параллельным хватом',
            description = 'В этом упражнении работает бицепс.',
            muscle_group = 'Мышцы рук',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%9F%D0%BE%D0%B4%D1%82%D1%8F%D0%B3%D0%B8%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F-%D0%BF%D0%B0%D1%80%D0%B0%D0%BB%D0%BB%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%BC-%D1%85%D0%B2%D0%B0%D1%82%D0%BE%D0%BC.gif',
            calories = 0.4,
            equipment = 'На турнике'
        ),

        Exercise(
            name ='Отжимания на брусьях узким хватом',
            description = 'В этом упражнении работает трицепс.',
            muscle_group = 'Мышцы рук',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/08/%D0%BE%D1%82%D0%B6%D0%B8%D0%BC%D0%B0%D0%BD%D0%B8%D1%8F-%D0%BD%D0%B0-%D0%B1%D1%80%D1%83%D1%81%D1%8C%D1%8F%D1%85-%D0%B4%D0%BB%D1%8F-%D1%82%D1%80%D0%B8%D1%86%D0%B5%D0%BF%D1%81%D0%BE%D0%B2.gif',
            calories = 0.4,
            equipment = 'На брусьях'
        ),

        Exercise(
            name ='Приседания',
            description = 'В этом упражнении даётся комплексная нагрузка на все мышцы ног.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/09/%D0%BF%D1%80%D0%B8%D1%81%D0%B5%D0%B4%D0%B0%D0%BD%D0%B8%D1%8F.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Широкие приседания',
            description = 'В этом упражнении даётся комплексная нагрузка на все мышцы ног.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BF%D1%80%D0%B8%D1%81%D0%B5%D0%B4%D0%B0%D0%BD%D0%B8%D1%8F-%D1%88%D0%B8%D1%80%D0%BE%D0%BA%D0%B8%D0%B5.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Выпады',
            description = 'В этом упражнении даётся комплексная нагрузка на все мышцы ног.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/09/%D0%B2%D1%8B%D0%BF%D0%B0%D0%B4%D1%8B-%D0%B2%D0%BF%D0%B5%D1%80%D0%B5%D0%B4.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Выпады назад',
            description = 'В этом упражнении даётся комплексная нагрузка на все мышцы ног.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%B2%D1%8B%D0%BF%D0%B0%D0%B4%D1%8B-%D0%BD%D0%B0%D0%B7%D0%B0%D0%B4.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Выпады в сторону',
            description = 'В этом упражнении даётся комплексная нагрузка на все мышцы ног.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%B2%D1%8B%D0%BF%D0%B0%D0%B4%D1%8B-%D0%B2-%D1%81%D1%82%D0%BE%D1%80%D0%BE%D0%BD%D1%83.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Шаги в сторону в полуприседе',
            description = 'В этом упражнении даётся комплексная нагрузка на все мышцы ног.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%88%D0%B0%D0%B3%D0%B8-%D0%B2-%D1%81%D1%82%D0%BE%D1%80%D0%BE%D0%BD%D1%83-%D0%B2-%D0%BF%D0%BE%D0%BB%D1%83%D0%BF%D1%80%D0%B8%D1%81%D0%B5%D0%B4%D0%B5-1.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Шаги полу-гуськом',
            description = 'В этом упражнении даётся комплексная нагрузка на все мышцы ног.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%85%D0%BE%D0%B4%D1%8C%D0%B1%D0%B0-%D0%B2-%D0%BF%D0%BE%D0%BB%D1%83%D0%BF%D1%80%D0%B8%D1%81%D0%B5%D0%B4%D0%B5.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Приседания с шагом в сторону',
            description = 'В этом упражнении даётся комплексная нагрузка на все мышцы ног.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%88%D0%B0%D0%B3%D0%B8-%D0%B2-%D1%81%D1%82%D0%BE%D1%80%D0%BE%D0%BD%D1%83-%D1%81-%D0%BF%D1%80%D0%B8%D1%81%D0%B5%D0%B4%D0%B0%D0%BD%D0%B8%D1%8F%D0%BC%D0%B8.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Подъем на стул (диван/скамью)',
            description = 'В этом упражнении даётся комплексная нагрузка на все мышцы ног.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%B7%D0%B0%D1%88%D0%B0%D0%B3%D0%B8%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BD%D0%B0-%D0%B2%D0%BE%D0%B7%D0%B2%D1%8B%D1%88%D0%B5%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D1%8C.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Боковой подъем на стул (диван/скамью)',
            description = 'В этом упражнении даётся комплексная нагрузка на все мышцы ног.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%B7%D0%B0%D1%88%D0%B0%D0%B3%D0%B8%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BD%D0%B0-%D0%B2%D0%BE%D0%B7%D0%B2%D1%8B%D1%88%D0%B5%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D1%8C-%D0%B1%D0%BE%D0%BA%D0%BE%D0%BC.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Приседания с подъемом бедра',
            description = 'В этом упражнении даётся комплексная нагрузка на все мышцы ног.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BF%D1%80%D0%B8%D1%81%D0%B5%D0%B4-%D1%81-%D0%BF%D0%BE%D0%B4%D1%8A%D0%B5%D0%BC%D0%BE%D0%BC-%D0%B1%D0%B5%D0%B4%D1%80%D0%B0.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Приседания со скручиванем корпуса',
            description = 'В этом упражнении даётся комплексная нагрузка на все мышцы ног.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BF%D1%80%D0%B8%D1%81%D0%B5%D0%B4-%D1%81-%D0%BF%D0%BE%D0%B2%D0%BE%D1%80%D0%BE%D1%82%D0%BE%D0%BC-%D0%BA%D0%BE%D1%80%D0%BF%D1%83%D1%81%D0%B0.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Приседания с подъемом на носки',
            description = 'В этом упражнении даётся комплексная нагрузка на все мышцы ног.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BF%D1%80%D0%B8%D1%81%D0%B5%D0%B4-%D1%81-%D0%BF%D0%BE%D0%B4%D1%8A%D0%B5%D0%BC%D0%BE%D0%BC-%D0%BD%D0%B0-%D0%BD%D0%BE%D1%81%D0%BA%D0%B8.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Приседания с боковым отведением ноги',
            description = 'В этом упражнении даётся комплексная нагрузка на все мышцы ног.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BF%D1%80%D0%B8%D1%81%D0%B5%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5-%D1%81-%D0%BE%D1%82%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%D0%BC-%D0%BD%D0%BE%D0%B3%D0%B8-%D0%B2-%D1%81%D1%82%D0%BE%D1%80%D0%BE%D0%BD%D1%83.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Махи вверх стоя на четвереньках',
            description = 'В этом упражнении работают ягодичные мышцы.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BC%D0%B0%D1%85%D0%B8-%D1%81%D0%BE%D0%B3%D0%BD%D1%83%D1%82%D0%BE%D0%B9-%D0%BD%D0%BE%D0%B3%D0%BE%D0%B9-%D0%BD%D0%B0-%D1%87%D0%B5%D1%82%D0%B2%D0%B5%D1%80%D0%B5%D0%BD%D1%8C%D0%BA%D0%B0%D1%85-1.gif',
            demonstration_video_2='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BC%D0%B0%D1%85%D0%B8-%D0%BD%D0%BE%D0%B3%D0%BE%D0%B9-%D1%81-%D0%B2%D1%8B%D0%BF%D1%80%D1%8F%D0%BC%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%D0%BC-%D0%BD%D0%B0-%D1%87%D0%B5%D1%82%D0%B2%D0%B5%D1%80%D0%B5%D0%BD%D1%8C%D0%BA%D0%B0%D1%85.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Махи ногой назад с упором о стул (стену)',
            description = 'В этом упражнении работают ягодичные мышцы.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BE%D1%82%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-%D0%BD%D0%BE%D0%B3%D0%B8-%D0%BD%D0%B0%D0%B7%D0%B0%D0%B4-%D1%81%D1%82%D0%BE%D1%8F-1.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Ягодичный мостик',
            description = 'В этом упражнении работают ягодичные мышцы.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%8F%D0%B3%D0%BE%D0%B4%D0%B8%D1%87%D0%BD%D1%8B%D0%B9-%D0%BC%D0%BE%D1%81%D1%82%D0%B8%D0%BA.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Ягодичный мостик на одной ноге',
            description = 'В этом упражнении работают ягодичные мышцы.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%8F%D0%B3%D0%BE%D0%B4%D0%B8%D1%87%D0%BD%D1%8B%D0%B9-%D0%BC%D0%BE%D1%81%D1%82%D0%B8%D0%BA-%D0%BD%D0%B0-%D0%BE%D0%B4%D0%BD%D0%BE%D0%B9-%D0%BD%D0%BE%D0%B3%D0%B5.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Маятник',
            description = 'В этом упражнении работают ягодичные мышцы.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BA%D1%80%D1%83%D0%B3%D0%BE%D0%B2%D1%8B%D0%B5-%D0%BC%D0%B0%D1%85%D0%B8-%D0%BD%D0%BE%D0%B3%D0%BE%D0%B9-%D0%BD%D0%B0-%D1%87%D0%B5%D1%82%D0%B2%D0%B5%D1%80%D0%B5%D0%BD%D1%8C%D0%BA%D0%B0%D1%85.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Отведение ноги в сторону на четвереньках',
            description = 'В этом упражнении работают ягодичные мышцы.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BC%D0%B0%D1%85%D0%B8-%D0%BD%D0%BE%D0%B3%D0%BE%D0%B9-%D0%B2%D0%B1%D0%BE%D0%BA-%D0%BD%D0%B0-%D1%87%D0%B5%D1%82%D0%B2%D0%B5%D1%80%D0%B5%D0%BD%D1%8C%D0%BA%D0%B0%D1%85.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Дотягивания до стула',
            description = 'В этом упражнении работают ягодичные мышцы.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/09/%D0%B4%D0%BE%D1%82%D1%8F%D0%B3%D0%B8%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F-%D1%81%D1%82%D0%BE%D1%8F.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Отведение ноги в сторону лежа',
            description = 'В этом упражнении работают мышцы внешней части бедра.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BC%D0%B0%D1%85%D0%B8-%D0%BD%D0%BE%D0%B3%D0%BE%D0%B9-%D0%B2%D0%B2%D0%B5%D1%80%D1%85-%D0%BB%D0%B5%D0%B6%D0%B0-%D0%BD%D0%B0-%D0%B1%D0%BE%D0%BA%D1%83.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Круговое вращение ногой лежа на боку',
            description = 'В этом упражнении работают мышцы внешней части бедра.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/09/%D0%BA%D1%80%D1%83%D0%B3%D0%BE%D0%B2%D1%8B%D0%B5-%D0%B2%D1%80%D0%B0%D1%89%D0%B5%D0%BD%D0%B8%D1%8F-%D0%BD%D0%BE%D0%B3%D0%BE%D0%B9-%D0%BB%D0%B5%D0%B6%D0%B0-%D0%BD%D0%B0-%D0%B1%D0%BE%D0%BA%D1%83.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Приведение бедра лежа на боку',
            description = 'В этом упражнении работают мышцы внутренней части бедра.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BF%D1%80%D0%B8%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B1%D0%B5%D0%B4%D1%80%D0%B0-%D0%BB%D0%B5%D0%B6%D0%B0-%D0%BD%D0%B0-%D0%B1%D0%BE%D0%BA%D1%83.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Приседания с гантелями в руках',
            description = 'В этом упражнении даётся комплексная нагрузка на все мышцы ног.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BF%D1%80%D0%B8%D1%81%D0%B5%D0%B4%D0%B0%D0%BD%D0%B8%D1%8F-%D1%81-%D0%B3%D0%B0%D0%BD%D1%82%D0%B5%D0%BB%D1%8F%D0%BC%D0%B8.gif',
            calories = 0.4,
            equipment = 'С гантелями'
        ),

        Exercise(
            name ='Широкие приседания с одной гантелей',
            description = 'В этом упражнении даётся комплексная нагрузка на все мышцы ног.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BF%D1%80%D0%B8%D1%81%D0%B5%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BF%D0%BB%D0%B8%D0%B5-%D1%81-%D0%B3%D0%B0%D0%BD%D1%82%D0%B5%D0%BB%D1%8F%D0%BC%D0%B8.gif',
            calories = 0.4,
            equipment = 'С гантелями'
        ),

        Exercise(
            name ='Приседание с гантелей на груди',
            description = 'В этом упражнении даётся комплексная нагрузка на все мышцы ног.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BF%D1%80%D0%B8%D1%81%D0%B5%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5-%D1%81-%D0%B3%D0%B0%D0%BD%D1%82%D0%B5%D0%BB%D0%B5%D0%B9-%D0%BD%D0%B0-%D0%B3%D1%80%D1%83%D0%B4%D0%B8.gif',
            calories = 0.4,
            equipment = 'С гантелями'
        ),

        Exercise(
            name ='Выпады с гантелями',
            description = 'В этом упражнении даётся комплексная нагрузка на все мышцы ног.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%B2%D1%8B%D0%BF%D0%B0%D0%B4%D1%8B-%D1%81-%D0%B3%D0%B0%D0%BD%D1%82%D0%B5%D0%BB%D1%8F%D0%BC%D0%B8.gif',
            calories = 0.4,
            equipment = 'С гантелями'
        ),

        Exercise(
            name ='Выпады назад с гантелями',
            description = 'В этом упражнении даётся комплексная нагрузка на все мышцы ног.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%B2%D1%8B%D0%BF%D0%B0%D0%B4%D1%8B-%D0%BD%D0%B0%D0%B7%D0%B0%D0%B4-%D1%81-%D0%B3%D0%B0%D0%BD%D1%82%D0%B5%D0%BB%D1%8F%D0%BC%D0%B8.gif',
            calories = 0.4,
            equipment = 'С гантелями'
        ),

        Exercise(
            name ='Болгарские выпады',
            description = 'В этом упражнении даётся комплексная нагрузка на все мышцы ног.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%B1%D0%BE%D0%BB%D0%B3%D0%B0%D1%80%D1%81%D0%BA%D0%B8%D0%B5-%D0%B2%D1%8B%D0%BF%D0%B0%D0%B4%D1%8B-%D1%81-%D0%B3%D0%B0%D0%BD%D1%82%D0%B5%D0%BB%D1%8F%D0%BC%D0%B8.gif',
            calories = 0.4,
            equipment = 'С гантелями'
        ),

        Exercise(
            name ='Мертвая тяга с гантелями',
            description = 'В этом упражнении даётся комплексная нагрузка на все мышцы ног.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BC%D0%B5%D1%80%D1%82%D0%B2%D0%B0%D1%8F-%D1%82%D1%8F%D0%B3%D0%B0-%D1%81-%D0%B3%D0%B0%D0%BD%D1%82%D0%B5%D0%BB%D1%8F%D0%BC%D0%B8.gif',
            calories = 0.4,
            equipment = 'С гантелями'
        ),

        Exercise(
            name ='Подъем на носки с гантелями',
            description = 'В этом упражнении даётся комплексная нагрузка на все мышцы ног.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BF%D0%BE%D0%B4%D1%8A%D1%91%D0%BC-%D0%BD%D0%B0-%D0%B8%D0%BA%D1%80%D1%8B-%D1%81-%D0%B3%D0%B0%D0%BD%D1%82%D0%B5%D0%BB%D1%8F%D0%BC%D0%B8.gif',
            calories = 0.4,
            equipment = 'С гантелями'
        ),

        Exercise(
            name ='Приседания с резинкой',
            description = 'В этом упражнении даётся комплексная нагрузка на все мышцы ног.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/04/%D0%BF%D1%80%D0%B8%D1%81%D0%B5%D0%B4%D0%B0%D0%BD%D0%B8%D1%8F.gif',
            calories = 0.4,
            equipment = 'С фитнес-резинкой'
        ),

        Exercise(
            name ='Приседания с махом ногой',
            description = 'В этом упражнении даётся комплексная нагрузка на все мышцы ног.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/04/%D0%B2%D1%8B%D0%BF%D0%B0%D0%B4%D1%8B-%D0%B2%D0%BF%D0%B5%D1%80%D0%B5%D0%B4-%D1%81-%D0%BC%D0%B0%D1%85%D0%BE%D0%BC-%D0%BD%D0%BE%D0%B3%D0%B8.gif',
            calories = 0.4,
            equipment = 'С фитнес-резинкой'
        ),

        Exercise(
            name ='Приседания с отведением ноги назад',
            description = 'В этом упражнении даётся комплексная нагрузка на все мышцы ног.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/04/%D0%BF%D1%80%D0%B8%D1%81%D0%B5%D0%B4-%D1%81-%D0%BE%D1%82%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%D0%BC-%D0%BD%D0%BE%D0%B3%D0%B8-%D0%BD%D0%B0%D0%B7%D0%B0%D0%B4.gif',
            calories = 0.4,
            equipment = 'С фитнес-резинкой'
        ),

        Exercise(
            name ='Приседания с отведением ноги в сторону',
            description = 'В этом упражнении даётся комплексная нагрузка на все мышцы ног.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/04/%D0%BF%D1%80%D0%B8%D1%81%D0%B5%D0%B6%D0%B0%D0%BD%D0%B8%D1%8F-%D1%81-%D0%BE%D1%82%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5%D0%BC-%D0%BD%D0%BE%D0%B3%D0%B8-%D0%B2-%D1%81%D1%82%D0%BE%D1%80%D0%BE%D0%BD%D1%83.gif',
            calories = 0.4,
            equipment = 'С фитнес-резинкой'
        ),

        Exercise(
            name ='Ходьба в сторону',
            description = 'В этом упражнении даётся комплексная нагрузка на все мышцы ног.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/04/%D1%85%D0%BE%D0%B4%D1%8C%D0%B1%D0%B0-%D0%B1%D0%BE%D0%BA%D0%BE%D0%BC.gif',
            calories = 0.4,
            equipment = 'С фитнес-резинкой'
        ),

        Exercise(
            name ='Ходьба в строну с приседаниями',
            description = 'В этом упражнении даётся комплексная нагрузка на все мышцы ног.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/04/%D1%85%D0%BE%D0%B4%D1%8C%D0%B1%D0%B0-%D0%B2-%D1%81%D1%82%D0%BE%D1%80%D0%BE%D0%BD%D1%83-%D1%81-%D0%BF%D1%80%D0%B8%D1%81%D0%B5%D0%B4%D0%B0%D0%BD%D0%B8%D1%8F%D0%BC%D0%B8.gif',
            calories = 0.4,
            equipment = 'С фитнес-резинкой'
        ),

        Exercise(
            name ='Махи ногой лежа на боку',
            description = 'В этом упражнении работают мышцы внешней части бедра.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/04/%D0%BC%D0%B0%D1%85%D0%B8-%D0%BD%D0%BE%D0%B3%D0%BE%D0%B9-%D0%BB%D0%B5%D0%B6%D0%B0-%D0%BD%D0%B0-%D0%B1%D0%BE%D0%BA%D1%83.gif',
            calories = 0.4,
            equipment = 'С фитнес-резинкой'
        ),

        Exercise(
            name ='Отведение ноги в сторону стоя',
            description = 'В этом упражнении работают мышцы внешней части бедра.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/04/%D0%BE%D1%82%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-%D0%BD%D0%BE%D0%B3%D0%B8-%D0%B2-%D1%81%D1%82%D0%BE%D1%80%D0%BE%D0%BD%D1%83-%D1%81%D1%82%D0%BE%D1%8F-%D1%81-%D0%BE%D0%BF%D0%BE%D1%80%D0%BE%D0%B9.gif',
            calories = 0.4,
            equipment = 'С фитнес-резинкой'
        ),

        Exercise(
            name ='Сгибания ног лежа',
            description = 'В этом упражнении работают ягодичные мышцы.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/04/%D1%81%D0%B3%D0%B8%D0%B1%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BD%D0%BE%D0%B3%D0%B8-%D0%BB%D0%B5%D0%B6%D0%B0-%D0%BD%D0%B0-%D0%B6%D0%B8%D0%B2%D0%BE%D1%82%D0%B5.gif',
            calories = 0.4,
            equipment = 'С фитнес-резинкой'
        ),

        Exercise(
            name ='Приседания',
            description = 'В этом упражнении даётся комплексная нагрузка на все мышцы ног.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BF%D1%80%D0%B8%D1%81%D0%B5%D0%B4%D0%B0%D0%BD%D0%B8%D1%8F-1.gif',
            calories = 0.4,
            equipment = 'С резиновыми петлями'
        ),

        Exercise(
            name ='Выпады',
            description = 'В этом упражнении даётся комплексная нагрузка на все мышцы ног.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%B2%D1%8B%D0%BF%D0%B0%D0%B4%D1%8B-%D1%81-%D1%80%D0%B5%D0%B7%D0%B8%D0%BD%D0%BE%D0%B9.gif',
            calories = 0.4,
            equipment = 'С резиновыми петлями'
        ),

        Exercise(
            name ='Мертвая тяга с резиновыми петлями',
            description = 'В этом упражнении даётся комплексная нагрузка на все мышцы ног.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BC%D0%B5%D1%80%D1%82%D0%B2%D0%B0%D1%8F-%D1%82%D1%8F%D0%B3%D0%B0-%D1%81-%D1%80%D0%B5%D0%B7%D0%B8%D0%BD%D0%BE%D0%B9.gif',
            calories = 0.4,
            equipment = 'С резиновыми петлями'
        ),

        Exercise(
            name ='Жим одной ногой',
            description = 'В этом упражнении даётся комплексная нагрузка на все мышцы ног.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%B6%D0%B8%D0%BC-%D0%BD%D0%BE%D0%B3%D0%BE%D0%B9-%D0%BB%D0%B5%D0%B6%D0%B0-1.gif',
            calories = 0.4,
            equipment = 'С резиновыми петлями'
        ),

        Exercise(
            name ='Приседания со штангой на плечах',
            description = 'В этом упражнении даётся комплексная нагрузка на все мышцы ног.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BF%D1%80%D0%B8%D1%81%D0%B5%D0%B4%D0%B0%D0%BD%D0%B8%D1%8F-%D1%81%D0%BE-%D1%88%D1%82%D0%B0%D0%BD%D0%B3%D0%BE%D0%B9.gif',
            calories = 0.4,
            equipment = 'Со штангой'
        ),

        Exercise(
            name ='Выпады',
            description = 'В этом упражнении даётся комплексная нагрузка на все мышцы ног.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%B2%D1%8B%D0%BF%D0%B0%D0%B4%D1%8B-%D1%81%D0%BE-%D1%88%D1%82%D0%B0%D0%BD%D0%B3%D0%BE%D0%B9.gif',
            calories = 0.4,
            equipment = 'Со штангой'
        ),

        Exercise(
            name ='Выпады назад',
            description = 'В этом упражнении даётся комплексная нагрузка на все мышцы ног.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%B2%D1%8B%D0%BF%D0%B0%D0%B4%D1%8B-%D1%81%D0%BE-%D1%88%D1%82%D0%B0%D0%BD%D0%B3%D0%BE%D0%B9-%D0%BD%D0%B0%D0%B7%D0%B0%D0%B4.gif',
            calories = 0.4,
            equipment = 'Со штангой'
        ),

        Exercise(
            name ='Выпады со штангой на месте',
            description = 'В этом упражнении даётся комплексная нагрузка на все мышцы ног.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%B2%D1%8B%D0%BF%D0%B0%D0%B4%D1%8B-%D0%BD%D0%B0-%D0%BC%D0%B5%D1%81%D1%82%D0%B5-1.gif',
            calories = 0.4,
            equipment = 'Со штангой'
        ),

        Exercise(
            name ='Мертвая тяга со штангой',
            description = 'В этом упражнении даётся комплексная нагрузка на все мышцы ног.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BC%D0%B5%D1%80%D1%82%D0%B2%D0%B0%D1%8F-%D1%82%D1%8F%D0%B3%D0%B0-%D1%81%D0%BE-%D1%88%D1%82%D0%B0%D0%BD%D0%B3%D0%BE%D0%B9.gif',
            calories = 0.4,
            equipment = 'Со штангой'
        ),

        Exercise(
            name ='Становая тяга со штангой «сумо»',
            description = 'В этом упражнении даётся комплексная нагрузка на все мышцы ног.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%B0%D1%8F-%D1%81%D1%83%D0%BC%D0%BE.gif',
            calories = 0.4,
            equipment = 'Со штангой'
        ),

        Exercise(
            name ='Подъем на носки стоя',
            description = 'В этом упражнении даётся комплексная нагрузка на все мышцы ног.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BF%D0%BE%D0%B4%D1%8A%D0%B5%D0%BC-%D0%BD%D0%B0-%D0%BD%D0%BE%D0%BA%D0%B0%D1%85-%D1%81%D0%BE-%D1%88%D1%82%D0%B0%D0%BD%D0%B3%D0%BE%D0%B9.gif',
            calories = 0.4,
            equipment = 'Со штангой'
        ),

        Exercise(
            name ='Подъем на носки стоя',
            description = 'В этом упражнении даётся комплексная нагрузка на все мышцы ног.',
            muscle_group = 'Мышцы ног',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BF%D0%BE%D0%B4%D1%8A%D0%B5%D0%BC-%D0%BD%D0%B0-%D0%BD%D0%BE%D0%BA%D0%B0%D1%85-%D1%81%D0%BE-%D1%88%D1%82%D0%B0%D0%BD%D0%B3%D0%BE%D0%B9.gif',
            calories = 0.4,
            equipment = 'Со штангой'
        ),

        Exercise(
            name ='Отжимания',
            description = 'В этом упражнении работает только передняя часть плеча.',
            muscle_group = 'Мышцы плеча',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BE%D1%82%D0%B6%D0%B8%D0%BC%D0%B0%D0%BD%D0%B8%D1%8F-%D0%BA%D0%BB%D0%B0%D1%81%D1%81%D0%B8%D0%BA.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Армейские отжимания',
            description = 'В этом упражнении работает передняя и средняя часть плеча.',
            muscle_group = 'Мышцы плеча',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%B0%D1%80%D0%BC%D0%B5%D0%B9%D1%81%D0%BA%D0%B8%D0%B5-%D0%BE%D1%82%D0%B6%D0%B8%D0%BC%D0%B0%D0%BD%D0%B8%D1%8F.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Жим гантель стоя или сидя',
            description = 'В этом упражнении работает преимущественно средний пучок и частично передний.',
            muscle_group = 'Мышцы плеча',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%B6%D0%B8%D0%BC-%D0%B3%D0%B0%D0%BD%D1%82%D0%B5%D0%BB%D0%B5%D0%B9-%D1%81%D1%82%D0%BE%D1%8F-2.gif',
            demonstration_video_2='https://makefitness.pro/wp-content/uploads/2020/02/%D0%B6%D0%B8%D0%BC-%D0%B3%D0%B0%D0%BD%D1%82%D0%B5%D0%BB%D0%B5%D0%B9-%D1%81%D0%B8%D0%B4%D1%8F.gif',
            calories = 0.4,
            equipment = 'С гантелями'
        ),

        Exercise(
            name ='Махи с гантелями стоя или сидя',
            description = 'В этом упражнении работает средний пучок.',
            muscle_group = 'Мышцы плеча',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BC%D0%B0%D1%85%D0%B8-%D1%81-%D0%B3%D0%B0%D0%BD%D1%82%D0%B5%D0%BB%D1%8F%D0%BC%D0%B8-%D1%81%D1%82%D0%BE%D1%8F.gif',
            demonstration_video_2='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BC%D0%B0%D1%85%D0%B8-%D1%81-%D0%B3%D0%B0%D0%BD%D1%82%D0%B5%D0%BB%D1%8F%D0%BC%D0%B8-%D1%81%D0%B8%D0%B4%D1%8F.gif',
            calories = 0.4,
            equipment = 'С гантелями'
        ),

        Exercise(
            name ='Тяга к подбородку',
            description = 'В этом упражнении работает средний пучок.',
            muscle_group = 'Мышцы плеча',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%82%D1%8F%D0%B3%D0%B0-%D0%B3%D0%B0%D0%BD%D1%82%D0%B5%D0%BB%D0%B5%D0%B9-%D0%BA-%D0%BF%D0%BE%D0%B4%D0%B1%D0%BE%D1%80%D0%BE%D0%B4%D0%BA%D1%83.gif',
            calories = 0.4,
            equipment = 'С гантелями'
        ),

        Exercise(
            name ='Жим Арнольда стоя или сидя',
            description = 'В этом упражнении работает передний и средний пучок.',
            muscle_group = 'Мышцы плеча',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%B6%D0%B8%D0%BC-%D0%B0%D1%80%D0%BD%D0%BE%D0%BB%D1%8C%D0%B4%D0%B0.gif',
            demonstration_video_2='https://makefitness.pro/wp-content/uploads/2020/02/%D0%B6%D0%B8%D0%BC-%D0%B0%D1%80%D0%BD%D0%BE%D0%BB%D1%8C%D0%B4%D0%B0-%D1%81%D0%B8%D0%B4%D1%8F.gif',
            calories = 0.4,
            equipment = 'С гантелями'
        ),

        Exercise(
            name ='Махи перед собой',
            description = 'В этом упражнении работает передний пучок.',
            muscle_group = 'Мышцы плеча',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BC%D0%B0%D1%85%D0%B8-%D0%BF%D0%B5%D1%80%D0%B5%D0%B4-%D1%81%D0%BE%D0%B1%D0%BE%D0%B9.gif',
            calories = 0.4,
            equipment = 'С гантелями'
        ),

        Exercise(
            name ='Махи в наклоне',
            description = 'В этом упражнении работает задний пучок.',
            muscle_group = 'Мышцы плеча',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BC%D0%B0%D1%85%D0%B8-%D0%B3%D0%B0%D0%BD%D1%82%D0%B5%D0%BB%D1%8F%D0%BC%D0%B8-%D0%B2-%D0%BD%D0%B0%D0%BA%D0%BB%D0%BE%D0%BD%D0%B5.gif',
            calories = 0.4,
            equipment = 'С гантелями'
        ),

        Exercise(
            name ='Жим штанги стоя или сидя',
            description = 'В этом упражнении работает средняя и передняя часть плеча.',
            muscle_group = 'Мышцы плеча',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%B6%D0%B8%D0%BC-%D1%88%D1%82%D0%B0%D0%BD%D0%B3%D0%B8-%D1%81%D1%82%D0%BE%D1%8F.gif',
            demonstration_video_2='https://makefitness.pro/wp-content/uploads/2020/02/%D0%B6%D0%B8%D0%BC-%D1%88%D1%82%D0%B0%D0%BD%D0%B3%D0%B8-%D1%81%D0%B8%D0%B4%D1%8F.gif',
            calories = 0.4,
            equipment = 'Со штангой'
        ),

        Exercise(
            name ='Жим из-за головы',
            description = 'В этом упражнении работает средняя часть плеча.',
            muscle_group = 'Мышцы плеча',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%B6%D0%B8%D0%BC-%D0%B8%D0%B7-%D0%B7%D0%B0-%D0%B3%D0%BE%D0%BB%D0%BE%D0%B2%D1%8B-1.gif',
            calories = 0.4,
            equipment = 'Со штангой'
        ),

        Exercise(
            name ='Тяга к подбородку',
            description = 'В этом упражнении работает средний пучок.',
            muscle_group = 'Мышцы плеча',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%82%D1%8F%D0%B3%D0%B0-%D1%88%D1%82%D0%B0%D0%BD%D0%B3%D0%B8-%D0%BA-%D0%BF%D0%BE%D0%B4%D0%B1%D0%BE%D1%80%D0%BE%D0%B4%D0%BA%D1%83.gif',
            calories = 0.4,
            equipment = 'Со штангой'
        ),

        Exercise(
            name ='Подъем перед собой',
            description = 'В этом упражнении работает передний пучок.',
            muscle_group = 'Мышцы плеча',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BF%D0%BE%D0%B4%D1%8A%D0%B5%D0%BC-%D1%88%D1%82%D0%B0%D0%BD%D0%B3%D0%B8-%D0%BF%D0%B5%D1%80%D0%B5%D0%B4-%D1%81%D0%BE%D0%B1%D0%BE%D0%B9.gif',
            calories = 0.4,
            equipment = 'Со штангой'
        ),

        Exercise(
            name ='Жим стоя(двумя руками или поочередно)',
            description = 'В этом упражнении работает средняя и передняя часть плеча.',
            muscle_group = 'Мышцы плеча',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%B6%D0%B8%D0%BC-%D0%BE%D1%82-%D0%B3%D1%80%D1%83%D0%B4%D0%B8-%D0%B2%D0%B2%D0%B5%D1%80%D1%85.gif',
            demonstration_video_2='https://makefitness.pro/wp-content/uploads/2020/02/%D0%B6%D0%B8%D0%BC-%D0%BE%D0%B4%D0%BD%D0%BE%D0%B9-%D1%80%D1%83%D0%BA%D0%BE%D0%B9-%D0%B2%D0%B2%D0%B5%D1%80%D1%85.gif',
            calories = 0.4,
            equipment = 'С резиновыми петлями'
        ),

        Exercise(
            name ='Жим из-за головы',
            description = 'В этом упражнении работает средний пучок.',
            muscle_group = 'Мышцы плеча',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%B6%D0%B8%D0%BC-%D0%B8%D0%B7-%D0%B7%D0%B0-%D0%B3%D0%BE%D0%BB%D0%BE%D0%B2%D1%8B-2.gif',
            calories = 0.4,
            equipment = 'С резиновыми петлями'
        ),

        Exercise(
            name ='Отведение в сторону',
            description = 'В этом упражнении работает средний пучок.',
            muscle_group = 'Мышцы плеча',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%9E%D1%82%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B2-%D1%81%D1%82%D0%BE%D1%80%D0%BE%D0%BD%D1%83.gif',
            calories = 0.4,
            equipment = 'С резиновыми петлями'
        ),

        Exercise(
            name ='Тяга к подбородку',
            description = 'В этом упражнении работает средний пучок.',
            muscle_group = 'Мышцы плеча',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%82%D1%8F%D0%B3%D0%B0-%D0%BA-%D0%BF%D0%BE%D0%B4%D0%B1%D0%BE%D1%80%D0%BE%D0%B4%D0%BA%D1%83-2.gif',
            calories = 0.4,
            equipment = 'С резиновыми петлями'
        ),

        Exercise(
            name ='Разведения стоя',
            description = 'В этом упражнении работает средний пучок.',
            muscle_group = 'Мышцы плеча',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%80%D0%B0%D0%B7%D0%B2%D0%BE%D0%B4%D0%BA%D0%B0-%D0%B2-%D0%BB%D0%BE%D0%BA%D1%82%D0%B5-%D1%81%D1%82%D0%BE%D1%8F.gif',
            calories = 0.4,
            equipment = 'С резиновыми петлями'
        ),

        Exercise(
            name ='Махи перед собой',
            description = 'В этом упражнении работает передний пучок.',
            muscle_group = 'Мышцы плеча',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BC%D0%B0%D1%85%D0%B8-%D0%BF%D0%B5%D1%80%D0%B5%D0%B4-%D1%81%D0%BE%D0%B1%D0%BE%D0%B9-%D0%BD%D0%B0-%D0%BF%D0%BB%D0%B5%D1%87%D0%B8-1.gif',
            calories = 0.4,
            equipment = 'С резиновыми петлями'
        ),

        Exercise(
            name ='Тяга в наклоне',
            description = 'В этом упражнении работает задний пучок.',
            muscle_group = 'Мышцы плеча',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%82%D1%8F%D0%B3%D0%B0-%D0%BD%D0%B0-%D0%BF%D0%BB%D0%B5%D1%87%D0%B8-1.gif',
            calories = 0.4,
            equipment = 'С резиновыми петлями'
        ),

        Exercise(
            name ='Отведение в наклоне',
            description = 'В этом упражнении работает задний пучок.',
            muscle_group = 'Мышцы плеча',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BE%D1%82%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-%D0%BD%D0%B0-%D0%B7%D0%B0%D0%B4%D0%BD%D1%8E%D1%8E-%D0%B4%D0%B5%D0%BB%D1%8C%D1%82%D1%83-%D0%B2-%D0%BD%D0%B0%D0%BA%D0%BB%D0%BE%D0%BD%D0%B5.gif',
            calories = 0.4,
            equipment = 'С резиновыми петлями'
        ),

        Exercise(
            name ='Разведение в стороны стоя',
            description = 'В этом упражнении работает задний пучок.',
            muscle_group = 'Мышцы плеча',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%80%D0%B0%D0%B7%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-%D0%BD%D0%B0-%D0%BF%D0%BB%D0%B5%D1%87%D0%B8-%D1%81%D1%82%D0%BE%D1%8F-1.gif',
            calories = 0.4,
            equipment = 'С резиновыми петлями'
        ),

        Exercise(
            name ='Касание пяток сидя',
            description = 'В этом упражнении работают мышцы пресса.',
            muscle_group = 'Мышцы пресса',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BA%D0%B0%D1%81%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BF%D1%8F%D1%82%D0%BE%D0%BA-%D1%81%D0%B8%D0%B4%D1%8F-%D1%81-%D0%BF%D0%BE%D0%B4%D1%8A%D0%B5%D0%BC%D0%BE%D0%BC-%D0%BD%D0%BE%D0%B3.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Дотягивания до щиколоток',
            description = 'В этом упражнении работают мышцы пресса.',
            muscle_group = 'Мышцы пресса',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%B4%D0%BE%D1%82%D1%8F%D0%B3%D0%B8%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%B4%D0%BE-%D1%89%D0%B8%D0%BA%D0%BE%D0%BB%D0%BE%D1%82%D0%BE%D0%BA.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Упрощенный»велосипед»',
            description = 'В этом упражнении работают мышцы пресса.',
            muscle_group = 'Мышцы пресса',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%B2%D0%B5%D0%BB%D0%BE%D1%81%D0%B8%D0%BF%D0%B5%D0%B4-%D1%83%D0%BF%D1%80%D0%BE%D1%89%D0%B5%D0%BD%D0%BD%D1%8B%D0%B9.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Упрощенный велосипед',
            description = 'В этом упражнении работают мышцы пресса.',
            muscle_group = 'Мышцы пресса',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%B2%D0%B5%D0%BB%D0%BE%D1%81%D0%B8%D0%BF%D0%B5%D0%B4-%D1%83%D0%BF%D1%80%D0%BE%D1%89%D0%B5%D0%BD%D0%BD%D1%8B%D0%B9.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Скручивания стоя',
            description = 'В этом упражнении работают мышцы пресса.',
            muscle_group = 'Мышцы пресса',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%81%D0%BA%D1%80%D1%83%D1%87%D0%B8%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F-%D1%81%D1%82%D0%BE%D1%8F.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Русский твистер',
            description = 'В этом упражнении работают мышцы пресса.',
            muscle_group = 'Мышцы пресса',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9-%D1%82%D0%B2%D0%B8%D1%81%D1%82%D0%B5%D1%80.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Обратные скручивания с согнутыми ногами',
            description = 'В этом упражнении работают мышцы пресса.',
            muscle_group = 'Мышцы пресса',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BE%D0%B1%D1%80%D0%B0%D1%82%D0%BD%D1%8B%D0%B5-%D1%81%D0%BA%D1%80%D1%83%D1%87%D0%B8%D0%B2-%D1%81-%D1%81%D0%BE%D0%B3%D0%BD%D1%83%D1%82%D1%8B%D0%BC%D0%B8-%D0%BD%D0%BE%D0%B3%D0%B0%D0%BC%D0%B8.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Скручивания',
            description = 'В этом упражнении работают мышцы пресса.',
            muscle_group = 'Мышцы пресса',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%81%D0%BA%D1%80%D1%83%D1%87%D0%B8%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Косые скручивания',
            description = 'В этом упражнении работают мышцы пресса.',
            muscle_group = 'Мышцы пресса',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BA%D0%BE%D1%81%D1%8B%D0%B5-%D1%81%D0%BA%D1%80%D1%83%D1%87%D0%B8%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F..gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Косые скручивания с подносом колена',
            description = 'В этом упражнении работают мышцы пресса.',
            muscle_group = 'Мышцы пресса',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BA%D0%BE%D1%81%D1%8B%D0%B5-%D1%81%D0%BA%D1%80%D1%83%D1%87%D0%B8%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F-%D1%81-%D0%BF%D0%BE%D0%B4%D0%BD%D0%BE%D1%81%D0%BE%D0%BC-%D0%BA%D0%BE%D0%BB%D0%B5%D0%BD%D0%B0.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Косые скручивания с велосипедом',
            description = 'В этом упражнении работают мышцы пресса.',
            muscle_group = 'Мышцы пресса',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BA%D0%BE%D1%81%D1%8B%D0%B5-%D1%81%D0%BA%D1%80%D1%83%D1%87%D0%B8%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F-%D1%81-%D0%B2%D0%B5%D0%BB%D0%BE%D1%81%D0%B8%D0%BF%D0%B5%D0%B4%D0%BE%D0%BC.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Обратные скручивания',
            description = 'В этом упражнении работают мышцы пресса.',
            muscle_group = 'Мышцы пресса',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BE%D0%B1%D1%80%D0%B0%D1%82%D0%BD%D1%8B%D0%B5-%D1%81%D0%BA%D1%80%D1%83%D1%87%D0%B8%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F-%D1%81-%D0%BE%D1%82%D1%80%D1%8B%D0%B2%D0%BE%D0%BC-%D0%BF%D0%BE%D1%8F%D1%81%D0%BD%D0%B8%D1%86%D1%8B.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Скручивания с подъемом ног',
            description = 'В этом упражнении работают мышцы пресса.',
            muscle_group = 'Мышцы пресса',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%81%D0%BA%D1%80%D1%83%D1%87%D0%B8%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F-%D1%81-%D0%BF%D0%BE%D0%B4%D1%8A%D0%B5%D0%BC%D0%BE%D0%BC-%D0%BD%D0%BE%D0%B3.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Велосипед',
            description = 'В этом упражнении работают мышцы пресса.',
            muscle_group = 'Мышцы пресса',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%B2%D0%B5%D0%BB%D0%BE%D1%81%D0%B8%D0%BF%D0%B5%D0%B4.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Маятник',
            description = 'В этом упражнении работают мышцы пресса.',
            muscle_group = 'Мышцы пресса',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BC%D0%B0%D1%8F%D1%82%D0%BD%D0%B8%D0%BA-%D0%BD%D0%BE%D0%B3%D0%B0%D0%BC%D0%B8.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Вертикальные ножницы',
            description = 'В этом упражнении работают мышцы пресса.',
            muscle_group = 'Мышцы пресса',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%B2%D0%B5%D1%80%D1%82%D0%B8%D0%BA%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5-%D0%BD%D0%BE%D0%B6%D0%BD%D0%B8%D1%86%D1%8B.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Горизонтальные ножницы',
            description = 'В этом упражнении работают мышцы пресса.',
            muscle_group = 'Мышцы пресса',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BD%D0%BE%D0%B6%D0%BD%D0%B8%D1%86%D1%8B-%D0%B3%D0%BE%D1%80%D0%B8%D0%B7%D0%BE%D0%BD%D1%82%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Звезда',
            description = 'В этом упражнении работают мышцы пресса.',
            muscle_group = 'Мышцы пресса',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%B7%D0%B2%D0%B5%D0%B7%D0%B4%D0%B0-%D0%BB%D0%B5%D0%B6%D0%B0.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Косой поднос колена в упоре',
            description = 'В этом упражнении работают мышцы пресса.',
            muscle_group = 'Мышцы пресса',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BA%D0%BE%D1%81%D0%BE%D0%B9-%D0%BF%D0%BE%D0%B4%D0%BD%D0%BE%D1%81-%D0%BA%D0%BE%D0%BB%D0%B5%D0%BD%D0%B0-%D0%B2-%D1%83%D0%BF%D0%BE%D1%80%D0%B5.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Опускание ног',
            description = 'В этом упражнении работают мышцы пресса.',
            muscle_group = 'Мышцы пресса',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BE%D0%BF%D1%83%D1%81%D0%BA%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BE%D0%B1%D0%B5%D0%B8%D1%85-%D0%BD%D0%BE%D0%B3.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Косые скручивания с поднятой ногой',
            description = 'В этом упражнении работают мышцы пресса.',
            muscle_group = 'Мышцы пресса',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%81%D0%BA%D1%80%D1%83%D1%87%D0%B8%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F-%D0%BA%D0%BE%D1%81%D1%8B%D0%B5-%D1%81-%D0%BF%D0%BE%D0%B4%D0%BD%D1%8F%D1%82%D0%BE%D0%B9-%D0%BD%D0%BE%D0%B3%D0%BE%D0%B9.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Скручивания лежа на боку',
            description = 'В этом упражнении работают мышцы пресса.',
            muscle_group = 'Мышцы пресса',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%81%D0%BA%D1%80%D1%83%D1%87%D0%B8%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F-%D0%BB%D0%B5%D0%B6%D0%B0-%D0%BD%D0%B0-%D0%B1%D0%BE%D0%BA%D1%83.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Раскладушка',
            description = 'В этом упражнении работают мышцы пресса.',
            muscle_group = 'Мышцы пресса',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D1%80%D0%B0%D1%81%D0%BA%D0%BB%D0%B0%D0%B4%D1%83%D1%88%D0%BA%D0%B0.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Косые скручивания в упоре с касанием колена',
            description = 'В этом упражнении работают мышцы пресса.',
            muscle_group = 'Мышцы пресса',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BA%D0%BE%D1%81%D1%8B%D0%B5-%D1%81%D0%BA%D1%80%D1%83%D1%87-%D0%BA%D0%B0%D1%81%D0%B0%D0%BD%D0%B8%D0%B5%D0%BC-%D0%BA%D0%BE%D0%BB%D0%BD%D0%B0-%D0%BB%D0%BE%D0%BA%D1%82%D0%B5%D0%BC-%D0%B2-%D0%BF%D0%BB%D0%B0%D0%BD%D0%BA%D0%B5.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Косые скручивания в боковой планке',
            description = 'В этом упражнении работают мышцы пресса.',
            muscle_group = 'Мышцы пресса',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BA%D0%BE%D1%81%D1%8B%D0%B5-%D1%81%D0%BA%D1%80%D1%83%D1%87%D0%B8%D0%B2-%D0%B2-%D0%B1%D0%BE%D0%BA-%D0%BF%D0%BB%D0%B0%D0%BD%D0%BA%D0%B5-%D1%80%D1%83%D0%BA%D0%B0-%D0%B7%D0%B0-%D0%B3%D0%BE%D0%BB%D0%BE%D0%B2%D0%BE%D0%B9.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Подъем таза в боковой планке',
            description = 'В этом упражнении работают мышцы пресса.',
            muscle_group = 'Мышцы пресса',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BF%D0%BE%D0%B4%D1%8A%D0%B5%D0%BC-%D1%82%D0%B0%D0%B7%D0%B0-%D0%B2-%D0%B1%D0%BE%D0%BA%D0%BE%D0%B2%D0%BE%D0%B9-%D0%BF%D0%BB%D0%B0%D0%BD%D0%BA%D0%B5-1.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        ),

        Exercise(
            name ='Приведение локтя в боковой планке',
            description = 'В этом упражнении работают мышцы пресса.',
            muscle_group = 'Мышцы пресса',
            demonstration_video='https://makefitness.pro/wp-content/uploads/2020/02/%D0%BF%D1%80%D0%B8%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-%D0%BB%D0%BE%D0%BA%D1%82%D1%8F-%D0%BA-%D0%BA%D0%BE%D0%BB%D0%B5%D0%BD%D0%BA%D0%B5-%D0%B2-%D0%B1%D0%BE%D0%BA%D0%BE%D0%B2%D0%BE%D0%B9-%D0%BF%D0%BB%D0%B0%D0%BD%D0%BA%D0%B5.gif',
            calories = 0.4,
            equipment = 'Со своим весом'
        )

    ]

    for exercise in exercises:
        exercise.save()
    return render(request, 'main_page.html')
    
    # # Сохранение всех упражнений в базе данных
    # # calories = [0.4, 0.3, 0.4, 0.2, 0.5, 0.8, 0.5, 1.4, 0.2, 0.7, 0.3, 0.5, 0.4, 0.9, 0.3, 1.4, 1.0, 0.2, 0.5]
    # # for calory, exercise in zip(calories, Exercise.objects.all()):
    # #     #exercise = Exercise.objects.get(id=id_exercise)
    # #     exercise.calories = calory
    # #     exercise.save()
   
    # for workout_exercise in WorkoutExercise.objects.all():
    #     workout_exercise.calories = workout_exercise.reps*workout_exercise.sets*workout_exercise.exercise.calories
    #     workout_exercise.save()
    # return render(request, 'main_page.html')
