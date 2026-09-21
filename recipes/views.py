from django.shortcuts import render, get_object_or_404
from django.db.models import Count

from recipes.models import Recipe


def recipe_list(request):
    recipes = Recipe.objects.all()

    return render(
        request,
        "recipes/recipe_list.html",
        {"recipes": recipes}
    )


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(
        Recipe,
        id=recipe_id
    )

    return render(
        request,
        "recipes/recipe_detail.html",
        {"recipe": recipe}
    )


def country_list(request):
    countries = (
        Recipe.objects
        .values("country")
        .annotate(recipe_count=Count("id"))
        .order_by("country")
    )

    return render(
        request,
        "recipes/country_list.html",
        {"countries": countries}
    )