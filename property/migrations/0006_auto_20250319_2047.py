# Generated by Django 2.2.24 on 2025-03-19 14:47

from django.db import migrations


def load_owner_data(apps, schema_editor):
    Owners = apps.get_model('property', 'Owner')
    Flats = apps.get_model('property', 'Flat')
    for flat in Flats:
        if not Owners.objects.filter(full_name=flat.owner).exists():
            Owners.objects.create(full_name=flat.owner, owners_phonenumber=flat.owners_phonenumber, owner_pure_phone=flat.owner_pure_phone, flats=flat)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_owner'),
    ]

    operations = [
        migrations.RunPython(load_owner_data)
    ]
