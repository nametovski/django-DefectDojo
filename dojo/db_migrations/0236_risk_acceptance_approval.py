from django.db import migrations, models


def approve_existing_risk_acceptances(apps, schema_editor):
    RiskAcceptance = apps.get_model('dojo', 'Risk_Acceptance')
    RiskAcceptance.objects.update(approved=True)

class Migration(migrations.Migration):
    dependencies = [
        ('dojo', '0235_clean_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='risk_acceptance',
            name='approved',
            field=models.BooleanField(
                default=False,
                help_text='Whether this risk acceptance has been approved by the owner.',
            ),
        ),
        migrations.RunPython(approve_existing_risk_acceptances, migrations.RunPython.noop),
    ]
