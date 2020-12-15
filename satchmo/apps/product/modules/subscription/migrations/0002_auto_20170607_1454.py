# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptionproduct',
            name='is_shippable',
            field=models.IntegerField(help_text='Is this product shippable?', verbose_name='Shippable?', choices=[(0, 'No Shipping Charges'), (1, 'Pay Shipping Once'), (2, 'Pay Shipping Each Billing Cycle')]),
        ),
    ]
