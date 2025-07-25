# ruff: noqa: N999
from django.db import migrations


def create_group(apps, schema_editor):
    Dojo_Group = apps.get_model("dojo", "Dojo_Group")
    Dojo_Group.objects.get_or_create(name="Risk-Approvers")


class Migration(migrations.Migration):
    dependencies = [
        ("dojo", "0239_alter_notifications_risk_acceptance_request"),
    ]

    operations = [
        migrations.RunPython(create_group, migrations.RunPython.noop),
    ]
