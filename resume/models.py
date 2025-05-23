"""set up our models"""
from django.db import models

# Create your models here.
class Project(models.Model):
    """Set up model for resume projects"""
    project_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        unique=True
    )
    proj_desc = models.TextField()
    proj_qr = models.ImageField(null=True, blank=True)
    screengrab = models.ImageField(
        null=True,
        blank=True
    )
    screengrab_2 = models.ImageField(
        null=True,
        blank=True
    )
    languages = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    live_site = models.CharField(
        max_length=100,
        default='',
        null=False,
        blank=False
    )
    github_repo = models.CharField(
        max_length=150,
        default='',
        null=True,
        blank=True
    )
    friendly_proj_name = models.CharField(
        max_length=30,
        default='',
        null=False,
        blank=False
    )
    home_display = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        """Set up how the projects are ordered"""
        ordering = ['project_name']

    def __str__(self):
        """return string value"""
        return self.project_name

    def get_friendly_district_name(self):
        """set up the friendly versions of our project names"""
        return self.friendly_proj_name
