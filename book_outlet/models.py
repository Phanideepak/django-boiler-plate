from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.name} ({self.code})'

    class Meta:
        verbose_name_plural = 'Country Entries'

class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=6)
    city = models.CharField(max_length = 50)

    def __str__(self):
        return f'{self.city} - {self.street} ({self.postal_code})'
    
    class Meta:
        verbose_name_plural = 'Address Entries'

class Author(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    address = models.OneToOneField(Address, on_delete = models.CASCADE, related_name= 'author', null = True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    
    #author = models.CharField(max_length=100, null = True)
    author = models.ForeignKey(Author, on_delete = models.CASCADE, null = True, related_name= 'books')

    is_bestselling = models.BooleanField(default = False)
    # Harry Potter 1
    # editable = False
    slug = models.SlugField(default = "", null = False, db_index = True, blank=True)
    published_countries = models.ManyToManyField(Country, related_name = 'books')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    def __str__(self):
        return f'id = {self.id}, title = {self.title} , author = {self.author},  rating = {self.rating}, slug = {self.slug}'