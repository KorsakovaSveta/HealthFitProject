from django.shortcuts import render, get_object_or_404, redirect
from .models import Products, UserFood, MealGroups, Water, Recipes, CookingSteps, Ingredients, TargetNutrition
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import JsonResponse
import re
@login_required
def choose_mealgroup(request):
    meal_groups = MealGroups.objects.all()
    total_kcal = UserFood.objects.filter(user=request.user).aggregate(total_kcal=Sum('kcal'))['total_kcal']
    total_protein = UserFood.objects.filter(user=request.user).aggregate(total_protein=Sum('protein'))['total_protein']
    total_fat = UserFood.objects.filter(user=request.user).aggregate(total_fat=Sum('fat'))['total_fat']
    total_carb = UserFood.objects.filter(user=request.user).aggregate(total_carb=Sum('carb'))['total_carb']
    total_water = Water.objects.filter(user=request.user).aggregate(total_water=Sum('water'))['total_water']
    targer_nutritions = TargetNutrition.objects.filter(user=request.user).order_by('id').last()

    print(total_kcal)
    return render(request, 'dairy.html', {'meal_groups': meal_groups, 'kcal': total_kcal, 'protein': total_protein, 'fat': total_fat, 'carb': total_carb, 'water': total_water / 1000, 'targer_nutritions': targer_nutritions})

@login_required
def search_and_add_product(request, mealgroup_id):
    user = request.user
    meal_group = get_object_or_404(MealGroups, id=mealgroup_id)  # Получаем выбранную группу
    query = request.GET.get('q', '')   # Для выбора группы приема пищи
    results = []

    if query:
        results = Products.objects.filter(products_name__icontains=query)  # Поиск по совпадению

    if request.method == 'POST':  # Обработка добавления продукта
        product_id = request.POST.get('product_id')
        gramming = int(request.POST.get('gramming', 0))
        
        if product_id and gramming:
            product = get_object_or_404(Products, id=product_id)
        
            # Расчет питательных веществ
            kcal = (product.kcal_per_100g * gramming) / 100
            protein = (product.protein_per_100g * gramming) / 100
            fat = (product.fat_per_100g * gramming) / 100
            carb = (product.carb_per_100g * gramming) / 100

            # Создание записи в UserFood
            UserFood.objects.create(
                user=user,
                product=product,
                meal_group=meal_group,
                gramming_product=gramming,
                kcal=kcal,
                protein=protein,
                fat=fat,
                carb=carb,
            )
            return redirect('search_products', mealgroup_id=meal_group.id)  # Перенаправление на ту же страницу после добавления

    context = {
        'query': query,
        'results': results,
        'meal_groups': meal_group,
    }
    return render(request, 'search_products.html', context)

# def kcal_protein_fat_carb(request):
    
#     total_kcal = UserFood.objects.filter(user=request.user).aggregate(total_kcal=Sum('kcal'))['total_kcal']
    
#     return render(request, 'dairy.html', {'kcal': total_kcal})
@login_required
def add_water(request):
    if request.method == "POST":
        water = request.POST.get('water')
        Water.objects.create(user=request.user, water=water)
        return JsonResponse({'status': 'success'}) 


@login_required
def view_recipes(request):
   
    recipes = Recipes.objects.order_by('recipe_name').distinct('recipe_name')
    print(recipes)
    return render(request, 'Рецепты.html', {'recipes': recipes[:15]})

@login_required
def view_recipes_breakfast(request):
   
    recipes = Recipes.objects.filter(group=1)
    print(recipes)
    return render(request, 'Рецепты.html', {'recipes': recipes[:15]})

@login_required
def view_recipes_lunch(request):
   
    recipes = Recipes.objects.filter(group=2)
    print(recipes)
    return render(request, 'Рецепты.html', {'recipes': recipes[:15]})

@login_required
def view_recipes_snack(request):
   
    recipes = Recipes.objects.filter(group=4)
    print(recipes)
    return render(request, 'Рецепты.html', {'recipes': recipes[:15]})

@login_required
def view_recipes_dinner(request):
   
    recipes = Recipes.objects.filter(group=3)
    print(recipes)
    return render(request, 'Рецепты.html', {'recipes': recipes[:15]})

@login_required
def view_recipe_steps(request, recipe_id):
    recipe = get_object_or_404(Recipes, id=recipe_id)
    steps = CookingSteps.objects.filter(recipe=recipe).order_by('id')
    ingredients = Ingredients.objects.filter(recipe=recipe).order_by('id')
    steps_description = []
    steps_description_dict = {}
    for step in steps:
        steps_description.append(step.step)
    
    
    pattern = re.compile(r'Шаг (\d+) (.+?)\.')
    for step_desc in steps_description:
        matches = pattern.findall(step_desc)
        for match in matches:
            steps_description_dict[match[0]] = match[1]
    print(steps_description_dict)
   
    context = {
        'recipe': recipe,
        'steps': steps_description_dict,
        'ingredients': ingredients
    }
    return render(request, 'Разбор рецепта.html', context)

@login_required
def target_nutritions(request):
    if request.method == 'POST':
        target_kcal = request.POST.get('target_kcal')
        target_protein = request.POST.get('target_protein')
        target_fat = request.POST.get('target_fat')
        target_carb = request.POST.get('target_carb')
        target_water = request.POST.get('target_water')
        TargetNutrition.objects.create(user=request.user, target_kcal=target_kcal, target_protein=target_protein, target_fat=target_fat, target_carb=target_carb, target_water=target_water)
        return JsonResponse({'status': 'success'}) 

