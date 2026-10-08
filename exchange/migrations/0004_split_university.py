from django.db import migrations


def split_university(apps, schema_editor):
    ExchangeProgram = apps.get_model('exchange', 'ExchangeProgram')
    for program in ExchangeProgram.objects.all():
        text = program.university
        if text.endswith(')'):
            name, country = text[:-1].split(' (')
        elif ' - ' in text:
            name, country = text.split(' - ')
        else:
            name, country = text.split(', ')
        program.name = name
        program.country = country
        program.save(update_fields=['name', 'country'])


def join_university(apps, schema_editor):

    ExchangeProgram = apps.get_model('exchange', 'ExchangeProgram')
    for program in ExchangeProgram.objects.all():
        program.university = f'{program.name}, {program.country}'
        program.save(update_fields=['university'])


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0003_exchangeprogram_country_exchangeprogram_name'),
    ]

    operations = [
        migrations.RunPython(split_university, join_university),]
