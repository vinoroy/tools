from django.db import models


class Portfolio(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name




class Asset(models.Model):


    assetChoices = (
        ('COMMON', 'Common stock'),
        ('PREFERRED', 'Prefered stock'),
    )


    feedTypeChoices = (
        ('YAHOO', 'Yahoo feed'),

    )


    assetID = models.CharField(max_length=60)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.SET_NULL, null=True)
    assetType = models.CharField(max_length=20, choices=assetChoices, default='1')
    purchaseDate = models.DateTimeField()
    purchasePrice = models.FloatField()
    volume = models.IntegerField()
    saleDate = models.DateField(null=True,blank=True)
    salePrice = models.FloatField(null=True,blank=True)
    priceFeedType= models.CharField(max_length=40, choices=feedTypeChoices, default='1')
    priceFeedRef = models.CharField(max_length=20)
    debtFeedType = models.CharField(max_length=20,null=True,blank=True)
    debtFeedRef = models.CharField(max_length=20,null=True,blank=True)
    percentOwnership = models.FloatField()
    thresholds = models.CharField(max_length=20,null=True,blank=True)



    def __str__(self):
        return self.assetID



