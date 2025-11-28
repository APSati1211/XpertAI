from django.db import models

class LegalPage(models.Model):
    title = models.CharField(max_length=200, help_text="Page Title (e.g. Privacy Policy)")
    slug = models.SlugField(unique=True, help_text="URL identifier (e.g. privacy-policy, terms)")
    content = models.TextField(help_text="Main content. HTML is supported for formatting.")
    last_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.title