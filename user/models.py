from django.db import models

# Create your models here.
class User(models.Model):
    GENDER = [
        ("M", "Male"),
        ("F", "Female"),
        ("NA", "Choose not to specify")
    ]
    SUFFIX = [
        ("Mr.", "Mr."),
        ("Mrs.", "Mrs."),
        ("Ms.", "Ms. ")
    ]
    first_name = models.CharField(max_length=30)
    middle_initial = models.CharField(max_length=1)
    last_name = models.CharField(max_length=30)
    suffix = models.CharField(max_length=10, choices=SUFFIX)
    email = models.EmailField(max_length=100)
    gender = models.CharField(max_length=2, choices=GENDER)

    def __str__(self):
        return self.create_full_name()
    
    def create_full_name(self):
        full_name = ' '.join([self.first_name, self.middle_initial, self.last_name])  
        return full_name
