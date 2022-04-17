from django.contrib import admin
from .models import User, Ingredients, Food

# Register your models here.
admin.site.register(User)
admin.site.register(Ingredients)
admin.site.register(Food)
