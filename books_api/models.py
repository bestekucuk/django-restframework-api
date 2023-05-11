from django.db import models

class Book(models.Model):
    title=models.CharField(max_length=50)
    page_number=models.IntegerField()
    publish_date=models.DateField()
    stock=models.IntegerField()