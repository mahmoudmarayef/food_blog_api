from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
import os

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='categories')

    def __str__(self):
        return self.title

@receiver(pre_delete, sender=Category)
def delete_image(sender, instance, **kwargs):
    # delete the image file from the local folder
    if instance.image:
        os.remove(instance.image.path)


# connect the signal receiver function to the pre_delete signal
pre_delete.connect(delete_image, sender=Category)

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.TextField()
    image = models.ImageField(upload_to='recipes')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
    
@receiver(pre_delete, sender=Recipe)
def delete_image(sender, instance, **kwargs):
    # delete the image file from the local folder
    if instance.image:
        os.remove(instance.image.path)


# connect the signal receiver function to the pre_delete signal
pre_delete.connect(delete_image, sender=Recipe)