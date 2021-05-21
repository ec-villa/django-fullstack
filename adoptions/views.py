from django.shortcuts import render
# Decide the logic and control flow for handling requests and
# definition of HTTP responses that are returned.
# Create your views here.
# from django.http import HttpResponse
from django.http import Http404

from .models import Pet, ExampleData

def home(request): 
    #return HttpResponse('<p>home view</p>')
    pets = Pet.objects.all()
    exampleDatas = ExampleData.objects.all()
    return render(request, 'home.html', {
        'pets': pets,
        'exampleDatas': exampleDatas,
    })

def pet_detail(request, pet_id):
    # return HttpResponse(f'<p>pet_detail view with id {pet_id}<p>')
    try:
        pet = Pet.objects.get(id=pet_id)
    except Pet.DoesNotExist:
        raise Http404('pet not found!')
    return render(request, 'pet_detail.html', {
            'pet': pet,
    })