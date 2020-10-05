from django.db import models

# Create your models here.
class Vacancy(models.Model):
    title=models.CharField(max_length=255)
    pub_date=models.DateTimeField()
    apply_date=models.DateTimeField()
    body=models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %d, %Y')

    def app_date_pretty(self):
        return self.apply_date.strftime('%b %d, %Y')
