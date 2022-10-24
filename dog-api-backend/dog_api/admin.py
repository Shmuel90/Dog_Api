from django.contrib.auth.models import Group, User
from django.contrib import admin
from dog_api.models import *

# Register your models here.
admin.site.unregister(Group)
# No users needed either
admin.site.unregister(User)

# Admin Models
class DogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'breed', 'gender', 'color', 'favoriteFood', 'favoriteToy')
    list_display_links = ('id', 'name')

class BreedAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'size', 'friendliness', 'trainability', 'sheddingAmount', 'exerciseNeeds')
    list_display_links = ('id', 'name')

# Normal Models
admin.site.register(Dog, DogAdmin)
admin.site.register(Breed, BreedAdmin)