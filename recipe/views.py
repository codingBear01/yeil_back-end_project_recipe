import json
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render

from .models import User, Ingredients, Food

# Create your views here.


def index(request):
    ingredients = Ingredients.objects.all().order_by("name")

    return render(
        request,
        "recipe/index.html",
        {
            "ingredients": ingredients,
        },
    )


def recipe(request):
    ingredients = Ingredients.objects.all().order_by("name")

    if request.method == "POST":
        checkedIngredients = request.POST.getlist("checkedIngredients")

        foodSet = []
        for check in checkedIngredients:
            selectedIngredients = Ingredients.objects.filter(name=check)
            filteredFood = Food.objects.all().filter(
                ingredients__in=selectedIngredients
            )

            for i in range(0, len(filteredFood)):
                if filteredFood[i] not in foodSet:
                    foodSet.append(filteredFood[i])

        return render(
            request,
            "recipe/index.html",
            {
                "ingredients": ingredients,
                "checkedIngredients": checkedIngredients,
                "foodSet": foodSet,
            },
        )

    return render(
        request,
        "recipe/index.html",
        {
            "ingredients": ingredients,
        },
    )
