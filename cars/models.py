from django.db import models
from django.urls import reverse

# Create your models here.

class Car(models.Model):
    TRANSMISSION_MANUAL = 0
    TRANSMISSION_AUTO = 1
    TRANSMISSION_CHOICES = (
        (TRANSMISSION_MANUAL, "Manual"),
        (TRANSMISSION_AUTO, "Automatic"),
    )
    
    maker = models.CharField(max_length=127)
    car_model = models.CharField(max_length=64)
    year = models.IntegerField()    
    transmission = models.PositiveSmallIntegerField(choices=TRANSMISSION_CHOICES, default=TRANSMISSION_MANUAL)
    color = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ("maker",)

    def __str__(self):
        return "{} {}".format(self.maker, self.car_model)

    def get_absolute_url(self):
        return reverse("cars:car_detail", args=[self.slug])
