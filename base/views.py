from django.views.generic import TemplateView, View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import CustomPasswordChangeForm
from .models import UserProfile
import requests

class MainPageView(LoginRequiredMixin, TemplateView):
    template_name = 'main_page.html'

    def post(self, request):
        if request.method == 'POST':
            # Дополнительная логика удаления аккаунта
            # Например, удаление пользователя из базы данных
            request.user.delete()
            logout(request)  # Выход пользователя после удаления аккаунта
            return redirect('login')  # Перенаправление на главную страницу после удаления
        return render(request, self.template_name)


class RegistrationView(View):
    template_name = 'registration_page.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')
       
        if password == confirm_password:
            try:
                
                validate_password(password)
                
                user = User.objects.create_user(username, email, password)
                login(request, user)
                user.save()
                messages.success(request, 'You have successfully registered!')
                return redirect('addbodyparams_page')
            
            except ValidationError as e:
                error_message = ' '.join(e.messages)
                return render(request, self.template_name, {'error_message': error_message})
            
            except Exception as e:
                error_message = 'Error creating account.'
                return render(request, self.template_name, {'error_message': error_message})
        else:
            error_message = 'Passwords do not match.'
            return render(request, self.template_name, {'error_message': error_message})
        
class LoginView(View):

    template_name = 'login_page.html'

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main_page')
            else:
                error_message = 'Incorrect email or password. Please try again.'
                return render(request, self.template_name, {'error_message': error_message})
        else:
            
            return render(request, self.template_name)
  


def user_logout(request):
    logout(request)
    return redirect('main_page')

class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'password_change.html'
    success_url = reverse_lazy('login')

class AddBodyParams(View):
    template_name = 'addbodyparams_page.html'

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        if request.method == 'POST':
            #user = authenticate(request, username=username, password=password)
            if request.user:
                height = request.POST.get('height')
                weight = request.POST.get('weight')
                birth_date = request.POST.get('birth_date')
                fitness_goal = request.POST.get('fitness_goal')

                user = UserProfile.objects.create(user=request.user, height=height, weight=weight, birth_date=birth_date, fitness_goal=fitness_goal)
                user.save()
                #login(request, user)
                return redirect('main_page')
            else:
                error_message = 'Incorrect email or password. Please try again.'
                return render(request, self.template_name, {'error_message': error_message})
        else:
            
            return render(request, self.template_name)
  
    