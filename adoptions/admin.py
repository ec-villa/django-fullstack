from django.contrib import admin
# Decisions of the adminstartive interface 
# for the APP that will allow us to see and edit data 
# Register your models here.

#import pet data 
from .models import Pet, ExampleData

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'species', 'breed', 'age', 'sex']

@admin.register(ExampleData)
class ExampleDataAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'office', 'age', 'salary']