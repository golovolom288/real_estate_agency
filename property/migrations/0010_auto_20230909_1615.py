from django.db import migrations
from property.models import Flat, Owner


def copy_data_from_flat_to_owner(apps, schema_editor):
    for flat in Flat.objects.all():
        owner, created = Owner.objects.get_or_create(
            owner=flat.owner,
            pure_phone=flat.pure_phone,
        )
        owner.apartments.add(flat)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_owner'),
    ]

    operations = [
        migrations.RunPython(copy_data_from_flat_to_owner)
    ]
