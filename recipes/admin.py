from django.contrib import admin
from .models import Recipe


class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "country",
        "created_at",
    )

    search_fields = (
        "name",
        "country",
    )

    list_filter = (
        "country",
    )


admin.site.register(Recipe, RecipeAdmin)