# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_modes', '0007_coursemode_bulk_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursemode',
            name='currency',
            field=models.CharField(default=b'inr', max_length=8),
        ),
    ]
