from django.db import models

# Create your models here.
class products(models.Model):
    name = models.CharField(max_length=50)
    image = models.FileField(upload_to='images/')
    time = models.DateTimeField(auto_now_add=())

    def __str__(self):
        return self.name

