import phonenumbers
from django.db import migrations


def add_owner_pure_phone(apps, schema_editor):
    Flats = apps.get_model('property', 'Flat')
    for flat in Flats.objects.filter(owners_phonenumber='+700000000000'):
        phonenumber_parse = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        if phonenumbers.is_valid_number(phonenumber_parse):
            flat.owner_pure_phone = phonenumbers.format_number(phonenumber_parse, phonenumbers.PhoneNumberFormat.E164)
            flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_auto_20250312_2032'),
    ]

    operations = [
        migrations.RunPython(add_owner_pure_phone)
    ]
