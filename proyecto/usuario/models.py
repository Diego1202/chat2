from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

# Create your models here.

def default_profile_image():
    return 'profiles/default_profile_image.png'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True, validators=[MinLengthValidator(10)])
    address = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='profiles/', blank=True, null=True)
    is_online = models.BooleanField(default=False)
    last_logout = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username.upper()}"
    
    def save(self, *args, **kwargs):
        if not self.image:
            self.image = default_profile_image()
        super(Profile, self).save(*args, **kwargs)


class Message(models.Model):
    sender = models.ForeignKey(Profile, related_name='sender_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(Profile, related_name='receiver_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    read_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.sender.user.username} -> {self.receiver.user.username}"