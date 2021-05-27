from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Tweet(models.Model):
    user = models.ForeignKey(User, related_name="tweets",on_delete=models.CASCADE)
    text = models.CharField(max_length=160)
    image = models.ImageField(upload_to ='uploads/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']


class Follow(models.Model):
    user = models.ForeignKey(User, related_name='friends', on_delete=models.CASCADE)
    target = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.user) + " follows " + str(self.target)

    class Meta:
        unique_together = ('user', 'target')