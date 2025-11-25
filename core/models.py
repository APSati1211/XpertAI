from django.db import models
from django.contrib.auth.models import User 
from django.db.models.signals import post_save # <-- NEW
from django.dispatch import receiver # <-- NEW

# Example model (Existing)
class ExampleModel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Website Theme (Existing)
class Theme(models.Model):
    primary_color = models.CharField(max_length=7, default='#000000')
    secondary_color = models.CharField(max_length=7, default='#FFFFFF')

    def __str__(self):
        return "Website Theme"

# --- NEW: USER PROFILE MODEL ---
class UserProfile(models.Model):
    # One-to-One link with User model
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
    # Image field for profile picture
    image = models.ImageField(
        upload_to='profiles/', 
        blank=True, 
        null=True,
        help_text="User profile picture for display in Admin header."
    )
    
    def __str__(self):
        return f"Profile for {self.user.username}"

# Signal: Naye User ke bante hi ek UserProfile object automatically banao
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    # Ensure profile is saved if User object is saved later
    try:
        instance.userprofile.save()
    except UserProfile.DoesNotExist:
        # Handle case where profile was deleted manually but user wasn't
        if not created:
            UserProfile.objects.create(user=instance)