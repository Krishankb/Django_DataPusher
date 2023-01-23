from django.db import models

class Account(models.Model):
    email = models.EmailField(unique=True, blank=False)
    account_id = models.CharField(max_length=255, unique=True)
    account_name = models.CharField(max_length=255, blank=False)
    app_secret_token = models.CharField(max_length=255, blank=True)
    website = models.URLField(blank=True)

class Destination(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    url = models.URLField(blank=False)
    http_method = models.CharField(max_length=10, blank=False)
    headers = models.JSONField(blank=False)
