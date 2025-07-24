from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('dojo', '0235_clean_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='risk_acceptance',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
