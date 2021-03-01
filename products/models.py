from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=45)

    class Meta(object):
        db_table = "menu"


class Category(models.Model):
    name = models.CharField(max_length=20)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

    class Meta(object):
        db_table = "categories"


class Drink(models.Model):
    category     = models.ForeignKey('Category', on_delete=models.CASCADE)
    korean_name  = models.CharField(max_length=45)
    english_name = models.CharField(max_length=45)
    description  = models.TextField(max_length=2000)

    class Meta(object):
        db_table = "drinks"


class AllergyDrink(models.Model):
    allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE)
    drink   = models.ForeignKey('Drink', on_delete=models.CASCADE)

    class Meta(object):
        db_table = "allergy_drink"


class Allergy(models.Model):
    name = models.CharField(max_length=45)

    class Meta(object):
        db_table = "allergy"


class Nutrition(models.Model):
    one_serving_kcal = models.DecimalField(max_digits=6, decimal_places=2)
    sugars_g         = models.DecimalField(max_digits=6, decimal_places=2)
    drink            = models.ForeignKey('Drink', on_delete=models.CASCADE)

    class Meta(object):
        db_table = "nutritions"


class Image(models.Model):
    image_url = models.TextField(max_length=500)
    drink     = models.ForeignKey('Drink', on_delete=models.CASCADE)

    class Meta(object):
        db_table = "images"
