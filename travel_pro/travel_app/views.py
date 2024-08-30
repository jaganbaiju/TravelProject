from django.http import HttpResponse
from django.shortcuts import render
from .models import PlaceModel
from .models import TeamModel

# Create your views here.


def index(request):
    place = PlaceModel.objects.all()
    team = TeamModel.objects.all()
    return render(request, 'index.html', {'place': place, 'team': team})
