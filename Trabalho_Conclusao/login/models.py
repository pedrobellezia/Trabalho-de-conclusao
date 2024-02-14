from django.db import models
<<<<<<< Updated upstream
=======

# Create your models here.

class User(models.Model):
    company_name = models.CharField(max_length=255)
    fantasy_name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    representative = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=20)
    email = models.EmailField()
    zipcode = models.CharField(max_length=20)
    street = models.CharField(max_length=255)
    number = models.CharField(max_length=20)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2, choices=STATE_CHOICES)
    phone = models.CharField(max_length=20)
    enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
>>>>>>> Stashed changes
