from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    short_description = models.CharField(max_length=512, blank=True)
    body = models.TextField()
    image = models.ImageField(upload_to="blogs/", blank=True, null=True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
