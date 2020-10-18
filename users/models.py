from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        User,
        verbose_name=_("profile_pk"),
        on_delete=models.CASCADE
    )
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics/')
    def __str__(self):
        return f'{self.user.username} Profile'
