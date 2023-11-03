from django.db import migrations


def insert_initial_data(apps, schema_editor):
    Product = apps.get_model('products', 'Product')

    Product.objects.all().delete()

    Product.objects.create(id=1, name='Apple', category='Fruit', price=1.20)
    Product.objects.create(id=2, name='Orange', category='Fruit', price=1.30)
    # ... Insert the rest of your data ...


class Migration(migrations.Migration):
    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(insert_initial_data),
    ]
