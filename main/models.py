from django.db import models
from PIL import Image

# Create your models here.
class SocialLink(models.Model):
    name = models.CharField(max_length=300)
    link = models.URLField(default="#")
    icon = models.CharField(max_length=300, default='')
    label = models.CharField(max_length=1,default='t')

    def __str__(self):
        return f'{self.name}'

class Profile(models.Model):
    name = models.CharField(max_length=300)
    job = models.CharField(max_length=300)
    home_desc = models.CharField(max_length=300)
    mobile = models.IntegerField()
    email = models.EmailField()
    location = models.CharField(max_length=300)
    aboutme = models.CharField(max_length=300)
    experience = models.IntegerField()
    projects = models.IntegerField()
    companies = models.IntegerField()
    cv = models.FileField(upload_to='files')
    blobimg = models.ImageField(upload_to='self')
    aboutimg = models.ImageField(upload_to='self')
    projectimg = models.ImageField(upload_to='self')
    discount = models.IntegerField()
    colortheme = models.IntegerField()

    def __str__(self):
        return f'profile'


class Skill(models.Model):
    name = models.CharField(max_length=300)
    time = models.IntegerField()
    icon = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name}'

class Subskill(models.Model):
    parent = models.ForeignKey(Skill,on_delete=models.CASCADE,related_name='parentskill')
    name = models.CharField(max_length=300)
    percentage = models.CharField(max_length=6,default="p__")

    def __str__(self):
        return f'{self.name} {self.parent.name}'

class Education(models.Model):
    stage = models.CharField(max_length=300)
    institution = models.CharField(max_length=300)
    time_from = models.IntegerField()
    time_to = models.IntegerField()

    class Meta:
        ordering = ('-time_from',)

    def __str__(self):
        return f'{self.stage}'

class Work(models.Model):
    position = models.CharField(max_length=300)
    company = models.CharField(max_length=300)
    time_from = models.IntegerField()
    time_to = models.IntegerField()

    class Meta:
        ordering = ('-time_from',)

    def __str__(self):
        return f'{self.position}'

class Service(models.Model):
    name = models.CharField(max_length=300)
    lastname = models.CharField(max_length=300,default='')
    icon = models.CharField(max_length=300)
    
    def __str__(self):
        return f'{self.name}'

class ServiceDetail(models.Model):
    parent = models.ForeignKey(Service,on_delete=models.CASCADE,related_name='parentservice')
    point = models.CharField(max_length=300)
 
    def __str__(self):
        return f'{self.parent.name}'

class Portfolio(models.Model):
    name = models.CharField(max_length=300)
    desc = models.CharField(max_length=300)
    img = models.ImageField(upload_to='portfolio')
    demo = models.URLField()

    def __str__(self):
        return f'{self.name}'

    def save(self):
        super().save()
        img = Image.open(self.img.path)
        if img.height > 400 or img.width > 400:
            size = (400,400)
            img.thumbnail(size)
            img.save(self.img.path)

class Testimonial(models.Model):
    name = models.CharField(max_length=300)
    position = models.CharField(max_length=300)
    star = models.IntegerField(default=1)
    star2 = models.IntegerField(default=1)
    star3 = models.IntegerField(default=1)
    saying = models.TextField()
    img = models.ImageField(upload_to='testimonial')

    def __str__(self):
        return f'{self.name}'

    def save(self):
        super().save()
        img = Image.open(self.img.path)
        if img.height > 200 or img.width > 200:
            size = (200,200)
            img.thumbnail(size)
            img.save(self.img.path)