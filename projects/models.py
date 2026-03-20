from django.db import models   # ✅ MUST BE FIRST LINE

class Project(models.Model):
    PROJECT_TYPE = (
        ('realestate', 'Real Estate'),
        ('shipyard', 'Shipyard'),
    )

    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField()
    project_type = models.CharField(max_length=20, choices=PROJECT_TYPE)
    status = models.CharField(max_length=50)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)

    def __str__(self):
        return self.name


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='projects/gallery/')

class Slider(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300)
    image = models.ImageField(upload_to='slider/')

    def __str__(self):
        return self.title

from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name