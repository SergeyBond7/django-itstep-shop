# Generated by Django 3.2.7 on 2021-11-07 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_remove_charactname_charact_desc_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='charactname',
            name='charact_desc_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='characts_name', to='app.charactdesc'),
        ),
    ]