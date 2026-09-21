from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=150)
    country = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()

    image_url = models.URLField(
        max_length=500,
        null=True,
        blank=True
    )

    image_position = models.CharField(
        max_length=50,
        default="center center"
    )

    youtube_url = models.URLField(
        max_length=500,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.name} - {self.country}"