from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    profile_picture = CloudinaryField("image", null=True, default=None, blank=True)
    theme = models.CharField(max_length=20, default='light')

    @property
    def image_url(self):
        if(self.profile_picture != None):
            return f"https://res.cloudinary.com/daryn06r2/{self.profile_picture}"
        else:
            return None
