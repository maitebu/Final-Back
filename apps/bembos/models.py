from django.db import models

# Create your models here.

class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Supplies(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='img', height_field=None, width_field=None, max_length=255)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    cod_order = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.cod_order

class OrderDetail(models.Model):
    id = models.AutoField(primary_key=True)
    supply = models.ManyToManyField(Supplies)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)

    def __str__(self):
        return self.id
    