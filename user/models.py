from django.db import models

# Create your models here.
class User(models.Model):
    GENDER = [
        ("M", "Male"),
        ("F", "Female"),
        ("NA", "Choose not to specify")
    ]
    first_name = models.CharField(max_length=30)
    middle_initial = models.CharField(max_length=1)
    last_name = models.CharField(max_length=30)
    suffix = models.CharField(max_length=10)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    gender = models.CharField(max_length=2, choices=GENDER)

    def __str__(self):
        return self.full_name
