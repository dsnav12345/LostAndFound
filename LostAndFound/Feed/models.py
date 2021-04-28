from django.db import models
from Accounts.models import User

# Create your models here.
class Post(models.Model):
    categorytypes = [
            ("Mobiles","Mobiles"),
            ("Watches","Watches"),
            ("MobileAccessories","MobileAccessories"),
            ("Laptops","Laptops"),
            ("Speakers","Speakers"),
            ("Camera","Camera"),
            ("Footwear","Footwear"),
            ("WinterWear","WinterWear"),
            ("WaterBottle","WaterBottle"),
            ("Bag","Bag"),
            ("Books","Books"),
            ("Cycle","Cycle"),
            ("BankingItems","BankingItems"),
            ("Diaries","Diaries"),
            ("Calculators","Calculators"),
            ("Spectacles","Spectacles"),
            ("Keys","Keys"),
            ("Purse","Purse"),
        ]
    name = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    date = models.DateField( auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    category = models.CharField(max_length=20, choices=categorytypes)
    image = models.ImageField(upload_to='pictures', blank=True)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)

class ImageSearchModel(models.Model):
    imgtosearch=models.ImageField(upload_to='pictures', blank=True)
