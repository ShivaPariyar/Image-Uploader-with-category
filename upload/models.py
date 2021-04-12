from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Image(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='myimage')
    title = models.CharField(max_length=100)
    description = models.TextField()
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
