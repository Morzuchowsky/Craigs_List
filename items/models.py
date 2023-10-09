from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse


class item(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()
    photo = models.ImageField(upload_to="gallary", default='no-image.png')
    seller = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('item_detail', args=[str(self.id)])
