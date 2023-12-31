# Generated by Django 4.2.6 on 2023-11-03 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0002_insert_initial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('wishlistId', models.AutoField(primary_key=True, serialize=False)),
                ('pseudo', models.CharField(max_length=200)),
                ('productId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'db_table': 'wishlists',
            },
        ),
    ]
