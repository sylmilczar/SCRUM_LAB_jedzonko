"""scrumlab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from jedzonko.views import IndexView, LandingPageView, RecipeID, RecipeList, RecipeAdd, RecipeModify, PlanID, \
    PlanAdd, AddRecipeToPlan, DashboardView, PlanList, RecipeRemove, SlugView, EditPlan, PlanRemove, DeleteRecipeFromPlan, Search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', IndexView.as_view()),
    path('', LandingPageView.as_view(), name='landing_page'),
    path('main/', DashboardView.as_view(), name='dashboard'),
    path('recipe/<int:id>/', RecipeID.as_view(), name="recipe_id_view"),
    path('recipe/list/', RecipeList.as_view(), name="recipe_list_view"),
    path('recipe/add/', RecipeAdd.as_view(), name="recipe_add_view"),
    path('recipe/remove/<int:recipe_id>', RecipeRemove.as_view(), name="recipe_remove"),
    path('recipe/modify/<int:id>/', RecipeModify.as_view(), name="recipe_modify_view"),
    path('plan/<int:id>/', PlanID.as_view(), name="plan_id_view"),
    path('plan/add/', PlanAdd.as_view(), name="plan_add_view"),
    path('plan/add-recipe/', AddRecipeToPlan.as_view(), name="add_recipe_to_plan"),
    path('plan/list/', PlanList.as_view(), name="plan_list_view"),
    path('plan/remove/<int:plan_id>', PlanRemove.as_view(), name="plan_remove"),
    # path('contact/', SlugContact.as_view(), name="slug_contact"),
    # path('about/', SlugAbout.as_view(), name="slug_about"),
    path('plan/modify/<int:plan_id>', EditPlan.as_view(), name="plan_modify"),
    path('plan/delete_recipe/<int:id_recipe>/<int:id_plan>/', DeleteRecipeFromPlan.as_view(), name="delete_recipe_from_plan_view"),
    path('search/', Search.as_view(), name="search"),
    path('<slug:slug>/', SlugView.as_view(), name="slug_view"),
]
