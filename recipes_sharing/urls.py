from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('all/', views.all_recipes, name='all_recipes'),  # All recipes
    path('login/', views.login, name='login'),  # User login
    path('logout/', views.logout, name='logout'),  # User logout
    path('register/', views.register, name='register'),  # User registration

    path('profile/<str:username>/', views.view_profile, name='view_profile'),  # View user profile
    path('profile/<str:username>/edit/', views.edit_profile, name='edit_profile'),  # Edit user profile
    path('profile/<str:username>/delete/', views.delete_profile, name='delete_profile'),  # Delete user profile
    
    path('search/', views.search, name='search'),  # Search recipes


    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),  # Recipe details
    path('create/', views.create_recipe, name='create_recipe'),  # Create new recipe
    path('recipe/<int:recipe_id>/comment/', views.add_comment, name='add_comment'),  # Add comment to recipe
    path('recipe/<int:recipe_id>/delete/', views.delete_recipe, name='delete_recipe'),  # Delete a recipe
    path('recipe/<int:recipe_id>/edit/', views.edit_recipe, name='edit_recipe'),  # Edit a recipe
   
    path('recipe/<int:recipe_id>/add_to_favorites/', views.like_recipe, name='like_recipe'),  # Add recipe to favorites
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)