# Generated by Django 3.2.7 on 2021-11-11 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charactdesc',
            name='product_id',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='characts_desc', to='app.product'),
        ),
    ]
