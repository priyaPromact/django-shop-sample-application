# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('product_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='shop.Product')),
                ('author', models.CharField(max_length=255)),
                ('cover_picture', models.ImageField(upload_to=b'img/book')),
                ('isbn', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['author'],
            },
            bases=('shop.product',),
        ),
    ]
