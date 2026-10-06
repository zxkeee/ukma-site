from django.db import migrations


def places_to_number(apps, schema_editor):
    ExchangeProgram = apps.get_model('exchange', 'ExchangeProgram')
    for program in ExchangeProgram.objects.all():
        for word in program.places.split():
            if word.isdigit():
                program.places_count = int(word)
        program.save(update_fields=['places_count'])


def places_to_text(apps, schema_editor):
    ExchangeProgram = apps.get_model('exchange', 'ExchangeProgram')
    for program in ExchangeProgram.objects.all():
        program.places = str(program.places_count)
        program.save(update_fields=['places'])


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0006_exchangeprogram_places_count'),
    ]

    operations = [
        migrations.RunPython(places_to_number, places_to_text),
    ]