from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import CheckConstraint, Q
from django.template.defaultfilters import slugify

from rent_flat.flat.const import Rooms, Development, Floor, Heat, Equipment, Province, County, City


class FlatLocation(models.Model):
    province = models.CharField(choices=Province.choices(), max_length=10)
    county = models.CharField(choices=County.choices(), max_length=10)
    city = models.CharField(choices=City.choices(), max_length=10)
    district = models.CharField(max_length=120)
    street = models.CharField(max_length=120, blank=True)

    def __str__(self):
        return f'{self.city}, {self.province}'


class Flat(models.Model):
    title = models.CharField(max_length=120)
    price = models.PositiveIntegerField()
    area = models.FloatField(validators=[MinValueValidator(0.0)])
    rooms = models.IntegerField(max_length=10, choices=Rooms.choices())
    created_at = models.DateTimeField(auto_now_add=True)
    development_type = models.CharField(max_length=10, choices=Development.choices())
    floor = models.CharField(max_length=10, choices=Floor.choices())
    heating = models.CharField(max_length=10, choices=Heat.choices())
    year = models.PositiveIntegerField()
    text = models.TextField()
    equipment = models.ManyToManyField(to='flat.Equip', related_name='flat')
    location = models.ForeignKey(FlatLocation, related_name='flat', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='flat', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']
        constraints = (
            # for checking in the DB
            CheckConstraint(
                check=Q(myfloat__gte=0.0),
                name='flat_myfloat_range'),
        )

    def __str__(self):
        return f'{self.title} | {self.created_at}'


def get_image_filename(instance, filename):
    title = instance.post.title
    slug = slugify(title)
    return "images/%s-%s" % (slug, filename)


class Equip(models.Model):
    name = models.CharField(choices=Equipment.choices(), max_length=10, blank=True)


class FlatImage(models.Model):
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image_filename, blank=True, verbose_name='Image')