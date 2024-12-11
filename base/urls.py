from django.urls import path
from . import views, fill_db, create_own_workout, view_and_edit_workouts, view_exercises, ai_workout_generation
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.MainPageView.as_view(), name = 'main_page'),
    path('registration/', views.RegistrationView.as_view(), name = 'registration'),
    path('login/', views.LoginView.as_view(), name = 'login'),
    path('logout/', views.user_logout, name = 'logout'),
    path('password-change/', views.CustomPasswordChangeView.as_view(), name='password_change'),
    path('create-exercises/', fill_db.create_exercise, name='create_exercises'),
    # path('delete-account/', views.DeleteAccountView.as_view(), name='delete_account')
    path('userinfo/', views.AddBodyParams.as_view(), name='userinfo'),
    path('view_exercises/', view_exercises.view_exercises, name='view_exercises'),
    path('create_workout/', create_own_workout.create_workout, name='create_workout'),
    # path('add_exercises_to_workout/', create_own_workout.AddExercisesToWorkout.as_view(), name='add_exercises_to_workout'),
    path('add_exercise_to_workout/', create_own_workout.add_exercise_to_workout, name='add_exercise_to_workout'),
    path('workouts/', view_and_edit_workouts.workout_list, name='workout_list'),
    path('workout/edit/<int:workout_id>/', view_and_edit_workouts.edit_workout, name='edit_workout'),
    path('workout/update/<int:workout_id>/', view_and_edit_workouts.update_workout, name='update_workout'),
    path('workout/<int:workout_id>/delete-exercise/<int:exercise_id>/', view_and_edit_workouts.delete_workout_exercise, name='delete_workout_exercise'),
    path('workout/<int:workout_id>/', view_and_edit_workouts.workout_detail, name='workout_detail'),

    path('generate_workout/', ai_workout_generation.generate_workout, name='generate_workout'),
    path('profile/', views.Profile.as_view(), name='profile')
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)