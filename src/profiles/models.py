from django.db import models

# Create your models here.
class Profile(models.Model):    # inherit from Models.model 
    # the properties we want it to have
    name        = models.CharField(max_length=120)    # Max_length required for Charfield 
    description = models.TextField()
    email       = models.EmailField()
    # Adding new props, we can use default=true, or null=true to make sure existing Profiles have this accounted for
    featured    = models.BooleanField(default=True)      
    # blank=False makes a field required.
    # null=False affects if field is required in database   