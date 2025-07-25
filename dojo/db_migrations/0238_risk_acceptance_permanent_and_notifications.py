# ruff: noqa: N999
import multiselectfield.db.fields
from django.db import migrations, models


def create_risk_approvers(apps, schema_editor):
    Dojo_Group = apps.get_model("dojo", "Dojo_Group")
    Dojo_Group.objects.get_or_create(name="Risk-Approvers")


class Migration(migrations.Migration):
    dependencies = [
        ("dojo", "0237_alter_risk_acceptance_approved"),
    ]

    operations = [
        migrations.AddField(
            model_name="risk_acceptance",
            name="permanent",
            field=models.BooleanField(default=False, help_text="Indicates this risk acceptance does not expire."),
        ),
        migrations.AddField(
            model_name="notifications",
            name="risk_acceptance_request",
            field=multiselectfield.db.fields.MultiSelectField(
                blank=True,
                choices=[("slack", "slack"), ("msteams", "msteams"), ("mail", "mail"), ("alert", "alert")],
                default=("alert", "alert"),
                max_length=24,
                verbose_name="Risk Acceptance Requests",
            ),
        ),
        migrations.RunPython(create_risk_approvers, migrations.RunPython.noop),
    ]
