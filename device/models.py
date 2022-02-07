from audioop import reverse
from django.db import models
from django.utils.text import slugify
from django.urls import reverse 

class Cam(models.Model):
    name = models.CharField(max_length=52)
    slug = models.SlugField(max_length=52, blank=True)
    desc = models.TextField(blank=True, null=True)
    turn_left = models.FloatField(help_text="Turn Camera to left", blank=True, default=0)
    turn_right = models.FloatField(help_text="Turn Camera to Right", blank=True, default=0)

    def __str__ (self):
       return self.name

    def save(self):
        self.slug = slugify(self.name, self.id)
        return super().save()

    def get_absolute_url(self):
        return reverse('this_camera', args=[self.slug])