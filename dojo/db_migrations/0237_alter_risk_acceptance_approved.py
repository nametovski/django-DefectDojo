# ruff: noqa: N999
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dojo", "0236_risk_acceptance_approval"),
    ]

    operations = [
        migrations.AlterField(
            model_name="risk_acceptance",
            name="approved",
            field=models.BooleanField(
                default=False,
                help_text="Whether this risk acceptance has been approved by the owner.",
            ),
        ),
    ]
