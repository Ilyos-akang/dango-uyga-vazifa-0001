from django.db import models
from django.utils import timezone

# Create your models here.

class Mahsulotlar_brend(models.Model):
    name=models.CharField(max_length=200)
    create_at=models.BooleanField(default=True)
    
    def __str__(self):
        return self.name


class Kompyuter(models.Model):
    category=models.ForeignKey(Mahsulotlar_brend,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    turi=models.CharField(max_length=200)
    price=models.CharField(max_length=200)
    image=models.ImageField(upload_to='rasmlar/',null=True,blank=True)
    desc=models.CharField(max_length=255)
    xotira=models.IntegerField(default=0)
    ram_xotira=models.IntegerField(default=0)
    ish_chiq_yil=models.DateTimeField(default=timezone.now,blank=True,null=True)
    yaroqlilik_muddati=models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    

""""Telefon model (name, brend, price, image, desc, stock, xotira, ram, created_at, updated_at)

komputer models.py faylda esa
Komputer model (name, brend, price, image, desc, stock, xotira, ram, ekran o'lchami, created_at, updated_at)
"""