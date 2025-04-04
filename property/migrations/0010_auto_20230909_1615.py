from django.db import migrations


def copy_data_from_flat_to_owner(apps, schema_editor):
    Flat = apps.get_model("Flat")
    Owner = apps.get_model("Owner")
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
