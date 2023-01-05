from django.db import models

class Led(models.Model):
    value = models.CharField(max_length=1)
    created_at = models.CharField(max_length=100)
    created_epoch = models.CharField(max_length=100)
    expiration = models.CharField(max_length=100)

class Pump(models.Model):
    value = models.CharField(max_length=1)
    created_at = models.CharField(max_length=100)
    created_epoch = models.CharField(max_length=100)
    expiration = models.CharField(max_length=100)

class humidity(models.Model):
    value = models.CharField(max_length=10)
    created_at = models.CharField(unique=True, max_length=100)
    created_epoch = models.CharField(max_length=100)
    expiration = models.CharField(max_length=100)

class temp(models.Model):
    value = models.CharField(max_length=10)
    created_at = models.CharField(unique=True, max_length=100)
    created_epoch = models.CharField(max_length=100)
    expiration = models.CharField(max_length=100)

class light(models.Model):
    value = models.CharField(max_length=10)
    created_at = models.CharField(unique=True, max_length=100)
    created_epoch = models.CharField(max_length=100)
    expiration = models.CharField(max_length=100)