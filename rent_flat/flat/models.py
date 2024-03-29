from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import CheckConstraint, Q
from django.template.defaultfilters import slugify
from smart_selects.db_fields import ChainedForeignKey

from .const import Rooms, Development, Floor, Heat, Equipment, Province, County, City, Status, District

User = settings.AUTH_USER_MODEL


class Equip(models.Model):
    name = models.CharField(choices=Equipment.choices(), max_length=30)

    def __str__(self):
        return f'{self.name}'


class Flat(models.Model):
    title = models.CharField(max_length=120)
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    equipment = models.ManyToManyField(Equip, related_name='flat', blank=True)
    user = models.ForeignKey(User, related_name='flat', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=Status.choices(), default=Status.Active)

    class Meta:
        ordering = ['-created_at']
        constraints = (
            # for checking in the DB
            CheckConstraint(
                check=Q(price__gte=0.0),
                name='flat_price_range'),
        )

    def __str__(self):
        return f'{self.title} | {self.created_at}'


def get_image_filename(instance, filename):
    title = instance.flat.title
    slug = slugify(title)
    return "images/%s-%s" % (slug, filename)


class FlatDetail(models.Model):
    area = models.FloatField(validators=[MinValueValidator(0.0)])
    rooms = models.CharField(choices=Rooms.choices(), max_length=30)
    development_type = models.CharField(max_length=10, choices=Development.choices())
    floor = models.CharField(max_length=10, choices=Floor.choices())
    heating = models.CharField(max_length=10, choices=Heat.choices())
    year = models.PositiveIntegerField()
    flat = models.OneToOneField(Flat, on_delete=models.CASCADE, related_name='detail')

    class Meta:
        constraints = (
            # for checking in the DB
            CheckConstraint(
                check=Q(area__gte=0.0),
                name='flatDetail_area_range'),
        )

    def __str__(self):
        return f'{self.flat}: {self.year}|{self.area}'


class FlatImage(models.Model):
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=get_image_filename, blank=True, verbose_name='Image')


class LocationArea(models.Model):
    province = models.CharField(choices=Province.choices(), max_length=20)
    county = models.CharField(choices=County.choices(), max_length=20)
    city = models.CharField(choices=City.choices(), max_length=20)

    def __str__(self):
        return f'{self.city}, {self.province}'


class LocationDistrict(models.Model):
    district = models.CharField(choices=District.choices(), max_length=20, null=True, blank=True)
    city = models.ForeignKey(LocationArea, related_name='district', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.district}'


class FlatLocation(models.Model):
    city = models.ForeignKey(LocationArea, related_name='location', on_delete=models.CASCADE)
    district = ChainedForeignKey(LocationDistrict, chained_field="city", chained_model_field="city",
                                 show_all=False,
                                 auto_choose=True,
                                 sort=True)
    street = models.CharField(max_length=100, blank=True, null=True)
    flat = models.OneToOneField(Flat, on_delete=models.CASCADE, related_name='location')

    def __str__(self):
        return f'{self.city}'