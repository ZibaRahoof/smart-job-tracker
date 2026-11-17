from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Job(models.Model):
    STATUS_CHOICES = [
        ('whishlist','Whishlist'),
        ('applied','Applied'),
        ('interview','Interview'),
        ('offer','Offer'),
        ('rejected','Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobs')
    company = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    location = models.CharField(max_length=150, blank=True)
    job_url = models.URLField(blank=True)
    description = models.TextField(blank=True)
    salary = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='wishlist')
    applied_date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} at {self.company}"
