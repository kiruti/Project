from django.db import models


class BuildingType(models.Model):
    name = models.CharField(null=True, blank=True, max_length=255)
    icon = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Building(models.Model):
    name = models.CharField(null=True, blank=True, max_length=255)
    building_type = models.ForeignKey(BuildingType, null=True, blank=True, on_delete=models.DO_NOTHING)
    floor_count = models.IntegerField(blank=True, null=True)
    image = models.ImageField(null=True, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    feature_collection = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def default(value, arg):
        """If value is unavailable, use given default."""
        return value or arg


class Floor(models.Model):
    name = models.CharField(null=True, blank=True, max_length=255)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    level = models.IntegerField()
    image = models.ImageField(null=True, blank=True)
    feature_collection = models.TextField(null=True, blank=True)
    room_count = models.IntegerField(blank=True, null=True)

    class Meta:
        unique_together = ('building', 'level',)

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(null=True, blank=True, max_length=255)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    feature_collection = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

