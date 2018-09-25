from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
import json
# Create your views here.
from core.models import Building, Floor, Room


def index(request):
    buildings = Building.objects.all()
    return render(request, 'web/index.html', context= {'buildings': buildings})

def buildling_api_indoor(request, building_id):
    building = Building.objects.get(id=building_id)
    rooms = {
        "type": "FeatureCollection",
        "features": []
    }
    for floor in building.floor_set.all():
        for room in floor.room_set.all():
            room_feature = json.loads(room.feature_collection)
            room_feature['properties'] = {
                "type": "way",
                "id": room.id,
                "tags": {
                    "buildingpart": "room",
                    "height": "1",
                    "indoor": "yes",
                    "name": room.name
                },
                "relations": [
                    {
                        "role": "buildingpart",
                        "rel": room.floor.id,
                        "reltags": {
                            "height": "1",
                            "level": room.floor.level,
                            "level:usage": "",
                            "name": room.floor.name,
                            "type": "level"
                        }
                    }
                ],
                "meta": {}
            }
            rooms['features'].append(room_feature)

    return JsonResponse(rooms)




def rooms_index(request):

    pass


def rooms_edit(request, building_id):
    building = Building.objects.get(id=building_id)
    return render(request, 'web/rooms_edit.html', context= {'building': building})

def rooms_update(request):
    pass


def rooms_create(request):
    name = request.POST.get('roomName')
    floor_id = request.POST.get('floorId')
    room = Room()
    room.name = name
    room.floor_id = floor_id
    room.latitude = request.POST.get('roomLatitude')
    room.longitude = request.POST.get('roomLongitude')
    room.feature_collection = request.POST.get('roomFeatureCollection')
    room.save()
    return  redirect('/')

def rooms_store(request):
    pass

def rooms_delete(request):
    pass