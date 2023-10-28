from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import CheckConstraint, Q
from django.template.defaultfilters import slugify

from .const import Rooms, Development, Floor, Heat, Equipment, Province, County, City, Status


class Equip(models.Model):
    name = models.CharField(choices=Equipment.choices(), max_length=30)

    def __str__(self):
        return f'{self.name}'


class Flat(models.Model):
    title = models.CharField(max_length=120)
    price = models.PositiveIntegerField()
    area = models.FloatField(validators=[MinValueValidator(0.0)])
    rooms = models.CharField(max_length=10, choices=Rooms.choices())
    created_at = models.DateTimeField(auto_now_add=True)
    development_type = models.CharField(max_length=10, choices=Development.choices())
    floor = models.CharField(max_length=10, choices=Floor.choices())
    heating = models.CharField(max_length=10, choices=Heat.choices())
    year = models.PositiveIntegerField()
    text = models.TextField()
    equipment = models.ManyToManyField(Equip, related_name='flat')
    user = models.ForeignKey(User, related_name='flat', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=Status.choices(), default=Status.Active)

    class Meta:
        ordering = ['-created_at']
        constraints = (
            # for checking in the DB
            CheckConstraint(
                check=Q(area__gte=0.0),
                name='flat_area_range'),
        )

    def __str__(self):
        return f'{self.title} | {self.created_at}'


def get_image_filename(instance, filename):
    title = instance.flat.title
    slug = slugify(title)
    return "images/%s-%s" % (slug, filename)


class FlatImage(models.Model):
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=get_image_filename, blank=True, verbose_name='Image')


class LocationCity(models.Model):
    province = models.CharField(choices=Province.choices(), max_length=20)
    county = models.CharField(choices=County.choices(), max_length=20)
    city = models.CharField(choices=City.choices(), max_length=20)

    def __str__(self):
        return f'{self.city}, {self.province}'


class FlatLocation(models.Model):
    city = models.ForeignKey(LocationCity, related_name='location', on_delete=models.CASCADE)
    district = models.CharField(max_length=100, blank=True)
    street = models.CharField(max_length=100, blank=True)
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, related_name='location')

    def __str__(self):
        return f'{self.city}'