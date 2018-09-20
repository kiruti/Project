from django.core import serializers
from django.shortcuts import render

# Create your views here.
from core.models import Building


def index(request):
    buildings = Building.objects.all()
    return render(request, 'web/index.html', context= {'buildings': buildings})