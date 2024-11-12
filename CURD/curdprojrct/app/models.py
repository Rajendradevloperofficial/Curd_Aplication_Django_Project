from django.db import models


class register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    screenshot = models.ImageField(upload_to='image')

    def __str__(self):
        return self.name+" "+self.email+" " + self.password
