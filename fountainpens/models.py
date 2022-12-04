from pyexpat import model
from statistics import mode
from tkinter import CASCADE
from django.db import models
from django.db.models.base import Model
from django.db.models.enums import Choices
from django.db.models.fields.related import ForeignKey
from traitlets import default

class Brand(models.Model):

    name = models.CharField(max_length=50)
    origin = models.CharField(max_length=50)
    established = models.IntegerField()

    def __str__(self) -> str:
	    return self.name +" "+ self.origin

class NibPoint(models.Model):

    point = models.CharField(max_length=50)

    def __str__(self) -> str:
	    return self.point

class NibSize(models.Model):

    size = models.CharField(max_length=50)

    def __str__(self) -> str:
	    return self.size

class NibColor(models.Model):

    color_name = models.CharField(max_length=50)

    def __str__(self) -> str:
	    return self.color_name

class Nib(models.Model):

    nib_size = models.ForeignKey(NibSize,on_delete=models.CASCADE)
    nib_point = models.ForeignKey(NibPoint,on_delete=models.CASCADE)
    nib_color = models.ForeignKey(NibColor,on_delete=models.CASCADE)
    nib_manufacturer = models.ForeignKey(Brand,on_delete=models.CASCADE)

    def __str__(self) -> str:
	    return str(self.nib_manufacturer) + " " + str(self.nib_size) + " " + str(self.nib_color) + " color " + str(self.nib_point) + " point"

class InkReserviorType(models.Model):

    reservior_type_name = models.CharField(max_length=50)

    def __str__(self) -> str:
	    return self.reservior_type_name

class InkReservior(models.Model):

    reservior_type = models.ForeignKey(InkReserviorType,on_delete=models.CASCADE)
    reservior_model_name = models.CharField(max_length=50)
    reservior_capacity = models.FloatField()
    reservior_brand = models.ForeignKey(Brand,on_delete=models.CASCADE)

    def __str__(self) -> str:
	    return str(self.reservior_brand) + " " + self.reservior_model_name + " " + str(self.reservior_type) + " " + str(self.reservior_capacity) + " ml"

class FountainPen(models.Model):

    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    pen_model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    supported_nib_size = models.ForeignKey(NibSize,on_delete=models.CASCADE)
    nib = models.ForeignKey(Nib,on_delete=models.CASCADE)
    ink_reservior = models.ForeignKey(InkReservior,on_delete=models.CASCADE)

    def __str__(self) -> str:
	    return str(self.brand) + " " + self.pen_model + " with " + str(self.nib)
                                                               