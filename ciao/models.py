from django.db import models
from django.contrib.auth.models import User

class AbstractUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(null=True, blank=True, upload_to='user/foto')
    first_name = models.CharField(null=False, blank=False, max_length=255)
    last_name = models.CharField(null=False, blank=False, max_length=255)
    name = models.CharField(null=False, blank=False, max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    gambar = models.ImageField(null=False, blank=False, upload_to='image')
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title