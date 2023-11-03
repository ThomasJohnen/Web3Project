from django.db import models


class Product(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.FloatField()

    class Meta:
        db_table = 'products'

    @classmethod
    def create_one(cls, id, name, category, price):
        if not cls.objects.filter(id=id).exists():
            product = cls(id=id, name=name, category=category, price=price)
            product.save()
            return True
        return False

    @classmethod
    def read_all(cls):
        return cls.objects.all()

    @classmethod
    def read_one(cls, id):
        return cls.objects.filter(id=id).first()

    def update(self, new_name, new_category, new_price):
        self.name = new_name
        self.category = new_category
        self.price = new_price
        self.save()

    @classmethod
    def delete_one(cls, id):
        product = cls.objects.filter(id=id).first()
        if product:
            product.delete()
            return True
        return False

    @classmethod
    def delete_all(cls):
        cls.objects.all().delete()
