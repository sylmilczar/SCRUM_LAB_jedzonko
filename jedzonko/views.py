import random
from datetime import datetime

from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.views import View
from django.urls import reverse

from jedzonko.models import Recipe, Plan, RecipePlan, Page
from jedzonko.enums import WeekDays


class IndexView(View):
    def get(self, request):
        ctx = {"actual_date": datetime.now()}
        return render(request, "test.html", ctx)


class LandingPageView(View):
    def get(self, request):
        recipes = list(Recipe.objects.all())
        listed_recipes = random.sample(recipes, 3)
        return render(request, 'index.html', context={"recipes": listed_recipes})


class RecipeID(View):
    def get(self, request, id):
        recipe = get_object_or_404(Recipe, pk=id)
        ctx = {"recipe": recipe}
        return render(request, 'app-recipe-details.html', context=ctx)

    def post(self, request, id):
        recipe = get_object_or_404(Recipe, pk=id)
        if 'like_recipe' in request.POST.keys() and request.POST['like_recipe']:
            recipe.votes += 1
        if 'dislike_recipe' in request.POST.keys() and request.POST['dislike_recipe']:
            recipe.votes -= 1
        recipe.save()
        return redirect('recipe_id_view', id)


class RecipeList(View):
    def get(self, request):
        recipe = Recipe.objects.all().order_by("-votes")
        recipe_paginator = Paginator(recipe, 50)
        page = request.GET.get('page')
        recip = recipe_paginator.get_page(page)
        count = Recipe.objects.all().count()

        return render(request, 'app-recipes.html', {'recip': recip, 'count': count})


class RecipeAdd(View):
    def get(self, request):
        return render(request, 'app-add-recipe.html')

    def post(self, request):

        if request.POST['recipe_name'] != '' and request.POST['recipe_description'] != '' and request.POST[
            'preparation_time'] != '' and request.POST['preparation_description'] != '' and request.POST[
            'ingredients'] != '':

            recipe_name = request.POST['recipe_name']
            description = request.POST['recipe_description']
            prep_time = request.POST['preparation_time']
            preparation_description = request.POST['preparation_description']
            ingredients = request.POST['ingredients']

            Recipe.objects.create(name=recipe_name, ingredients=ingredients, description=description,
                                  preparation_time_mins=prep_time, preparation_description=preparation_description)
            context = {
                'message_ok': 'Przepis dodany poprawnie.',
            }
        else:
            context = {
                'message_nok': 'Wypełnij poprawnie wszystkie pola!',
            }
        return render(request, 'app-add-recipe.html', context=context)


class RecipeModify(View):
    def get(self, request, id):
        recipe = get_object_or_404(Recipe, pk=id)
        ctx = {"recipe": recipe}
        return render(request, 'app-edit-recipe.html', context=ctx)

    def post(self, request, id):
        recipe_modify_name = request.POST['recipe_modify_name']
        recipe_modify_description = request.POST['recipe_modify_description']
        recipe_modify_preparation_time = request.POST['recipe_modify_preparation_time']
        recipe_modify_preparation_description = request.POST['recipe_modify_preparation_description']
        recipe_modify_ingredients = request.POST['recipe_modify_ingredients']

        if recipe_modify_name and recipe_modify_description and recipe_modify_preparation_time and \
                recipe_modify_preparation_description and recipe_modify_ingredients:
            Recipe.objects.create(name=recipe_modify_name, ingredients=recipe_modify_ingredients,
                                  description=recipe_modify_description,
                                  preparation_time_mins=recipe_modify_preparation_time,
                                  preparation_description=recipe_modify_preparation_description)
            return redirect(reverse("recipe_list_view"))
        recipe = get_object_or_404(Recipe, pk=id)
        ctx = {"recipe": recipe,
               'message': 'Wypełnij poprawnie wszystkie pola!'}
        return render(request, 'app-edit-recipe.html', ctx)


class PlanID(View):
    def get(self, request, id):
        plane = get_object_or_404(Plan, pk=id)
        number_web = id
        recipeplan = RecipePlan.objects.filter(plan=id).order_by("order")
        recipe = Recipe.objects.all()
        weekday_name = WeekDays.CHOICES
        recipe_plans = plane.plans.all().order_by('day_name', 'order')
        context = {"plane": plane,
                   'day_options': WeekDays.CHOICES,
                   "recipeplan": recipeplan,
                   "recipe": recipe,
                   'weekday_name': weekday_name,
                   'recipe_plans': recipe_plans,
                   'number_web': number_web,
                   }

        return render(request, 'app-details-schedules.html', context=context)


