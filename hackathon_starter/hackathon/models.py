from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

class Profile(models.Model):
    user = models.ForeignKey(User)
    oauth_token = models.CharField(max_length=200)
    oauth_secret = models.CharField(max_length=200)

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)