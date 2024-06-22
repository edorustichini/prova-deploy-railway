from django.db import models
from django.contrib.auth.models import User



class Recipe(models.Model):
    recipe_name = models.CharField(max_length=70)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    description = models.CharField(max_length=300)
    ingredients = models.TextField()

    preparation_instructions = models.TextField()
    cooking_time = models.PositiveIntegerField(null=True, blank=True)  # in minuti
    
    creation_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='recipe_images', blank=True, null=True) 
    
    DIFFICULTIES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]
    difficulty = models.CharField(max_length=10, choices=DIFFICULTIES, null=True, blank=True)
    
    liked_by = models.ManyToManyField(User, related_name='liked_recipes', blank=True, null=True) # userò liked_recipes per accedere ai like di un utente
    
    CATEGORIES = [
        ('A', 'Antipasto'),
        ('P', 'Primo Piatto'),
        ('S', 'Secondo Piatto'),
        ('C', 'Contorno'),
        ('D', 'Dessert'),
    ]
    categories = models.CharField(max_length=1, null=True, blank=True, choices=CATEGORIES)
    
    calories = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.recipe_name
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=150,null=True, blank=True) 
    profile_image = models.ImageField(upload_to='media/profile_images', blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True) # data di creazione del profilo
    
    def __str__(self):
        return self.user.username
    

class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments') # un commento è relativo ad una sola ricetta
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_content = models.CharField(max_length=300)
    creation_date = models.DateTimeField(auto_now_add=True) # data aggiunta del commento

    
    
    def __str__(self):
        return f'Comment by {self.author.username} on {self.recipe.recipe_name}'