class PlanAdd(View):
    def get(self, request):
        return render(request, 'app-add-schedules.html')

    def post(self, request):
        if request.POST['name'] != '' and request.POST['description'] != '':
            plan_name = request.POST.get('name')
            plan_description = request.POST.get('description')
            new_plan = Plan.objects.create(name=plan_name, description=plan_description)
            new_plan_id = new_plan.id
            return redirect("plan_id_view", new_plan_id)
        else:
            return render(request, 'app-add-schedules.html',
                          context={'message_not_ok': 'Wypełnij poprawnie wysztkie pola'})


class PlanList(View):
    def get(self, request):
        plan = Plan.objects.all().order_by('name')
        plan_paginator = Paginator(plan, 50)
        page = request.GET.get('page')
        plan_p = plan_paginator.get_page(page)
        count = Plan.objects.all().count()

        context = {
            'plan_p': plan_p,
            'count': count
        }
        return render(request, 'app-schedules.html', context=context)


class AddRecipeToPlan(View):
    def get(self, request):
        plans = Plan.objects.all()
        recipes = Recipe.objects.all()

        context = {
            'plans': plans,
            'recipes': recipes,
            'day_options': WeekDays.CHOICES
        }

        return render(request, 'app-schedules-meal-recipe.html', context=context)

    def post(self, request):
        meal_name = request.POST['meal_name']
        order = request.POST['order']
        day_name = request.POST['day_name']
        plan_id = request.POST.get('plan')
        recipe_id = request.POST.get('recipe')

        RecipePlan.objects.create(
            meal_name=meal_name,
            order=order,
            day_name=day_name,
            plan_id=plan_id,
            recipe_id=recipe_id
        )

        return redirect('plan_id_view', plan_id)


class DashboardView(View):
    def get(self, request):
        plan = Plan.objects.count()
        recipe = Recipe.objects.count()

        weekday_name = WeekDays.CHOICES
        latest_plan = Plan.objects.latest('id')
        recipe_plans = latest_plan.plans.all().order_by('day_name', 'order')
        plan_view = Plan.objects.all().order_by('-created')

        context = {'plan': plan,
                   'recipe': recipe,
                   'weekday_name': weekday_name,
                   'latest_plan': latest_plan,
                   'plan_view': plan_view,
                   'recipe_plans': recipe_plans,
                   }

        return render(request, 'dashboard.html', context=context)


class RecipeRemove(View):
    def get(self, request, recipe_id):
        recipe = Recipe.objects.get(pk=recipe_id)
        recipe.delete()
        return redirect("recipe_list_view")

#
# class SlugContact(View):
#     def get(self, request):
#         contact = Page.objects.filter(title='contact')
#         if contact:
#             return render(request, 'app-contact.html')
#         return redirect('/#contact')


class SlugView(View):
    def get(self, request, slug):
        try:
            slug_page = Page.objects.get(slug=slug)
            context = {
                'page': slug_page,
            }
            return render(request, f'app-{slug}.html', context=context)
        except Page.DoesNotExist:
            return redirect(f'/#{slug}')


class EditPlan(View):
    def get(self, request, plan_id):
        plan = get_object_or_404(Plan, pk=plan_id)
        context = {"plan": plan}
        return render(request, 'app-edit-schedules.html', context=context)

    def post(self, request, plan_id):
        plan = get_object_or_404(Plan, pk=plan_id)
        plan.name = request.POST['plan_name']
        plan.description = request.POST['plan_description']
        plan.save()
        return redirect('plan_id_view', plan_id)
    
    
class Search(View):
    def post(self, request):
        message_search = request.POST['search_for']
        message_search = message_search
        recipe = Recipe.objects.filter(name__icontains=message_search) | Recipe.objects.filter(
            description__icontains=message_search) | Recipe.objects.filter(ingredients__icontains=message_search)




        recipe_paginator = Paginator(recipe, 50)
        page = request.GET.get('page')
        recip = recipe_paginator.get_page(page)
        count = recipe.count()
        return render(request, 'app-recipes.html', {'recip': recip, 'count': count, 'message_search': message_search})


class PlanRemove(View):
    def get(self, request, plan_id):
        plan = Plan.objects.get(pk=plan_id)
        plan.delete()
        return redirect("plan_list_view")


class DeleteRecipeFromPlan(View):
    def get(self, request, id_recipe, id_plan):
        RecipePlan.objects.filter(pk=id_recipe).delete()
        return redirect("plan_id_view", id_plan)


