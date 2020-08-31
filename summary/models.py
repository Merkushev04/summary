from django.db import models


class Intro(models.Model):
    image = models.ImageField(upload_to='foto/%Y/%m/%d', blank=True)
    position = models.CharField(max_length=250)
    intro = models.TextField(max_length=2500)

    def __str__(self):
        return self.position


class Contact(models.Model):
    name = models.CharField(max_length=250)
    information = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Education(models.Model):
    university = models.CharField(max_length=250)
    specialization = models.CharField(max_length=250)
    date_start = models.DateField()
    date_end = models.DateField()

    def __str__(self):
        return self.specialization


class Skill(models.Model):
    name = models.CharField(max_length=250)
    level = models.DecimalField(max_digits=3, decimal_places=0)

    def __str__(self):
        return self.name


class Work(models.Model):
    place = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    duties = models.TextField(max_length=2000)
    instruments = models.TextField(max_length=2000, blank='True' )
    date_start = models.DateField()
    date_end = models.DateField()

    def __str__(self):
        return self.place


class Courses(models.Model):
    site = models.CharField(max_length=250)
    specialization = models.CharField(max_length=250)

    def __str__(self):
        return self.site


class Project(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=5000)
    link = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Message(models.Model):
    company = models.CharField(max_length=250)
    contact = models.CharField(max_length=250)
    message = models.TextField(max_length=2000)

    def __str__(self):
        return self.company


