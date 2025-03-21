# Generated by Django 2.2.24 on 2025-03-19 14:34

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_auto_20250312_2034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='ФИО')),
                ('owners_phonenumber', models.CharField(blank=True, default=0, max_length=20, null=True, verbose_name='Номер владельца')),
                ('owner_pure_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='Номер нормализованный владельца')),
                ('flats', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Собственник', to='property.Flat', verbose_name='Квартиры в собственности')),
            ],
        ),
    ]
