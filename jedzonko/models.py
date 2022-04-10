from django.db import models
from django.utils.text import slugify

from jedzonko.enums import WeekDays


class Recipe(models.Model):
    name = models.CharField(max_length=125)
    ingredients = models.TextField()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    preparation_time_mins = models.IntegerField(default=33)
    votes = models.IntegerField(default=0)
    preparation_description = models.TextField(default="")


class Plan(models.Model):
    name = models.CharField(max_length=125)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    recipes = models.ManyToManyField('Recipe', through='recipeplan')


class RecipePlan(models.Model):
    meal_name = models.CharField(max_length=64)
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, related_name='recipes')
    plan = models.ForeignKey('Plan', on_delete=models.CASCADE, related_name='plans')
    order = models.IntegerField()
    day_name = models.CharField(max_length=64, choices=WeekDays.CHOICES)


class Page(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Page, self).save(*args, **kwargs)
