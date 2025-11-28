from django.db import models

# 1. Hero Section (Singleton)
class ServiceHero(models.Model):
    title = models.CharField(max_length=255, default="Our Services")
    subtitle = models.TextField(default="End-to-end financial solutions tailored for your growth.")
    
    class Meta:
        verbose_name = "Hero Section"
        verbose_name_plural = "Hero Section"

    def __str__(self):
        return "Service Page Hero"

# 2. Bottom CTA (Singleton)
class ServiceCTA(models.Model):
    title = models.CharField(max_length=255, default="Need a Custom Solution?")
    text = models.TextField(default="Our experts are ready to help you design, deploy, and optimize your finance strategy.")
    button_text = models.CharField(max_length=50, default="Contact Us")

    class Meta:
        verbose_name = "Bottom CTA"
        verbose_name_plural = "Bottom CTA"

    def __str__(self):
        return "Service Page CTA"

