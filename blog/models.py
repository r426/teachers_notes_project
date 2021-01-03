from django.db import models


class Grade2blogpost(models.Model):
    grade = models.CharField(max_length=10, default='Grade 2')
    date = models.DateField()
    title = models.TextField(max_length=200)
    intro = models.TextField(max_length=400, default='intro')
    description = models.TextField()
    image = models.ImageField(upload_to='blog/images/', default='blog/images/soon.png')
    file = models.FileField(upload_to='blog/downloads/', blank='True')
    credits = models.TextField(blank='True')

    def __str__(self):
        return self.title


class Grade3blogpost(models.Model):
    grade = models.CharField(max_length=10, default='Grade 3')
    date = models.DateField()
    title = models.TextField(max_length=200)
    intro = models.TextField(max_length=400, default='intro')
    description = models.TextField()
    image = models.ImageField(upload_to='blog/images/', default='blog/images/soon.png')
    file = models.FileField(upload_to='blog/downloads/', blank='True')
    credits = models.TextField(blank='True')

    def __str__(self):
        return self.title


class Grade4blogpost(models.Model):
    grade = models.CharField(max_length=10, default='Grade 4')
    date = models.DateField()
    title = models.TextField(max_length=200)
    intro = models.TextField(max_length=400, default='intro')
    description = models.TextField()
    image = models.ImageField(upload_to='blog/images/', default='blog/images/soon.png')
    file = models.FileField(upload_to='blog/downloads/', blank='True')
    credits = models.TextField(blank='True')

    def __str__(self):
        return self.title

# These functions return the default name
