from django.db import migrations

import phonenumbers


def normalize_phone_numbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')

    for flat in Flat.objects.iterator():
        if flat.phonenumber:
            try:
                parsed_number = phonenumbers.parse(flat.phonenumber, 'RU')
                if phonenumbers.is_valid_number(parsed_number):
                    normalized_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
                    flat.pure_phone = normalized_number
                    flat.save()
            except phonenumbers.phonenumberutil.NumberFormatException:
                pass


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_auto_20230909_1546'),
    ]

    operations = [
        migrations.RunPython(normalize_phone_numbers)
    ]
