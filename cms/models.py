from django.db import models

class SiteContent(models.Model):
    PAGE_CHOICES = [
        ("home", "Home"),
        ("about", "About"),
        ("services", "Services"),
        ("features", "Features"),
        ("stakeholders", "Stakeholders"),
        ("lead_system", "Lead System"),
        ("blog", "Blog"),
        ("resources", "Resources"),
        ("careers", "Careers"),
        ("contact", "Contact"),
        ("portfolio", "Portfolio"),
    ]

    page = models.CharField(max_length=50, choices=PAGE_CHOICES)
    section = models.CharField(max_length=100)   # e.g. hero_title, hero_text, service1_title
    title = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to="cms/", blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("page", "section")
        ordering = ["page", "section"]

    def __str__(self):
        return f"{self.page} - {self.section}"
