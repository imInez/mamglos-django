from django.db import models
from django.utils import timezone
import os
from PIL import Image



class Dog(models.Model):
    dog_name = models.CharField(max_length=25)
    dog_description = models.TextField()
    dog_picture = models.ImageField(default='default_dog.jpg', upload_to='dogs_pics')
    dog_gallery = models.TextField(default='https://www.facebook.com/pg/stowarzyszenieMamGlos/photos/?tab=albums')
    was_adopted = models.BooleanField(default=False)
    added = models.DateTimeField(default=timezone.now, blank=True, null=True)
    adoption_date = models.DateField(default=timezone.now)

    def save(self):
        super().save()

        img = Image.open(self.dog_picture.path)
        if img.width > img.height and img.width > 750:
            output_size = (750, 500)
        else:
            output_size = (500,500)
        img.thumbnail(output_size)
        img.save(self.dog_picture.path)


    def __str__(self):
        return self.dog_name



class Employee(models.Model):
    employee_name = models.CharField(max_length=35)
    employee_picture = models.ImageField(default='personImage.png', upload_to='employees_pics')

    def __str__(self):
        return self.employee_name


class Article(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now)
    tldr = models.TextField(max_length=200)
    fb_link = models.TextField(blank=True)
    article_text = models.TextField()
    is_main_article = models.BooleanField(default=False)
    is_lost = models.BooleanField(default=False)
    is_found = models.BooleanField(default=False)
    is_support = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.is_main_article:
                Article.objects.filter(is_main_article=True).update(is_main_article=False)
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class ArticlePicture(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='articles_pics', blank=True)

class Partner(models.Model):
    name = models.TextField(default='nazwa')
    logo = models.ImageField(default='default_logo.jpg', upload_to='partners_pics')
    thanks_link = models.TextField(default='https://www.facebook.com/stowarzyszenieMamGlos/')

    def __str__(self):
        return self.name

class Document(models.Model):
    file = models.FileField(upload_to='documents')
    filename_str = models.CharField(max_length=50, default='plik')

    def filename(self):
        if self.filename_str is not 'plik':
            return self.filename_str
        else:
            return os.path.basename(self.file.name)

    def __str__(self):
        return os.path.basename(self.file.name)



