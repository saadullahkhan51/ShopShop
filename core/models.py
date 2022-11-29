from django.db import models

COLLECTION_CHOICES = (
    ('SU', 'Summer'),
    ('FL', 'Fall'),
    ('SP', 'Spring'),
    ('WN', 'Winter'),
)

# will implement later
SIZE_CHOICES = ()

# will implement later
COLOR_CHOICES = ()

# Create your models here.
class Product(models.Model):
    # all fields subclass Field, become db columns
    title = models.CharField(max_length=100)
    price = models.FloatField()
    collection = models.CharField(choices=COLLECTION_CHOICES, max_length=2)
    description = models.TextField(max_length=100)
    '''
        www.example.com/product/23 --> references by id
        www.example.com/product/Bonanza Kamez Shalwar --> www.example.com/product/Bonanza%20Kamez%20Shalwar --> still not very meaningful
        www.example.com/product/bonanza-kamez-shalwar --> slug down-cases and replaces spaces with hyphens
    '''
    slug = models.SlugField()

    def __str__(self):
        return f"{self.title}, {self.price}"

class Order(models.Model):
    pass

class OrderItem(models.Model):
    pass