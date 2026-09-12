from django.shortcuts import render

recipes = [
    {
        "id": 1,
        "name": "Піца Маргарита",
        "country": "Італія",
        "description": "Класична італійська піца з томатним соусом, моцарелою та базиліком.",
        "image": "https://images.unsplash.com/photo-1574071318508-1cdbab80d002"
    },
    {
        "id": 2,
        "name": "Суші",
        "country": "Японія",
        "description": "Традиційна японська страва з рису, риби та морепродуктів.",
        "image": "https://images.unsplash.com/photo-1579871494447-9811cf80d66c"
    },
    {
        "id": 3,
        "name": "Борщ",
        "country": "Україна",
        "description": "Традиційна українська страва з буряком, капустою та овочами.",
        "image": "https://images.unsplash.com/photo-1547592180-85f173990554"
    },
    {
        "id": 4,
        "name": "Такос",
        "country": "Мексика",
        "description": "Мексиканська страва з тортильї, м'яса, овочів та соусу.",
        "image": "https://images.unsplash.com/photo-1551504734-5ee1c4a1479b"
    }
]

def recipe_list(request):
    return render(request, "recipes/recipe_list.html", {"recipes": recipes})


def recipe_detail(request, recipe_id):
    recipe = next((r for r in recipes if r["id"] == recipe_id), None)

    return render(
        request,
        "recipes/recipe_detail.html",
        {"recipe": recipe}
    )