from django.db import models


class File(models.Model):

    transaction_date= models.DateField(null=False,blank=False)
    channel = models.CharField(max_length=100, null=False,blank=False)
    country = models.CharField(max_length=100,null=False,blank=False)
    os = models.CharField(max_length=100,blank=False)
    impressions = models.IntegerField(blank=False)
    clicks = models.IntegerField(blank=False)
    installs = models.IntegerField(null=False)
    spend = models.FloatField(null=False)
    revenue = models.FloatField(null=False)

    def __str__(self):
        return self.channel




